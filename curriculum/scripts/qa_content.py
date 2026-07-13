#!/usr/bin/env python3
"""Validate bilingual public teaching sources without requiring network access."""

from __future__ import annotations

import argparse
import datetime as dt
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

from scriptlib import CURRICULUM, flatten_ids, load_yaml, parse_front_matter, semantic_key, sha256_file


LINK_RE = re.compile(r"(?<!!)\[[^]]*\]\(([^)\s]+)(?:\s+['\"][^'\"]*['\"])?\)")
IMAGE_RE = re.compile(r"!\[([^]]*)\]\(([^)\s]+)(?:\s+['\"]([^'\"]*)['\"])?\)(\{[^}]*\})?")
TERM_RE = re.compile(r"\[term:([A-Za-z0-9_.:-]+)\]")
REMOTE_RE = re.compile(r"^(?:https?|ftp)://", re.I)


@dataclass(frozen=True)
class Finding:
    code: str
    path: str
    message: str
    severity: str = "error"

    def render(self) -> str:
        return f"{self.severity.upper()} {self.code} {self.path}: {self.message}"


@dataclass
class Document:
    path: Path
    relative: Path
    metadata: dict[str, Any]
    body: str
    language: str | None
    pair_id: str | None


def language_from(path: Path, metadata: dict[str, Any]) -> str | None:
    declared = metadata.get("lang") or metadata.get("language")
    if declared in {"en", "fr"}:
        return str(declared)
    for part in path.parts:
        if part in {"en", "fr"}:
            return part
    return None


def structural_pair_id(relative: Path, metadata: dict[str, Any]) -> str | None:
    declared = metadata.get("pair_id") or metadata.get("artifact_id")
    if declared:
        return str(declared)
    parts = ["{lang}" if part in {"en", "fr"} else part for part in relative.parts]
    return "/".join(parts)


def collect_documents(root: Path, policy: dict[str, Any]) -> tuple[list[Document], list[Finding]]:
    documents: list[Document] = []
    findings: list[Finding] = []
    extensions = set(policy.get("content_extensions", [".md", ".qmd"]))
    for path in sorted((root / "courses").rglob("*")) if (root / "courses").exists() else []:
        if not path.is_file() or path.suffix.lower() not in extensions:
            continue
        relative = path.relative_to(root)
        try:
            metadata, body = parse_front_matter(path)
        except (OSError, UnicodeError, ValueError) as exc:
            findings.append(Finding("Q001", str(relative), str(exc)))
            continue
        language = language_from(relative, metadata)
        documents.append(
            Document(path, relative, metadata, body, language, structural_pair_id(relative, metadata))
        )
    return documents, findings


def validate_pairs(documents: list[Document], policy: dict[str, Any]) -> list[Finding]:
    findings: list[Finding] = []
    by_pair: dict[str, dict[str, list[Document]]] = {}
    fields = policy.get("technical_contract_fields", [])
    for document in documents:
        if document.language not in {"en", "fr"}:
            findings.append(Finding("PAIR001", str(document.relative), "cannot determine en/fr language"))
            continue
        if not document.pair_id:
            findings.append(Finding("PAIR002", str(document.relative), "missing pair_id/artifact_id"))
            continue
        by_pair.setdefault(document.pair_id, {}).setdefault(document.language, []).append(document)
    for pair_id, editions in by_pair.items():
        for language in ("en", "fr"):
            count = len(editions.get(language, []))
            if count != 1:
                findings.append(Finding("PAIR003", pair_id, f"expected one {language} edition, found {count}"))
        if not editions.get("en") or not editions.get("fr"):
            continue
        en, fr = editions["en"][0], editions["fr"][0]
        en_revision, fr_revision = en.metadata.get("pair_revision"), fr.metadata.get("pair_revision")
        if not en_revision or not fr_revision or en_revision != fr_revision:
            findings.append(Finding("PAIR004", pair_id, f"stale/missing pair_revision: en={en_revision!r}, fr={fr_revision!r}"))
        en_contract = en.metadata.get("technical_contract", {})
        fr_contract = fr.metadata.get("technical_contract", {})
        if not isinstance(en_contract, dict) or not isinstance(fr_contract, dict):
            findings.append(Finding("PAIR005", pair_id, "technical_contract must be a mapping in both editions"))
            continue
        for field in fields:
            if field in en_contract or field in fr_contract:
                if semantic_key(en_contract.get(field)) != semantic_key(fr_contract.get(field)):
                    findings.append(Finding("PAIR006", pair_id, f"technical contract mismatch in {field}"))
    return findings


def rubric_findings(document: Document) -> list[Finding]:
    findings: list[Finding] = []
    rubric = document.metadata.get("rubric")
    contract = document.metadata.get("technical_contract", {})
    if not isinstance(rubric, dict):
        return findings
    rows = rubric.get("rows", [])
    if not isinstance(rows, list):
        return [Finding("RUBRIC001", str(document.relative), "rubric.rows must be a list")]
    try:
        calculated = sum(float(row["points"]) for row in rows)
        declared = float(rubric.get("total", contract.get("rubric_total")))
    except (KeyError, TypeError, ValueError):
        return [Finding("RUBRIC002", str(document.relative), "rubric rows and total must have numeric points")]
    if abs(calculated - declared) > 1e-9:
        findings.append(Finding("RUBRIC003", str(document.relative), f"rubric rows total {calculated:g}, declared {declared:g}"))
    contract_total = contract.get("rubric_total") if isinstance(contract, dict) else None
    if contract_total is not None and abs(float(contract_total) - declared) > 1e-9:
        findings.append(Finding("RUBRIC004", str(document.relative), "rubric total differs from technical contract"))
    return findings


def termbase_data(root: Path) -> tuple[set[str], list[tuple[str, str]]]:
    path = root / "i18n" / "termbase.yml"
    if not path.exists():
        return set(), []
    data = load_yaml(path) or {}
    ids = flatten_ids(data)
    avoided: list[tuple[str, str]] = []
    for term in data.get("terms", []) if isinstance(data, dict) else []:
        if not isinstance(term, dict):
            continue
        for value in term.get("avoided_terms", term.get("avoid", [])) or []:
            if isinstance(value, str):
                avoided.append((str(term.get("id", "unknown")), value))
            elif isinstance(value, dict):
                for localized in value.values():
                    if isinstance(localized, str):
                        avoided.append((str(term.get("id", "unknown")), localized))
    return ids, avoided


def validate_document(document: Document, root: Path, outcome_ids: set[str], term_ids: set[str], avoided: list[tuple[str, str]], policy: dict[str, Any]) -> list[Finding]:
    findings: list[Finding] = []
    path_label = str(document.relative)
    metadata = document.metadata
    contract = metadata.get("technical_contract", {})
    declared_outcomes = metadata.get("outcomes", contract.get("outcomes", []) if isinstance(contract, dict) else [])
    if isinstance(declared_outcomes, str):
        declared_outcomes = [declared_outcomes]
    for outcome in declared_outcomes or []:
        if outcome not in outcome_ids:
            findings.append(Finding("OUTCOME001", path_label, f"unknown outcome ID {outcome}"))
    glossary_ids = set(metadata.get("glossary_terms", []) or []) | set(TERM_RE.findall(document.body))
    for term_id in glossary_ids:
        if term_id not in term_ids:
            findings.append(Finding("GLOSSARY001", path_label, f"unknown glossary ID {term_id}"))
    searchable = re.sub(r"```.*?```", "", document.body, flags=re.S)
    for term_id, phrase in avoided:
        if phrase and re.search(rf"\b{re.escape(phrase)}\b", searchable, flags=re.I):
            findings.append(Finding("GLOSSARY002", path_label, f"avoided term {phrase!r} from {term_id}"))
    findings.extend(rubric_findings(document))

    restricted_tokens = policy.get("restricted_path_tokens", [])
    path_lower = path_label.lower()
    if any(token.lower() in path_lower for token in restricted_tokens):
        findings.append(Finding("RESTRICT001", path_label, "restricted/instructor path is inside the public course tree"))
    for marker in policy.get("restricted_markers", []):
        if marker.lower() in (document.body + semantic_key(metadata)).lower():
            findings.append(Finding("RESTRICT002", path_label, f"restricted marker {marker!r} leaked into public content"))
    if metadata.get("restricted") is True or str(metadata.get("audience", "")).lower() in {"instructor", "examiner"}:
        findings.append(Finding("RESTRICT003", path_label, "restricted metadata is not allowed in public output"))

    for match in IMAGE_RE.finditer(document.body):
        caption, target, _title, attributes = match.groups()
        if not caption.strip():
            findings.append(Finding("FIG001", path_label, f"image {target} has no localized caption"))
        if not attributes or not re.search(r"\bfig-alt\s*=\s*['\"][^'\"]+['\"]", attributes):
            findings.append(Finding("FIG002", path_label, f"image {target} has no distinct fig-alt text"))
        if not REMOTE_RE.match(target) and not target.startswith("data:"):
            candidate = (document.path.parent / target.split("#", 1)[0]).resolve()
            if not candidate.exists():
                findings.append(Finding("FIG003", path_label, f"missing image target {target}"))
    for target in LINK_RE.findall(document.body):
        if REMOTE_RE.match(target) or target.startswith(("mailto:", "tel:")):
            continue
        raw_path, _, anchor = target.partition("#")
        candidate = document.path if not raw_path else (document.path.parent / raw_path).resolve()
        if not candidate.exists():
            findings.append(Finding("LINK001", path_label, f"broken internal link {target}"))
        elif anchor and candidate.suffix.lower() in {".md", ".qmd"}:
            target_text = candidate.read_text(encoding="utf-8")
            explicit = f"#{anchor}" in target_text
            generated = any(slugify(heading) == anchor for heading in re.findall(r"^#{1,6}\s+(.+)$", target_text, re.M))
            if not (explicit or generated):
                findings.append(Finding("LINK002", path_label, f"missing anchor {target}"))
    return findings


def slugify(heading: str) -> str:
    value = re.sub(r"\{[^}]*\}\s*$", "", heading).strip().lower()
    value = re.sub(r"[^\w\s-]", "", value, flags=re.UNICODE)
    return re.sub(r"[-\s]+", "-", value).strip("-")


def validate_external_links(documents: list[Document], root: Path, offline: bool) -> list[Finding]:
    findings: list[Finding] = []
    registry_path = root / "environments" / "external-links.yml"
    registry = load_yaml(registry_path) or {}
    entries = registry.get("entries", []) if isinstance(registry, dict) else []
    valid_entries = [entry for entry in entries if isinstance(entry, dict)]
    by_url = {entry.get("url"): entry for entry in valid_entries if entry.get("url")}
    used: set[str] = set()
    required = {"id", "url", "title", "publisher_or_author", "source_kind", "edition_or_version", "retrieved_on", "review_due", "owner", "affected_artifacts", "citation_text", "archive_permission", "license_or_terms", "availability"}
    ids = [entry.get("id") for entry in valid_entries if entry.get("id")]
    urls = [entry.get("url") for entry in valid_entries if entry.get("url")]
    if len(ids) != len(set(ids)):
        findings.append(Finding("EXT010", str(registry_path.relative_to(root)), "duplicate external-link ID"))
    if len(urls) != len(set(urls)):
        findings.append(Finding("EXT011", str(registry_path.relative_to(root)), "duplicate external-link URL"))
    for document in documents:
        for target in LINK_RE.findall(document.body):
            if not REMOTE_RE.match(target):
                continue
            used.add(target)
            if target not in by_url:
                findings.append(Finding("EXT001", str(document.relative), f"external URL has no registry entry: {target}"))
    today = dt.date.today()
    for url, entry in by_url.items():
        missing = sorted(field for field in required if entry.get(field) in (None, "", []))
        if missing:
            findings.append(Finding("EXT002", str(registry_path.relative_to(root)), f"{entry.get('id', url)} missing {', '.join(missing)}"))
        try:
            review_due = dt.date.fromisoformat(str(entry.get("review_due")))
            if review_due < today:
                findings.append(Finding("EXT003", str(registry_path.relative_to(root)), f"{entry.get('id', url)} review expired {review_due}"))
        except ValueError:
            findings.append(Finding("EXT004", str(registry_path.relative_to(root)), f"{entry.get('id', url)} has invalid review_due"))
        try:
            retrieved_on = dt.date.fromisoformat(str(entry.get("retrieved_on")))
            if retrieved_on > today:
                findings.append(Finding("EXT012", str(registry_path.relative_to(root)), f"{entry.get('id', url)} retrieval date is in the future"))
        except ValueError:
            findings.append(Finding("EXT013", str(registry_path.relative_to(root)), f"{entry.get('id', url)} has invalid retrieved_on"))
        permission = entry.get("archive_permission")
        archive_path = entry.get("archive_path")
        if permission == "permitted":
            if not entry.get("permission_evidence") or not archive_path or not re.fullmatch(r"[0-9a-f]{64}", str(entry.get("sha256", ""))):
                findings.append(Finding("EXT005", str(registry_path.relative_to(root)), f"{entry.get('id', url)} permitted archive lacks evidence/path/checksum"))
            elif archive_path:
                archive = root / archive_path
                if not archive.exists():
                    findings.append(Finding("EXT006", str(registry_path.relative_to(root)), f"missing archived copy {archive_path}"))
                elif sha256_file(archive) != entry.get("sha256"):
                    findings.append(Finding("EXT007", str(registry_path.relative_to(root)), f"checksum mismatch for {archive_path}"))
                elif entry.get("bytes") != archive.stat().st_size:
                    findings.append(Finding("EXT014", str(registry_path.relative_to(root)), f"byte count mismatch for {archive_path}"))
        elif permission not in {"prohibited", "unknown"}:
            findings.append(Finding("EXT008", str(registry_path.relative_to(root)), f"invalid archive_permission {permission!r}"))
        if offline and entry.get("availability") == "required" and permission != "permitted":
            if not entry.get("offline_substitute"):
                findings.append(Finding("EXT009", str(registry_path.relative_to(root)), f"required source {entry.get('id', url)} has no lawful offline path"))
    return findings


def run(root: Path, offline: bool = True) -> list[Finding]:
    policy = load_yaml(root / "environments" / "qa-policy.yml") or {}
    documents, findings = collect_documents(root, policy)
    outcome_path = root / "data" / "outcomes.yml"
    outcome_ids = flatten_ids(load_yaml(outcome_path) or {}) if outcome_path.exists() else set()
    term_ids, avoided = termbase_data(root)
    findings.extend(validate_pairs(documents, policy))
    for document in documents:
        findings.extend(validate_document(document, root, outcome_ids, term_ids, avoided, policy))
    findings.extend(validate_external_links(documents, root, offline))
    return sorted(findings, key=lambda item: (item.path, item.code, item.message))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=CURRICULUM)
    parser.add_argument("--offline", action="store_true", help="require lawful offline routes; never performs network I/O")
    args = parser.parse_args()
    findings = run(args.root.resolve(), offline=args.offline)
    for finding in findings:
        print(finding.render())
    errors = sum(item.severity == "error" for item in findings)
    print(f"QA: {errors} error(s), {len(findings) - errors} warning(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
