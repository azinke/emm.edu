#!/usr/bin/env python3
"""Networked, read-only health probe for the registered external URLs."""

from __future__ import annotations

import argparse
import concurrent.futures
import sys
import urllib.error
import urllib.request
from pathlib import Path

from scriptlib import CURRICULUM, load_yaml


def probe(entry: dict, timeout: int) -> tuple[str, bool, str]:
    identity = str(entry.get("id", entry.get("url", "<missing>")))
    url = entry.get("url")
    if not url:
        return identity, False, "missing URL"
    headers = {"User-Agent": "emm.edu-link-check/1.0", "Range": "bytes=0-0"}
    request = urllib.request.Request(url, headers=headers, method="GET")
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            status = getattr(response, "status", 200)
            final = response.geturl()
            return identity, 200 <= status < 400, f"HTTP {status} final={final}"
    except (urllib.error.URLError, TimeoutError, ValueError) as exc:
        return identity, False, str(exc)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=CURRICULUM)
    parser.add_argument("--timeout", type=int, default=20)
    args = parser.parse_args()
    registry = load_yaml(args.root / "environments" / "external-links.yml") or {}
    entries = registry.get("entries", [])
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        results = list(pool.map(lambda entry: probe(entry, args.timeout), entries))
    failures = 0
    for identity, passed, detail in results:
        print(f"{'PASS' if passed else 'FAIL'} {identity}: {detail}")
        failures += not passed
    print(f"EXTERNAL-LINKS checked={len(results)} failures={failures}")
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
