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
- Use reference designators and named signals consistently across circuit,
  equation, code, PCB, and test procedure.
- Give diagrams useful captions and alternative text. Add a prose description
  when relationships are too complex for short alt text.
- Never use color as the only carrier of state, polarity, warning, or pass/fail.

## Headings

- Write section headings as natural, chapter-specific claims. Do not reuse a
  fixed template vocabulary across chapters, and do not use the literal word
  "model" as a heading; name the actual idea instead.
- Headings should still map cleanly to the editorial functions in
  [`chapter-template.qmd`](chapter-template.qmd) (motivate, build, apply, test,
  find limits, decide, consolidate) — the wording is yours, the sequence is not.

## Diagrams and code that survive print

- Draw Mermaid flowcharts vertically (`flowchart TB`) with concise node text so
  they do not scale off the PDF page; carry longer descriptions in the caption
  and alt text rather than in wide nodes.
- Mermaid renders no math: write symbols in node text as Unicode subscripts
  (`Rₜₕ`, `Rᵢₙ ∥ Cᵢₙ`) or plain names, never `$…$`. Put any real math in the
  caption or alt text, where LaTeX/MathML does render.
- Keep code and verbatim listings short-lined; the PDF build wraps long lines,
  but a line that must wrap is usually a line that should be split.

## Circuits

- Place an explicit connection dot at every junction where three or more
  conductors meet (`node[circ]` / the `*` node in CircuitikZ), so a genuine node
  is never ambiguous with a crossing.
- Bring test points out to clear space and place their labels off the wires and
  components — never draw a label over a conductor or symbol.

## Citation

- Citations render as bracketed numbers (`[1]`) via `book/styles/numeric.csl`;
  cite at the point of use and let the number, not an author–year block,
  interrupt the prose.
