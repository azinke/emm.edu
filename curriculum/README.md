# Curriculum source

The curriculum is organized around one canonical textbook.

```text
curriculum/
├── book/          textbook source, reading roadmap, part openers, and chapter registry
├── circuits/      CircuitikZ source; no committed circuit SVG
├── courses/       course and semester routes through chapter IDs
├── labs/          practical experiences mapped to chapters
├── projects/      system-integration spine
├── instructor/    lecture templates and derived teaching guidance
├── authoring/     compact editorial and technical conventions
└── tools/         structural validation and build helpers
```

## Where work belongs

Add an explanation, derivation, worked example, or general exercise to
`book/`. Add a physical investigation to `labs/`. Add multi-domain integration
to `projects/`. Add only delivery-specific timing and teaching cues to
`instructor/`.

Courses contain mappings, not course manuscripts. A concept used by three
courses is still authored once.

## Current maturity

The architecture and complete topic registry are in place. Chapter files are
deliberately marked `outline` until their technical content, exercises, and
physical evidence have been authored and reviewed. Status must describe reality.

## Checks

```sh
python3 curriculum/tools/validate.py
quarto render curriculum/book --to html   # when Quarto is installed
```

The validator checks unique IDs, registry paths, course/lab/project references,
Quarto coverage, internal links, forbidden committed circuit SVG files, and
basic chapter front matter.
