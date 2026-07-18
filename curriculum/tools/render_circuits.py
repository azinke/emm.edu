#!/usr/bin/env python3
"""Render canonical CircuitikZ source to build-only PDF and PNG artifacts."""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
import tomllib
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
CIRCUIT_DIR = ROOT / "curriculum" / "circuits"
BUILD_DIR = ROOT / "build" / "circuits"
PUBLISH_DIR = ROOT / "curriculum" / "book" / "figures"


def require_tool(name: str) -> str:
    path = shutil.which(name)
    if path is None:
        raise RuntimeError(f"required tool not found: {name}")
    return path


def require_tex_packages(kpsewhich: str) -> None:
    for package in ("standalone.cls", "circuitikz.sty", "siunitx.sty"):
        result = subprocess.run(
            [kpsewhich, package], check=False, capture_output=True, text=True
        )
        if result.returncode != 0 or not result.stdout.strip():
            raise RuntimeError(f"required TeX package not found: {package}")


def render(circuit_id: str, source: Path, xelatex: str, pdftoppm: str) -> Path:
    BUILD_DIR.mkdir(parents=True, exist_ok=True)
    subprocess.run(
        [
            xelatex,
            "-halt-on-error",
            "-interaction=nonstopmode",
            f"-jobname={circuit_id}",
            f"-output-directory={BUILD_DIR}",
            str(source),
        ],
        cwd=ROOT,
        check=True,
    )
    pdf = BUILD_DIR / f"{circuit_id}.pdf"
    subprocess.run(
        [
            pdftoppm,
            "-png",
            "-singlefile",
            "-r",
            "240",
            str(pdf),
            str(BUILD_DIR / circuit_id),
        ],
        check=True,
    )
    return BUILD_DIR / f"{circuit_id}.png"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--id", help="render only one circuit ID")
    parser.add_argument(
        "--publish",
        action="store_true",
        help="also copy the PNG to curriculum/book/figures",
    )
    parser.add_argument(
        "--check-tools", action="store_true", help="check dependencies without rendering"
    )
    args = parser.parse_args()

    try:
        xelatex = require_tool("xelatex")
        pdftoppm = require_tool("pdftoppm")
        kpsewhich = require_tool("kpsewhich")
        require_tex_packages(kpsewhich)
        if args.check_tools:
            print("circuit tools available")
            return 0

        catalog = tomllib.loads((CIRCUIT_DIR / "catalog.toml").read_text())
        records = catalog["circuit"]
        selected = [record for record in records if args.id in (None, record["id"])]
        if args.id and not selected:
            raise RuntimeError(f"unknown circuit ID: {args.id}")

        for record in selected:
            source = CIRCUIT_DIR / record["source"]
            print(f"rendering {record['id']} from {source.relative_to(ROOT)}")
            png = render(record["id"], source, xelatex, pdftoppm)
            if args.publish:
                PUBLISH_DIR.mkdir(parents=True, exist_ok=True)
                published = PUBLISH_DIR / png.name
                shutil.copy2(png, published)
                print(f"published {published.relative_to(ROOT)}")
    except (OSError, KeyError, RuntimeError, subprocess.CalledProcessError) as error:
        print(f"circuit render failed: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
