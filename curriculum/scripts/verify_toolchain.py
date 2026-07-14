#!/usr/bin/env python3
"""Report frozen tool availability and host evidence without claiming a benchmark."""

from __future__ import annotations

import argparse
import platform
import shutil
import subprocess
import sys
from pathlib import Path

import yaml

from scriptlib import CURRICULUM, dump_json, load_yaml, version_tuple


COMMANDS = {"python": [sys.executable, "--version"], "quarto": ["quarto", "--version"], "pandoc": ["pandoc", "--version"], "xelatex": ["xelatex", "--version"], "kicad_cli": ["kicad-cli", "version"], "imagemagick": ["magick", "--version"], "poppler": ["pdfinfo", "-v"]}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=CURRICULUM)
    parser.add_argument("--require-release", action="store_true", help="fail if release-only dependencies are absent")
    args = parser.parse_args()
    root = args.root.resolve()
    contract = load_yaml(root / "environments" / "toolchain.yml") or {}
    results: dict[str, dict] = {}
    errors: list[str] = []
    for tool, declaration in contract.get("tools", {}).items():
        if tool == "pyyaml":
            found, output = True, yaml.__version__
        elif tool == "svg_converter":
            command = next(
                (
                    candidate
                    for candidate in (("rsvg-convert", "--version"), ("inkscape", "--version"))
                    if shutil.which(candidate[0])
                ),
                None,
            )
            found, output = bool(command), ""
            if command:
                completed = subprocess.run(command, capture_output=True, text=True, check=False)
                output = (completed.stdout or completed.stderr).splitlines()[0]
        else:
            command = COMMANDS.get(tool)
            executable = shutil.which(command[0]) if command else None
            found, output = bool(executable), ""
            if found:
                completed = subprocess.run(command, capture_output=True, text=True, check=False)
                output = (completed.stdout or completed.stderr).splitlines()[0]
        required = declaration.get("required", False) or declaration.get("required_for_offline_fallback", False) or (args.require_release and declaration.get("required_for_release", False))
        if required and not found:
            errors.append(f"{tool} is required but unavailable")
        results[tool] = {"found": found, "reported": output, "tested": declaration.get("tested"), "required_now": bool(required)}
        print(f"{'OK' if found else 'MISSING'} {tool}: {output or '-'}")
    report = {"host": {"os": platform.platform(), "machine": platform.machine(), "python": platform.python_version()}, "tools": results, "errors": errors, "benchmark_claim": "none; physical profile evidence remains required"}
    dump_json(root / "build" / "reports" / "toolchain.json", report)
    for error in errors:
        print(f"ERROR {error}", file=sys.stderr)
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
