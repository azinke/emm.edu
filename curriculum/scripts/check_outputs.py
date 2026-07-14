#!/usr/bin/env python3
"""Apply rendering, print-readiness, bilingual, and low-bandwidth output gates."""

from __future__ import annotations

import argparse
import re
import shutil
import sys
from pathlib import Path

from scriptlib import CURRICULUM, load_yaml, run_command


REMOTE_ASSET_RE = re.compile(r"<(?:img|script|iframe)\b[^>]*\bsrc=[\"'](?:https?:)?//|<link\b[^>]*\bhref=[\"'](?:https?:)?//|url\([\"']?(?:https?:)?//", re.I)


def pdf_pages(path: Path) -> int | None:
    if shutil.which("pdfinfo"):
        result = run_command(["pdfinfo", str(path)], cwd=path.parent)
        match = re.search(r"^Pages:\s+(\d+)", result.stdout, re.M)
        return int(match.group(1)) if match else None
    data = path.read_bytes()
    return len(re.findall(rb"/Type\s*/Page\b", data)) or None


def unembedded_fonts(output: str) -> list[str]:
    rows = [line.split() for line in output.splitlines()[2:] if line.strip()]
    return [row[0] for row in rows if len(row) >= 5 and row[-5].lower() != "yes"]


def check_pdf(path: Path, root: Path, policy: dict, errors: list[str]) -> None:
    label = path.relative_to(root)
    if not path.read_bytes().startswith(b"%PDF-"):
        errors.append(f"PDF {label}: invalid PDF signature")
        return
    pages = pdf_pages(path)
    if not pages:
        errors.append(f"PDF {label}: could not establish page count")
    elif pages > int(policy.get("print", {}).get("max_pages_per_document", 120)):
        errors.append(f"PRINT {label}: {pages} pages exceeds policy")
    if shutil.which("pdfinfo"):
        info = run_command(["pdfinfo", str(path)], cwd=path.parent)
        size = re.search(r"^Page size:\s+([0-9.]+) x ([0-9.]+) pts", info.stdout, re.M)
        if size and not (590 <= float(size.group(1)) <= 600 and 837 <= float(size.group(2)) <= 847):
            errors.append(f"PRINT {label}: expected A4, found {size.group(1)} x {size.group(2)} pt")
    if shutil.which("pdffonts"):
        fonts = run_command(["pdffonts", str(path)], cwd=path.parent)
        font_rows = [line.split() for line in fonts.stdout.splitlines()[2:] if line.strip()]
        if not font_rows:
            errors.append(f"FONT {label}: no embedded font evidence")
        for font in unembedded_fonts(fonts.stdout):
            errors.append(f"FONT {label}: font {font} is not embedded")
    if shutil.which("pdftotext"):
        text = run_command(["pdftotext", "-layout", str(path), "-"], cwd=path.parent)
        if text.returncode:
            errors.append(f"RESTRICT {label}: PDF text extraction failed; leakage scan cannot pass")
            return
        lowered = text.stdout.lower()
        for marker in policy.get("restricted_markers", []):
            if str(marker).lower() in lowered:
                errors.append(f"RESTRICT {label}: restricted marker {marker!r} in rendered PDF")
        extracted_pages = text.stdout.split("\f")
        if extracted_pages and not extracted_pages[-1]:
            extracted_pages.pop()
        blank_pages = sum(not page.strip() for page in extracted_pages)
        allowed = int(policy.get("print", {}).get("max_blank_pages", 1))
        if blank_pages > allowed:
            errors.append(f"PRINT {label}: {blank_pages} blank pages exceeds {allowed}")
    else:
        errors.append(f"RESTRICT {label}: pdftotext is required for PDF leakage scanning")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=CURRICULUM)
    args = parser.parse_args()
    root = args.root.resolve()
    policy = load_yaml(root / "environments" / "qa-policy.yml") or {}
    budgets = policy.get("size_budgets_bytes", {})
    errors: list[str] = []
    products = 0
    for language in ("en", "fr"):
        for format_name, pattern, budget_key in (("html", "*.html", "html_per_page"), ("slides", "*.html", "slide_deck"), ("pdf", "*.pdf", "pdf_per_document")):
            directory = root / "build" / language / format_name
            for path in sorted(directory.rglob(pattern)) if directory.exists() else []:
                products += 1
                budget = int(budgets.get(budget_key, 2**63 - 1))
                if path.stat().st_size > budget:
                    errors.append(f"SIZE {path.relative_to(root)}: {path.stat().st_size} > {budget} bytes")
                if path.suffix == ".html":
                    text = path.read_text(encoding="utf-8", errors="replace")
                    lowered = text.lower()
                    for marker in policy.get("restricted_markers", []):
                        if str(marker).lower() in lowered:
                            errors.append(f"RESTRICT {path.relative_to(root)}: restricted marker {marker!r} in rendered output")
                    if REMOTE_ASSET_RE.search(text):
                        errors.append(f"OFFLINE {path.relative_to(root)}: remote asset reference remains")
                    declared = re.search(r"<html[^>]+lang=[\"']([^\"']+)", text, re.I)
                    if not declared or not declared.group(1).lower().startswith(language):
                        errors.append(f"LANG {path.relative_to(root)}: missing/wrong HTML language")
                    if re.search(r"(?:\\\(|\\\[|\$\$).+?(?:\\\)|\\\]|\$\$)", text, re.S) and not re.search(r"<math[ >]", text, re.I):
                        errors.append(f"MATH {path.relative_to(root)}: source math present without MathML")
                    if not re.search(r"font-family\s*:", text, re.I):
                        errors.append(f"FONT {path.relative_to(root)}: no explicit bilingual-capable font stack")
                    if "<img" in text and not re.search(r"<(?:figcaption|p class=[\"']caption)", text, re.I):
                        errors.append(f"CAPTION {path.relative_to(root)}: rendered image lacks visible caption")
                    if re.search(r"class=[\"'][^\"']*mermaid", text, re.I) and "<svg" not in text:
                        errors.append(f"SCHEMATIC {path.relative_to(root)}: Mermaid content lacks a static SVG fallback")
                else:
                    check_pdf(path, root, policy, errors)
    bundle_budget = int(budgets.get("offline_bundle", 2**63 - 1))
    bundle_size = sum(path.stat().st_size for path in (root / "build").rglob("*") if path.is_file())
    if bundle_size > bundle_budget:
        errors.append(f"SIZE build: {bundle_size} > {bundle_budget} bytes")
    for error in errors:
        print(f"ERROR {error}")
    print(f"OUTPUT-QA products={products} bundle_bytes={bundle_size} errors={len(errors)}")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
