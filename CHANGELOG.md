# Changelog

## [Unreleased]

### Added

- New chapters: A08 (optoelectronics, displays, and HMI), S08 (machine learning
  at the edge), S09 (off-grid power, solar, and energy harvesting), and S10
  (low-power wide-area networks and IoT connectivity), wired into the registry,
  courses, projects, and part openers.
- Coverage levels (`introduce`, `reinforce`, `master`) on every course chapter
  mapping, derived from the semester in which each course teaches the chapter.
- `outcomes.toml`: the 14 program outcomes encoded as data mapped to chapters.
- `tools/report.py`: maturity dashboard, program-outcome assurance matrix, and
  prerequisite dependency graph generated from the canonical registry.

### Changed

- `tools/validate.py` now checks course chapter coverage levels, chapter
  prerequisite scheduling across semesters, and that every program outcome is
  both introduced and mastered.
- Resolved three chapter prerequisite scheduling gaps: R06 (dropped from the
  semester-2 sustainable-design course), R05 (dropped from the semester-3
  metrology course), and the X01 precision-instrument study (moved to the
  semester-5 mixed-signal course, after data conversion is taught).
- Replaced the generated, course-first content scaffold with one canonical
  textbook and lightweight course, lab, project, and instructor mappings.
- Reorganized the subject from electrical foundations through complete systems.
- Replaced the committed circuit SVG convention with CircuitikZ source and
  build-only PDF/PNG derivatives.

## [0.2.0] - 2026-07-13

- Established the initial curriculum blueprint and production scaffold.
