#!/usr/bin/env python3
"""Deterministic offline stand-in used to prove each smoke-hook interface."""

from __future__ import annotations

import argparse
import sys


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--kind", required=True, choices=["code", "numerical", "hdl", "simulation", "kicad"])
    parser.add_argument("--fail", action="store_true")
    args = parser.parse_args()
    print(f"mock {args.kind} hook executed offline")
    return 17 if args.fail else 0


if __name__ == "__main__":
    sys.exit(main())
