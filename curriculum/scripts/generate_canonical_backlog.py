#!/usr/bin/env python3
"""Generate deterministic child backlog items from canonical manifests."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "curriculum" / "data"
OUTPUT = ROOT / "curriculum" / "backlog" / "canonical-child-backlog.yml"
FACETS = ["technical", "safety", "language", "accessibility", "license", "build", "apparatus", "approval"]
PILOTS = ["second-instructor-rehearsal", "en-learner-usability", "fr-learner-usability", "small-cohort"]


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def generated() -> dict:
    sources = [DATA / "course-manifests.yml", DATA / "unit-manifests.yml"]
    records: list[tuple[str, dict]] = []
    for kind, path, key in (("course", sources[0], "courses"), ("unit", sources[1], "units")):
        records.extend((kind, record) for record in load(path)[key])

    items = []
    for kind, manifest in sorted(records, key=lambda item: (item[0], item[1].get("id", item[1].get("semantic_id")))):
        manifest_id = manifest.get("id", manifest.get("semantic_id"))
        for resource, applicability in sorted(manifest["resource_applicability"].items()):
            base = f"BL-{manifest_id}-{resource}".upper().replace("_", "-")
            editions = []
            for language in manifest["editions"]:
                editions.append({
                    "id": f"{base}-{language.upper()}",
                    "language": language,
                    "paired_with": f"{base}-{'FR' if language == 'en' else 'EN'}",
                    "status": "not-started",
                    "evidence_link": None,
                    "approver": manifest["owners"]["language"],
                })
            items.append({
                "id": base,
                "manifest_id": manifest_id,
                "manifest_kind": kind,
                "resource": resource,
                "applicability": applicability,
                "edition_children": editions,
                "approval_facets": [{"facet": facet, "status": "pending", "evidence_link": None, "approver": manifest["owners"]["technical"] if facet != "language" else manifest["owners"]["language"]} for facet in FACETS],
                "apparatus_paths": [{"path": path, "status": "pending", "physical_pilot_evidence": None, "approver": "laboratory-owner"} for path in (manifest["apparatus_paths"].keys() if isinstance(manifest["apparatus_paths"], dict) else manifest["apparatus_paths"])],
                "pilots": [{"type": pilot, "status": "pending", "evidence_link": None, "approver": "pilot-owner"} for pilot in PILOTS],
                "defect_disposition": {"open_defect_ids": [], "resolved_defect_ids": [], "accepted_deviation_ids": [], "release_blocked": True, "approver": "release-manager"},
                "evidence_links": [],
                "approver": "release-manager",
                "status": "not-started",
            })
    return {
        "schema_version": "1.0.0",
        "version": "1.0.0",
        "generated_at": "2026-07-13",
        "generated_from": [str(path.relative_to(ROOT)) for path in sources],
        "generation_rule": "one child per declared resource and manifest; every child owns paired editions, independent approval facets, apparatus routes, pilots, defects, evidence, and approval",
        "items": items,
    }


def render() -> str:
    return json.dumps(generated(), ensure_ascii=False, indent=2) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="check the committed backlog for generation drift")
    args = parser.parse_args()
    expected = render()
    if args.check:
        if not OUTPUT.exists() or OUTPUT.read_text(encoding="utf-8") != expected:
            print(f"backlog generation drift: {OUTPUT.relative_to(ROOT)}")
            return 1
        print(f"backlog generation check passed ({len(generated()['items'])} resource children)")
        return 0
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(expected, encoding="utf-8")
    print(f"wrote {OUTPUT.relative_to(ROOT)} with {len(generated()['items'])} resource children")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
