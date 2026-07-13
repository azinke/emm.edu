#!/usr/bin/env python3
"""Capture one explicitly permitted source and update its checksum metadata."""

from __future__ import annotations

import argparse
import sys
import urllib.request
from pathlib import Path

import yaml

from scriptlib import CURRICULUM, load_yaml, sha256_file


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source_id")
    parser.add_argument("--root", type=Path, default=CURRICULUM)
    parser.add_argument("--from-file", type=Path, help="capture a previously and lawfully obtained local file")
    parser.add_argument("--allow-network", action="store_true", help="explicit maintainer-only network retrieval")
    args = parser.parse_args()
    root = args.root.resolve()
    registry_path = root / "environments" / "external-links.yml"
    registry = load_yaml(registry_path) or {}
    entries = registry.get("entries", [])
    matches = [entry for entry in entries if entry.get("id") == args.source_id]
    if len(matches) != 1:
        print(f"ERROR expected exactly one registry entry for {args.source_id}", file=sys.stderr)
        return 2
    entry = matches[0]
    if entry.get("archive_permission") != "permitted" or not entry.get("permission_evidence"):
        print("ERROR capture requires archive_permission=permitted and permission_evidence", file=sys.stderr)
        return 2
    archive_path = entry.get("archive_path")
    if not archive_path:
        print("ERROR permitted entry needs archive_path", file=sys.stderr)
        return 2
    destination = (root / archive_path).resolve()
    try:
        destination.relative_to(root)
    except ValueError:
        print("ERROR archive_path must remain inside curriculum", file=sys.stderr)
        return 2
    destination.parent.mkdir(parents=True, exist_ok=True)
    if args.from_file:
        payload = args.from_file.read_bytes()
    elif args.allow_network:
        request = urllib.request.Request(entry["url"], headers={"User-Agent": "emm.edu-source-capture/1.0"})
        with urllib.request.urlopen(request, timeout=30) as response:
            payload = response.read()
    else:
        print("ERROR provide --from-file or explicit --allow-network; ordinary builds never retrieve", file=sys.stderr)
        return 2
    destination.write_bytes(payload)
    entry["bytes"] = len(payload)
    entry["sha256"] = sha256_file(destination)
    registry_path.write_text(yaml.safe_dump(registry, sort_keys=False, allow_unicode=True), encoding="utf-8")
    print(f"CAPTURED {args.source_id} {destination.relative_to(root)} bytes={len(payload)} sha256={entry['sha256']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
