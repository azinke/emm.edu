# English curriculum style guide

This is the normative prose guide for the English academic edition. Use it with
the shared [`technical-authoring-conventions`](../guides/technical-authoring-conventions.md),
the controlled [`termbase`](termbase.yml), and the
[`French style guide`](style-guide-fr.md). English and French are coequal routes to
one technical contract; English is not the canonical edition.

## Voice and structure

- Address the learner directly with a plain imperative: “Measure the voltage,”
  “Compare the traces,” “Justify the choice.” Use “you” when agency matters.
- Prefer short concrete sentences and verbs over noun clusters: “Measure three
  units and report the range,” not “performance of measurement activities.”
- Use international English. Avoid idioms, culture-bound jokes, unexplained sports
  metaphors, double negatives, and irrelevant reading complexity.
- State the engineering question or claim in headings. “Loading changes the
  measured divider voltage” is stronger than “Voltage dividers.”
- Separate instruction, evidence, caution, and explanation. Each numbered
  procedure step contains one observable action and its checkpoint.
- Distinguish `must` (requirement), `should` (recommended default), `may`
  (permission), and `can` (capability). Do not use them interchangeably.
- State who acts: learner, team, instructor, reviewer, or system. Do not hide
  accountability in the passive voice.

## Technical language

- Spell out an acronym on first meaningful use, then give its professional form:
  printed circuit board (PCB), pulse-width modulation (PWM). Retain common
  datasheet/tool acronyms such as GPIO, SPI, I²C, UART, FPGA, CMRR, and PSRR.
- Use one concept term consistently. When a legitimate synonym helps source
  navigation, introduce it once and map it to the termbase concept ID.
- Do not use `accuracy`, `precision`, `resolution`, `tolerance`, `repeatability`,
  and `uncertainty` as synonyms. Define the metrological property intended.
- Label `ground` precisely: protective earth, chassis, signal reference, or 0 V.
  Do not imply that these nodes are necessarily connected.
- Keep identifiers, commands, paths, register names, protocol tokens, net names,
  reference designators, and diagnostics exactly as tools emit them. Explain them
  in prose; do not rewrite them.
- Prefer inclusive, role-specific language. Avoid “obvious,” “simple,” “normal
  user,” “native speaker,” and deficit labels for people or contexts.

## Numbers, notation, and units

- Use a decimal point in prose: `3.3 V`. Machine data, code, SPICE, filenames, and
  version strings also use the point.
- Put a nonbreaking space where supported between number and unit: `10 kΩ`,
  `25 °C`, `2.0 ms`. Unit symbols never take a plural or full stop.
- Use SI prefixes and avoid `billion` ambiguity. Write `1 × 10^9`, `1 GHz`, or the
  exact quantity. Use a true minus sign in rendered mathematics where supported.
- Use `µ` in publication and accept `u` only in ASCII-only tool fields. Preserve
  upper/lower case: `m` is milli, `M` is mega, `Hz`, `V`, `A`, `Ω`.
- Define every symbol at first use, keep one symbol per quantity in a unit, show
  units during substitution, and state vector/phasor/complex and RMS/peak
  conventions.
- Give a value with the conditions that make it meaningful: input, supply,
  temperature, frequency, load, instrument bandwidth, reference, tolerance, and
  uncertainty as applicable.

## Instructions, questions, and assessment

- Ask for observable reasoning: estimate, sketch, calculate, measure, compare,
  diagnose, choose, justify, or qualify. “Understand” is not an assessable command.
- Put the prediction before the revealed observation. Ask for a reason and, where
  useful, confidence; do not penalize an honest prediction merely for differing
  from the result.
- Avoid trick wording, double negatives, grammatical distractors, and local facts
  irrelevant to the construct. Distractors represent plausible technical models
  or process errors.
- Grade engineering meaning, evidence, safety, and clarity—not accent, idiom, or
  nonessential grammar—unless language production is the explicit outcome.
- Publish allowed resources, numerical/terminology conventions, rubric, mastery
  threshold, individual/team boundary, and wording-challenge route.

## Context and claims

- Name the context-brief ID/version when context affects a requirement. State the
  changed calculation, architecture, test, cost, safety, service, or lifecycle
  choice. Do not use a place or community as decorative scenery.
- Avoid presenting any country or community only through scarcity. Include
  scientific, industrial, artistic, consumer, entrepreneurial, and public-service
  contexts, and describe observed conditions rather than stereotypes.
- Say exactly who designed, assembled, tested, calibrated, deployed, or serviced
  the named configuration. Never infer national origin from team location or final
  assembly; use the approved contribution/origin guide and dossier.
- Qualify every performance claim by conditions and required evidence rung. “It
  worked once” is not reliability, field fitness, or general yield.

## English–French parity checklist

- [ ] Same semantic ID, version, lifecycle, outcomes, prerequisites, timing, points,
      mastery threshold, allowed resources, safety limits, values, equations, raw
      data, figures, faults, expected ranges, and rubric totals.
- [ ] Prose is natural English rather than a trace of French syntax.
- [ ] Captions, alt text, long descriptions, transcripts, and answer explanations
      are complete, not left in the other language.
- [ ] Shared technical identifiers and source locators are unchanged.
- [ ] Technical correction has a paired-language issue and both editions were
      corrected, reviewed, and released together.
- [ ] Learners in both language pathways piloted the wording and cognitive demand.

Machine translation may create an internal draft only. A qualified technical
reviewer and a fluent pedagogical reviewer approve the released edition.
