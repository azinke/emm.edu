# Electronics from Elements to Systems

This repository is building a free, book-first guide to electronics: electrical
quantities and components first, complete embedded and electronic systems last.
It is intended to work both as an independent textbook and as the common content
base for a four-year curriculum.

The previous course-first scaffold has been replaced. Theory now lives once in
the book; courses, laboratories, projects, and future lectures reference stable
chapter IDs.

## Start here

- [Curriculum architecture](blueprint/COURSE_MASTER_DOCUMENT.md)
- [Book and directory guide](curriculum/README.md)
- [Book contents](curriculum/book/index.qmd)
- [Course catalog](curriculum/courses/README.md)
- [Circuit-as-code conventions](curriculum/circuits/README.md)
- [Authoring guide](curriculum/authoring/README.md)

## Validate

```sh
python3 curriculum/tools/validate.py
```

Generate the maturity dashboard, program-outcome assurance matrix, and
prerequisite dependency graph (written under `build/reports/`):

```sh
python3 curriculum/tools/report.py
```

When Quarto is installed:

```sh
quarto render curriculum/book --to html
```

Generated publications and rendered circuit derivatives belong under `build/`
and are not source.
