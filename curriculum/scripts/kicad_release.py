#!/usr/bin/env python3
"""Enforce the frozen KiCad ERC/DRC, waiver, and release-output contract."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import shutil
import sys
from pathlib import Path
from typing import Any

from scriptlib import CURRICULUM, dump_json, isolated_environment, load_yaml, run_command, sha256_file, version_tuple


def validate_waivers(project: Path, contract: dict[str, Any], revision: str | None) -> tuple[list[dict[str, Any]], list[str]]:
    waiver_contract = contract.get("waiver", {})
    path = project / waiver_contract.get("filename", "kicad-waivers.yml")
    if not path.exists():
        return [], []
    data = load_yaml(path) or {}
    waivers = data.get("waivers", []) if isinstance(data, dict) else []
    errors: list[str] = []
    required = waiver_contract.get("required_fields", [])
    allowed_roles = set(waiver_contract.get("approval_roles", []))
    today = dt.date.today()
    for waiver in waivers:
        if not isinstance(waiver, dict):
            errors.append("waiver entry must be a mapping")
            continue
        identity = waiver.get("id", "<missing-id>")
        missing = [field for field in required if waiver.get(field) in (None, "", [])]
        if missing:
            errors.append(f"waiver {identity} missing {', '.join(missing)}")
            continue
        if waiver.get("approved_by") not in allowed_roles:
            errors.append(f"waiver {identity} approved_by is not an authorized role")
        try:
            if dt.date.fromisoformat(str(waiver["expires_on"])) < today:
                errors.append(f"waiver {identity} expired on {waiver['expires_on']}")
        except ValueError:
            errors.append(f"waiver {identity} has invalid expires_on")
        if revision and waiver.get("affected_revision") != revision:
            errors.append(f"waiver {identity} does not match project revision {revision}")
    return [waiver for waiver in waivers if isinstance(waiver, dict)], errors


def report_has_exclusions(path: Path) -> bool:
    if not path.exists():
        return False
    text = path.read_text(encoding="utf-8", errors="replace")
    try:
        value = json.loads(text)
        if value.get("exclusions") or value.get("excluded_violations"):
            return True
        return any(item.get("severity") == "exclusion" for key in ("violations", "unconnected_items", "schematic_parity") for item in value.get(key, []) if isinstance(item, dict))
    except (json.JSONDecodeError, AttributeError):
        return bool(re.search(r"\bexcluded\b", text, re.I))


def report_violations(path: Path) -> list[dict[str, Any]] | None:
    """Return normalized KiCad violations, or None when the report is unreadable."""
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None
    normalized: list[dict[str, Any]] = []
    for section in ("violations", "unconnected_items", "schematic_parity"):
        for violation in value.get(section, []) or []:
            if not isinstance(violation, dict):
                continue
            uuids = sorted(
                item["uuid"]
                for item in violation.get("items", []) or []
                if isinstance(item, dict) and isinstance(item.get("uuid"), str)
            )
            normalized.append(
                {
                    "rule": str(violation.get("type", section)),
                    "exact_item": uuids,
                    "severity": violation.get("severity"),
                    "description": violation.get("description", ""),
                    "section": section,
                }
            )
    return normalized


def waiver_matches(waiver: dict[str, Any], check: str, violation: dict[str, Any], revision: str | None) -> bool:
    exact = waiver.get("exact_item")
    if isinstance(exact, str):
        exact = [exact]
    return (
        waiver.get("check") == check
        and waiver.get("rule") == violation.get("rule")
        and sorted(exact or []) == violation.get("exact_item")
        and (not revision or waiver.get("affected_revision") == revision)
    )


def release_artifact_candidates(project: Path) -> dict[str, bool]:
    patterns = {
        "schematic_pdf": ["*.sch.pdf", "*-schematic.pdf"],
        "pcb_pdf": ["*.pcb.pdf", "*-pcb.pdf"],
        "gerbers": ["*.gbr", "*.gtl", "*.gbl"],
        "drill_files": ["*.drl"],
        "bom": ["*bom*.csv", "*bom*.tsv"],
        "position_files": ["*pos*.csv", "*.pos"],
        "assembly_drawing": ["*assembly*.pdf"],
    }
    return {name: any(any(project.rglob(pattern)) for pattern in patterns) for name, patterns in patterns.items()}


def run(project: Path, contract_path: Path, report_dir: Path, require_release: bool) -> tuple[bool, dict[str, Any]]:
    contract = load_yaml(contract_path) or {}
    result: dict[str, Any] = {"project": str(project), "contract": str(contract_path), "owner": contract.get("owner"), "checks": [], "errors": []}
    executable = shutil.which("kicad-cli")
    if not executable:
        result["errors"].append("kicad-cli is unavailable")
        return False, result
    env = isolated_environment(report_dir / ".xdg")
    version_result = run_command([executable, "version"], cwd=project, env=env)
    version = version_tuple(version_result.stdout + version_result.stderr)
    result["tool_version"] = (version_result.stdout or version_result.stderr).strip()
    if not version or version[0] != int(contract.get("supported_major", -1)):
        result["errors"].append(f"KiCad major {version[0] if version else 'unknown'} is not frozen major {contract.get('supported_major')}")
    minimum = version_tuple(str(contract.get("minimum_version", "0.0.0")))
    if version and version < minimum:
        result["errors"].append(f"KiCad {version} is below minimum {minimum}")
    schematics = sorted(project.glob("*.kicad_sch"))
    boards = sorted(project.glob("*.kicad_pcb"))
    if not schematics and not boards:
        result["errors"].append("no .kicad_sch or .kicad_pcb found")
    report_dir.mkdir(parents=True, exist_ok=True)
    project_metadata = load_yaml(project / "release.yml") if (project / "release.yml").exists() else {}
    revision = project_metadata.get("revision") if isinstance(project_metadata, dict) else None
    waivers, waiver_errors = validate_waivers(project, contract, revision)
    result["errors"].extend(waiver_errors)
    used_waivers: set[str] = set()
    for check, paths in (("erc", schematics), ("drc", boards)):
        for source in paths:
            report_path = report_dir / f"{source.stem}-{check}.json"
            command = [executable, "sch" if check == "erc" else "pcb", check, "--format", "json", "--severity-all"]
            if check == "drc" and schematics:
                command.append("--schematic-parity")
            command += ["--exit-code-violations", "--output", str(report_path), str(source)]
            command_result = run_command(command, cwd=project, timeout=180, env=env)
            record = {"check": check, "source": source.name, "report": str(report_path), **command_result.__dict__}
            violations = report_violations(report_path)
            unwaived: list[dict[str, Any]] = []
            if violations is not None:
                for violation in violations:
                    matches = [waiver for waiver in waivers if waiver_matches(waiver, check, violation, revision)]
                    if matches:
                        used_waivers.update(str(waiver.get("id")) for waiver in matches)
                    else:
                        unwaived.append(violation)
                record["violations"] = violations
                record["unwaived_violations"] = unwaived
            result["checks"].append(record)
            if violations is None and command_result.returncode:
                result["errors"].append(f"{check.upper()} execution/report failure for {source.name} (exit {command_result.returncode})")
            elif unwaived:
                rules = ", ".join(sorted({item["rule"] for item in unwaived}))
                result["errors"].append(f"{check.upper()} has {len(unwaived)} unwaived violation(s) for {source.name}: {rules}")
            if report_has_exclusions(report_path) and not (project / contract.get("waiver", {}).get("filename", "kicad-waivers.yml")).exists():
                result["errors"].append(f"{check.upper()} contains native exclusions without waiver manifest")
    result["used_waivers"] = sorted(used_waivers)
    unused = sorted(str(waiver.get("id")) for waiver in waivers if str(waiver.get("id")) not in used_waivers)
    if unused:
        result["errors"].append(f"waivers do not match a reported violation: {', '.join(unused)}")
    if require_release:
        if not schematics or not boards:
            result["errors"].append("release gate requires both schematic and PCB source")
        present = release_artifact_candidates(project)
        result["release_artifacts"] = present
        for name, found in present.items():
            if not found:
                result["errors"].append(f"missing release artifact: {name}")
        if not revision:
            result["errors"].append("release.yml with revision is required")
    manifest_files = [path for path in project.rglob("*") if path.is_file() and not str(path).startswith(str(report_dir))]
    result["sha256_manifest"] = {str(path.relative_to(project)): sha256_file(path) for path in sorted(manifest_files)}
    manifest_path = report_dir / "release-manifest.sha256"
    manifest_path.write_text(
        "".join(f"{checksum}  {relative}\n" for relative, checksum in result["sha256_manifest"].items()),
        encoding="utf-8",
    )
    result["release_manifest"] = str(manifest_path)
    if require_release:
        result["release_artifacts"].update(
            {
                "erc_json": bool(schematics) and all(Path(item["report"]).exists() for item in result["checks"] if item["check"] == "erc"),
                "drc_json": bool(boards) and all(Path(item["report"]).exists() for item in result["checks"] if item["check"] == "drc"),
                "release_manifest_sha256": manifest_path.exists(),
            }
        )
    return not result["errors"], result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project", type=Path)
    parser.add_argument("--contract", type=Path, default=CURRICULUM / "environments" / "kicad-contract.yml")
    parser.add_argument("--report-dir", type=Path)
    parser.add_argument("--require-release", action="store_true")
    parser.add_argument("--expect", choices=("pass", "fail"), default="pass")
    args = parser.parse_args()
    project = args.project.resolve()
    report_dir = (args.report_dir or CURRICULUM / "build" / "reports" / "kicad" / project.name).resolve()
    passed, report = run(project, args.contract.resolve(), report_dir, args.require_release)
    dump_json(report_dir / "contract-result.json", report)
    observed = "pass" if passed else "fail"
    print(f"KICAD observed={observed} expected={args.expect} checks={len(report['checks'])} owner={report.get('owner')}")
    for error in report["errors"]:
        print(f"ERROR {error}")
    return 0 if observed == args.expect else 1


if __name__ == "__main__":
    sys.exit(main())
