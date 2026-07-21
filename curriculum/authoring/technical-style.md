# Technical style

## Reader-facing voice

- Aim for the practical, reader-facing directness associated with strong No
  Starch Press engineering books. Write as an experienced peer who respects an
  ambitious reader enough to show the exact mechanics. This tone does not relax
  the factual bar: preserve mathematical derivations, exact definitions,
  low-level behavior, edge cases, citations, and evidence boundaries.
- Treat grammatical person, active or passive voice, and sentence mood as
  separate choices. Declarative sentences are the default for exposition,
  definitions, transitions, mechanisms, and conclusions. Use **you** when the
  reader genuinely predicts, reasons, calculates, compares, or decides. Reserve
  imperative sentences for actual instructions: a procedure step, exercise,
  prediction prompt, safety action, or explicit inspection task.
- Judge imperative mood across the passage, not sentence by sentence. Repeatedly
  opening paragraphs with “Consider,” “Predict,” “Inspect,” “Trace,” “Use,”
  “Define,” or “Let” produces a worksheet cadence even when each command is
  individually defensible. Exposition should normally connect the setup,
  mechanism, result, and consequence in declarative prose. A central calculation
  may still use one deliberate prediction prompt, and a complex visual may still
  use one focused inspection task.
- Scenario setup and symbol introduction are usually statements, not reader
  actions: “The worked interface uses an SN74HC04” is more fluid than “Use an
  SN74HC04,” and “$I_L$ denotes the load current” is more natural than “Let $I_L$
  be the load current.” Conventional mathematical “let” is acceptable when it
  makes a formal derivation clearer; avoid a succession of such commands in
  ordinary teaching prose.
- Active voice does not require imperative mood. Do not mechanically turn
  “Equation 3 gives the current” into “Use Equation 3 to calculate the current,”
  or “The output resistance limits the gain” into “Notice that the output
  resistance limits the gain.” The declarative versions state the technical
  relationship more naturally unless the reader must perform the named action.
- Use a concrete technical subject for factual claims: the source drives current,
  the cache controller invalidates a line, the transistor changes load current,
  and the extractor computes parasitics. Do not default to **we**, “the reader,”
  “one,” or an abstract passive construction.
- Prefer active voice and name the actor: “you measure TP1 relative to TP0,”
  “the source drives current,” and “the probe adds capacitance.” Use passive
  voice only when the actor is unknown or genuinely irrelevant.
- Apply the person, voice, and mood rules to maturity and safety callouts,
  learning outcomes, captions, alt text, table notes, requirements, procedures,
  exercises, and answer choices. A chapter whose body prose is direct but whose
  surrounding material remains awkward or inconsistent has not passed the
  editorial review. Parallel commands suit operational requirements and
  procedures; they usually do not suit explanatory paragraphs.
- Keep sentences direct. Put one main claim in each sentence. Split a sentence
  when it carries a mechanism, a qualification, and a consequence at once.
  Short sentences should still show the logical link: *because*, *therefore*,
  *but*, and *so* are useful engineering words.
- Open with the physical situation or question. Then give the term, mechanism,
  or equation that explains it. Avoid throat-clearing such as “It is important
  to note,” “Clearly,” “Obviously,” or “As everyone knows.”
- Avoid localized idioms, cute metaphors, and inflated vocabulary. A short
  physical analogy can help, but state where it stops matching the circuit.
- Create warmth through relevant guidance. Direct the reader to inspect,
  calculate, compare, or decide when that action advances the lesson; otherwise
  state the relationship or conclusion directly. Do not manufacture friendliness
  with jokes, filler, rhetorical hype, or the removal of difficult technical
  material.
- Define a technical term at first use in the chapter. Bold the term and give a
  compact plain-language meaning in the same sentence: “**Impedance** is the
  total opposition a circuit presents to sinusoidal current.” Follow with the
  precise mathematical definition when the chapter needs it.
- Do not use “just,” “simply,” “trivial,” or “obvious” to hide a reasoning step.
  If the step is short, show it. If it depends on earlier material, name the
  exact result and link to it.
- Remove author-centered narration such as “this is worth noting,” “the
  trade-off is now visible,” “the important bridge is,” “the result is
  counterintuitive,” or “the program is an oracle.” Replace it with the
  technical content: name the trade-off, show why the result differs from the
  prediction, or state what evidence the program provides.
- Do not dismiss a mechanism with “beyond the scope” or a similar placeholder.
  Explain the minimum causal chain needed for the present result. Then name the
  later chapter that develops the topic and state what that later treatment
  adds.

## Conceptual pacing

- Make the reading path linear. A section normally moves from observation or
  question to explanation or derivation, then to consequence, application, or
  decision. Begin each paragraph from the current question or a result already
  established. When the scale, case, representation, or task changes, state the
  reason for the change and the connection to what came before. A heading does
  not substitute for that transition.
- Make each handoff point in both directions. Its opening words should identify
  the result, limitation, or question carried from the preceding passage, and
  the rest should show why the next concept is needed. Empty sequencing such as
  “Next, consider...” and a bare demonstrative such as “This matters” do not
  supply either connection unless the referent and consequence are explicit.
- Move in visible steps: physical object → terminal behavior → compact
  description → circuit interaction → system consequence → test. When a chapter
  moves from a component to a circuit or from a circuit to a system, add the
  bridge in prose. Never rely on the schematic alone to make that connection.
- Introduce one new abstraction at a time. Tie it to a quantity the reader can
  point to on a schematic, waveform, table, or physical assembly before using it
  in a longer derivation.
- Before a central calculation, ask for a sign, trend, limiting case, or order of
  magnitude. After the calculation, compare the result with that prediction and
  explain what the number means in the circuit.
- State why each non-ideal effect enters. For example, do not only add an output
  resistance to an amplifier equivalent; explain which internal or terminal
  behavior makes the ideal zero-resistance assumption fail.
- When causality matters, trace an event chain instead of naming an effect. Use
  the pattern **change → local physical or logical response → changed quantity
  → terminal or system consequence**. For Miller compensation, for example,
  follow both capacitor terminals as the inverting stage moves them in opposite
  directions before introducing the multiplied input capacitance. Apply the
  same discipline to body effect, charge injection, supply bounce, aliasing,
  cache coherence, and software-visible hardware state.
- After every equation that drives a design choice, explain what each variable
  represents in the real circuit or system and how changing it propagates to the
  measured result. Do not let a symbol remain only an algebraic placeholder.
- When an explanation branches into several cases, use bullets for alternatives
  and numbered steps for a sequence. Keep paragraphs focused enough that a
  self-studying reader can stop and check one claim at a time.

## Visual anchors

- Place a schematic beside the first explanation that depends on topology. Place
  a waveform beside the first explanation that depends on time, phase, clipping,
  or switching order. Place a graph or table beside the first comparison that
  depends on a trend or operating region.
- Lead into every visual with a question or observation that tells the reader
  what to inspect. Follow it with the conclusion the visual supports. A figure
  must participate in the explanation; it is not decoration.
- A functional block diagram specifies an interface; an implementation
  schematic explains a mechanism. Use both when the chapter teaches both claims.
  Label vector widths, bit order, mode and opcode inputs, enables, active-low
  polarity, status outputs, and signal direction as applicable. For a repeated
  structure, expose one stage, show how the stage boundary repeats, and highlight
  the relevant candidate or critical path under the stated delay model.
- During drafting, use an explicit bracketed cue such as
  `[Diagram cue: show the source, return path, and declared current direction.]`
  when the required visual does not yet exist. Replace the cue with a sourced,
  accessible figure before the chapter reaches review status.
- Use a small ASCII schematic only when it remains unambiguous in plain text and
  print. Use CircuitikZ for component-level circuits and a recoverable vector
  figure for waveforms or diagrams whose geometry carries meaning.
- When the taught reasoning is graphical, exercise it graphically. Include at
  least one supplied visual to trace, analyze, or debug and one task to draw,
  complete, group, or repair a visual. The prompt must declare enough labels,
  conventions, polarities, and conditions for a determinate answer. Captions and
  alt text describe the given diagram without disclosing the solution.

## Readability pass

- Read each paragraph as a self-study unit. Its first sentence should establish
  the point, its middle should explain or demonstrate it, and its last sentence
  should interpret the result or hand the reader to the next step.
- Read the prose once without relying on headings. Look for a derivation followed
  abruptly by evidence, a component followed by a system claim, or an
  explanation followed by a procedure without a sentence that motivates the
  change. Add the conceptual handoff or reorder the material.
- Audit orphan sentences: a sentence is orphaned when neither its subject nor a
  clear connective ties it to the current paragraph question. Move it beside the
  claim it qualifies, supply the missing causal or contrast relationship, or
  remove it only when it duplicates an established point. Perform the same test
  on the first sentence after every heading.
- Audit sentence mood as well as sentence length. If a normal factual statement
  has become “Use,” “Apply,” “Define,” “Consider,” “Observe,” or “Notice,” ask
  whether the reader must actually do something. Restore declarative exposition
  when no action is required.
- Audit local command density. Search paragraph openings and adjacent sentences
  for “Consider,” “Predict,” “Inspect,” “Trace,” “Use,” “Define,” and “Let,” then
  read each match in context. Recast clusters as a continuous explanation; retain
  direct commands for safety, ordered procedures, exercises, and the few
  prediction or inspection pauses that materially improve learning.
- Include front matter, learning outcomes, callouts, captions, tables, and
  exercises in the readability pass. These locations often introduce a term
  before the main explanation does.
- Break dense blocks before the reader must track more than one equation,
  operating condition, or causal branch at once.
- Inspect every sentence longer than about 35 words. Length alone is not an
  error, but a long sentence often contains several claims that should become
  separate sentences or a list.
- Treat semicolons as a warning during revision. Keep one when it makes a
  two-part comparison clearer. Replace a chain of semicolons with bullets or
  shorter sentences.
- Make requirement lists grammatically parallel and operational. Prefer commands
  such as “drive,” “measure,” “report,” “require,” and “reject,” each with a
  stated condition and endpoint. Do not mix noun fragments, passive test
  descriptions, and decision rules in one list.
- Make captions active and electrically informative. State what the circuit ties,
  drives, senses, omits, or idealizes. Do not hide body connections, bias
  networks, return paths, or omitted loads behind “is tied” or “not shown” when
  the circuit or drawing can be named as the actor.
- Use bold text for a term when it is first defined, not as general emphasis.
  Use italics sparingly for a contrast or a named assumption.
- Keep notation precise, but prefer words when a symbol would appear only once.
  Never make the reader decode notation that does no later work.
- Write for readers who may be learning electronics and technical English at the
  same time. Prefer literal descriptions over idioms such as “the reading is
  fiction,” “the design has no legs,” or “this buys headroom.”
- Keep the correct technical term when it matters. Define it in plain language
  rather than replacing it with a vague everyday word.
- A readability edit may split, reorder, or clarify a derivation. It may not
  delete the assumptions, sign convention, domain, non-ideal terms, limiting
  case, citation, or evidence qualification that makes the derivation correct.
  Direct prose and deep rigor reinforce each other.

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
- Before deriving a signed mismatch, offset, error, residual, or difference,
  define the ordering of its indices or endpoints. Recompute the sign after you
  fix that ordering. A magnitude-only check cannot validate a signed equation.
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
- Keep conventional current, signed terminal charge, and carrier motion
  separate. If you use $i\,dt=dQ$, name the terminal that owns $Q$ and the
  positive current direction. Electrons generally move opposite positive
  conventional current; do not use the two descriptions interchangeably.
- Show at least one limiting case and one second-order effect that breaks each
  first-order model. Where something is genuinely approximate or contested, say so
  with the bound rather than smoothing it over.
- Audit the full domain of every central formula. State waveform shape,
  operating region, initial condition, loading, monotonicity, and parameter
  inequalities that affect its coefficient or form. If the raw algebra becomes
  nonphysical outside the domain, write a piecewise relation or an explicit
  clamp such as $[x]_+=\max(x,0)$.
- Before claiming independence from a design parameter, substitute all
  intermediate definitions and state what remains fixed. For example, a gain
  that appears independent of bias current after one cancellation may still
  depend on that current through overdrive. Distinguish “fixed geometry” from
  “scaled geometry at fixed current density.”
- Attach operating conditions directly to stored-charge and switching
  approximations. A uniform-channel charge expression may require quasi-static
  strong inversion and $|V_{DS}|\ll V_{OV}$; an edge-loss coefficient may
  require linear full-rail ramps. A later generic caveat does not repair an
  equation whose local validity conditions are missing.

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
- Do not add a generic `Summary` merely because other chapters have one. Use a
  topic-specific synthesis when it completes the chapter's reasoning, or omit it
  when it would only repeat the preceding conclusion.
- Give each document level a distinct job. The landing page invites the reader
  and shows the route through the book. The Preface owns shared notation,
  evidence, safety, and reading conventions. A part introduction explains that
  part's question and progression. A chapter introduction begins from its
  chapter-specific phenomenon or decision. Do not restate the complete book
  thesis, curriculum map, or shared conventions at every level.
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

- The Preface owns the book-wide evidence progression and its complete
  terminology. Chapters should enact it through topic-specific predictions,
  calculations, simulations, measurements, and decisions, and state the local
  evidence status where it affects a claim. Do not reproduce the full ladder,
  book thesis, or workflow in every chapter introduction, synthesis, or callout;
  link to the Preface sparingly when the complete framework matters.
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
- A statistical result names the distribution, parameter support, correlations,
  seed, sample count, PVT conditions, metric extraction, and failure rule.
  Prevent or reject nonphysical samples such as negative current factors. State
  when independent teaching draws omit process correlations. Zero observed
  failures requires a finite-sample confidence bound; it does not prove zero
  failure probability, yield, or coverage of missing physics.
- A PDK-backed evidence chain records the PDK, simulator, extractor, device
  cells, include files, commands, deterministic PVT matrix, statistical
  descriptions, DRC/LVS status, extraction settings, and pre/post-layout metric
  changes. Rerun the full required PVT matrix after extraction. If a requirement
  reaches an external pin, include pad, ESD, bond/bump, and package descriptions
  and distinguish die-pad from external-pin metrics. Never rename a synthetic
  capacitance proxy or hand-chosen parameter perturbation as PEX, a foundry
  corner, or yield evidence.
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
- Verify a figure's position in the reading sequence, not only its existence and
  numbering. It should follow the sentence that introduces it and precede prose
  that interprets details the reader has not yet seen. A PDF float may violate
  that order even when the build succeeds. Use controlled placement such as
  `fig-pos="H"` only when immediate adjacency is necessary, then inspect the
  resulting page breaks; do not pin every figure by default.
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

- For binary logic schematics, use the distinctive-shape gate family introduced
  in D02 and documented in IEEE/ANSI 91/91a-1991. The book's informal house label for this
  family is Anglo-Saxon convention; American and Anglo-American are alternative
  informal teaching aliases, not standards titles.
  Do not imply that IEEE and IEC are mutually
  exclusive names for two symbol shapes. Preserve IEC rectangular forms when
  reproducing or comparing an IEC source, but do not mix symbol families inside
  one ordinary schematic.
- Draw multiplexers and demultiplexers as labeled tapered functional blocks,
  with the multiple-port side wider than the single-port side. Show select
  inputs, port numbers, select-bit significance, enable and inversion marks, and
  signal direction. A tapered MUX/DEMUX is a hierarchical function symbol, not
  an elementary gate. Other architectural blocks may use labeled rectangles
  when they describe hierarchy rather than individual Boolean gates.
- Use labeled functional blocks for comparators, adders/subtractors, ALUs,
  encoders, decoders, and similar hierarchy. A block outline does not replace
  interface detail: show operand and result widths, bit order, mode or opcode
  inputs, carry/borrow/cascade ports, and defined flags as applicable. Follow the
  interface view with a gate, stage, or data-path view when the prose derives
  internal operation.
- Draw AND, OR, XOR, buffers, and inversions with formal gate symbols. Use an
  output bubble for logical inversion, so NAND, NOR, and XNOR remain visually
  related to their uncomplemented gates. Keep input/output polarity, active-low
  names, junction dots, and non-connecting crossings explicit.

- Use a rectangular visual grammar. Place the positive supply toward the top,
  the return or negative rail toward the bottom, inputs toward the left, and
  outputs toward the right when the topology permits. Align repeated branches,
  matched devices, test points, and corresponding BJT/MOS panels to a common
  grid. Preserve generous white space between functional blocks rather than
  compressing the circuit to minimize page area.
- Route external wires as horizontal and vertical segments. A diagonal stroke is
  acceptable inside a standard transistor, diode, op-amp, switch, or other
  component symbol; it is not a reason to continue the wire diagonally. Avoid
  slanted wires, arbitrary zigzags, skewed rails, diamond-shaped routing, and
  decorative bends. If a wire cannot reach a terminal cleanly, change device
  placement or orientation instead of adding an angled segment.
- Connect to exact named symbol anchors. In CircuitikZ/TikZ, derive conductors
  from anchors such as `(Q1.B)`, `(Q1.C)`, `(Q1.E)`, `(M1.G)`, `(M1.D)`, and
  `(M1.S)`, then use `|-` and `-|` projections or named intermediate coordinates
  for right-angle turns. Do not use a visually estimated coordinate near a
  terminal: a small symbol, scale, or orientation change can otherwise leave a
  gap or make a wire appear to pass through the device.
- Apply exact-anchor routing to every gate and functional-block port, not only
  transistor terminals. A wire that visually approaches a port is not connected.
  Inspect every rendered endpoint at high zoom and at final print scale; correct
  gaps, overshoot, doubled segments, and half-grid offsets at the source.
- Rotate or mirror a device when doing so makes connected terminals face one
  another and removes a crossing. Matched mirror devices should normally face
  inward with a short shared-control connection; route a diode-connected strap
  outside and above or beside the reference device, never through its body. In a
  stacked topology, align the upper device with the lower device whose current
  path it continues. Do not preserve a library symbol's default orientation at
  the expense of clarity.
- Prefer topology-preserving placement over long return paths. Nodes that have
  different electrical roles — for example, a mirror's reference node, shared
  control node, and output node — must remain spatially distinct. Place devices
  so those nodes can be connected by short orthogonal paths without a wire
  crossing another device or masquerading as a different node.
- Eliminate wire crossings through placement, spacing, mirroring, and alignment.
  If a crossing is genuinely unavoidable, use an explicit line jump or bridge
  with no junction dot, explain the convention when it is not self-evident, and
  keep the crossing far from labels and terminals. Two lines that nearly touch,
  overlap for a short distance, or cross at a component body are never acceptable
  substitutes for a clear connection.
- Place an explicit connection dot at every junction where three or more
  conductors meet (`node[circ]` / the `*` node in CircuitikZ), so a genuine node
  is never ambiguous with a crossing. Do not place decorative dots at ordinary
  two-terminal component joins or ground-symbol connections.
- Leave a visible straight lead between every multiway junction and the adjacent
  component body. A dot on or immediately against a transistor outline can look
  like a wire passing through the symbol. Likewise, do not place an open test
  point directly on a crowded branch.
- Bring test points out to clear space and place their labels off the wires and
  components — never draw a label over a conductor or symbol.
- Keep device designators, component values, node names, polarity signs, and
  current arrows in dedicated white space. Move the label or enlarge the drawing;
  never accept a collision. In multi-panel figures, check the boundary between
  panels explicitly: labels and arrows near one panel must not read as though they
  belong to the next. Use consistent label positions and device scale across
  analogous panels.
- Declare current direction and voltage polarity graphically wherever the prose
  or equations use signed quantities. Make a current-source direction visible at
  the final print scale; if the library symbol's internal arrow becomes
  ambiguous, add a separate adjacent direction arrow with enough clearance and
  alignment that it cannot be mistaken for another branch or neighboring panel.
- Draw an electrically complete circuit for every operating regime being taught.
  Trace DC with coupling and bypass capacitors open, the declared AC range with
  their stated impedances, and each switched state separately. A DC-bias port,
  resistor, or idealized bias-current source must provide the required terminal
  path; an AC source behind a coupling capacitor does not. Distinguish an
  AC-reference path from a DC-bias path in both the drawing and caption.
- Show idealizations explicitly. An ideal current source, AC ground, bias port,
  or omitted load must be drawn or declared in the caption and prose. Do not
  leave a transistor terminal apparently floating while relying on an unstated
  external circuit to establish its operating point.
- In limiting, bias, clamp, and protection circuits, rate the mandatory resistor,
  fuse, bias network, rail sink, or other supporting element as well as the named
  device. Trace the complete current path and confirm that the schematic,
  equations, and acceptance boundary contain the same elements.
- Keep dual and related schematics visually homologous. A BJT and MOSFET pair
  should use the same rail, signal, bias, and output layout unless a real device
  difference requires otherwise. Use the same reference designators, signal
  names, current directions, voltage polarities, and test-point vocabulary as the
  equations, prose, code, data tables, and procedures.
- Give each circuit a caption and alt text that state the topology, signal path,
  bias/return path, important node roles, and any idealized source or reference.
  Alt text should describe electrical relationships rather than merely listing
  visible shapes.
- Render after every geometry change with
  `python3 curriculum/tools/render_circuits.py --id <id>`. Inspect the
  standalone raster at full size and at its intended QMD width. When a chapter
  contains several circuits, inspect them together as a set for inconsistent
  scale, spacing, orientation, or visual grammar.
- A successful compile proves only that the source is syntactically valid.
  Visual acceptance requires checking for unintended diagonals, crossings,
  near-connections, missing dots, extra dots, cropped labels, excessive white
  space, compressed branches, and unreadable arrows. Then inspect the rendered
  HTML and the actual full-book PDF page, because a clean standalone image can
  still be too small or badly placed in the chapter.

## Citation

- Citations render as bracketed numbers (`[1]`) via `book/styles/numeric.csl`;
  cite at the point of use and let the number, not an author–year block,
  interrupt the prose.
- Cite the first consequential claim; a closing References note is a guide, not a
  substitute for point-of-use support. Prefer primary standards, manufacturer
  documents, and canonical technical sources.
- Cite standards-based symbols and terminology, canonical circuit
  organizations and algorithms, manufacturer data, and every non-original or
  genuinely adapted figure where first used. Credit adapted or reproduced
  figures in their captions and record their license or permission provenance.
  An original explanatory drawing still needs adjacent support for sourced
  topology or notation. Algebra derived completely in the chapter does not need
  a citation after every manipulation.
- Verify new bibliography metadata against an official or primary source and
  audit that every citation key resolves before rendering the final draft.
- Keep `link-citations: true` and `link-bibliography: true` in the book
  configuration. A PDF review must confirm that each citation number links to
  its bibliography entry and that a DOI or URL in that entry is an external
  verification link. A successful bibliography render alone does not establish
  citation navigation.
- Use a labelled cross-document target for prose that points to the consolidated
  bibliography; a relative `.qmd` link can remain a source-file URI in the
  merged PDF.

## Book structure and numbering

- Part titles contain only the semantic title. Do not embed Roman numerals or
  other manual counters: the PDF class supplies the part number, and a manual
  prefix produces duplicate numbering.
- Frontmatter and backmatter pages use one metadata title. Do not repeat that
  title as a body-level H1; doing so creates duplicate chapters and hyperlink
  destinations. Treat numbering as a book-level concern because format metadata
  on `index.qmd` can affect the complete combined document.
- Place appendices in Quarto's native `book.appendices` structure and the
  consolidated bibliography in `book.references`. Do not model appendices as
  an ordinary additional part merely to obtain navigation.
- Verify the extracted PDF table of contents after structural edits. It must
  contain each frontmatter/backmatter entry once, exactly one automatic number
  for every main part, and conventional appendix lettering rather than an
  accidental eighth part.
