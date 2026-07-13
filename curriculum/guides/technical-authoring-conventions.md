# Technical notation, schematic, source, and accessible-figure conventions

These shared rules apply identically to English and French artifacts. Natural
prose is language-specific; equations, component values, safety limits, expected
ranges, data, figures, reference designators, and evidence thresholds form one
technical contract.

## Mathematical and engineering notation

- Define symbols locally and maintain a unit-level symbol table. Do not reuse one
  symbol for unrelated quantities in the same unit.
- Typeset variables in italic and units/functions in upright form where the format
  permits. Use clear subscripts: `V_out`, `R_th`, not ambiguous adjacency.
- State reference direction, polarity, coordinate system, passive sign convention,
  phase convention, and whether a magnitude is instantaneous, peak, peak-to-peak,
  RMS, average, phasor, or complex.
- Keep full precision during computation, round once for reporting, and match
  significant figures to input uncertainty and purpose. A displayed digit is not
  evidence of accuracy.
- Every equation is dimensionally valid; every worked result includes units,
  assumptions, domain, order-of-magnitude check, and engineering interpretation.
- Distinguish equality, approximation, proportionality, bounds, ranges, and
  uncertainty. Report measured results as value ± uncertainty with coverage basis
  when available; never invent an exact expected measurement.
- Use ISO dates (`YYYY-MM-DD`) and unambiguous versions/revisions. Give local time
  zone where timing matters. Use SI units; non-SI units require a reason and
  conversion.
- Keep decimal points in machine-readable content. Localize prose decimals without
  changing parameter files or raw data.

## Schematics, block diagrams, plots, and waveforms

- Teach IEC symbols and recognize ANSI alternatives. Metadata and legends state
  the convention; do not mix conventions silently.
- Every schematic shows values/part IDs, reference designators, named nets and test
  points, source/return conventions, connector pin numbers, signal direction, and
  relevant ratings. Crossing lines and junctions must be unambiguous.
- Do not use earth, chassis, analog ground, digital ground, and 0 V symbols as
  decorative equivalents. Label active-low signals textually (`nRESET` or an
  explicit bar/bubble convention) and document polarity.
- Block diagrams expose system boundary, interfaces, energy/data/control flows,
  ownership, and off-page references. Architecture cannot depend on spatial
  placement or color alone.
- Plots have meaningful title/caption, labeled axes and units, scales/transforms,
  legend, sample/condition, uncertainty or variation representation, and source.
  Choose line styles, markers, direct labels, and patterns that survive grayscale.
- Waveforms state x/y scale, reference, probe/test point, bandwidth/coupling,
  trigger or alignment, operating conditions, and whether ideal, simulated, or
  measured. Screenshots do not substitute for recoverable data.
- Logic/timing diagrams define unknown/high-impedance/don't-care states, clock
  edge, latency, setup/hold reference, and asynchronous relationships.

## Accessible figures and media

1. Write the figure's instructional purpose before drawing it. Remove decorative
   detail that increases cognitive load without evidence value.
2. Store editable source and stable figure ID. Render vector graphics where
   practical and preserve legibility in print, zoom, grayscale, and low bandwidth.
3. Provide localized captions that state the conclusion or reason for the figure,
   not only its noun label.
4. Provide concise alt text conveying purpose and essential content. Do not repeat
   a nearby caption verbatim or begin with “image of.”
5. Give a long description for complex schematics, plots, timing diagrams, and
   multi-panel figures: orientation/reading order, components/axes, relationships,
   key values/patterns, anomalies, and intended conclusion.
6. Encode states, traces, warnings, polarity, and pass/fail through labels, shapes,
   line styles, patterns, or position in addition to color. Maintain sufficient
   contrast and avoid tiny embedded text.
7. For photographs, label relevant terminals/components and state configuration,
   scale, orientation, and whether the image is representative or actual pilot
   evidence. Remove personal/sensitive data.
8. Caption/transcribe audio and video, add chapter markers, describe meaningful
   visual action, and ship a still/data/text fallback. Animation must not be the
   sole access to a derivation or result.
9. Test reading order, keyboard navigation where interactive, printable fallback,
   and an outcome-preserving route with representative users before stable release.

Use [`reference-artifact-metadata.yml`](../templates/teaching-resources/reference-artifact-metadata.yml)
to record these checks.

## Citation, originality, and provenance

- Cite a source at the point its claim, figure, data, method, code, or wording is
  used. The bibliography alone does not reveal provenance.
- Prefer primary, authoritative material for standards, regulations, safety limits,
  device behavior, platform support, and current capabilities. Record issuer/
  author, title, identifier, edition/version/revision, date, exact locator,
  retrieval date, and access/license terms.
- Textbooks and secondary explanations may support pedagogy; they do not replace
  checking the primary source for a version-bound or consequential claim.
- Mark quotations and keep them minimal. Paraphrase from understanding and cite;
  changing a few words is not original authorship.
- For reused/adapted figures, code, HDL, PCB, datasets, and media, record creator,
  canonical source, version, license/permission, required attribution, and exact
  modifications. Confirm license compatibility before publication.
- Original artifacts still name creators/contributors, creation method, tool
  versions where material, and license. AI-assisted material is declared and
  independently verified; a tool is not an authority for a claim or a source of
  fabricated citations.
- Keep external-link metadata and a checksum/archive only when permission permits.
  Never evade access controls. Keep restricted assessments, student data, and
  partner-confidential evidence out of public artifacts.
- Use the claim register for testable assertions and the reference-artifact record
  for asset provenance. Both language editions cite the same technical source even
  when their explanations differ.

## Review checklist

- [ ] Equations, values, units, notation, references, and conditions match EN/FR.
- [ ] Independent reviewer reproduced major calculations/results from source data.
- [ ] Schematic convention, polarity, references, nets, and test points are explicit.
- [ ] Plots/waveforms distinguish ideal, simulated, and measured evidence.
- [ ] Editable source, stable ID, captions, alt text, long descriptions, and
      non-color encoding are complete.
- [ ] Original/reused/adapted status, attribution, license, modification, and tool
      assistance are recorded.
- [ ] Date-sensitive sources have reviewer, review due date, and event trigger.
