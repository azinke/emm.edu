#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Reject unsupported M04 task completion and release-state claims."""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Any

import yaml


PHYSICAL_TASKS = {"M04-E3-T02", "M04-E3-T03", "M04-E3-T04", "M04-E4-T01", "M04-E4-T02", "M04-E4-T03"}
APPROVED_FACETS = {"approved", "approved-with-conditions"}


def validate(record: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    all_tasks: dict[str, Any] = {}
    for section in ("e3_tasks", "e4_tasks"):
        tasks = record.get(section, {})
        if not isinstance(tasks, dict):
            errors.append(f"{section} must be a mapping")
            continue
        all_tasks.update(tasks)
    for task_id, task in all_tasks.items():
        if not isinstance(task, dict):
            errors.append(f"{task_id} must be a mapping")
            continue
        status = task.get("status")
        if status not in {"pending", "complete"}:
            errors.append(f"{task_id} has invalid status {status!r}")
        if status == "complete":
            evidence = task.get("evidence", [])
            reviewer = str(task.get("reviewer", ""))
            if not evidence:
                errors.append(f"{task_id} complete without evidence")
            if not reviewer or reviewer.startswith("pending"):
                errors.append(f"{task_id} complete without attributable reviewer")
            if task_id in PHYSICAL_TASKS:
                for item in evidence:
                    provenance = str(item.get("provenance", "")) if isinstance(item, dict) else ""
                    if provenance in {"simulation", "prepared", "prepared-synthetic-non-personal"}:
                        errors.append(f"{task_id} uses non-physical provenance {provenance}")
    decision = record.get("release_decision")
    if decision == "approved":
        incomplete = sorted(task_id for task_id, task in all_tasks.items() if task.get("status") != "complete")
        if incomplete:
            errors.append(f"release approved with incomplete tasks: {', '.join(incomplete)}")
        facets = record.get("facets", {})
        bad_facets = sorted(name for name, value in facets.items() if value not in APPROVED_FACETS)
        if bad_facets:
            errors.append(f"release approved with unapproved facets: {', '.join(bad_facets)}")
    elif decision != "deferred":
        errors.append(f"invalid release_decision {decision!r}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("record", type=Path, nargs="?", default=Path(__file__).with_name("status.yml"))
    args = parser.parse_args()
    data = yaml.safe_load(args.record.read_text(encoding="utf-8"))
    errors = validate(data)
    for error in errors:
        print(f"ERROR {error}")
    print(f"M04-EVIDENCE-GATE errors={len(errors)} record={args.record}")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
