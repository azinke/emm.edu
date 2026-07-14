# Circuit as code

Instructional schematics use CircuitikZ source. The editable artifact is a
`.tex` file in this directory; a drawn SVG is never the source.

## Why this route

- symbols, values, nets, and labels are reviewable as text;
- diagrams use one style and scale;
- source is diffable and can be reused in print and web output;
- print receives vector PDF;
- web receives a high-resolution PNG generated from the same source;
- no circuit SVG is committed or edited.

[`catalog.toml`](catalog.toml) stores the caption and alternative text separately
from the drawing code. The example
[`f03-voltage-divider.tex`](f03-voltage-divider.tex) is a complete standalone
CircuitikZ document.

## Render

Install a TeX distribution containing `standalone`, `circuitikz`, and
`siunitx`, plus Poppler's `pdftoppm`. Then run:

```sh
python3 curriculum/tools/render_circuits.py
```

The command writes `build/circuits/<id>.pdf` and
`build/circuits/<id>.png`. Both are disposable build products.

## Authoring rules

- Prefer IEC/european resistor symbols; state deliberate alternatives.
- Include reference designators, values or parameter names, named nets, test
  points, polarity, and current direction when they matter.
- Distinguish 0 V, protective earth, chassis, and signal references.
- Keep circuit behavior understandable in grayscale and without spatial color.
- Use KiCad, not CircuitikZ, for a manufacturing schematic.
- Use WaveDrom source for timing and Mermaid for system architecture; neither is
  a substitute for an electrical schematic.
