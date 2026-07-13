#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Deterministic two-node oracle for the ESE111 Chapter 4 network."""

from __future__ import annotations

import argparse
import itertools
import json
from dataclasses import asdict, dataclass


@dataclass(frozen=True)
class Result:
    source_v: float
    tp_a_v: float
    tp_b_v: float
    i_r1_a: float
    i_r2_a: float
    i_r3_a: float
    i_r4_a: float
    i_meter_a: float
    kcl_a_residual_a: float
    kcl_b_residual_a: float
    kvl_source_r1_r2_residual_v: float
    kvl_r2_r3_r4_residual_v: float
    power_balance_residual_w: float


def solve(source_v: float = 6.0, r1: float = 10_000.0, r2: float = 22_000.0,
          r3: float = 33_000.0, r4: float = 15_000.0,
          meter_b_ohm: float | None = None) -> Result:
    """Solve with currents positive VS→A, A→COM, A→B, and B→COM."""
    values = (source_v, r1, r2, r3, r4)
    if source_v < 0 or any(value <= 0 for value in values[1:]):
        raise ValueError("source must be non-negative and resistances must be positive")
    if meter_b_ohm is not None and meter_b_ohm <= 0:
        raise ValueError("meter input resistance must be positive")

    g1, g2, g3, g4 = (1.0 / value for value in (r1, r2, r3, r4))
    gm = 0.0 if meter_b_ohm is None else 1.0 / meter_b_ohm
    a11, a12 = g1 + g2 + g3, -g3
    a21, a22 = -g3, g3 + g4 + gm
    b1 = g1 * source_v
    determinant = a11 * a22 - a12 * a21
    tp_a = b1 * a22 / determinant
    tp_b = -a21 * b1 / determinant

    i1 = (source_v - tp_a) / r1
    i2 = tp_a / r2
    i3 = (tp_a - tp_b) / r3
    i4 = tp_b / r4
    im = 0.0 if meter_b_ohm is None else tp_b / meter_b_ohm
    kcl_a = i1 - i2 - i3
    kcl_b = i3 - i4 - im
    kvl_source_r1_r2 = source_v - i1 * r1 - i2 * r2
    kvl_r2_r3_r4 = i2 * r2 - i3 * r3 - i4 * r4
    supplied = source_v * i1
    dissipated = i1 * i1 * r1 + i2 * i2 * r2 + i3 * i3 * r3 + i4 * i4 * r4
    if meter_b_ohm is not None:
        dissipated += im * im * meter_b_ohm
    return Result(
        source_v, tp_a, tp_b, i1, i2, i3, i4, im, kcl_a, kcl_b,
        kvl_source_r1_r2, kvl_r2_r3_r4, supplied - dissipated,
    )


def corner_ranges(r4_nominal: float) -> dict[str, list[float]]:
    """Enumerate source ±0.5%, four resistors ±1%, and 1/10 MOhm meters."""
    results = []
    for factors in itertools.product((0.995, 1.005), *((0.99, 1.01),) * 4):
        source_factor, r1f, r2f, r3f, r4f = factors
        for meter in (1_000_000.0, 10_000_000.0):
            results.append(solve(6.0 * source_factor, 10_000 * r1f, 22_000 * r2f,
                                 33_000 * r3f, r4_nominal * r4f, meter))
    fields = ("tp_a_v", "tp_b_v", "i_r1_a", "i_r2_a", "i_r3_a", "i_r4_a")
    return {field: [min(getattr(row, field) for row in results),
                    max(getattr(row, field) for row in results)] for field in fields}


def report() -> dict[str, object]:
    return {
        "model_id": "ESE111-CH04-MODEL-01",
        "provenance": "deterministic analytical simulation; not physical measurement",
        "nominal_unloaded": asdict(solve()),
        "nominal_minimal_meter": asdict(solve(meter_b_ohm=1_000_000.0)),
        "baseline_corner_ranges": corner_ranges(15_000.0),
        "redesign_22k_corner_ranges": corner_ranges(22_000.0),
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--compact", action="store_true")
    args = parser.parse_args()
    print(json.dumps(report(), indent=None if args.compact else 2, sort_keys=True))
