# Technical style

- Define voltage polarity and current direction before applying sign
  conventions.
- Use SI units, dimensional checks, and honest significant figures.
- Distinguish equality, approximation, tolerance, bound, and uncertainty.
- State whether amplitudes are instantaneous, peak, peak-to-peak, RMS, average,
  phasor, or spectral density.
- Name the operating conditions and validity range of every compact model.
- Label axes, units, test points, bandwidth, references, and uncertainty on data
  figures.
- Prefer recoverable source and data over screenshots.
- Keep required static figure assets inside the Quarto project. Commit editable
  source and any render-ready derivative directly referenced by QMD unless a
  documented pre-render step generates it; treat copies under `build/` as
  generated output.
- Use reference designators and named signals consistently across circuit,
  equation, code, PCB, and test procedure.
- Give diagrams useful captions and alternative text. Add a prose description
  when relationships are too complex for short alt text.
- Never use color as the only carrier of state, polarity, warning, or pass/fail.

## Factual rigor

- Derive relations from first principles with assumptions and validity range
  stated, or cite a primary source; never assert a technical claim from memory.
- Identify each important relation as a definition, conservation law,
  constitutive relation, approximation, empirical fit, tolerance, bound, or
  requirement. Do not present a steady-state or small-signal special case as a
  universal law.
- In a balance around a chosen boundary, distinguish quantities crossing the
  boundary, conversion or generation inside it, and accumulation inside it. Do
  not count an internal conversion again as an outward transfer before it has
  crossed the boundary, and state the condition that makes accumulation vanish.
- State the denominator and interval of every efficiency or utilization ratio.
  Bounds such as $0\le\eta\le1$ require every input, including any relevant net
  release of stored energy, to be included.
- Make every quantitative claim either worked (numbers the reader can check) or
  cited to a datasheet, standard, or canonical reference. Do not invent device
  numbers — cite a real part, or label representative values as typical or
  illustrative — and distinguish exact, typical, and worst-case.
- Keep provenance visible when comparing values: identify which value was
  calculated in the chapter, which was specified by a manufacturer or standard,
  and which was measured. Derive a result before using it in a datasheet or
  acceptance comparison.
- A datasheet value and its test condition are one statement. Keep current,
  voltage, temperature, pulse width, waveform, load, and endpoint attached to the
  number. Do not multiply or otherwise combine limits from incompatible test
  conditions as if they bound one operating point. Where the required corner is
  absent, use a justified one-sided or source-network bound, or label the result
  as a feasibility screen.
- When charge storage or field energy contributes to terminal current, define the
  signed stored charge and separate conduction current from
  charge-rate/displacement current. State explicitly when either component is
  negligible.
- Show at least one limiting case and one second-order effect that breaks each
  first-order model. Where something is genuinely approximate or contested, say so
  with the bound rather than smoothing it over.

## Headings and structure

- Build a textbook skeleton, not a sequence of blog headlines. Prefer compact,
  chapter-specific noun phrases or precise declarative claims that name the
  concept, method, operating region, or decision. Avoid promotional, teasing,
  conversational, or cute titles. Do not use the literal word "model" as a
  heading; name the actual idea instead.
- Read the heading hierarchy by itself. It should reveal the conceptual
  progression, and neighboring headings should be parallel in scale and grammar.
  Use `###` only for a genuine subdivision, worked example, operating region, or
  procedure within its parent `##` section.
- Structure follows the topic, not a fixed skeleton. Keep the shared opening
  (`Central question`, `Learning outcomes`) and close (`Exercises`, `Connections`,
  `References`); arrange the middle — derivation, regions of operation, parameter
  tables, worked examples, design procedures, trade-off tables — however teaches
  the material best.
- Whatever the arrangement, still fulfil the editorial functions in
  [`chapter-template.qmd`](chapter-template.qmd): motivate from something
  observable, elicit a prediction, build the theory, work concrete numbers,
  reconcile with evidence, expose failure modes, and end in a bounded decision.
  These are functions to fulfil, not sections to stamp.

## Device-family scope

- When introducing a device class, provide a system-oriented selection map, not
  merely the historically central device. Classify names by structure or
  mechanism, material, application role, and optimization; these axes overlap.
- Include the families a designer is likely to encounter, their distinctive
  terminal behavior, decisive datasheet evidence, important naming traps, and
  commonly named exceptions that do not share the assumed structure.
- Keep the overview broad enough to support selection, then link specialist
  analysis and circuit design to the downstream chapter that owns it. An
  exhaustive recognition map does not require duplicating every later design
  treatment.

## Evidence and decisions

- Label invented or generated values **illustrative** or **synthetic** beside the
  table, figure, or scenario. State what they can teach and that they do not
  qualify a physical claim.
- An **unallocated quantity** remains after only some paths have been inventoried;
  it is not yet a component loss or fault. A **closure residual** compares
  independently obtained terms after all declared paths are assigned. Do not
  manufacture a zero residual by defining the final term as the remainder.
- Authentic measurements identify configuration, test points, instrument and
  range, loading, calibration state, raw observations, operating conditions, and
  uncertainty basis. Keep surface observations distinct from inaccessible
  internal quantities unless a validated correlation is provided.
- A bounded decision names the measurand, conditions, uncertainty, guard band,
  and explicit decision rule. Equality does not satisfy a strict limit, and a
  typical specification does not become a worst-case guarantee through
  calculation.
- Do not use “no abnormal heating” or a similar undefined observation as a pass
  criterion. Define a temperature measurand and guarded limit, or identify smoke,
  odor, discoloration, and unplanned rapid temperature rise as safety stop
  conditions rather than acceptance evidence.
- A protection decision covers the entire current and energy path: source and
  impedance, limiting element, protection device, protected receiver or load,
  rail source/sink behavior, return path, and relevant parasitics. Bound current
  and power in every participating element; a clamp voltage alone is not a
  complete protection claim.

## Diagrams and code that survive print

- Draw Mermaid flowcharts vertically (`flowchart TB`) with concise node text so
  they do not scale off the PDF page; carry longer descriptions in the caption
  and alt text rather than in wide nodes.
- Use a dependency diagram when branching or merging is materially clearer than
  a short list. Give every arrow one declared meaning and make direct
  prerequisite edges match `book/chapters.toml` exactly. Keep canonical page
  order, conceptual spines, and downstream handoffs out of that graph unless
  they are visually and semantically distinguished; prose is usually clearer
  for those routes.
- Give every Mermaid figure a label, caption, and alt text. If its natural width
  exceeds the PDF text block, set an explicit `fig-width`, then inspect both the
  HTML and PDF render for clipping, crossed labels, unreadable type, and
  ambiguous edges.
- If a diagram remains unstable, oversized, or unreadable under Mermaid layout,
  replace it with recoverable static vector source and a controlled render
  derivative. Keep the asset within `curriculum/book/figures/`; a path outside
  the Quarto project may render in one format yet fail to be packaged for HTML.
- Treat HTML and PDF as separate acceptance targets. Confirm that every rendered
  HTML image `src` exists and loads; for PDF, inspect the actual full-book page,
  not only the standalone image or the renderer's exit status. Check wide
  figures, long tables, captions, and page breaks visually.
- Mermaid renders no math: write symbols in node text as Unicode subscripts
  (`Rₜₕ`, `Rᵢₙ ∥ Cᵢₙ`) or plain names, never `$…$`. Put any real math in the
  caption or alt text, where LaTeX/MathML does render.
- Keep code and verbatim listings short-lined; the PDF build wraps long lines,
  but a line that must wrap is usually a line that should be split.
- Keep names and assumptions synchronized across diagram, prose, equations, code,
  data, and test. If a diagram is architectural rather than a component
  schematic, say so. If code turns an unallocated quantity into an assumed
  component loss, make that hypothesis explicit rather than hiding it in a
  variable name.
- Executable arithmetic is not automatically a simulation, and generated output
  is not a measurement. State the evidence status of every executable result.
- Quarto cross-references already supply their configured prefix. Write “from
  `@eq-name`” and “as shown in `@fig-name`,” not “from equation `@eq-name`” or
  “Figure `@fig-name`,” which render duplicated prefixes. Do not begin a physical
  source line with a cross-reference token; Pandoc can misread it as example-list
  syntax and emit a bare number. Inspect forward references; if one renders as a
  bare number, introduce the labelled target first or use “the figure below.”

## Circuits

- Place an explicit connection dot at every junction where three or more
  conductors meet (`node[circ]` / the `*` node in CircuitikZ), so a genuine node
  is never ambiguous with a crossing. Do not place decorative dots at ordinary
  two-terminal component joins or ground-symbol connections.
- Bring test points out to clear space and place their labels off the wires and
  components — never draw a label over a conductor or symbol.
- In limiting, bias, clamp, and protection circuits, rate the mandatory resistor,
  fuse, bias network, rail sink, or other supporting element as well as the named
  device. Trace the complete current path and confirm that the schematic,
  equations, and acceptance boundary contain the same elements.

## Citation

- Citations render as bracketed numbers (`[1]`) via `book/styles/numeric.csl`;
  cite at the point of use and let the number, not an author–year block,
  interrupt the prose.
- Cite the first consequential claim; a closing References note is a guide, not a
  substitute for point-of-use support. Prefer primary standards, manufacturer
  documents, and canonical technical sources.
- Verify new bibliography metadata against an official or primary source and
  audit that every citation key resolves before rendering the final draft.
