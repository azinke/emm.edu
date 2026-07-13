#!/usr/bin/env python3
"""Compare rendered PNGs with reviewed goldens using policy thresholds."""

from __future__ import annotations

import argparse
import re
import shutil
import sys
from pathlib import Path

from scriptlib import CURRICULUM, load_yaml, run_command


def metric_value(output: str) -> float | None:
    match = re.search(r"\(([-+0-9.eE]+)\)", output)
    if match:
        return float(match.group(1))
    match = re.search(r"[-+0-9.eE]+", output)
    return float(match.group(0)) if match else None


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("actual", type=Path)
    parser.add_argument("golden", type=Path)
    parser.add_argument("--root", type=Path, default=CURRICULUM)
    parser.add_argument("--diff", type=Path)
    args = parser.parse_args()
    if not shutil.which("compare"):
        print("SKIP ImageMagick compare is unavailable; visual regression remains required for release")
        return 3
    policy = load_yaml(args.root / "environments" / "qa-policy.yml") or {}
    threshold = float(policy.get("visual_regression", {}).get("root_mean_square_error", 0.01))
    diff = args.diff or args.actual.with_name(args.actual.stem + "-diff.png")
    result = run_command(["compare", "-metric", "RMSE", str(args.golden), str(args.actual), str(diff)], cwd=args.actual.parent)
    metric = metric_value(result.stderr)
    if metric is None:
        print(f"ERROR unable to parse ImageMagick metric: {result.stderr}", file=sys.stderr)
        return 2
    print(f"VISUAL-RMSE {metric:.8f} threshold={threshold:.8f} diff={diff}")
    return 1 if metric > threshold else 0


if __name__ == "__main__":
    sys.exit(main())
