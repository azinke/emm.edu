#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Exercise public and restricted Git bundle backup/restore without a network."""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import platform
import shutil
import subprocess
import sys
import tempfile
import time


ALLOWED_PUBLIC_BOUNDARY = {
    "curriculum-private/README.md",
    "curriculum-private/current-assessments/.gitkeep",
    "curriculum-private/protected-student-partner-data/.gitkeep",
    "curriculum-private/restricted-solutions/.gitkeep",
}


def run(*args: str, cwd: Path | None = None) -> str:
    environment = os.environ.copy()
    for key in tuple(environment):
        if key.lower() in {"http_proxy", "https_proxy", "ftp_proxy", "all_proxy"}:
            environment.pop(key, None)
    environment.update(
        {
            "GIT_CONFIG_GLOBAL": os.devnull,
            "GIT_CONFIG_NOSYSTEM": "1",
            "GIT_TERMINAL_PROMPT": "0",
            "GIT_ASKPASS": "",
            "GIT_ALLOW_PROTOCOL": "file",
            "NO_PROXY": "*",
        }
    )
    result = subprocess.run(args, cwd=cwd, env=environment, text=True, capture_output=True)
    if result.returncode:
        raise RuntimeError(f"command failed ({' '.join(args)}): {result.stderr.strip()}")
    return result.stdout.strip()


def git_root(path: Path) -> Path:
    return Path(run("git", "rev-parse", "--show-toplevel", cwd=path)).resolve()


def inside(path: Path, parent: Path) -> bool:
    try:
        path.relative_to(parent)
        return True
    except ValueError:
        return False


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def refs(repo: Path) -> set[str]:
    lines = run("git", "for-each-ref", "--format=%(objectname) %(refname)", cwd=repo)
    return set(lines.splitlines()) if lines else set()


def bundle_and_restore(source: Path, bundle: Path, restore: Path) -> dict[str, str | int | bool]:
    run("git", "bundle", "create", str(bundle), "--all", cwd=source)
    run("git", "bundle", "verify", str(bundle), cwd=source)
    source_refs = refs(source)
    bundle_refs = set(run("git", "bundle", "list-heads", str(bundle), cwd=source).splitlines())
    advertised_head = f"{run('git', 'rev-parse', 'HEAD', cwd=source)} HEAD"
    if source_refs != bundle_refs - {advertised_head}:
        raise RuntimeError("bundle ref set differs from source ref set")
    run(
        "git",
        "clone",
        "--no-local",
        str(bundle),
        str(restore),
    )
    run("git", "fsck", "--full", "--strict", cwd=restore)
    source_head = run("git", "rev-parse", "HEAD", cwd=source)
    restored_head = run("git", "rev-parse", "HEAD", cwd=restore)
    source_tree = run("git", "rev-parse", "HEAD^{tree}", cwd=source)
    restored_tree = run("git", "rev-parse", "HEAD^{tree}", cwd=restore)
    if source_head != restored_head or source_tree != restored_tree:
        raise RuntimeError("restored HEAD/tree differs from backup source")
    return {
        "head": source_head,
        "tree": source_tree,
        "bundle_sha256": sha256(bundle),
        "ref_count": len(source_refs),
        "working_tree_clean": not bool(run("git", "status", "--porcelain", cwd=source)),
    }


def scan_public_boundary(repo: Path) -> None:
    tracked = set(run("git", "ls-tree", "-r", "--name-only", "HEAD", cwd=repo).splitlines())
    violations = sorted(
        path
        for path in tracked
        if path.startswith("curriculum-private/") and path not in ALLOWED_PUBLIC_BOUNDARY
    )
    if violations:
        raise RuntimeError("public restore contains restricted-boundary payload paths")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--public-repo", type=Path, required=True)
    parser.add_argument("--private-store", type=Path, required=True)
    parser.add_argument("--keep", type=Path, help="approved controlled directory for drill artifacts")
    parser.add_argument(
        "--offline-command",
        nargs=argparse.REMAINDER,
        help="command to run inside the restored public clone",
    )
    args = parser.parse_args()
    started = time.monotonic()
    try:
        public = git_root(args.public_repo.resolve())
        private = git_root(args.private_store.resolve())
        if public == private or inside(private, public) or inside(public, private):
            raise ValueError("restricted store is not separate from public checkout")

        if args.keep:
            work = args.keep.expanduser().resolve()
            if work.exists() and any(work.iterdir()):
                raise ValueError("--keep directory must be empty")
            work.mkdir(parents=True, exist_ok=True, mode=0o700)
            cleanup = False
        else:
            work = Path(tempfile.mkdtemp(prefix="emm-recovery-drill-"))
            cleanup = True

        try:
            public_result = bundle_and_restore(
                public, work / "public.bundle", work / "public-restored"
            )
            scan_public_boundary(work / "public-restored")
            offline_result = "not-requested"
            if args.offline_command:
                run(*args.offline_command, cwd=work / "public-restored")
                offline_result = "pass"
            private_result = bundle_and_restore(
                private, work / "restricted.bundle", work / "restricted-restored"
            )
            canary = work / "restricted-restored" / "audit" / "synthetic-canary.txt"
            canary_sha256 = sha256(canary) if canary.exists() else "not-present"
            report = {
                "drill_id": "M02-E4-T04",
                "status": "pass",
                "timestamp_utc": datetime.now(timezone.utc).isoformat(),
                "duration_seconds": round(time.monotonic() - started, 3),
                "network_dependency": "none; proxies disabled and Git file protocol only",
                "environment": {
                    "os": platform.platform(),
                    "machine": platform.machine(),
                    "python": platform.python_version(),
                    "git": run("git", "--version"),
                },
                "public": public_result,
                "restricted": private_result,
                "restricted_canary_sha256": canary_sha256,
                "public_boundary_scan": "pass",
                "offline_command": offline_result,
                "temporary_artifacts_destroyed": cleanup,
            }
            print(json.dumps(report, indent=2, sort_keys=True))
        finally:
            if cleanup:
                shutil.rmtree(work, ignore_errors=True)
    except (OSError, RuntimeError, ValueError) as error:
        print(f"backup/restore drill failed: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
