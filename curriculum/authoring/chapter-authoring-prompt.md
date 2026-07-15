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
- Before writing a signed equation, declare its reference direction, polarity,
  coordinate axis, integration path, or positive surface normal as applicable. A
  symbol such as $V_{AB}$, $I$, work, gain, or phase is incomplete until its
  reference is unambiguous.
- Distinguish the status of every important relation: **definition**, exact
  conservation law, constitutive relation, approximation, empirical fit,
  rule-of-thumb screen, tolerance, or requirement. Derive the general conservation
  statement before its steady-state or lumped special case; do not turn "negligible
  accumulation" into "accumulation is impossible."
- Every quantitative claim is either **worked** (numbers you can check) or **cited**
  to a datasheet, standard, or canonical reference. Do not invent device numbers;
  use representative values and label them *typical / illustrative*, or cite a real
  part. Distinguish **exact vs. typical vs. worst-case**.
- Demonstrate governing equations when doing so helps the reader form the concept.
  A useful demonstration normally includes: declared references; numerical
  substitution; units; an honest number of significant figures; interpretation in
  words; and one revealing variation such as reversing the reference, doubling an
  input, taking a limiting case, or changing an operating condition. Do not leave a
  central equation as a formula to memorize, but do not manufacture arithmetic for
  a relation whose meaning is already transparent.
- Name the operating region and limits of every compact model (small-signal,
  ideal-diode, lumped, linear, etc.); show at least one limiting case and one
  second-order effect that breaks the first-order picture.
- Keep distinct phenomena distinct even when casual language merges them: carrier
  motion versus electromagnetic propagation, source response versus load response,
  stored quantity versus flow rate, potential versus potential difference, and
  physical behavior versus instrument indication. State whether a claim concerns
  steady state, a switching transient, sinusoidal steady state, or a bounded time
  interval.
- If something is genuinely uncertain, contested, or approximate, say so with the
  bound — don't smooth it over.
- A design that merely equals a strict limit does not pass it. Carry tolerances,
  environmental effects, parasitics, connection losses, and measurement uncertainty
  far enough to decide whether margin is real; otherwise label the result a nominal
  feasibility estimate rather than a verified design.

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
- **Evidence integrity:** never present invented or internally generated values as
  measured data. Label them **synthetic / illustrative** beside the table or figure,
  explain what they can teach, and state that they do not qualify the physical
  claim. Authentic measurements identify configuration, instrument, range,
  calibration state, raw observations, and uncertainty basis. A datasheet accuracy
  limit is not automatically a $k=2$ expanded uncertainty.
- **Acceptance decisions:** name the measurand, test points, operating and
  environmental conditions, instrument loading, accuracy/calibration inputs,
  uncertainty basis, guard band, and explicit pass/fail decision rule. A display
  inside the specification is not a pass when the guarded interval crosses a
  boundary; equality does not satisfy a strict limit.
- **Headings:** natural and chapter-specific — never the word "model" in a heading,
  never a generic template label reused book-wide.
- **Mermaid:** vertical `flowchart TB`, concise nodes, detail in caption/alt, **no
  `$…$`** — Unicode subscripts (`Rₜₕ`, `Rᵢₙ ∥ Cᵢₙ`) or plain names. Every figure has
  caption + alt text.
- **Code:** standard-library, parameterized, runnable, with an expected-output
  block; lines short enough to survive print without awkward wrapping. Run it,
  compare actual and expected output, and keep variable names synchronized with the
  prose while avoiding symbol names that become ambiguous in code.
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

## Make equations teach

For each equation central to the chapter, build a short explanatory chain. Scale
the chain to the equation's importance; a defining relation may need only a
paragraph, while the governing design equation may need a full worked example.

1. **Name the physical question.** Say what the relation lets the reader predict or
   decide before displaying symbols.
2. **Declare references and quantities.** Define every symbol, sign, amplitude type,
   and SI unit. For vector or field relations, declare axes, path, surface, or
   geometry before reducing them to scalars.
3. **Derive or source it.** Show the shortest first-principles path that preserves
   understanding. Identify each approximation at the line where it enters.
4. **Check dimensions.** Do this explicitly for the central relation and whenever a
   unit conversion or derived unit is instructional.
5. **Demonstrate it.** Estimate first, substitute checkable values, report sensible
   precision, and interpret the sign and magnitude in the physical system.
6. **Interrogate it.** Reverse a reference, vary one parameter, examine zero and
   large-value limits, or add the leading non-ideal effect. Tell the reader what
   observation would reveal that the relation is being used outside its range.
7. **Hand it to practice.** Connect the result to the schematic, code, data, test
   point, component selection, or acceptance criterion that consumes it.

Avoid two common failures: a wall of algebra with no physical reading, and friendly
prose that never gives the reader enough mathematics to reproduce the result.

## Workflow
1. Draft the `.qmd` at the registry `file` path. Build an equation inventory while
   drafting: for every central relation record its status, references, assumptions,
   units, demonstration, limiting case, and downstream use.
2. Audit quantitative inputs. Cite real specifications or mark values
   illustrative; include temperature, frequency, tolerance, aging, geometry,
   loading, connector/contact effects, and other operating conditions whenever they
   can change the decision. A nominal calculation is not a worst-case design.
3. Audit evidence. Separate prediction, synthetic teaching data, simulation,
   authentic measurement, and qualified claim. Make the prose say exactly which
   rung has actually been reached.
4. Author and render any circuits. Inspect the rendered images, not just the source,
   for arrow direction, polarity, junction dots, legible labels, and correspondence
   with the equations and test points.
5. Run every code listing and compare it with its expected-output block.
6. `python3 curriculum/tools/validate.py` — must pass.
7. `quarto render curriculum/book/<file> --to html` — must succeed; verify no
   "model" in headings, `[1]` citations, `TB` mermaid with Unicode subscripts, the
   MCQ with a–d options, figures resolving, and equations rendering.
8. Read the rendered chapter once as a student: can every central result be
   recomputed, can every sign be interpreted, and is it clear what is exact,
   illustrative, measured, assumed, or still unverified?
9. Report the layout you chose and why, any new `references.bib` keys, and the
   verification results.

## Quality bar
Correct, specific, and thorough — quality lecture material a student could learn
from and an instructor could teach from unchanged. Depth and factual precision beat
brevity; a generic or hand-wavy chapter is a failed chapter. Completeness does not
mean mentioning every adjacent topic. It means that the chapter's promised exit
capability is fully supported: prerequisites are named, central quantities are
defined, equations are derived and demonstrated, evidence is honestly classified,
failure boundaries are visible, exercises cover the misconceptions, and the final
decision is valid under stated conditions.
