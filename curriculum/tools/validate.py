#!/usr/bin/env python3
"""Validate the book-first curriculum structure using only the Python standard library."""

from __future__ import annotations

import re
import sys
import tomllib
from collections import Counter
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[2]
CURRICULUM = ROOT / "curriculum"
errors: list[str] = []
checks = 0
VALID_CHAPTER_STATUSES = {"outline", "draft", "review", "released"}
VALID_PAGE_ROLES = {"frontmatter", "part", "backmatter"}
VALID_COVERAGE_LEVELS = {"introduce", "reinforce", "master"}


def load_toml(path: Path) -> dict:
    global checks
    checks += 1
    try:
        return tomllib.loads(path.read_text(encoding="utf-8"))
    except (OSError, tomllib.TOMLDecodeError) as error:
        errors.append(f"{path.relative_to(ROOT)}: {error}")
        return {}


def load_front_matter(path: Path) -> dict[str, str]:
    """Read the scalar fields used by the structural checks without a YAML dependency."""
    global checks
    checks += 1
    try:
        text = path.read_text(encoding="utf-8")
    except OSError as error:
        errors.append(f"{path.relative_to(ROOT)}: {error}")
        return {}
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        errors.append(f"{path.relative_to(ROOT)}: missing YAML front matter")
        return {}
    try:
        end = lines.index("---", 1)
    except ValueError:
        errors.append(f"{path.relative_to(ROOT)}: unclosed YAML front matter")
        return {}
    metadata: dict[str, str] = {}
    field_pattern = re.compile(r"^([A-Za-z][A-Za-z0-9_-]*):\s*(.*?)\s*$")
    for line in lines[1:end]:
        match = field_pattern.match(line)
        if not match:
            continue
        key, value = match.groups()
        if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
            value = value[1:-1]
        metadata[key] = value
    return metadata


def unique(records: list[dict], key: str, label: str) -> set[str]:
    global checks
    values = [record.get(key) for record in records]
    missing = [index for index, value in enumerate(values, 1) if not value]
    if missing:
        errors.append(f"{label}: records missing {key}: {missing}")
    duplicates = [value for value, count in Counter(values).items() if value and count > 1]
    if duplicates:
        errors.append(f"{label}: duplicate {key}: {', '.join(sorted(duplicates))}")
    checks += len(values)
    return {value for value in values if isinstance(value, str) and value}


def check_refs(
    records: list[dict], field: str, valid: set[str], label: str
) -> None:
    global checks
    for record in records:
        owner = record.get("id", "<unknown>")
        values = record.get(field, [])
        if isinstance(values, str):
            values = [values]
        for value in values:
            checks += 1
            if value not in valid:
                errors.append(f"{label} {owner}: unknown {field} value {value}")


def check_prerequisite_cycles(records: list[dict], chapter_ids: set[str]) -> None:
    graph = {
        record["id"]: record.get("prerequisites", [])
        for record in records
        if record.get("id") in chapter_ids
    }
    visiting: set[str] = set()
    visited: set[str] = set()

    def visit(node: str, trail: list[str]) -> None:
        if node in visiting:
            start = trail.index(node)
            errors.append("chapter prerequisite cycle: " + " -> ".join(trail[start:] + [node]))
            return
        if node in visited:
            return
        visiting.add(node)
        for dependency in graph.get(node, []):
            visit(dependency, trail + [node])
        visiting.remove(node)
        visited.add(node)

    for chapter_id in graph:
        visit(chapter_id, [])


def check_default_reading_order(records: list[dict]) -> None:
    order = {record["id"]: index for index, record in enumerate(records)}
    for record in records:
        for dependency in record.get("prerequisites", []):
            if dependency.startswith(("M", "T")):
                continue
            if order.get(dependency, -1) > order.get(record["id"], -1):
                errors.append(
                    f"chapter {record['id']}: prerequisite {dependency} appears later "
                    "in the default reading order"
                )


def load_course_chapters(
    courses: list[dict], chapter_ids: set[str]
) -> tuple[dict[str, list[str]], dict[str, set[str]]]:
    """Validate leveled course chapter mappings and index them for later checks."""
    global checks
    course_chapter_map: dict[str, list[str]] = {}
    chapter_levels: dict[str, set[str]] = {}
    for course in courses:
        owner = course.get("id", "<unknown>")
        entries = course.get("chapters")
        if not isinstance(entries, list) or not entries:
            errors.append(f"course {owner}: missing chapters list")
            course_chapter_map[owner] = []
            continue
        ids: list[str] = []
        for entry in entries:
            checks += 1
            if not isinstance(entry, dict) or "id" not in entry or "level" not in entry:
                errors.append(f"course {owner}: chapter entry needs id and level: {entry!r}")
                continue
            chapter_id = entry["id"]
            level = entry["level"]
            if chapter_id not in chapter_ids:
                errors.append(f"course {owner}: unknown chapter id {chapter_id}")
            if level not in VALID_COVERAGE_LEVELS:
                errors.append(
                    f"course {owner}: chapter {chapter_id} has invalid level {level}; "
                    "expected one of " + ", ".join(sorted(VALID_COVERAGE_LEVELS))
                )
            ids.append(chapter_id)
            chapter_levels.setdefault(chapter_id, set()).add(level)
        duplicates = [value for value, count in Counter(ids).items() if count > 1]
        if duplicates:
            errors.append(f"course {owner}: duplicate chapters: {', '.join(sorted(duplicates))}")
        course_chapter_map[owner] = ids
    return course_chapter_map, chapter_levels


def check_chapter_semester_coherence(
    chapters: list[dict],
    course_chapter_map: dict[str, list[str]],
    semester_by_course: dict[str, int],
) -> None:
    """Every non-appendix prerequisite chapter must be taught no later than its dependents.

    Complements the course-level prerequisite check: a course route can otherwise
    schedule a chapter before the chapter theory it depends on. Appendix chapters
    (M/T) are just-in-time references and are exempt, matching the reading-order rule.
    """
    global checks
    prerequisites = {record["id"]: record.get("prerequisites", []) for record in chapters}
    earliest: dict[str, int] = {}
    for course_id, chapter_ids in course_chapter_map.items():
        semester = semester_by_course.get(course_id)
        if semester is None:
            continue
        for chapter_id in chapter_ids:
            earliest[chapter_id] = min(earliest.get(chapter_id, 10**9), semester)
    for chapter_id, semester in sorted(earliest.items()):
        for prerequisite in prerequisites.get(chapter_id, []):
            if prerequisite.startswith(("M", "T")):
                continue
            checks += 1
            prerequisite_semester = earliest.get(prerequisite)
            if prerequisite_semester is None:
                errors.append(
                    f"chapter {chapter_id} is taught in semester {semester}, but its "
                    f"prerequisite {prerequisite} is taught by no scheduled course"
                )
            elif prerequisite_semester > semester:
                errors.append(
                    f"chapter {chapter_id} is first taught in semester {semester}, before "
                    f"its prerequisite {prerequisite} (first taught in semester "
                    f"{prerequisite_semester})"
                )


def check_internal_links() -> None:
    global checks
    link_pattern = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")
    for path in list(ROOT.glob("*.md")) + list((ROOT / "blueprint").rglob("*.md")) + list(
        CURRICULUM.rglob("*.md")
    ) + list(CURRICULUM.rglob("*.qmd")):
        text = path.read_text(encoding="utf-8")
        for raw_target in link_pattern.findall(text):
            target = raw_target.strip().split(maxsplit=1)[0].strip("<>")
            checks += 1
            if (
                not target
                or target.startswith(("#", "http://", "https://", "mailto:"))
                or "{{" in target
            ):
                continue
            relative = unquote(target.split("#", 1)[0])
            if relative and not (path.parent / relative).exists():
                errors.append(
                    f"{path.relative_to(ROOT)}: broken internal link {raw_target}"
                )


def main() -> int:
    global checks
    chapter_data = load_toml(CURRICULUM / "book" / "chapters.toml")
    chapters = chapter_data.get("chapter", [])
    chapter_ids = unique(chapters, "id", "chapters")
    chapter_files = unique(chapters, "file", "chapters")
    check_refs(chapters, "prerequisites", chapter_ids, "chapter")
    check_prerequisite_cycles(chapters, chapter_ids)
    check_default_reading_order(chapters)

    chapter_order = [record.get("file", "") for record in chapters]
    part_directories: dict[str, set[str]] = {}
    for record in chapters:
        path = CURRICULUM / "book" / record.get("file", "")
        checks += 1
        if not path.is_file():
            errors.append(f"chapter {record.get('id')}: missing {path.relative_to(ROOT)}")
            continue
        metadata = load_front_matter(path)
        if metadata.get("chapter-id") != record.get("id"):
            errors.append(
                f"{path.relative_to(ROOT)}: chapter-id must be {record.get('id')}"
            )
        if metadata.get("title") != record.get("title"):
            errors.append(
                f"{path.relative_to(ROOT)}: title does not match chapters.toml"
            )
        if metadata.get("status") not in VALID_CHAPTER_STATUSES:
            errors.append(
                f"{path.relative_to(ROOT)}: status must be one of "
                + ", ".join(sorted(VALID_CHAPTER_STATUSES))
            )
        part = record.get("part")
        if isinstance(part, str):
            part_directories.setdefault(part, set()).add(Path(record["file"]).parent.as_posix())

    for part, directories in part_directories.items():
        checks += 1
        if len(directories) != 1:
            errors.append(
                f"chapter part {part}: files span multiple directories: "
                + ", ".join(sorted(directories))
            )

    quarto = (CURRICULUM / "book" / "_quarto.yml").read_text(encoding="utf-8")
    listed_order = re.findall(
        r"(?m)^\s*-\s+(?:part:\s+)?([^\s]+\.qmd)\s*$", quarto
    )
    listed = set(listed_order)
    if len(listed) != len(listed_order):
        duplicates = [
            path for path, count in Counter(listed_order).items() if count > 1
        ]
        errors.append("duplicate pages in _quarto.yml: " + ", ".join(sorted(duplicates)))

    all_book_pages = {
        path.relative_to(CURRICULUM / "book").as_posix()
        for path in (CURRICULUM / "book").rglob("*.qmd")
    }
    missing_from_quarto = all_book_pages - listed
    extra_in_quarto = listed - all_book_pages
    if missing_from_quarto:
        errors.append(
            "book pages absent from _quarto.yml: "
            + ", ".join(sorted(missing_from_quarto))
        )
    if extra_in_quarto:
        errors.append(
            "missing book pages named in _quarto.yml: "
            + ", ".join(sorted(extra_in_quarto))
        )
    listed_chapter_order = [path for path in listed_order if path in chapter_files]
    checks += 1
    if listed_chapter_order != chapter_order:
        errors.append("chapter order in _quarto.yml does not match chapters.toml")

    supporting_pages = all_book_pages - chapter_files
    part_pages_by_id: dict[str, list[str]] = {}
    for relative in sorted(supporting_pages):
        metadata = load_front_matter(CURRICULUM / "book" / relative)
        role = metadata.get("page-role")
        if not metadata.get("title"):
            errors.append(f"curriculum/book/{relative}: supporting page missing title")
        if role not in VALID_PAGE_ROLES:
            errors.append(
                f"curriculum/book/{relative}: page-role must be one of "
                + ", ".join(sorted(VALID_PAGE_ROLES))
            )
            continue
        if role == "part":
            part_id = metadata.get("part-id")
            if not part_id:
                errors.append(f"curriculum/book/{relative}: part page missing part-id")
            else:
                part_pages_by_id.setdefault(part_id, []).append(relative)
                expected_directories = part_directories.get(part_id, set())
                if Path(relative).parent.as_posix() not in expected_directories:
                    errors.append(
                        f"curriculum/book/{relative}: part-id {part_id} does not match its directory"
                    )

    chapter_parts = set(part_directories)
    part_page_ids = set(part_pages_by_id)
    checks += len(supporting_pages)
    if chapter_parts != part_page_ids:
        errors.append(
            "chapter/part-page mismatch; symmetric difference: "
            + ", ".join(sorted(chapter_parts ^ part_page_ids))
        )
    duplicate_part_pages = [
        part_id for part_id, paths in part_pages_by_id.items() if len(paths) > 1
    ]
    if duplicate_part_pages:
        errors.append(
            "parts with multiple introduction pages: "
            + ", ".join(sorted(duplicate_part_pages))
        )

    quarto_part_pages = set(
        re.findall(r"(?m)^\s*-\s+part:\s+([^\s]+\.qmd)\s*$", quarto)
    )
    declared_part_pages = {
        paths[0] for paths in part_pages_by_id.values() if len(paths) == 1
    }
    if quarto_part_pages != declared_part_pages:
        errors.append(
            "_quarto.yml part entries do not match pages with page-role: part"
        )
    checks += len(listed)

    lab_data = load_toml(CURRICULUM / "labs" / "catalog.toml")
    labs = lab_data.get("lab", [])
    lab_ids = unique(labs, "id", "labs")
    check_refs(labs, "chapter_ids", chapter_ids, "lab")

    project_data = load_toml(CURRICULUM / "projects" / "spine.toml")
    projects = project_data.get("project", [])
    project_ids = unique(projects, "id", "projects")
    check_refs(projects, "chapter_ids", chapter_ids, "project")

    course_data = load_toml(CURRICULUM / "courses" / "catalog.toml")
    courses = course_data.get("course", [])
    course_ids = unique(courses, "id", "courses")
    course_chapter_map, chapter_levels = load_course_chapters(courses, chapter_ids)
    check_refs(courses, "lab_ids", lab_ids, "course")
    check_refs(courses, "project_ids", project_ids, "course")
    check_refs(courses, "prerequisite_ids", course_ids, "course")
    check_refs(courses, "corequisite_ids", course_ids, "course")

    outcome_data = load_toml(CURRICULUM / "courses" / "outcomes.toml")
    outcomes = outcome_data.get("outcome", [])
    unique(outcomes, "id", "outcomes")
    check_refs(outcomes, "chapter_ids", chapter_ids, "outcome")
    for outcome in outcomes:
        owner = outcome.get("id", "<unknown>")
        outcome_chapters = outcome.get("chapter_ids", [])
        checks += 1
        if not outcome.get("statement"):
            errors.append(f"outcome {owner}: missing statement")
        if not any(chapter_id in chapter_levels for chapter_id in outcome_chapters):
            errors.append(f"outcome {owner}: no course introduces any of its chapters")
        elif not any(
            "master" in chapter_levels.get(chapter_id, set())
            for chapter_id in outcome_chapters
        ):
            errors.append(
                f"outcome {owner}: no course carries any of its chapters to master level"
            )

    program = load_toml(CURRICULUM / "courses" / "program.toml")
    semesters = program.get("semester", [])
    used_courses: list[str] = []
    semester_by_course: dict[str, int] = {}
    for semester in semesters:
        number = semester.get("number", "?")
        ids = semester.get("course_ids", [])
        used_courses.extend(ids)
        for course_id in ids:
            semester_by_course[course_id] = number
        check_refs([{"id": f"semester {number}", "course_ids": ids}], "course_ids", course_ids, "program")
        check_refs(
            [{"id": f"semester {number}", "project_ids": [semester.get("project_id")]}],
            "project_ids",
            project_ids,
            "program",
        )
        calculated = sum(
            course.get("credits", 0) for course in courses if course.get("id") in ids
        )
        checks += 1
        if calculated != semester.get("credits"):
            errors.append(
                f"semester {number}: declared {semester.get('credits')} credits, mapped {calculated}"
            )
    if set(used_courses) != course_ids:
        errors.append(
            "program/course catalog mismatch; symmetric difference: "
            + ", ".join(sorted(set(used_courses) ^ course_ids))
        )
    duplicate_program_courses = [
        course_id for course_id, count in Counter(used_courses).items() if count > 1
    ]
    if duplicate_program_courses:
        errors.append("courses used more than once: " + ", ".join(duplicate_program_courses))
    if sum(semester.get("credits", 0) for semester in semesters) != program.get(
        "credits_total"
    ):
        errors.append("program credits_total does not equal semester sum")

    for course in courses:
        course_id = course["id"]
        semester = semester_by_course.get(course_id)
        if semester is None:
            continue
        for prerequisite in course.get("prerequisite_ids", []):
            checks += 1
            prerequisite_semester = semester_by_course.get(prerequisite)
            if prerequisite_semester is not None and prerequisite_semester >= semester:
                errors.append(
                    f"course {course_id}: prerequisite {prerequisite} is not in "
                    "an earlier semester"
                )
        for corequisite in course.get("corequisite_ids", []):
            checks += 1
            if semester_by_course.get(corequisite) != semester:
                errors.append(
                    f"course {course_id}: corequisite {corequisite} is not in "
                    "the same semester"
                )

    check_chapter_semester_coherence(chapters, course_chapter_map, semester_by_course)

    mapped_chapters = {
        chapter_id
        for chapter_id in (
            [chapter_id for ids in course_chapter_map.values() for chapter_id in ids]
            + [chapter_id for record in projects for chapter_id in record.get("chapter_ids", [])]
        )
    }
    unmapped_chapters = chapter_ids - mapped_chapters
    checks += len(chapter_ids)
    if unmapped_chapters:
        errors.append(
            "chapters unused by every course and project: "
            + ", ".join(sorted(unmapped_chapters))
        )

    circuit_data = load_toml(CURRICULUM / "circuits" / "catalog.toml")
    circuits = circuit_data.get("circuit", [])
    unique(circuits, "id", "circuits")
    check_refs(circuits, "chapter_id", chapter_ids, "circuit")
    for circuit in circuits:
        source = CURRICULUM / "circuits" / circuit.get("source", "")
        checks += 1
        if source.suffix != ".tex" or not source.is_file():
            errors.append(f"circuit {circuit.get('id')}: source must be an existing .tex file")
        for field in ("caption", "alt"):
            if not circuit.get(field):
                errors.append(f"circuit {circuit.get('id')}: missing {field}")

    svg_files = list((CURRICULUM / "circuits").rglob("*.svg"))
    checks += 1
    if svg_files:
        errors.append(
            "committed circuit SVG files are forbidden: "
            + ", ".join(str(path.relative_to(ROOT)) for path in svg_files)
        )

    check_internal_links()

    if errors:
        print(f"validation failed with {len(errors)} error(s):", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print(
        f"validation passed: {len(chapters)} chapters, {len(courses)} courses, "
        f"{len(labs)} labs, {len(projects)} projects, {checks} checks"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
