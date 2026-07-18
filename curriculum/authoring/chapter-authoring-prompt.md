# Task: author a full chapter of *Electronics: From Elements to Systems*

You are authoring one chapter of a free, practical, model-based electronics book,
taking it from outline to a complete, teachable `draft` that reads as clean lecture
material. Later chapters are more technical than the foundations — so the layout is
yours to design, but the conventions and the factual bar below are fixed.

Write in the reader-facing style of *Dive Into Systems*: an expert peer builds
the idea with the student, one visible step at a time. Technical depth must make
the explanation clearer, not more distant.

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
6. The nearest completed prerequisite chapter and relevant downstream outlines —
   preserve notation, do not re-teach their scope, and hand forward exactly what
   later chapters expect.

## Invariant 0 — teach the reader in the room

- Use active voice. Name what acts: the source drives current, the transistor
  changes the load current, we choose a reference, and you compare the
  prediction with the measurement.
- Keep sentences punchy and direct. Give each sentence one main job. Split a
  sentence that tries to introduce a mechanism, qualify it, and state its
  consequence at once.
- Define each technical term in **bold** at first use in the chapter, followed
  immediately by a plain-language meaning. Add the formal definition or equation
  after the reader knows what physical idea the term names.
- Build every abstraction from something observable. Use the sequence physical
  object → terminal behavior → compact description → circuit interaction →
  system consequence → test whenever it fits the topic.
- Bridge every scale change in prose. When a diode becomes a rectifier, explain
  how its one-way terminal behavior selects parts of the input waveform. When a
  transistor becomes an amplifier, explain how bias places the device where a
  small input change can control a larger output change. Never make the schematic
  carry that conceptual jump by itself.
- Ask for a sign, direction, trend, limiting case, or order-of-magnitude
  prediction before a central calculation. Reconcile the result with that
  prediction afterward.
- Avoid localized idioms, decorative metaphors, inflated vocabulary, and
  throat-clearing. Do not write “It is important to note,” “Obviously,”
  “Simply,” or “As we all know.”
- Never use “beyond the scope” as a substitute for explanation. Give the shortest
  causal account that supports the current result. Then link to the later chapter
  and state what deeper question it answers.
- Keep paragraphs focused. Use bullets for alternatives, features, or failure
  modes. Use numbered lists only when order matters.
- Anchor topology with a circuit diagram, time behavior with a waveform, and
  operating regions or trade-offs with a graph or table. Introduce what the reader
  should inspect, then interpret what the visual shows. During drafting, leave an
  explicit `[Diagram cue: ...]`, `[Waveform cue: ...]`, or `[Graph cue: ...]`
  when an essential visual is missing; replace it before review.

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
- In every boundary balance, keep three things separate: **quantities crossing the
  chosen boundary**, **conversion or generation inside it**, and **accumulation
  inside it**. Do not count one transfer twice — for example, once as internal
  dissipation and again as heat that has not yet crossed the boundary during
  warm-up. State exactly when steady or whole-cycle averaging makes accumulation
  vanish.
- State the denominator and storage condition of every efficiency or utilization
  ratio. A port ratio can exceed one while stored energy is being released; the
  bound $0\le\eta\le1$ applies only when every energy input, including any net
  storage release relevant to the interval, is accounted for.
- Every quantitative claim is either **worked** (numbers you can check) or **cited**
  to a datasheet, standard, or canonical reference. Do not invent device numbers;
  use representative values and label them *typical / illustrative*, or cite a real
  part. Distinguish **exact vs. typical vs. worst-case**.
- Keep the provenance of a comparison visible. A chapter calculation compared
  with a datasheet limit is not wholly "documented": name which value was derived,
  which was specified by the manufacturer, and which — if any — was measured.
  Present the derivation before using its result in a rating or acceptance
  comparison.
- Treat the **test condition as part of every datasheet number**. Do not combine a
  voltage limit at one current, temperature, pulse width, or waveform with a
  current limit from another condition as though they describe one operating
  point. If the needed corner is not specified, use a justified one-sided
  monotonic bound, a source-network available-power bound, a cited curve with its
  evidence class, or mark the result as an unqualified screen. Rate every mandatory
  current-limiting, biasing, or energy-absorbing element as well as the named
  device.
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
- When stored charge or field energy contributes at a terminal, separate total
  terminal current into its conduction and charge-rate or displacement components.
  Define which terminal owns the signed charge before writing its time derivative,
  and state the condition under which one component may be neglected; do not
  silently equate total current with only the capacitive or stored-charge term.
- If something is genuinely uncertain, contested, or approximate, say so with the
  bound — don't smooth it over.
- A design that merely equals a strict limit does not pass it. Carry tolerances,
  environmental effects, parasitics, connection losses, and measurement uncertainty
  far enough to decide whether margin is real; otherwise label the result a nominal
  feasibility estimate rather than a verified design. Round a derived strict bound
  inward (conservatively), or mark the displayed value approximate and retain the
  unrounded value for the decision; never let display rounding admit a value that
  the unrounded inequality rejects.
- A protection or limiting claim includes the complete current and energy path:
  source and source impedance, limiting element, protection device, protected
  load or receiver, supply-rail source/sink behavior, return path, and relevant
  parasitics. Bound the current and power in every participating element. A clamp
  voltage alone does not establish receiver survival, rail regulation, transient
  capability, or thermal safety.

## Invariant 3 — conventions (identical across all chapters)
- **Front matter:** `title` (registry), one-sentence `description`, `chapter-id`,
  `status: draft`. Open with a **maturity callout**, plus a **safety-boundary
  callout** wherever energy/voltage warrants it (prose authorizes nothing beyond
  the current-limited, extra-low-voltage boundary).
- **Numeric `[1]` citations** (global via `styles/numeric.csl`): cite at the point
  of use with `[@key]`, prefer primary/canonical sources, add accurate entries to
  `references.bib`, and close with a short `## References` note and a `## Connections`
  section that links prerequisites, downstream chapters, labs, projects, and
  just-in-time appendices by ID. The closing note never substitutes for a citation
  at the first consequential claim. Verify every new bibliography entry against an
  official or primary source, then audit that every citation key resolves.
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
- **Residual language:** an **unallocated quantity** is what remains after only
  some paths have been inventoried; it is not yet localized to a component or
  failure. A **closure residual** compares independently obtained terms after all
  declared paths are assigned and should be consistent with zero within
  uncertainty. Never manufacture a zero residual by defining the final term as the
  remainder and then presenting the identity as evidence.
- **Acceptance decisions:** name the measurand, test points, operating and
  environmental conditions, instrument loading, accuracy/calibration inputs,
  uncertainty basis, guard band, and explicit pass/fail decision rule. A display
  inside the specification is not a pass when the guarded interval crosses a
  boundary; equality does not satisfy a strict limit. When the instrument changes
  the measurand in the favorable direction — for example, a probe that accelerates
  a capacitor discharge — correct the result or add an explicit one-sided loading
  bound to the decision rule rather than hiding the effect in generic uncertainty.
  Do not use undefined observations such as “no abnormal heating” as acceptance
  criteria: define a temperature measurand and guarded limit, or label smoke, odor,
  discoloration, and unplanned rapid temperature rise as safety stop conditions
  rather than evidence of a pass.
- **Headings:** build a textbook skeleton, not a sequence of blog headlines. Use
  compact, chapter-specific noun phrases or precise declarative claims that name
  the concept, method, operating region, or decision. A reader scanning only the
  table of contents should see the intellectual progression. Avoid promotional,
  teasing, conversational, or cute titles; never use the word "model" in a heading
  and never paste generic template labels into the middle of every chapter.
- **Static figures and asset provenance:** keep recoverable figure source inside
  the Quarto project, normally under `curriculum/book/figures/`, so HTML packaging
  does not depend on paths outside the project. Commit the editable source and,
  when the QMD references a derived raster and no pre-render generator creates it,
  commit that render-ready derivative too. Copies under `build/` are generated and
  ignored. Do not move a required chapter input into `build/` without adding and
  documenting a deterministic generation step that runs before Quarto.
- **Mermaid:** vertical `flowchart TB`, concise nodes, detail in caption/alt, **no
  `$…$`** — Unicode subscripts (`Rₜₕ`, `Rᵢₙ ∥ Cᵢₙ`) or plain names. Every figure has
  a label, caption, and alt text. In a dependency diagram, define the arrow
  semantics and match direct prerequisites to `chapters.toml`; do not mix them
  with page order, conceptual spines, or downstream handoffs. Give a wide figure
  an explicit print width and inspect both HTML and PDF. If Mermaid layout remains
  unstable, oversized, or unreadable after simplification, replace it with a
  recoverable static vector figure and a controlled render derivative rather than
  accepting renderer-dependent geometry.
- **Code:** standard-library, parameterized, runnable, with an expected-output
  block; lines short enough to survive print without awkward wrapping. Run it,
  compare actual and expected output, and keep variable names synchronized with the
  prose while avoiding symbol names that become ambiguous in code. Make every
  consequential assumption visible in the variable assignment or adjacent prose:
  do not silently rename "unallocated" power as component "loss," treat a
  hypothesis as an observation, or imply that executable arithmetic is a physical
  simulation.
- **Circuits:** CircuitikZ source in `curriculum/circuits/<id>.tex`, registered in
  `catalog.toml`, referenced as `../../../build/circuits/<id>.png`. Treat clean
  rectangular geometry as an acceptance requirement: route external conductors
  horizontally and vertically on a deliberate grid; diagonal strokes belong only
  to the standard component symbol or to a rare, explicitly meaningful geometry.
  Never use a diagonal wire merely to reach a terminal. Derive every device
  connection from its exact named anchor (`B`, `C`, `E`, `G`, `D`, `S`, and so on)
  and use orthogonal coordinate projections; do not aim a hard-coded endpoint near
  a symbol and hope it touches. Orient or mirror devices so connected terminals
  face one another, paired devices are visually symmetric, stacked devices align,
  and wires do not cross a component body or one another. For example, make
  current-mirror control terminals face inward and place a stacked output device
  directly above the lower device it serves when that removes a long return path.
  Use explicit connection dots at every 3+ conductor junction **and nowhere
  else**; ordinary two-terminal component connections and ground-symbol
  connections do not receive decorative dots. Separate functional branches and
  panels with enough white space that labels, polarity marks, current arrows, and
  test points never touch wires or symbols. Regenerate with
  `python3 curriculum/tools/render_circuits.py --id <id>` after every geometry
  change and verify the actual image visually; compilation success is not visual
  acceptance. Trace every DC, signal, post-switch, and stored-energy path on the
  rendered schematic and confirm that it contains exactly the elements in the
  governing equation. A coupling capacitor that is open at DC cannot supply a
  bias path, and a clamp drawn across $L$ is not equivalent to one drawn across
  $R_w+L$. Give portrait or unusually large figures an explicit QMD `width` and
  inspect their final HTML and full-book PDF placement, not only the standalone
  PNG. Apply the complete circuit-drawing checklist in `technical-style.md`.
- **Exercises:** open with `### Quick check` — do not put “multiple choice” in the
  heading — containing 5–6 one-best-answer items with options a–d and an answer
  key. Follow with retrieval, estimation, derivation, data interpretation,
  debugging, and open design; include a few inline self-check answers, while full
  solutions stay out of the public book.
- **Quarto cross-references at line starts:** never begin a physical line with
  `@eq-`, `@fig-`, or `@tbl-`, especially an indented ordered-list continuation.
  Pandoc can interpret that token as example-list syntax and silently replace a
  cross-reference with a bare number. Keep the reference on the preceding physical
  line or prefix the same line with ordinary prose, then inspect the rendered text.
  Inspect forward references especially: if a reference before its target renders
  as a bare number, move the target earlier or use unambiguous prose such as “the
  figure below” until the labelled figure has been introduced.
- **Quarto cross-reference wording:** `@eq-...`, `@fig-...`, and `@tbl-...`
  already render the configured prefix. Write “from @eq-name” or “as shown in
  @fig-name,” not “from equation @eq-name” or “Figure @fig-name,” which produces
  duplicated text such as “equation Equation 3.2.”
- **Representations stay synchronized** (schematic ↔ equations ↔ code ↔ data ↔ test).
  If a diagram is intentionally architectural rather than a component schematic,
  say so; use the same boundary names, test points, quantities, and assumptions in
  its caption, tables, equations, code, and acceptance procedure.

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
  biasing/selection example. It should also give a system-oriented family map
  broad enough for later design work: distinguish structure or mechanism,
  material, application role, and optimization; show where names overlap or are
  misleading; include important non-members commonly called by the family name;
  state the decisive datasheet evidence; and hand detailed specialist design to
  its owning downstream chapter;
- a **design/realization chapter** may run: requirement → architecture options →
  trade-off table → procedure → verification/acceptance.

Whatever the arrangement, the chapter must still **motivate with something
observable, elicit a prediction, build the theory rigorously, work concrete
numbers, reconcile with evidence, expose failure modes, and end in a bounded,
defensible decision or capability.** Those are functions to fulfill, not sections
to stamp. Use tables, derivations, procedures, and comparisons freely where they
teach better than prose.

## Make the table of contents teach

Design the heading hierarchy before filling it with prose. It is the chapter's
conceptual map and should remain useful after the examples are forgotten.

1. Keep the shared opening and closing headings fixed, but let the middle expose
   the topic's own logic. Each `##` should represent one durable conceptual unit;
   add a `###` only for a genuine subdivision, worked example, operating region,
   or procedure within it.
2. Prefer book-like headings such as `Terminal power and the passive sign
   convention`, `Small-signal behavior around the operating point`, or `Worked
   design: gain, loading, and margin`. Avoid titles such as `The number that
   changes everything`, `Why this part gets hot`, or `A surprising result`.
3. Keep neighboring headings parallel in scale and grammar. Do not mix a broad
   field (`Noise`) with a tiny example (`A 2.2 kΩ resistor`) at the same level.
4. Use consistent prefixes where they help navigation — for example, `Worked
   example: ...`, `Worked design: ...`, or `Acceptance test: ...` — but do not turn
   the whole book into a fixed template.
5. Read the headings alone as a student before drafting and again after review.
   They should reveal prerequisite idea → governing relations → application →
   limits → evidence → decision without sounding promotional or conversational.

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
1. Draft the heading skeleton first. Read it without body prose and verify that it
   is book-like, parallel in scale, specific to the topic, and sufficient to show
   the learning arc. Then draft the `.qmd` at the registry `file` path.
2. Build an equation inventory while drafting: for every central relation record
   its status, references, assumptions, units, demonstration, limiting case, and
   downstream use. For every balance, also record the boundary, internal
   conversions, accumulation term, and the condition under which it vanishes.
3. Audit quantitative inputs. Cite real specifications or mark values
   illustrative; include temperature, frequency, tolerance, aging, geometry,
   loading, connector/contact effects, and other operating conditions whenever they
   can change the decision. Keep each specification attached to its test current,
   pulse width, waveform, temperature, and endpoint definition. Do not combine
   limits from incompatible conditions, and screen the ratings and derating of
   every required series, bias, shunt, or energy-absorbing element. A nominal
   calculation is not a worst-case design.
4. Audit terminology and provenance. Distinguish unallocated quantities from
   independently evaluated closure residuals; chapter calculations from datasheet
   limits; typical values from guaranteed bounds; and surface observations from
   inaccessible internal quantities. Include front matter, learning outcomes,
   callouts, captions, tables, and exercises in the first-use terminology audit.
   A term introduced in a learning outcome still needs a plain-language
   definition there or must be moved to the main explanation.
5. Audit evidence. Separate prediction, synthetic teaching data, simulation,
   authentic measurement, and qualified claim. Make the prose say exactly which
   rung has actually been reached.
6. Author and render any circuits. Begin with a rectangular placement plan:
   power rail above, return rail below, signal flow left-to-right where practical,
   repeated branches aligned, and functional panels separated. Connect exact
   component anchors with horizontal and vertical segments; rotate or mirror
   devices before accepting a crossing, diagonal wire, long wraparound route, or
   compressed shape. Inspect the standalone images and their final chapter
   placement for:
   - an electrically complete DC path as well as the intended incremental,
     transient, or switched path;
   - arrow direction, voltage polarity, named nodes, and correspondence with the
     equations and test points;
   - junction dots only at genuine three-or-more-conductor nodes;
   - readable labels with no wire, symbol, arrow, or neighboring-panel collision;
   - visible leads between device bodies and junctions;
   - consistent device scale, alignment, symmetry, and spacing; and
   - no unintended wire crossings, wires through symbols, diagonal routing, or
     ambiguous near-connections.
   For every switched or clamped circuit, trace the pre-switch and post-switch
   loops and confirm each loop against the differential equation and energy
   account. For every capacitively coupled or bypassed circuit, trace DC with the
   capacitors open and the claimed AC regime with their stated impedances. Render
   again after each geometric correction. A successful CircuitikZ compile is only
   a syntax check; acceptance requires visual inspection at the QMD width in HTML
   and on the actual full-book PDF page.
7. Author static figures from recoverable source. Keep required assets inside the
   Quarto project, record how every derivative was produced, and commit a
   render-ready derivative when the QMD directly references it and no pre-render
   hook creates it. Check that the final HTML image `src` resolves to an existing
   file; a successful render does not prove that an externally referenced image
   was packaged. For the PDF, inspect the actual full-book page for clipping,
   overflow, unreadable type, and bad page breaks.
8. Run every code listing and compare it with its expected-output block. Confirm
   that code names preserve the distinctions and assumptions made in the prose.
9. Start independent review passes on the **completed draft** when review agents
   are available:
   - **technical:** recompute every central numerical result, audit signs,
     dimensions, conservation boundaries, datasheet-condition compatibility,
     limiting cases, complete current/power paths, and conclusions;
   - **pedagogical:** read as a learner and instructor, audit the heading skeleton,
     prerequisite burden, misconceptions, family/scope completeness, examples,
     exercises, and exit capability;
   - **repository/editorial:** audit front matter, links, citations, evidence
     labels, diagram rules, code/output agreement, and Connections; and
   - **rendering/accessibility:** inspect actual HTML asset resolution, alt text,
     equation and cross-reference wording, the full-book PDF pages containing wide
     figures or long tables, and any format-specific clipping or overflow.
   Apply substantiated improvements, then repeat the affected calculation or
   render checks; a review of the outline alone is not a final review.
10. Re-read the final heading list and every point-of-use citation. Verify that
   bibliography keys resolve, inspect newly rendered bibliography entries for
   broken TeX/UTF-8 escaping in names and organizations, and confirm that the final
   `## References` note is not the first citation for a consequential claim.
11. `python3 curriculum/tools/validate.py` — must pass.
12. `quarto render curriculum/book/<file> --to html` — must succeed; verify no
   "model" in headings, `[1]` citations, `TB` mermaid with Unicode subscripts, the
   MCQ with a–d options, figures resolving, equations rendering, and no missing or
   duplicate internal targets or duplicated prefixes such as “Equation Equation.”
   Inspect every chapter-local image URL and confirm its target exists. Compare
   `git status --short` before and after the render so generated `.html` or
   `site_libs/` artifacts are not left in the source tree; use the declared
   single-file command unless full-project output placement has been explicitly
   verified.
13. Render the full book to PDF when pagination, wide figures, long tables, or
   cross-chapter numbering can affect the result. Inspect the actual pages that
   contain new or changed material; a standalone image and a successful XeLaTeX
   exit do not establish that content fits the page.
14. Read the rendered chapter once as a student: can every central result be
   recomputed, can every sign be interpreted, and is it clear what is exact,
   illustrative, measured, assumed, or still unverified? Read the table of contents
   once more: does it still teach the chapter's progression? Inspect sentences
   longer than about 35 words and semicolon chains. Split them unless their
   structure genuinely helps the reader. Check that no idiom or metaphor carries
   a technical claim that should be stated literally.
15. Report the layout you chose and why, meaningful review-driven corrections, any
   new `references.bib` keys, and the verification results.

## Quality bar
Correct, specific, and thorough — quality lecture material a student could learn
from and an instructor could teach from unchanged. Depth and factual precision beat
brevity, but precision does not excuse dense or detached prose. A generic,
hand-wavy, or needlessly difficult chapter is a failed chapter. Completeness does not
mean mentioning every adjacent topic. It means that the chapter's promised exit
capability is fully supported: prerequisites are named, central quantities are
defined, equations are derived and demonstrated, evidence is honestly classified,
failure boundaries are visible, exercises cover the misconceptions, the heading
skeleton teaches the conceptual arc, citations support consequential claims at the
point of use, and the final decision is valid under stated conditions.
