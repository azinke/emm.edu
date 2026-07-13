#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Offline regression tests for M02-E4 governance controls."""

from __future__ import annotations

from pathlib import Path
import subprocess
import sys
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[2]
SCRIPTS = ROOT / "curriculum" / "scripts"


class GovernanceTests(unittest.TestCase):
    def test_required_controls_exist(self) -> None:
        required = (
            ROOT / "CHANGELOG.md",
            ROOT / "VERSION",
            ROOT / ".github" / "PULL_REQUEST_TEMPLATE.md",
            ROOT / "curriculum" / "governance" / "versioning-and-release.md",
            ROOT / "curriculum" / "governance" / "restricted-material.md",
            ROOT / "curriculum" / "governance" / "review-checklist.md",
            ROOT / "curriculum" / "governance" / "backup-restore.md",
            ROOT / "curriculum" / "governance" / "licensing-and-contributions.md",
            ROOT / "curriculum" / "qualification" / "README.md",
        )
        self.assertEqual([], [str(path) for path in required if not path.is_file()])

    def test_private_store_refuses_public_child(self) -> None:
        result = subprocess.run(
            [
                sys.executable,
                str(SCRIPTS / "initialize_restricted_store.py"),
                str(ROOT / "should-not-exist-private"),
                "--drill",
            ],
            text=True,
            capture_output=True,
        )
        self.assertNotEqual(0, result.returncode)
        self.assertIn("separate", result.stderr)

    def test_public_history_has_no_restricted_payload(self) -> None:
        result = subprocess.run(
            [sys.executable, str(SCRIPTS / "audit_public_history.py")],
            text=True,
            capture_output=True,
        )
        self.assertEqual(0, result.returncode, result.stdout + result.stderr)
        self.assertIn("history audit passed", result.stdout)

    def test_private_store_and_restore_drill(self) -> None:
        with tempfile.TemporaryDirectory(prefix="emm-governance-test-") as temp:
            private = Path(temp) / "restricted"
            provision = subprocess.run(
                [
                    sys.executable,
                    str(SCRIPTS / "initialize_restricted_store.py"),
                    str(private),
                    "--drill",
                ],
                text=True,
                capture_output=True,
            )
            self.assertEqual(0, provision.returncode, provision.stderr)
            drill = subprocess.run(
                [
                    sys.executable,
                    str(SCRIPTS / "backup_restore_drill.py"),
                    "--public-repo",
                    str(ROOT),
                    "--private-store",
                    str(private),
                ],
                text=True,
                capture_output=True,
            )
            self.assertEqual(0, drill.returncode, drill.stderr)
            self.assertIn('"status": "pass"', drill.stdout)


if __name__ == "__main__":
    unittest.main()
