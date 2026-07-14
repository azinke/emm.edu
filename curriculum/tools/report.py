#!/usr/bin/env python3
"""Generate curriculum reports from the canonical registry using only the standard library.

Produces three Markdown sections:

1. a chapter maturity dashboard (status counts per part);
2. a program-outcome assurance-of-learning matrix (outcome x semester, with the
   deepest coverage level reached, derived from the leveled course mappings);
3. a chapter prerequisite dependency graph as Mermaid source.

The report is a build artifact, not canonical source. It is written under
`build/reports/` (git-ignored) and also printed to stdout. Run
`python3 curriculum/tools/validate.py` first; this tool assumes valid data.
"""

from __future__ import annotations

import sys
import tomllib
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
CURRICULUM = ROOT / "curriculum"
BOOK = CURRICULUM / "book"

STATUS_ORDER = ["outline", "draft", "review", "released"]
LEVEL_RANK = {"introduce": 1, "reinforce": 2, "master": 3}
LEVEL_MARK = {"introduce": "I", "reinforce": "R", "master": "M"}


def load(path: Path) -> dict:
    return tomllib.loads(path.read_text(encoding="utf-8"))


def read_status(file_relative: str) -> str:
    """Read the `status:` scalar from a chapter's YAML front matter."""
    lines = (BOOK / file_relative).read_text(encoding="utf-8").splitlines()
    if not lines or lines[0].strip() != "---":
        return "unknown"
    for line in lines[1:]:
        if line.strip() == "---":
            break
        if line.strip().startswith("status:"):
            return line.split(":", 1)[1].strip().strip("\"'")
    return "unknown"


def maturity_dashboard(chapters: list[dict]) -> list[str]:
    parts: dict[str, Counter] = defaultdict(Counter)
    order: list[str] = []
    for chapter in chapters:
        part = chapter.get("part", "?")
        if part not in order:
            order.append(part)
        parts[part][read_status(chapter["file"])] += 1
    lines = ["## Chapter maturity dashboard", ""]
    header = "| Part | " + " | ".join(STATUS_ORDER) + " | total |"
    lines.append(header)
    lines.append("|" + "---|" * (len(STATUS_ORDER) + 2))
    totals: Counter = Counter()
    for part in order:
        counts = parts[part]
        totals.update(counts)
        cells = [str(counts.get(status, 0)) for status in STATUS_ORDER]
        lines.append(f"| {part} | " + " | ".join(cells) + f" | {sum(counts.values())} |")
    grand = [str(totals.get(status, 0)) for status in STATUS_ORDER]
    lines.append(f"| **all** | " + " | ".join(grand) + f" | {sum(totals.values())} |")
    lines.append("")
    return lines


def assurance_matrix(
    outcomes: list[dict], courses: list[dict], semesters: list[dict]
) -> list[str]:
    semester_by_course = {
        course_id: sem["number"] for sem in semesters for course_id in sem["course_ids"]
    }
    numbers = sorted({sem["number"] for sem in semesters})

    # Deepest coverage level a chapter reaches in each semester.
    chapter_semester_level: dict[str, dict[int, int]] = defaultdict(dict)
    for course in courses:
        semester = semester_by_course.get(course["id"])
        if semester is None:
            continue
        for entry in course["chapters"]:
            rank = LEVEL_RANK[entry["level"]]
            current = chapter_semester_level[entry["id"]].get(semester, 0)
            chapter_semester_level[entry["id"]][semester] = max(current, rank)

    lines = ["## Program-outcome assurance-of-learning matrix", ""]
    lines.append(
        "Deepest coverage per semester: `I` introduce, `R` reinforce, `M` master."
    )
    lines.append("")
    lines.append("| Outcome | " + " | ".join(f"S{n}" for n in numbers) + " | Peak |")
    lines.append("|" + "---|" * (len(numbers) + 2))
    inverse = {rank: mark for mark, rank in LEVEL_RANK.items()}
    for outcome in outcomes:
        per_semester: dict[int, int] = defaultdict(int)
        peak = 0
        for chapter_id in outcome["chapter_ids"]:
            for semester, rank in chapter_semester_level.get(chapter_id, {}).items():
                per_semester[semester] = max(per_semester[semester], rank)
                peak = max(peak, rank)
        cells = []
        for number in numbers:
            rank = per_semester.get(number, 0)
            cells.append(LEVEL_MARK[inverse[rank]] if rank else "")
        peak_mark = LEVEL_MARK[inverse[peak]] if peak else "-"
        lines.append(f"| {outcome['id']} | " + " | ".join(cells) + f" | {peak_mark} |")
    lines.append("")
    return lines


def dependency_graph(chapters: list[dict]) -> list[str]:
    lines = ["## Chapter prerequisite dependency graph", "", "```mermaid", "graph LR"]
    for chapter in chapters:
        node = chapter["id"]
        prerequisites = chapter.get("prerequisites", [])
        if not prerequisites:
            lines.append(f"    {node}")
        for prerequisite in prerequisites:
            lines.append(f"    {prerequisite} --> {node}")
    lines.append("```")
    lines.append("")
    return lines


def main() -> int:
    chapters = load(BOOK / "chapters.toml")["chapter"]
    courses = load(CURRICULUM / "courses" / "catalog.toml")["course"]
    outcomes = load(CURRICULUM / "courses" / "outcomes.toml")["outcome"]
    semesters = load(CURRICULUM / "courses" / "program.toml")["semester"]

    sections = ["# Curriculum report", ""]
    sections.append(
        "Generated from the canonical registry by `curriculum/tools/report.py`. "
        "This is a build artifact; do not edit by hand."
    )
    sections.append("")
    sections += maturity_dashboard(chapters)
    sections += assurance_matrix(outcomes, courses, semesters)
    sections += dependency_graph(chapters)
    report = "\n".join(sections).rstrip() + "\n"

    output = ROOT / "build" / "reports" / "curriculum-report.md"
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(report, encoding="utf-8")
    print(report)
    print(f"# wrote {output.relative_to(ROOT)}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
