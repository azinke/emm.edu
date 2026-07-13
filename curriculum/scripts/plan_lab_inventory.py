#!/usr/bin/env python3
"""Generate a deterministic M03 laboratory inventory plan.

The tool deliberately rejects planning scenarios unless explicitly enabled. This
prevents an example cohort from becoming procurement evidence by copy/paste.
"""

from __future__ import annotations

import argparse
import json
import math
import sys
from pathlib import Path


def positive_int(value: object, field: str) -> int:
    if not isinstance(value, int) or isinstance(value, bool) or value <= 0:
        raise ValueError(f"{field} must be a positive integer")
    return value


def calculate(plan: dict, catalog: dict, allow_planning_scenario: bool = False) -> dict:
    if plan.get("status") != "approved-cohort" and not allow_planning_scenario:
        raise ValueError("cohort plan is not approved; pass --allow-planning-scenario only for modelling")
    cohort_id = plan.get("cohort_id")
    if not isinstance(cohort_id, str) or not cohort_id.strip():
        raise ValueError("cohort_id is required")
    students = positive_int(plan.get("enrolled_students"), "enrolled_students")
    section = positive_int(plan.get("largest_section"), "largest_section")
    pair_size = positive_int(plan.get("pair_size"), "pair_size")
    rotations = positive_int(plan.get("rotations"), "rotations")
    rooms = positive_int(plan.get("qualified_rooms"), "qualified_rooms")
    if section > students:
        raise ValueError("largest_section cannot exceed enrolled_students")
    on_hand = plan.get("serviceable_on_hand", {})
    on_order = plan.get("accepted_on_order", {})
    if not isinstance(on_hand, dict) or not isinstance(on_order, dict):
        raise ValueError("stock maps must be objects")

    result_items = []
    seen: set[str] = set()
    for item in catalog.get("items", []):
        item_id = item.get("id")
        if not isinstance(item_id, str) or not item_id or item_id in seen:
            raise ValueError(f"invalid or duplicate catalog item id: {item_id!r}")
        seen.add(item_id)
        item_class = item.get("class")
        ratio = positive_int(item.get("ratio"), f"{item_id}.ratio")
        if item_class == "personal":
            base = students
        elif item_class == "pair":
            base = math.ceil(students / pair_size)
        elif item_class == "simultaneous-personal":
            base = math.ceil(section / rotations)
        elif item_class == "simultaneous-pair":
            base = math.ceil(section / (pair_size * rotations))
        elif item_class == "shared":
            base = math.ceil(section / ratio)
        elif item_class == "room":
            base = rooms
        else:
            raise ValueError(f"{item_id}: unsupported class {item_class!r}")
        spare_fraction = item.get("spare_fraction")
        reserve = item.get("deliberate_fault_reserve", 0)
        if not isinstance(spare_fraction, (int, float)) or spare_fraction < 0:
            raise ValueError(f"{item_id}.spare_fraction must be non-negative")
        if not isinstance(reserve, int) or reserve < 0:
            raise ValueError(f"{item_id}.deliberate_fault_reserve must be a non-negative integer")
        serviceable = on_hand.get(item_id, 0)
        accepted = on_order.get(item_id, 0)
        if not all(isinstance(v, int) and v >= 0 for v in (serviceable, accepted)):
            raise ValueError(f"{item_id}: stock quantities must be non-negative integers")
        gross = math.ceil(base * (1 + spare_fraction)) + reserve
        result_items.append({
            "id": item_id,
            "name_en": item.get("name_en"),
            "name_fr": item.get("name_fr"),
            "inventory_class": item_class,
            "base_quantity": base,
            "spare_fraction": spare_fraction,
            "deliberate_fault_reserve": reserve,
            "gross_requirement": gross,
            "serviceable_on_hand": serviceable,
            "accepted_on_order": accepted,
            "planned_order_quantity": max(0, gross - serviceable - accepted),
        })
    return {
        "schema_version": "1.0.0",
        "evidence_status": "approved-cohort-plan" if plan.get("status") == "approved-cohort" else "planning-scenario-not-procurement-evidence",
        "cohort_id": cohort_id,
        "deployment_profile": plan.get("deployment_profile"),
        "inputs": {
            "enrolled_students": students,
            "largest_section": section,
            "pair_size": pair_size,
            "rotations": rotations,
            "qualified_rooms": rooms,
        },
        "items": result_items,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("plan", type=Path)
    parser.add_argument("catalog", type=Path)
    parser.add_argument("--allow-planning-scenario", action="store_true")
    args = parser.parse_args()
    try:
        plan = json.loads(args.plan.read_text(encoding="utf-8"))
        catalog = json.loads(args.catalog.read_text(encoding="utf-8"))
        result = calculate(plan, catalog, args.allow_planning_scenario)
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        print(f"inventory plan failed: {exc}", file=sys.stderr)
        return 2
    json.dump(result, sys.stdout, ensure_ascii=False, indent=2)
    print()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

