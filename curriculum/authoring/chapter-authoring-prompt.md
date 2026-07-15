# Task: author a full chapter of *Electronics: From Elements to Systems*

You are authoring one chapter of a free, practical, model-based electronics book,
taking it from outline to a complete, teachable `draft` that reads as clean lecture
material. Later chapters are more technical than the foundations — so the layout is
yours to design, but the conventions and the factual bar below are fixed.

## Chapter to write
- **Chapter ID:** `<CHAPTER_ID>`   (e.g. A01)
- **Working directory:** `/home/azinke/versioned/github/emm.edu`

## Read these first (do not skip)
1. `curriculum/book/chapters.toml` — `<CHAPTER_ID>`'s title, `part`, `file`,
   `prerequisites`. Fixed; do not rename or re-scope.
2. `curriculum/book/01-foundations/f01-safe-practice.qmd` — the reference for
   **voice, depth, and rigor** (not a layout to copy).
3. `curriculum/authoring/technical-style.md`, `.../README.md`, `.../chapter-template.qmd`.
4. The part introduction (`.../<part>/index.qmd`) — fit its arc, spines, exit
   capability, and vocabulary.
5. `curriculum/book/references.bib` — reuse existing keys; add real ones as needed.

## Invariant 1 — the book's thesis (must run through every chapter)
A circuit is **one object described in many languages** (physical, schematic,
equations, simulation, firmware, measurement, requirement, test); understanding is
their agreement, and disagreement is the useful signal. Develop important results
as **predict → build → measure → reconcile → decide**, and rest each claim on the
evidence ladder (estimate → calculation → simulation → measurement → repeated test
→ reproduction → field evidence → qualified claim), stopping at the lowest rung the
stakes allow.

## Invariant 2 — factual rigor (this is a technical text; be correct or be silent)
- Every equation is derivable and dimensionally correct; **derive from first
  principles** with assumptions and validity range stated, or cite a primary source
  — never assert from memory.
- Every quantitative claim is either **worked** (numbers you can check) or **cited**
  to a datasheet, standard, or canonical reference. Do not invent device numbers;
  use representative values and label them *typical / illustrative*, or cite a real
  part. Distinguish **exact vs. typical vs. worst-case**.
- Name the operating region and limits of every compact model (small-signal,
  ideal-diode, lumped, linear, etc.); show at least one limiting case and one
  second-order effect that breaks the first-order picture.
- If something is genuinely uncertain, contested, or approximate, say so with the
  bound — don't smooth it over.

## Invariant 3 — conventions (identical across all chapters)
- **Front matter:** `title` (registry), one-sentence `description`, `chapter-id`,
  `status: draft`. Open with a **maturity callout**, plus a **safety-boundary
  callout** wherever energy/voltage warrants it (prose authorizes nothing beyond
  the current-limited, extra-low-voltage boundary).
- **Numeric `[1]` citations** (global via `styles/numeric.csl`): cite at the point
  of use with `[@key]`, prefer primary/canonical sources, add accurate entries to
  `references.bib`, and close with a short `## References` note and a `## Connections`
  section that links prerequisites, downstream chapters, labs, projects, and
  just-in-time appendices by ID.
- **Notation:** SI throughout; reference directions before any signed result;
  distinguish equality / approximation / tolerance / bound / uncertainty; state the
  amplitude type (instantaneous, peak, pk-pk, RMS, average, phasor, spectral
  density); uncertainty is first-class.
- **Headings:** natural and chapter-specific — never the word "model" in a heading,
  never a generic template label reused book-wide.
- **Mermaid:** vertical `flowchart TB`, concise nodes, detail in caption/alt, **no
  `$…$`** — Unicode subscripts (`Rₜₕ`, `Rᵢₙ ∥ Cᵢₙ`) or plain names. Every figure has
  caption + alt text.
- **Code:** standard-library, parameterized, runnable, with an expected-output
  block; short lines that wrap in print.
- **Circuits:** CircuitikZ source in `curriculum/circuits/<id>.tex`, registered in
  `catalog.toml`, referenced as `../../../build/circuits/<id>.png`; explicit
  connection dot at every 3+ conductor junction; test-point labels off wires and
  components; regenerate with `python3 curriculum/tools/render_circuits.py --id <id>`
  and verify visually.
- **Exercises:** open with a **multiple-choice quick check** (5–6 items, options a–d,
  with an answer key), then retrieval, estimation, derivation, data interpretation,
  debugging, and open design; a few self-check answers inline; full solutions stay
  out of the public book.
- **Representations stay synchronized** (schematic ↔ equations ↔ code ↔ data ↔ test).

## Adaptable structure — design the layout the topic needs
F01's ten sections fit a bench-habits chapter. A technical chapter should be
organized around **its own logic**, not that skeleton. Keep `## Central question`
and `## Learning outcomes` as the opening (consistent book-wide) and the closing
`## Exercises`, `## Connections`, `## References`; between them, arrange whatever
serves clean teaching — for example:
- a **theory chapter** may run: phenomenon → first-principles derivation → the
  governing relations → regions of operation → worked numerical examples →
  second-order effects and limits → a design/selection procedure;
- a **device chapter** may add: physical structure and I–V behavior, a parameter
  table sourced from a real datasheet, large- vs. small-signal treatment, and a
  biasing/selection example;
- a **design/realization chapter** may run: requirement → architecture options →
  trade-off table → procedure → verification/acceptance.

Whatever the arrangement, the chapter must still **motivate with something
observable, elicit a prediction, build the theory rigorously, work concrete
numbers, reconcile with evidence, expose failure modes, and end in a bounded,
defensible decision or capability.** Those are functions to fulfill, not sections
to stamp. Use tables, derivations, procedures, and comparisons freely where they
teach better than prose.

## Workflow
1. Draft the `.qmd` at the registry `file` path; author and render any circuits.
2. `python3 curriculum/tools/validate.py` — must pass.
3. `quarto render curriculum/book/<file> --to html` — must succeed; verify no
   "model" in headings, `[1]` citations, `TB` mermaid with Unicode subscripts, the
   MCQ with a–d options, figures resolving, and equations rendering.
4. Report the layout you chose and why, any new `references.bib` keys, and the
   verification results.

## Quality bar
Correct, specific, and thorough — quality lecture material a student could learn
from and an instructor could teach from unchanged. Depth and factual precision beat
brevity; a generic or hand-wavy chapter is a failed chapter.
