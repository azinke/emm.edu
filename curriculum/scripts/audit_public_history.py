#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Reject restricted payload paths and high-confidence secrets in reachable Git history."""

from __future__ import annotations

import re
from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[2]
ALLOWED_BOUNDARY_PATHS = {
    "curriculum-private/README.md",
    "curriculum-private/current-assessments/.gitkeep",
    "curriculum-private/protected-student-partner-data/.gitkeep",
    "curriculum-private/restricted-solutions/.gitkeep",
}
SECRET_PATTERNS = (
    ("private-key", re.compile(rb"-----BEGIN (?:RSA |EC |OPENSSH |DSA )?PRIVATE KEY-----")),
    ("github-token", re.compile(rb"\bgh[oprsu]_[A-Za-z0-9]{30,}\b")),
    ("aws-access-key", re.compile(rb"\b(?:AKIA|ASIA)[A-Z0-9]{16}\b")),
)
MAX_BLOB_BYTES = 5 * 1024 * 1024


def git(*args: str, input_bytes: bytes | None = None) -> bytes:
    result = subprocess.run(
        ("git", *args), cwd=ROOT, input=input_bytes, capture_output=True
    )
    if result.returncode:
        raise RuntimeError(result.stderr.decode("utf-8", "replace").strip())
    return result.stdout


def main() -> int:
    try:
        objects = git("rev-list", "--objects", "--all").decode("utf-8", "replace").splitlines()
        violations: list[str] = []
        blob_ids: set[str] = set()
        for line in objects:
            object_id, separator, path = line.partition(" ")
            object_type = git("cat-file", "-t", object_id).strip()
            if separator and object_type == b"blob":
                if path.startswith("curriculum-private/") and path not in ALLOWED_BOUNDARY_PATHS:
                    violations.append(f"restricted boundary path in history: {path} ({object_id[:12]})")
                if any(token in path.lower() for token in ("restricted-solution", "current-assessment", "student-record", "partner-confidential")):
                    if path not in ALLOWED_BOUNDARY_PATHS and not path.startswith("curriculum/governance/"):
                        violations.append(f"restricted classification path in history: {path} ({object_id[:12]})")
            if object_type == b"blob":
                blob_ids.add(object_id)

        for object_id in blob_ids:
            size = int(git("cat-file", "-s", object_id))
            if size > MAX_BLOB_BYTES:
                continue
            payload = git("cat-file", "blob", object_id)
            for rule, pattern in SECRET_PATTERNS:
                if pattern.search(payload):
                    violations.append(f"{rule} pattern in reachable blob {object_id[:12]}")

        if violations:
            for violation in sorted(set(violations)):
                print(f"ERROR HISTORY001 {violation}")
            return 1
        print(f"public history audit passed ({len(blob_ids)} unique reachable blobs)")
        return 0
    except (OSError, RuntimeError, ValueError) as error:
        print(f"history audit failed: {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
