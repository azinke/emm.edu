from __future__ import annotations

import importlib.util
import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPTS = Path(__file__).resolve().parents[1]
CURRICULUM = SCRIPTS.parent
FIXTURES = Path(__file__).parent / "fixtures"
sys.path.insert(0, str(SCRIPTS))

import qa_content
import run_smoke_hooks
import build_publications


class QualityFixtureTests(unittest.TestCase):
    def test_seeded_quality_defects_are_all_detected(self) -> None:
        findings = qa_content.run(FIXTURES / "qa-seeded-failure", offline=True)
        codes = {finding.code for finding in findings}
        expected = {"PAIR004", "PAIR006", "OUTCOME001", "RUBRIC003", "GLOSSARY001", "GLOSSARY002", "LINK001", "EXT001", "FIG001", "FIG002", "FIG003", "RESTRICT002"}
        self.assertTrue(expected.issubset(codes), f"missing seeded detections: {expected - codes}")
        self.assertTrue(
            any(
                finding.code == "PAIR006" and "answer_key_digest" in finding.message
                for finding in findings
            ),
            "seeded answer-key parity defect was not detected",
        )

    def test_localized_avoided_term_does_not_reject_the_other_language(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            termbase = root / "i18n" / "termbase.yml"
            termbase.parent.mkdir(parents=True)
            termbase.write_text(
                "terms:\n"
                "  - id: ee.voltage\n"
                "    avoided_terms:\n"
                "      - fr: voltage\n",
                encoding="utf-8",
            )
            term_ids, avoided = qa_content.termbase_data(root)
            en = qa_content.Document(root / "en.md", Path("courses/FIX/en/en.md"), {}, "voltage", "en", "pair")
            fr = qa_content.Document(root / "fr.md", Path("courses/FIX/fr/fr.md"), {}, "voltage", "fr", "pair")
            policy = {"restricted_path_tokens": [], "restricted_markers": []}
            self.assertFalse(any(f.code == "GLOSSARY002" for f in qa_content.validate_document(en, root, set(), term_ids, avoided, policy)))
            self.assertTrue(any(f.code == "GLOSSARY002" for f in qa_content.validate_document(fr, root, set(), term_ids, avoided, policy)))


class SmokeInterfaceTests(unittest.TestCase):
    def test_all_five_interfaces_execute(self) -> None:
        results, errors = run_smoke_hooks.run(CURRICULUM, [FIXTURES / "smoke-pass.yml"], "all")
        self.assertEqual(errors, [])
        self.assertEqual({result["kind"] for result in results}, {"code", "numerical", "hdl", "simulation", "kicad"})
        self.assertTrue(all(result["status"] == "pass" for result in results))

    def test_nonzero_hook_is_a_failure(self) -> None:
        results, errors = run_smoke_hooks.run(CURRICULUM, [FIXTURES / "smoke-seeded-failure.yml"], "all")
        self.assertEqual(results[0]["status"], "fail")
        self.assertTrue(errors)


class KiCadContractTests(unittest.TestCase):
    def test_seeded_project_is_rejected_by_real_kicad_when_available(self) -> None:
        if not shutil.which("kicad-cli"):
            self.skipTest("kicad-cli unavailable; deterministic smoke contract remains covered")
        with tempfile.TemporaryDirectory() as temporary:
            completed = subprocess.run(
                [sys.executable, str(SCRIPTS / "kicad_release.py"), str(FIXTURES / "kicad-seeded-failure"), "--report-dir", temporary, "--expect", "fail"],
                cwd=CURRICULUM.parent,
                capture_output=True,
                text=True,
                check=False,
            )
        self.assertEqual(completed.returncode, 0, completed.stdout + completed.stderr)
        self.assertIn("observed=fail expected=fail", completed.stdout)


class BuildFallbackTests(unittest.TestCase):
    def test_remote_build_resource_is_rejected_before_render(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            source = root / "courses" / "FIX" / "en" / "chapters" / "remote.md"
            source.parent.mkdir(parents=True)
            source.write_text("---\ntitle: Remote\n---\n\n![Diagram](https://example.invalid/diagram.svg)\n", encoding="utf-8")
            errors = build_publications.reject_remote_resources(root, ["en"])
            self.assertEqual(len(errors), 1)
            self.assertIn("archive it locally", errors[0])

    def test_pandoc_build_produces_separate_language_html_pdf_and_slides(self) -> None:
        if not shutil.which("pandoc") or not shutil.which("xelatex"):
            self.skipTest("pandoc/xelatex unavailable")
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            for language, title in (("en", "Example"), ("fr", "Exemple")):
                chapter = root / "courses" / "FIX" / language / "chapters" / "one.md"
                slide = root / "courses" / "FIX" / language / "slides" / "one.md"
                chapter.parent.mkdir(parents=True)
                slide.parent.mkdir(parents=True)
                chapter.write_text(f"---\ntitle: {title}\n---\n\n# {title}\n", encoding="utf-8")
                slide.write_text(f"---\ntitle: {title}\n---\n\n# {title}\n\n## Point\n\nText.\n", encoding="utf-8")
            completed = subprocess.run(
                [sys.executable, str(SCRIPTS / "build_publications.py"), "--root", str(root), "--engine", "pandoc", "--offline"],
                cwd=CURRICULUM.parent,
                capture_output=True,
                text=True,
                check=False,
            )
            self.assertEqual(completed.returncode, 0, completed.stdout + completed.stderr)
            self.assertTrue((root / "build" / "en" / "html" / "FIX" / "chapters" / "one.html").exists())
            self.assertTrue((root / "build" / "fr" / "html" / "FIX" / "chapters" / "one.html").exists())
            self.assertTrue((root / "build" / "en" / "pdf" / "FIX" / "chapters" / "one.pdf").exists())
            self.assertTrue((root / "build" / "fr" / "pdf" / "FIX" / "chapters" / "one.pdf").exists())
            self.assertTrue((root / "build" / "en" / "slides" / "FIX" / "slides" / "one.html").exists())
            self.assertTrue((root / "build" / "fr" / "slides" / "FIX" / "slides" / "one.html").exists())


class VisualRegressionTests(unittest.TestCase):
    def test_identical_and_changed_images_are_distinguished(self) -> None:
        if not shutil.which("magick") or not shutil.which("compare"):
            self.skipTest("ImageMagick unavailable")
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            policy = root / "environments" / "qa-policy.yml"
            policy.parent.mkdir(parents=True)
            policy.write_text("visual_regression:\n  root_mean_square_error: 0.01\n", encoding="utf-8")
            golden, same, changed = root / "golden.png", root / "same.png", root / "changed.png"
            subprocess.run(["magick", "-size", "20x20", "xc:white", str(golden)], check=True)
            shutil.copyfile(golden, same)
            subprocess.run(["magick", "-size", "20x20", "xc:black", str(changed)], check=True)
            base = [sys.executable, str(SCRIPTS / "visual_regression.py")]
            identical = subprocess.run(base + [str(same), str(golden), "--root", str(root)], capture_output=True, text=True)
            different = subprocess.run(base + [str(changed), str(golden), "--root", str(root)], capture_output=True, text=True)
            self.assertEqual(identical.returncode, 0, identical.stdout + identical.stderr)
            self.assertEqual(different.returncode, 1, different.stdout + different.stderr)


class RenderedLeakageTests(unittest.TestCase):
    @staticmethod
    def write_policy(root: Path) -> None:
        policy = root / "environments" / "qa-policy.yml"
        policy.parent.mkdir(parents=True)
        policy.write_text(
            "restricted_markers: [RESTRICTED-SOLUTION]\n"
            "size_budgets_bytes: {html_per_page: 100000, slide_deck: 100000, pdf_per_document: 1000000, offline_bundle: 2000000}\n"
            "print: {page_size: A4, max_blank_pages: 1, max_pages_per_document: 120}\n",
            encoding="utf-8",
        )

    def test_restricted_marker_in_rendered_html_fails_output_gate(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self.write_policy(root)
            output = root / "build" / "en" / "html" / "leak.html"
            output.parent.mkdir(parents=True)
            output.write_text(
                '<!doctype html><html lang="en"><style>body{font-family:sans-serif}</style>'
                '<body>RESTRICTED-SOLUTION</body></html>',
                encoding="utf-8",
            )
            completed = subprocess.run(
                [sys.executable, str(SCRIPTS / "check_outputs.py"), "--root", str(root)],
                capture_output=True,
                text=True,
                check=False,
            )
            self.assertEqual(completed.returncode, 1, completed.stdout + completed.stderr)
            self.assertIn("restricted marker", completed.stdout)

    def test_restricted_marker_in_rendered_pdf_fails_output_gate(self) -> None:
        if not all(shutil.which(tool) for tool in ("pandoc", "xelatex", "pdftotext")):
            self.skipTest("PDF toolchain unavailable")
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            self.write_policy(root)
            source = root / "leak.md"
            output = root / "build" / "en" / "pdf" / "leak.pdf"
            output.parent.mkdir(parents=True)
            source.write_text("---\ntitle: Leak\n---\n\nRESTRICTED-SOLUTION\n", encoding="utf-8")
            subprocess.run(["pandoc", str(source), "--pdf-engine", "xelatex", "-o", str(output)], check=True)
            completed = subprocess.run(
                [sys.executable, str(SCRIPTS / "check_outputs.py"), "--root", str(root)],
                capture_output=True,
                text=True,
                check=False,
            )
            self.assertEqual(completed.returncode, 1, completed.stdout + completed.stderr)
            self.assertIn("rendered PDF", completed.stdout)


if __name__ == "__main__":
    unittest.main()
