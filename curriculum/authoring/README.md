# Authoring guide

## Start with the dependency boundary

Before drafting, add or update the entry in
[`book/chapters.toml`](../book/chapters.toml). State the chapter's central
question, prerequisites, conceptual endpoint, and downstream use. If that
boundary cannot be stated cleanly, the topic may belong inside an existing
chapter.

Use [`chapter-template.qmd`](chapter-template.qmd) for new chapters.

`chapters.toml` is also the canonical reading order. Keep `_quarto.yml` in the
same order; validation rejects drift between the registry and rendered book.

## Maintain the reader's map

Each top-level part has an `index.qmd` with `page-role: part` and a `part-id`
matching the registry. A part introduction should explain its question, entry
knowledge, learning arc, exit capability, and practical evidence. It synthesizes
the chapters; it does not duplicate their exposition.

Other rendered pages declare `page-role: frontmatter` or
`page-role: backmatter`. Every `.qmd` below `book/` must appear in
`book/_quarto.yml`, so an orphan page cannot silently disappear from the book.
Update the [reading roadmap](../book/roadmap.qmd) only when a route or maturity
definition changes, not whenever a chapter gains a section.

## Build the explanation around evidence

Use this sequence where it fits the idea:

1. show a device, waveform, failure, or need;
2. ask for a directional and approximate prediction;
3. introduce the simplest useful model and its limits;
4. derive the relation with units and reference directions;
5. work estimate → calculate → sanity-check → interpret;
6. compare the model with simulation and physical or authentic data;
7. diagnose a mismatch;
8. make a design choice and define an acceptance test.

These are editorial functions, not visible section names. Title each section
naturally for its own chapter — a specific claim about the system at hand, not a
generic phrase repeated book-wide, and never the bare word "model" as a heading.
See [`technical-style.md`](technical-style.md) for headings, diagrams, code, and
citation conventions.

## Keep representations synchronized

A circuit example should connect schematic, quantities, equations, conditions,
and measured test points. Code and simulation must expose parameters rather than
hide them in a screenshot. Raw data remains available beside analysis code.
Manufacturing examples use native KiCad source.

## Scope each layer correctly

- Book: durable concepts, derivations, examples, general exercises.
- Lab: apparatus, procedure, hazards, measurements, and evidence.
- Project: requirements, integration, reviews, and acceptance.
- Instructor: timing, prompts, demonstrations, teaching choices.
- Course: ordering and assessment mapping only.

## Review

A reviewer should be able to recompute the central result, reproduce executable
artifacts, trace claims to sources, inspect circuit code, identify the safety
boundary, and explain what evidence would falsify the main conclusion.

Run `python3 curriculum/tools/validate.py` before rendering or review.
