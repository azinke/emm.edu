#!/usr/bin/env python3
"""Discover and execute code/numerical/HDL/simulation/KiCad smoke hook manifests."""

from __future__ import annotations

import argparse
import os
import shutil
import sys
import xml.etree.ElementTree as ET
from pathlib import Path
from typing import Any

from scriptlib import CURRICULUM, REPOSITORY, dump_json, isolated_environment, load_yaml, run_command


ALLOWED = {"code", "numerical", "hdl", "simulation", "kicad"}


def discover(root: Path, explicit: list[Path]) -> list[Path]:
    if explicit:
        return [path.resolve() for path in explicit]
    courses = root / "courses"
    return sorted(courses.rglob("smoke-hooks.yml")) if courses.exists() else []


def expand(value: str, manifest: Path, report_dir: Path) -> str:
    return value.format(repository=REPOSITORY, manifest_dir=manifest.parent, report_dir=report_dir)


def validate_hook(hook: Any, manifest: Path) -> list[str]:
    if not isinstance(hook, dict):
        return [f"{manifest}: hook must be a mapping"]
    errors = []
    for field in ("id", "kind", "command", "working_directory", "requires", "timeout_seconds"):
        if field not in hook:
            errors.append(f"{manifest}: hook missing {field}")
    if hook.get("kind") not in ALLOWED:
        errors.append(f"{manifest}: invalid hook kind {hook.get('kind')!r}")
    if not isinstance(hook.get("command"), list) or not hook.get("command") or not all(isinstance(item, str) for item in hook.get("command", [])):
        errors.append(f"{manifest}: command must be a non-empty argv list")
    if hook.get("network", False):
        errors.append(f"{manifest}: smoke hooks may not request network")
    return errors


def junit(results: list[dict], path: Path) -> None:
    suite = ET.Element("testsuite", name="content-smoke-hooks", tests=str(len(results)), failures=str(sum(item["status"] != "pass" for item in results)))
    for item in results:
        case = ET.SubElement(suite, "testcase", name=item["id"], classname=item["kind"], time=str(item.get("duration_seconds", 0)))
        if item["status"] != "pass":
            failure = ET.SubElement(case, "failure", message=item.get("reason", "command failed"))
            failure.text = item.get("stderr", "")
        ET.SubElement(case, "system-out").text = item.get("stdout", "")
    path.parent.mkdir(parents=True, exist_ok=True)
    ET.ElementTree(suite).write(path, encoding="utf-8", xml_declaration=True)


def run(root: Path, manifests: list[Path], requested_kind: str) -> tuple[list[dict], list[str]]:
    results: list[dict] = []
    errors: list[str] = []
    report_dir = root / "build" / "reports" / "smoke"
    report_dir.mkdir(parents=True, exist_ok=True)
    for manifest in manifests:
        data = load_yaml(manifest) or {}
        hooks = data.get("hooks", []) if isinstance(data, dict) else []
        for hook in hooks:
            hook_errors = validate_hook(hook, manifest)
            errors.extend(hook_errors)
            if hook_errors or (requested_kind != "all" and hook.get("kind") != requested_kind):
                continue
            missing = [tool for tool in hook.get("requires", []) if not shutil.which(str(tool))]
            required = bool(hook.get("required", True))
            if missing:
                status = "fail" if required else "skip"
                reason = f"missing dependencies: {', '.join(missing)}"
                results.append({"id": hook["id"], "kind": hook["kind"], "status": status, "reason": reason, "manifest": str(manifest)})
                if required:
                    errors.append(f"{hook['id']}: {reason}")
                continue
            command = [expand(item, manifest, report_dir) for item in hook["command"]]
            working = Path(expand(str(hook["working_directory"]), manifest, report_dir))
            if not working.is_absolute():
                working = manifest.parent / working
            env = isolated_environment(report_dir / ".xdg" / hook["id"])
            result = run_command(command, cwd=working.resolve(), timeout=int(hook["timeout_seconds"]), env=env)
            status = "pass" if result.returncode == 0 else "fail"
            record = {"id": hook["id"], "kind": hook["kind"], "manifest": str(manifest), "status": status, **result.__dict__}
            results.append(record)
            if status == "fail":
                errors.append(f"{hook['id']}: exit {result.returncode}")
    return results, errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=CURRICULUM)
    parser.add_argument("--manifest", type=Path, action="append", default=[])
    parser.add_argument("--kind", choices=("all", *sorted(ALLOWED)), default="all")
    args = parser.parse_args()
    root = args.root.resolve()
    manifests = discover(root, args.manifest)
    results, errors = run(root, manifests, args.kind)
    report_dir = root / "build" / "reports"
    dump_json(report_dir / "smoke-hooks.json", {"manifests": [str(item) for item in manifests], "results": results, "errors": errors})
    junit(results, report_dir / "smoke-hooks.xml")
    for item in results:
        print(f"{item['status'].upper()} {item['kind']} {item['id']}{': ' + item.get('reason', '') if item.get('reason') else ''}")
    for error in errors:
        print(f"ERROR {error}", file=sys.stderr)
    print(f"SMOKE manifests={len(manifests)} hooks={len(results)} errors={len(errors)}")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
