#!/usr/bin/env python3
"""Offline validator for canonical curriculum data, schemas, and child backlog.

All checks use the Python standard library.  The canonical ``.yml`` files are
JSON-compatible YAML 1.2, so validation never needs a network or package index.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import defaultdict
from datetime import date
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
DATA_FILES = [
    "outcomes.yml", "prerequisite-graph.yml", "platform-matrix.yml",
    "component-inventory.yml", "project-dependencies.yml", "context-briefs.yml",
    "local-value-ladder.yml", "claims.yml", "manufacturing-capabilities.yml",
    "suppliers.yml", "costs.yml", "facilities.yml", "safety.yml", "assessments.yml",
    "course-manifests.yml", "unit-manifests.yml",
]
SCHEMA_NAMES = {
    "platform", "component", "project", "context", "deployment-profile", "jurisdiction",
    "manufacturing-capability", "supplier", "cost", "facility", "contribution",
    "claim-source", "safety", "assessment", "course-manifest", "unit-manifest", "backlog",
    "outcome", "prerequisite-graph", "termbase",
}
STATUS = {
    "approved-baseline", "brief", "draft", "review", "technical-review", "language-review",
    "pilot", "pilot-ready", "stable", "released", "retired", "approved",
    "mapping-in-progress", "qualification-pending", "quote-required", "not-started", "pending",
}
ID_RE = re.compile(r"^[A-Za-z][A-Za-z0-9]*(?:[-.][A-Za-z0-9]+)*$")
REVIEW_DUE_CLASSES = {"platform-bound", "standard-bound", "regulation-bound", "price-bound", "frontier-annual", "contextual-empirical"}
REQUIRED_HANDS_ON = {
    "real_life_question", "prediction", "student_action", "physical_or_data_evidence",
    "fault_or_anomaly", "design_decision", "acceptance_test",
}
BOILERPLATE_HANDS_ON_RE = re.compile(
    r"^\s*(?:\[[^]]*\]|<[^>]*>|tbd|todo|to be determined|lorem ipsum|"
    r"question|prediction|observable action|acceptance criterion)\s*$",
    re.IGNORECASE,
)
REQUIRED_FACETS = {"technical", "safety", "language", "accessibility", "license", "build", "apparatus", "approval"}
REQUIRED_PILOTS = {"second-instructor-rehearsal", "en-learner-usability", "fr-learner-usability", "small-cohort"}


def load_json(path: Path, errors: list[str]) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        errors.append(f"missing canonical file: {path}")
    except json.JSONDecodeError as exc:
        errors.append(f"invalid JSON-compatible YAML {path}: {exc}")
    return {}


def load_documents(root: Path = ROOT) -> tuple[dict[str, Any], dict[str, Any], Any, list[str]]:
    errors: list[str] = []
    data_dir = root / "curriculum" / "data"
    docs = {name: load_json(data_dir / name, errors) for name in DATA_FILES}
    docs["termbase.yml"] = load_json(root / "curriculum" / "i18n" / "termbase.yml", errors)
    profiles = sorted((data_dir / "deployment-profiles").glob("*.yml"))
    if not profiles:
        errors.append("missing dated deployment profile")
    docs["deployment-profiles"] = [load_json(path, errors) for path in profiles]
    schemas = {path.stem.removesuffix(".schema"): load_json(path, errors) for path in sorted((root / "curriculum" / "schemas").glob("*.schema.json"))}
    backlog = load_json(root / "curriculum" / "backlog" / "canonical-child-backlog.yml", errors)
    return docs, schemas, backlog, errors


def records(document: dict, key: str) -> list[dict]:
    value = document.get(key, [])
    return value if isinstance(value, list) else []


def check_unique(items: list[dict], field: str, label: str, errors: list[str]) -> set[str]:
    values: set[str] = set()
    for item in items:
        value = item.get(field)
        if not isinstance(value, str) or not value:
            errors.append(f"{label}: missing {field}")
            continue
        if value in values:
            errors.append(f"{label}: duplicate {field} {value}")
        values.add(value)
        if not ID_RE.match(value):
            errors.append(f"{label}: invalid ID {value}")
    return values


def check_status(value: Any, label: str, errors: list[str]) -> None:
    if value not in STATUS:
        errors.append(f"{label}: invalid status {value!r}")


def parse_date(value: Any, label: str, errors: list[str]) -> date | None:
    if not isinstance(value, str):
        errors.append(f"{label}: missing or invalid date")
        return None
    try:
        return date.fromisoformat(value)
    except ValueError:
        errors.append(f"{label}: invalid ISO date {value!r}")
        return None


def validate_outcomes(doc: dict, errors: list[str]) -> tuple[set[str], set[str], set[str]]:
    peos, plos, cos = records(doc, "peos"), records(doc, "plos"), records(doc, "course_outcomes")
    unit_outcomes = records(doc, "unit_outcomes")
    peo_ids = check_unique(peos, "id", "PEO", errors)
    plo_ids = check_unique(plos, "id", "PLO", errors)
    co_ids = check_unique(cos, "id", "course outcome", errors)
    unit_outcome_ids = check_unique(unit_outcomes, "id", "unit outcome", errors)
    if peo_ids != {f"PEO-{n}" for n in range(1, 6)}:
        errors.append("outcomes: expected complete PEO-1 through PEO-5 set")
    if plo_ids != {f"PLO-{n:02d}" for n in range(1, 15)}:
        errors.append("outcomes: expected complete PLO-01 through PLO-14 set")
    levels = {entry.get("level") for entry in records(doc, "progression_levels")}
    if levels != set(range(5)):
        errors.append("outcomes: progression levels must be exactly 0 through 4")
    for peo in peos:
        check_status(peo.get("status"), peo.get("id", "PEO"), errors)
        for target in peo.get("maps_to", []):
            if target not in plo_ids:
                errors.append(f"{peo.get('id')}: unknown outcome mapping {target}")
    for plo in plos:
        check_status(plo.get("status"), plo.get("id", "PLO"), errors)
        if not 3 <= plo.get("minimum_level", -1) <= 4:
            errors.append(f"{plo.get('id')}: invalid graduation progression level")
        if not plo.get("graduation_evidence"):
            errors.append(f"{plo.get('id')}: missing evidence mapping")
    for outcome in cos:
        check_status(outcome.get("status"), outcome.get("id", "course outcome"), errors)
        mappings = outcome.get("maps_to", [])
        if not mappings:
            errors.append(f"{outcome.get('id')}: missing mappings")
        for target in mappings:
            if target not in plo_ids:
                errors.append(f"{outcome.get('id')}: unknown outcome mapping {target}")
        if not outcome.get("evidence"):
            errors.append(f"{outcome.get('id')}: missing evidence mapping")
    for outcome in unit_outcomes:
        check_status(outcome.get("status"), outcome.get("id", "unit outcome"), errors)
        if not outcome.get("unit_id") or not outcome.get("course_id"):
            errors.append(f"{outcome.get('id')}: missing unit/course traceability")
        mappings = outcome.get("maps_to", [])
        if not mappings:
            errors.append(f"{outcome.get('id')}: missing mappings")
        for target in mappings:
            if target not in plo_ids | co_ids:
                errors.append(f"{outcome.get('id')}: unknown outcome mapping {target}")
        if not outcome.get("evidence") or not outcome.get("assessment_points"):
            errors.append(f"{outcome.get('id')}: missing evidence or assessment mapping")
        if not outcome.get("source_record"):
            errors.append(f"{outcome.get('id')}: missing source record")
    return peo_ids, plo_ids, co_ids | unit_outcome_ids


def validate_graph(doc: dict, course_ids: set[str], errors: list[str]) -> set[str]:
    nodes = records(doc, "nodes")
    node_ids = check_unique(nodes, "id", "prerequisite node", errors)
    gates = {node["id"] for node in nodes if node.get("kind") == "gate" and "id" in node}
    if gates != {f"G{n}" for n in range(1, 10)}:
        errors.append("prerequisite graph: expected complete G1-G9 gate set")
    graph: dict[str, set[str]] = defaultdict(set)
    incoming: dict[str, int] = defaultdict(int)
    outgoing: dict[str, int] = defaultdict(int)
    for edge in records(doc, "requires"):
        source, target = edge.get("from"), edge.get("to")
        if source not in node_ids or target not in node_ids:
            errors.append(f"prerequisite graph: unknown link {source!r} -> {target!r}")
            continue
        graph[source].add(target)
        incoming[target] += 1
        outgoing[source] += 1
    state: dict[str, int] = {}
    trail: list[str] = []

    def visit(node: str) -> None:
        state[node] = 1
        trail.append(node)
        for nxt in graph[node]:
            if state.get(nxt) == 1:
                start = trail.index(nxt)
                errors.append("prerequisite graph: dependency cycle " + " -> ".join(trail[start:] + [nxt]))
            elif state.get(nxt, 0) == 0:
                visit(nxt)
        trail.pop()
        state[node] = 2

    for node in node_ids:
        if state.get(node, 0) == 0:
            visit(node)
    allowed_roots = set(doc.get("root_policy", {}).get("allowed_roots", []))
    terminals = set(doc.get("root_policy", {}).get("terminal_nodes", []))
    for node in node_ids:
        if not incoming[node] and not outgoing[node] and node not in allowed_roots | terminals:
            errors.append(f"prerequisite graph: orphan node {node}")
    for course_id in course_ids:
        if course_id not in node_ids:
            errors.append(f"prerequisite graph: missing course node {course_id}")
    for node in nodes:
        if node.get("kind") == "gate":
            if not node.get("requires") or not node.get("remediation") or "unlocks" not in node:
                errors.append(f"{node.get('id')}: incomplete gate requirements, unlocks, or remediation")
    return node_ids


def validate_termbase(doc: dict, errors: list[str]) -> set[str]:
    concepts = records(doc, "terms")
    ids = check_unique(concepts, "id", "termbase concept", errors)
    if len(concepts) < 130:
        errors.append(f"termbase: expected the complete master glossary, found {len(concepts)} concepts")
    for concept in concepts:
        cid = concept.get("id", "termbase concept")
        if concept.get("concept_id") != cid:
            errors.append(f"{cid}: concept_id must equal id")
        for field in ("definition", "terms", "avoided_terms", "acronym_policy", "example", "status", "reviewer"):
            if field not in concept:
                errors.append(f"{cid}: missing termbase field {field}")
        for bilingual in ("definition", "example"):
            value = concept.get(bilingual, {})
            if not all(isinstance(value.get(lang), str) and value[lang].strip() for lang in ("en", "fr")):
                errors.append(f"{cid}: missing bilingual {bilingual}")
        check_status(concept.get("status"), cid, errors)
    return ids


def validate_schemas(schemas: dict[str, dict], errors: list[str]) -> None:
    missing = SCHEMA_NAMES - set(schemas)
    extra_ids: set[str] = set()
    if missing:
        errors.append("schemas: missing " + ", ".join(sorted(missing)))
    for name, schema in schemas.items():
        if schema.get("$schema") != "https://json-schema.org/draft/2020-12/schema":
            errors.append(f"schema {name}: wrong or missing JSON Schema draft")
        sid = schema.get("$id")
        if not sid:
            errors.append(f"schema {name}: missing $id")
        elif sid in extra_ids:
            errors.append(f"schema {name}: duplicate $id {sid}")
        extra_ids.add(sid)
        if schema.get("type") != "object" or not schema.get("required"):
            errors.append(f"schema {name}: missing object contract or required fields")


def validate_claims_and_context(docs: dict[str, Any], as_of: date, errors: list[str]) -> tuple[set[str], set[str]]:
    claims = records(docs["claims.yml"], "claims")
    contexts = records(docs["context-briefs.yml"], "contexts")
    claim_ids = check_unique(claims, "id", "claim", errors)
    context_ids = check_unique(contexts, "id", "context", errors)
    profile_ids = {profile.get("id") for profile in docs["deployment-profiles"]}
    for claim in claims:
        cid = claim.get("id", "claim")
        check_status(claim.get("status"), cid, errors)
        if not claim.get("source") or not claim.get("verification_method") or not claim.get("reviewer"):
            errors.append(f"{cid}: incomplete claim source/provenance")
        if claim.get("claim_class") in REVIEW_DUE_CLASSES:
            due = parse_date(claim.get("review_due"), f"{cid} review_due", errors)
            if due and due < as_of:
                errors.append(f"{cid}: expired claim review date {due.isoformat()}")
        for context_id in claim.get("context_ids", []):
            if context_id not in context_ids:
                errors.append(f"{cid}: unknown context ID {context_id}")
    for context in contexts:
        cid = context.get("id", "context")
        if context.get("layer") not in {"deployment-pack", "project-context"}:
            errors.append(f"{cid}: invalid context layer")
        if context.get("profile_id") not in profile_ids:
            errors.append(f"{cid}: unknown deployment profile {context.get('profile_id')}")
        if not context.get("evidence_ids"):
            errors.append(f"{cid}: missing provenance evidence")
        for evidence in context.get("evidence_ids", []):
            if evidence not in claim_ids:
                errors.append(f"{cid}: unknown evidence link {evidence}")
        parse_date(context.get("review_due"), f"{cid} review_due", errors)
    for profile in docs["deployment-profiles"]:
        pid = profile.get("id", "deployment profile")
        check_status(profile.get("status"), pid, errors)
        if profile.get("universal_contract", {}).get("threshold_changes_permitted") is not False:
            errors.append(f"{pid}: deployment profile may not lower the universal contract")
        if profile.get("release_eligible") and (profile.get("required_evidence_gaps") or any(j.get("verification_status") != "approved" for j in profile.get("jurisdictions", []))):
            errors.append(f"{pid}: profile cannot be release eligible with evidence or jurisdiction gaps")
        parse_date(profile.get("review_due"), f"{pid} review_due", errors)
    return claim_ids, context_ids


def validate_manifests(docs: dict[str, Any], outcome_ids: set[str], node_ids: set[str], claim_ids: set[str], context_ids: set[str], as_of: date, errors: list[str]) -> tuple[list[dict], list[dict]]:
    courses = records(docs["course-manifests.yml"], "courses")
    units = records(docs["unit-manifests.yml"], "units")
    course_ids = check_unique(courses, "id", "course manifest", errors)
    unit_ids = check_unique(units, "semantic_id", "unit manifest", errors)
    for manifest, kind in [(item, "course") for item in courses] + [(item, "unit") for item in units]:
        mid = manifest.get("id", manifest.get("semantic_id", kind))
        check_status(manifest.get("status"), mid, errors)
        editions = set(manifest.get("editions", []))
        if editions != {"en", "fr"}:
            errors.append(f"{mid}: missing EN/FR paired editions")
        parity = parse_date(manifest.get("last_parity_review"), f"{mid} last_parity_review", errors)
        if parity and (as_of - parity).days > 365:
            errors.append(f"{mid}: stale paired-language record ({parity.isoformat()})")
        for outcome in manifest.get("outcomes", []):
            if outcome not in outcome_ids:
                errors.append(f"{mid}: unknown outcome link {outcome}")
        if not manifest.get("outcomes"):
            errors.append(f"{mid}: missing outcome mappings")
        for prerequisite in manifest.get("prerequisites", []):
            if prerequisite not in node_ids and prerequisite not in outcome_ids:
                errors.append(f"{mid}: unknown prerequisite link {prerequisite}")
        layer = manifest.get("localization_layer")
        linked_contexts = manifest.get("context_ids", [])
        if layer == "universal-core" and linked_contexts:
            errors.append(f"{mid}: universal-core record embeds deployment context IDs")
        if layer in {"deployment-pack", "project-context"} and not linked_contexts:
            errors.append(f"{mid}: deployment/context record missing context IDs")
        if layer not in {"universal-core", "deployment-pack", "project-context"}:
            errors.append(f"{mid}: invalid localization layer {layer!r}")
        for context_id in linked_contexts:
            if context_id not in context_ids:
                errors.append(f"{mid}: unknown context ID {context_id}")
        for claim_id in manifest.get("claim_register_ids", []):
            if claim_id not in claim_ids:
                errors.append(f"{mid}: unknown claim link {claim_id}")
        if kind == "unit":
            if manifest.get("course_id") not in course_ids:
                errors.append(f"{mid}: unknown parent course {manifest.get('course_id')}")
            hands = manifest.get("hands_on_contract", {})
            missing = REQUIRED_HANDS_ON - set(hands)
            if missing or any(
                hands.get(field) is None or not str(hands.get(field, "")).strip()
                for field in REQUIRED_HANDS_ON
            ):
                errors.append(f"{mid}: incomplete hands-on contract {sorted(missing)}")
            boilerplate = sorted(
                field
                for field in REQUIRED_HANDS_ON
                if BOILERPLATE_HANDS_ON_RE.fullmatch(str(hands.get(field, "")))
            )
            if boilerplate:
                errors.append(f"{mid}: boilerplate hands-on contract fields {boilerplate}")
            if manifest.get("platform_binding") in {"platform-bound", "frontier-annual"} and not manifest.get("claim_review_due"):
                errors.append(f"{mid}: missing claim review date")
    for course in courses:
        for unit_id in course.get("unit_ids", []):
            if unit_id not in unit_ids:
                errors.append(f"{course.get('id')}: unknown unit manifest {unit_id}")
    return courses, units


def validate_provenance(docs: dict[str, Any], context_ids: set[str], errors: list[str]) -> set[str]:
    ladder = docs["local-value-ladder.yml"]
    level_ids = check_unique(records(ladder, "levels"), "id", "contribution level", errors)
    if level_ids != {f"V{n}" for n in range(5)}:
        errors.append("contribution ladder: expected complete V0-V4 levels")
    contribution_ids = check_unique(records(ladder, "contribution_records"), "id", "contribution record", errors)
    for record in records(ladder, "contribution_records"):
        rid = record.get("id", "contribution")
        check_status(record.get("status"), rid, errors)
        if record.get("target_level") not in level_ids:
            errors.append(f"{rid}: unknown contribution target")
        required = ["contributions", "imported_dependencies", "make_buy_rationale", "capability_gaps", "next_local_step", "permitted_claim", "legal_review", "reviewer"]
        if any(field not in record for field in required):
            errors.append(f"{rid}: missing contribution/provenance evidence")
        if any(phrase in record.get("permitted_claim", "").lower() for phrase in ("made in", "fabriqué au", "local origin")) and not record.get("context_ids"):
            errors.append(f"{rid}: geographic origin claim missing context and jurisdiction provenance")
        for context_id in record.get("context_ids", []):
            if context_id not in context_ids:
                errors.append(f"{rid}: unknown context ID {context_id}")
    return contribution_ids


def validate_backlog(backlog: dict, courses: list[dict], units: list[dict], errors: list[str]) -> None:
    items = records(backlog, "items")
    ids = check_unique(items, "id", "backlog item", errors)
    del ids
    actual: dict[tuple[str, str], int] = defaultdict(int)
    manifests = {manifest.get("id", manifest.get("semantic_id")): manifest for manifest in courses + units}
    for item in items:
        iid = item.get("id", "backlog item")
        manifest_id = item.get("manifest_id")
        resource = item.get("resource")
        actual[(manifest_id, resource)] += 1
        if manifest_id not in manifests:
            errors.append(f"{iid}: unknown canonical manifest {manifest_id}")
            continue
        manifest = manifests[manifest_id]
        if resource not in manifest.get("resource_applicability", {}):
            errors.append(f"{iid}: unknown resource child {resource}")
        editions = item.get("edition_children", [])
        if {edition.get("language") for edition in editions} != {"en", "fr"} or any(not edition.get("paired_with") for edition in editions):
            errors.append(f"{iid}: incomplete paired EN/FR edition children")
        if {facet.get("facet") for facet in item.get("approval_facets", [])} != REQUIRED_FACETS:
            errors.append(f"{iid}: incomplete approval facets")
        expected_paths = set(manifest["apparatus_paths"].keys() if isinstance(manifest["apparatus_paths"], dict) else manifest["apparatus_paths"])
        if {route.get("path") for route in item.get("apparatus_paths", [])} != expected_paths:
            errors.append(f"{iid}: incomplete apparatus paths")
        if {pilot.get("type") for pilot in item.get("pilots", [])} != REQUIRED_PILOTS:
            errors.append(f"{iid}: incomplete instructor/learner pilot children")
        if not isinstance(item.get("defect_disposition"), dict) or "approver" not in item["defect_disposition"]:
            errors.append(f"{iid}: missing defect disposition")
        if "evidence_links" not in item or not item.get("approver"):
            errors.append(f"{iid}: missing evidence link field or approver")
        check_status(item.get("status"), iid, errors)
    expected = {(mid, resource) for mid, manifest in manifests.items() for resource in manifest.get("resource_applicability", {})}
    missing = sorted(expected - set(actual))
    duplicates = sorted(key for key, count in actual.items() if count != 1)
    if missing:
        errors.append(f"backlog: missing {len(missing)} canonical manifest/resource children")
    if duplicates:
        errors.append(f"backlog: duplicate manifest/resource children {duplicates[:3]}")


def validate_supporting_links(docs: dict[str, Any], errors: list[str]) -> None:
    suppliers = check_unique(records(docs["suppliers.yml"], "suppliers"), "id", "supplier", errors)
    components = check_unique(records(docs["component-inventory.yml"], "components"), "id", "component", errors)
    profiles = {profile.get("id") for profile in docs["deployment-profiles"]}
    for filename, key in (("platform-matrix.yml", "platforms"), ("component-inventory.yml", "components"), ("manufacturing-capabilities.yml", "capabilities"), ("suppliers.yml", "suppliers"), ("costs.yml", "costs"), ("facilities.yml", "facilities"), ("assessments.yml", "assessments")):
        for item in records(docs[filename], key):
            check_status(item.get("status"), item.get("id", filename), errors)
    for cost in records(docs["costs.yml"], "costs"):
        if cost.get("supplier_id") not in suppliers:
            errors.append(f"{cost.get('id')}: unknown supplier link")
        if cost.get("item_id") not in components:
            errors.append(f"{cost.get('id')}: unknown item link")
        if cost.get("source_amount") is not None and not all(cost.get(field) is not None for field in ("source_currency", "landed_amount", "exchange_rate", "quoted_on", "valid_until")):
            errors.append(f"{cost.get('id')}: incomplete source/landed cost provenance")
    for filename, key in (("manufacturing-capabilities.yml", "capabilities"), ("suppliers.yml", "suppliers"), ("costs.yml", "costs"), ("facilities.yml", "facilities")):
        for item in records(docs[filename], key):
            if item.get("profile_id") not in profiles:
                errors.append(f"{item.get('id')}: unknown deployment profile link")


def validate_documents(docs: dict[str, Any], schemas: dict[str, dict], backlog: dict, *, as_of: date) -> list[str]:
    errors: list[str] = []
    for name, document in docs.items():
        if name == "deployment-profiles":
            continue
        if isinstance(document, dict):
            check_status(document.get("status"), name, errors)
    _, plo_ids, co_ids = validate_outcomes(docs["outcomes.yml"], errors)
    course_outcome_course_ids = {item.get("course_id") for item in records(docs["outcomes.yml"], "course_outcomes")}
    node_ids = validate_graph(docs["prerequisite-graph.yml"], course_outcome_course_ids, errors)
    validate_termbase(docs["termbase.yml"], errors)
    validate_schemas(schemas, errors)
    claim_ids, context_ids = validate_claims_and_context(docs, as_of, errors)
    outcome_ids = plo_ids | co_ids
    courses, units = validate_manifests(docs, outcome_ids, node_ids, claim_ids, context_ids, as_of, errors)
    validate_provenance(docs, context_ids, errors)
    validate_backlog(backlog, courses, units, errors)
    validate_supporting_links(docs, errors)
    return errors


def apply_fixture(docs: dict[str, Any], backlog: dict, fixture: dict) -> None:
    target = backlog if fixture["document"] == "backlog" else docs[fixture["document"]]
    parts = [part.replace("~1", "/").replace("~0", "~") for part in fixture["pointer"].strip("/").split("/")]
    cursor = target
    for part in parts[:-1]:
        cursor = cursor[int(part)] if isinstance(cursor, list) else cursor[part]
    final = parts[-1]
    if isinstance(cursor, list):
        cursor[int(final)] = fixture["value"]
    else:
        cursor[final] = fixture["value"]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--as-of", type=date.fromisoformat, default=date.today())
    parser.add_argument("--fixture", type=Path, help="apply a seeded negative JSON mutation before validation")
    args = parser.parse_args()
    docs, schemas, backlog, load_errors = load_documents(args.root.resolve())
    fixture = None
    if args.fixture:
        fixture = json.loads(args.fixture.read_text(encoding="utf-8"))
        apply_fixture(docs, backlog, fixture)
    errors = load_errors + validate_documents(docs, schemas, backlog, as_of=args.as_of)
    if fixture and fixture.get("expect"):
        if not any(fixture["expect"] in error for error in errors):
            errors.append(f"seeded fixture did not trigger expected diagnostic: {fixture['expect']}")
    if errors:
        print(f"canonical validation failed ({len(errors)} errors):", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print("canonical validation passed: outcomes, graph, termbase, schemas, manifests, backlog, context, claims, and provenance")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
