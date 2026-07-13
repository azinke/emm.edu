#!/usr/bin/env python3
"""Seeded positive and negative verification for the canonical E1 model."""

from __future__ import annotations

import json
import subprocess
import sys
import unittest
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / "curriculum" / "scripts" / "validate_canonical.py"
FIXTURES = ROOT / "curriculum" / "tests" / "fixtures" / "canonical"


class CanonicalValidationTests(unittest.TestCase):
    maxDiff = None

    def run_validator(self, *extra: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, str(SCRIPT), "--root", str(ROOT), "--as-of", "2026-07-13", *extra],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )

    def test_canonical_positive_fixture(self) -> None:
        result = self.run_validator()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("canonical validation passed", result.stdout)

    def test_seeded_negative_fixtures_are_caught(self) -> None:
        fixtures = sorted(FIXTURES.glob("*.json"))
        self.assertGreaterEqual(len(fixtures), 6)
        for fixture in fixtures:
            expected = json.loads(fixture.read_text(encoding="utf-8"))["expect"]
            with self.subTest(fixture=fixture.name):
                result = self.run_validator("--fixture", str(fixture))
                self.assertNotEqual(result.returncode, 0, result.stdout)
                self.assertIn(expected, result.stderr)

    def test_generators_have_no_drift(self) -> None:
        for script in ("generate_canonical_data.py", "generate_canonical_backlog.py"):
            with self.subTest(script=script):
                result = subprocess.run(
                    [sys.executable, str(ROOT / "curriculum" / "scripts" / script), "--check"],
                    cwd=ROOT,
                    text=True,
                    capture_output=True,
                    check=False,
                )
                self.assertEqual(result.returncode, 0, result.stdout + result.stderr)


if __name__ == "__main__":
    unittest.main()
