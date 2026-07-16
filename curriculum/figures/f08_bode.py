#!/usr/bin/env python3
"""Generate the calculated first-order RC Bode teaching figure as SVG."""

from __future__ import annotations

import argparse
from math import atan, degrees, log10, sqrt
from pathlib import Path
import shutil
import subprocess


WIDTH = 900
HEIGHT = 620
LEFT = 90
RIGHT = 30
TOP = 45
PANEL_H = 220
GAP = 85


def x_coord(ratio: float) -> float:
    return LEFT + (log10(ratio) + 2.0) * (WIDTH - LEFT - RIGHT) / 4.0


def mag_y(db_value: float) -> float:
    return TOP + (5.0 - db_value) * PANEL_H / 50.0


def phase_y(degrees_value: float) -> float:
    panel_top = TOP + PANEL_H + GAP
    return panel_top + (5.0 - degrees_value) * PANEL_H / 100.0


def path(points: list[tuple[float, float]]) -> str:
    commands = [f"M {points[0][0]:.2f} {points[0][1]:.2f}"]
    commands.extend(f"L {x:.2f} {y:.2f}" for x, y in points[1:])
    return " ".join(commands)


def generate_svg() -> str:
    ratios = [10 ** (-2.0 + index * 4.0 / 240.0) for index in range(241)]
    exact_mag = [
        (x_coord(ratio), mag_y(20.0 * log10(1.0 / sqrt(1.0 + ratio**2))))
        for ratio in ratios
    ]
    exact_phase = [
        (x_coord(ratio), phase_y(-degrees(atan(ratio))))
        for ratio in ratios
    ]
    asymptote = [
        (x_coord(0.01), mag_y(0.0)),
        (x_coord(1.0), mag_y(0.0)),
        (x_coord(100.0), mag_y(-40.0)),
    ]
    items = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" '
        f'height="{HEIGHT}" viewBox="0 0 {WIDTH} {HEIGHT}">',
        '<rect width="100%" height="100%" fill="white"/>',
        '<g font-family="sans-serif" font-size="15" fill="black" '
        'stroke="black" stroke-width="1">',
    ]
    x_ticks = [(0.01, "0.01"), (0.1, "0.1"), (1.0, "1"),
               (10.0, "10"), (100.0, "100")]
    for ratio, label in x_ticks:
        x = x_coord(ratio)
        items.append(
            f'<line x1="{x:.2f}" y1="{TOP}" x2="{x:.2f}" '
            f'y2="{TOP + 2 * PANEL_H + GAP}" stroke="#bbbbbb"/>'
        )
        items.append(
            f'<text x="{x:.2f}" y="{HEIGHT - 20}" '
            f'text-anchor="middle" stroke="none">{label}</text>'
        )
    for db_value in (0, -10, -20, -30, -40):
        y = mag_y(db_value)
        items.append(
            f'<line x1="{LEFT}" y1="{y:.2f}" x2="{WIDTH - RIGHT}" '
            f'y2="{y:.2f}" stroke="#dddddd"/>'
        )
        items.append(
            f'<text x="{LEFT - 12}" y="{y + 5:.2f}" text-anchor="end" '
            f'stroke="none">{db_value}</text>'
        )
    for angle in (0, -30, -45, -60, -90):
        y = phase_y(angle)
        items.append(
            f'<line x1="{LEFT}" y1="{y:.2f}" x2="{WIDTH - RIGHT}" '
            f'y2="{y:.2f}" stroke="#dddddd"/>'
        )
        items.append(
            f'<text x="{LEFT - 12}" y="{y + 5:.2f}" text-anchor="end" '
            f'stroke="none">{angle}°</text>'
        )
    corner_x = x_coord(1.0)
    items.extend([
        f'<line x1="{corner_x:.2f}" y1="{TOP}" x2="{corner_x:.2f}" '
        f'y2="{TOP + 2 * PANEL_H + GAP}" stroke="black" '
        'stroke-dasharray="2 6" stroke-width="2"/>',
        f'<path d="{path(exact_mag)}" fill="none" stroke="black" '
        'stroke-width="3"/>',
        f'<path d="{path(asymptote)}" fill="none" stroke="#555555" '
        'stroke-width="2" stroke-dasharray="10 7"/>',
        f'<path d="{path(exact_phase)}" fill="none" stroke="black" '
        'stroke-width="3"/>',
        f'<circle cx="{corner_x:.2f}" cy="{mag_y(-3.0103):.2f}" r="5" '
        'fill="white" stroke="black" stroke-width="2"/>',
        f'<circle cx="{corner_x:.2f}" cy="{phase_y(-45.0):.2f}" r="5" '
        'fill="white" stroke="black" stroke-width="2"/>',
        f'<text x="{corner_x + 10:.2f}" y="{mag_y(-3.0103) - 10:.2f}" '
        'stroke="none">−3.010 dB at f = fc</text>',
        f'<text x="{corner_x + 10:.2f}" y="{phase_y(-45.0) - 10:.2f}" '
        'stroke="none">−45° at f = fc</text>',
        '<text x="24" y="155" transform="rotate(-90 24 155)" '
        'text-anchor="middle" stroke="none">Magnitude (dB)</text>',
        '<text x="24" y="470" transform="rotate(-90 24 470)" '
        'text-anchor="middle" stroke="none">Phase (degrees)</text>',
        f'<text x="{WIDTH / 2:.2f}" y="{HEIGHT - 2}" '
        'text-anchor="middle" stroke="none">Normalized frequency f / fc</text>',
        '<line x1="620" y1="65" x2="675" y2="65" stroke="black" '
        'stroke-width="3"/>',
        '<text x="685" y="70" stroke="none">exact response</text>',
        '<line x1="620" y1="90" x2="675" y2="90" stroke="#555555" '
        'stroke-width="2" stroke-dasharray="10 7"/>',
        '<text x="685" y="95" stroke="none">Bode asymptote</text>',
        '<text x="700" y="205" stroke="none">−20 dB/decade</text>',
        '</g>',
        '</svg>',
    ])
    return "\n".join(items)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "output",
        nargs="?",
        type=Path,
        default=Path(__file__).with_name("f08-rc-bode.svg"),
    )
    args = parser.parse_args()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(generate_svg(), encoding="utf-8")
    print(f"wrote {args.output}")
    inkscape = shutil.which("inkscape")
    if inkscape is None:
        raise RuntimeError("inkscape is required to generate the PNG")
    png_output = args.output.with_suffix(".png")
    subprocess.run(
        [
            inkscape,
            str(args.output),
            "--export-type=png",
            f"--export-filename={png_output}",
            "--export-width=1800",
        ],
        check=True,
    )
    print(f"wrote {png_output}")


if __name__ == "__main__":
    main()
