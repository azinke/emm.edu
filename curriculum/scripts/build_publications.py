#!/usr/bin/env python3
"""Build distinct EN/FR HTML, PDF, and slide products without network access."""

from __future__ import annotations

import argparse
import os
import re
import shutil
import sys
from pathlib import Path

from scriptlib import CURRICULUM, dump_json, isolated_environment, run_command


FORMATS = ("html", "pdf", "slides")
LANGUAGES = ("en", "fr")
PANDOC_SVG_SHIM = CURRICULUM / "scripts" / "tool-shims" / "rsvg-convert"
REMOTE_RESOURCE_RE = re.compile(
    r"!\[[^]]*\]\(\s*https?://|<(?:img|script|link)\b[^>]*(?:src|href)=[\"']\s*(?:https?:)?//|@import\s+(?:url\()?['\"]?https?://",
    re.I,
)


def sources(root: Path, language: str, slides: bool) -> list[Path]:
    result: list[Path] = []
    for extension in ("*.qmd", "*.md"):
        for path in (root / "courses").glob(f"**/{language}/**/{extension}"):
            is_slide = "slides" in path.parts
            if is_slide == slides and not any(part.startswith(".") for part in path.relative_to(root).parts):
                result.append(path)
    return sorted(set(result))


def destination(root: Path, language: str, format_name: str, source: Path, suffix: str) -> Path:
    relative = source.relative_to(root / "courses")
    without_language = Path(*(part for part in relative.parts if part != language))
    return root / "build" / language / format_name / without_language.with_suffix(suffix)


def pandoc_command(
    source: Path,
    output: Path,
    language: str,
    format_name: str,
    root: Path,
    latex_template: Path | None = None,
) -> list[str]:
    source_text = source.read_text(encoding="utf-8")
    heading = re.search(r"^#\s+(.+)$", source_text, re.M)
    fallback_title = heading.group(1).strip() if heading else source.stem.replace("-", " ").title()
    common = [
        "pandoc", str(source), "--from", "markdown+tex_math_single_backslash",
        "--standalone", "--metadata", f"lang={language}", "--metadata", f"title={fallback_title}",
        "--resource-path", os.pathsep.join((str(source.parent), str(root))),
        "--fail-if-warnings",
    ]
    if format_name == "html":
        return common + ["--to", "html5", "--embed-resources", "--mathml", "--output", str(output)]
    if format_name == "slides":
        return common + ["--to", "html5", "--embed-resources", "--mathml", "--section-divs", "--template", str(CURRICULUM / "environments" / "pandoc-slides.html"), "--output", str(output)]
    pdf = common + ["--to", "pdf", "--pdf-engine", "xelatex", "--variable", "papersize=a4", "--variable", "geometry:margin=22mm"]
    if latex_template:
        pdf += ["--template", str(latex_template)]
    return pdf + ["--output", str(output)]


def pandoc_latex_template(root: Path, env: dict[str, str]) -> tuple[Path | None, str | None]:
    """Make Pandoc's long-table footnote enhancement optional on minimal TeX installs."""
    if shutil.which("kpsewhich"):
        for package in ("footnotehyper.sty", "footnote.sty"):
            lookup = run_command(["kpsewhich", package], cwd=root, env=env)
            if lookup.returncode == 0 and lookup.stdout.strip():
                return None, None

    default = run_command(
        ["pandoc", "--print-default-data-file=templates/default.latex"],
        cwd=root,
        env=env,
    )
    if default.returncode:
        return None, default.stderr.strip() or "Pandoc did not provide its default LaTeX template"
    original = r"\IfFileExists{footnotehyper.sty}{\usepackage{footnotehyper}}{\usepackage{footnote}}"
    replacement = (
        r"\IfFileExists{footnotehyper.sty}{\usepackage{footnotehyper}}{%" "\n"
        r"  \IfFileExists{footnote.sty}{\usepackage{footnote}}{\providecommand{\makesavenoteenv}[1]{}}%" "\n"
        r"}"
    )
    if original not in default.stdout:
        return None, "Pandoc's LaTeX template has an unsupported long-table footnote block"
    template = root / "build" / ".pandoc" / "default.latex"
    template.parent.mkdir(parents=True, exist_ok=True)
    template.write_text(default.stdout.replace(original, replacement, 1), encoding="utf-8")
    return template, None


def reject_remote_resources(root: Path, languages: list[str]) -> list[str]:
    errors: list[str] = []
    for language in languages:
        for source in sorted(set(sources(root, language, False) + sources(root, language, True))):
            text = source.read_text(encoding="utf-8")
            if REMOTE_RESOURCE_RE.search(text):
                errors.append(f"{source.relative_to(root)} contains a remote build resource; archive it locally")
    return errors


def needs_svg_conversion(root: Path, languages: list[str]) -> bool:
    return any(
        ".svg" in source.read_text(encoding="utf-8").lower()
        for language in languages
        for source in sources(root, language, False)
    )


def build_pandoc(root: Path, languages: list[str], formats: list[str], report: list[dict]) -> int:
    required = ["pandoc"] + (["xelatex"] if "pdf" in formats else [])
    missing = [tool for tool in required if not shutil.which(tool)]
    if (
        "pdf" in formats
        and needs_svg_conversion(root, languages)
        and not shutil.which("rsvg-convert")
        and not shutil.which("inkscape")
    ):
        missing.append("rsvg-convert or inkscape")
    if missing:
        print(f"ERROR missing Pandoc fallback dependencies: {', '.join(missing)}", file=sys.stderr)
        return 2
    env = isolated_environment(root / "build" / ".xdg")
    if "pdf" in formats and not shutil.which("rsvg-convert") and shutil.which("inkscape"):
        env["PATH"] = os.pathsep.join((str(PANDOC_SVG_SHIM.parent), env["PATH"]))
        print("INFO using the installed Inkscape as Pandoc's SVG-to-PDF fallback")
    latex_template = None
    if "pdf" in formats:
        latex_template, template_error = pandoc_latex_template(root, env)
        if template_error:
            print(f"ERROR cannot prepare Pandoc LaTeX template: {template_error}", file=sys.stderr)
            return 2
        if latex_template:
            print("INFO TeX footnote package unavailable; using the safe long-table template fallback")
    failures = 0
    for language in languages:
        for format_name in formats:
            candidates = sources(root, language, format_name == "slides")
            for source in candidates:
                suffix = ".pdf" if format_name == "pdf" else ".html"
                output = destination(root, language, format_name, source, suffix)
                output.parent.mkdir(parents=True, exist_ok=True)
                result = run_command(
                    pandoc_command(source, output, language, format_name, root, latex_template),
                    cwd=root,
                    env=env,
                )
                report.append({"engine": "pandoc", "language": language, "format": format_name, "source": str(source.relative_to(root)), "output": str(output.relative_to(root)), **result.__dict__})
                if result.returncode:
                    failures += 1
                    print(f"ERROR pandoc {language}/{format_name} {source}: {result.stderr.strip()}", file=sys.stderr)
    return 1 if failures else 0


def build_quarto(root: Path, languages: list[str], formats: list[str], report: list[dict]) -> int:
    if not shutil.which("quarto"):
        print("ERROR Quarto is not installed; release build cannot run", file=sys.stderr)
        return 2
    failures = 0
    env = isolated_environment(root / "build" / ".xdg")
    env["QUARTO_DENO_EXTRA_OPTIONS"] = "--cached-only"
    for language in languages:
        for format_name in formats:
            candidates = sources(root, language, format_name == "slides")
            quarto_format = "revealjs" if format_name == "slides" else format_name
            for source in candidates:
                suffix = ".pdf" if format_name == "pdf" else ".html"
                output = destination(root, language, format_name, source, suffix)
                output.parent.mkdir(parents=True, exist_ok=True)
                command = ["quarto", "render", str(source), "--profile", language, "--to", quarto_format, "--output-dir", str(output.parent)]
                if format_name in {"html", "slides"}:
                    command += ["--embed-resources"]
                result = run_command(command, cwd=root, env=env)
                report.append({"engine": "quarto", "language": language, "format": format_name, "source": str(source.relative_to(root)), "output": str(output.relative_to(root)), **result.__dict__})
                if result.returncode:
                    failures += 1
                    print(f"ERROR quarto {language}/{format_name} {source}: {result.stderr.strip()}", file=sys.stderr)
    return 1 if failures else 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=CURRICULUM)
    parser.add_argument("--engine", choices=("auto", "quarto", "pandoc"), default="auto")
    parser.add_argument("--language", choices=("all", *LANGUAGES), default="all")
    parser.add_argument("--format", choices=("all", *FORMATS), default="all")
    parser.add_argument("--offline", action="store_true", help="documented invariant; all build subprocesses are isolated and network-free")
    args = parser.parse_args()
    root = args.root.resolve()
    languages = list(LANGUAGES) if args.language == "all" else [args.language]
    formats = list(FORMATS) if args.format == "all" else [args.format]
    resource_errors = reject_remote_resources(root, languages)
    if resource_errors:
        for error in resource_errors:
            print(f"ERROR OFFLINE {error}", file=sys.stderr)
        return 2
    engine = args.engine
    if engine == "auto":
        engine = "quarto" if shutil.which("quarto") else "pandoc"
        print(f"INFO selected {engine} engine")
    report: list[dict] = []
    status = build_quarto(root, languages, formats, report) if engine == "quarto" else build_pandoc(root, languages, formats, report)
    report_path = root / "build" / "reports" / "publication-build.json"
    dump_json(report_path, {"engine": engine, "offline": True, "runs": report})
    counts = {format_name: sum(run["format"] == format_name and run["returncode"] == 0 for run in report) for format_name in formats}
    print(f"BUILD engine={engine} products={counts} status={'pass' if status == 0 else 'fail'}")
    return status


if __name__ == "__main__":
    sys.exit(main())
