#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Provision a separate restricted curriculum Git store.

The store must be outside the public checkout. Production initialization requires
a private remote; --drill creates a committed synthetic store for recovery tests.
"""

from __future__ import annotations

import argparse
import os
from pathlib import Path
import stat
import subprocess
import sys


PUBLIC_ROOT = Path(__file__).resolve().parents[2]


def run(*args: str, cwd: Path) -> None:
    result = subprocess.run(args, cwd=cwd, text=True, capture_output=True)
    if result.returncode:
        raise RuntimeError(f"command failed ({' '.join(args)}): {result.stderr.strip()}")


def is_within(path: Path, parent: Path) -> bool:
    try:
        path.relative_to(parent)
        return True
    except ValueError:
        return False


def write_private(path: Path, content: str) -> None:
    path.write_text(content, encoding="utf-8")
    path.chmod(stat.S_IRUSR | stat.S_IWUSR)


def provision(target: Path, remote: str | None, drill: bool) -> None:
    target = target.expanduser().resolve()
    if is_within(target, PUBLIC_ROOT) or is_within(PUBLIC_ROOT, target):
        raise ValueError("restricted store must be separate from the public checkout")
    if target.exists() and any(target.iterdir()):
        raise ValueError(f"target is not empty: {target}")
    if not drill and not remote:
        raise ValueError("production initialization requires --remote")

    target.mkdir(parents=True, exist_ok=True, mode=0o700)
    target.chmod(0o700)
    run("git", "init", "--initial-branch=main", cwd=target)

    areas = (
        "current-assessments",
        "restricted-solutions",
        "student-data",
        "partner-confidential",
        "audit",
    )
    for area in areas:
        directory = target / area
        directory.mkdir(mode=0o700)
        write_private(directory / ".gitkeep", "")

    write_private(
        target / "README.md",
        "# Restricted EMM curriculum store\n\n"
        "Classification: restricted. This repository is not public courseware.\n"
        "Access, retention, transfer, incident, and backup decisions follow the "
        "approved institutional policy and public control GOV-SEC-001.\n",
    )
    write_private(
        target / "access-policy.yml",
        "version: 1.0.0\n"
        "classification: restricted\n"
        "owner_roles: [assessment-owner, data-steward]\n"
        "named_accounts_only: true\n"
        "term_access_review_required: true\n"
        "mfa_required_where_available: true\n"
        "public_payload_export: prohibited\n"
        "backup_restore_cadence: each-release-and-termly\n",
    )
    if drill:
        write_private(
            target / "audit" / "synthetic-canary.txt",
            "SYNTHETIC RECOVERY CANARY; NO PERSON, ANSWER, OR PARTNER DATA.\n",
        )

    if remote:
        run("git", "remote", "add", "origin", remote, cwd=target)

    if drill:
        run("git", "config", "user.name", "Recovery Drill", cwd=target)
        run("git", "config", "user.email", "drill.invalid@example.invalid", cwd=target)
        run("git", "add", ".", cwd=target)
        run("git", "commit", "-m", "Initialize synthetic restricted drill store", cwd=target)

    for root, directories, files in os.walk(target):
        root_path = Path(root)
        if ".git" in root_path.parts:
            continue
        root_path.chmod(0o700)
        for name in directories:
            if name != ".git":
                (root_path / name).chmod(0o700)
        for name in files:
            (root_path / name).chmod(0o600)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("target", type=Path)
    parser.add_argument("--remote", help="approved private remote URL")
    parser.add_argument("--drill", action="store_true", help="create synthetic committed test store")
    args = parser.parse_args()
    try:
        provision(args.target, args.remote, args.drill)
    except (OSError, RuntimeError, ValueError) as error:
        print(f"restricted-store initialization failed: {error}", file=sys.stderr)
        return 1
    print(f"restricted store initialized at {args.target.expanduser().resolve()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
