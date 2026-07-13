# Pull-request and release review checklist

Record `approved`, `not_applicable` with reason, or `changes_requested` for every
facet. An author cannot be the sole approver of a high-stakes assessment,
hazardous activity, or final technical release. Approval applies only to the
identified commit and is invalidated by a relevant change.

## Change identity and alignment

- [ ] Stable artifact/semantic IDs, owner, type, version, lifecycle state, and
  EN/FR pairing are valid.
- [ ] Outcomes, prerequisites, activity, evidence, rubric rows, next dependency,
  context layer, and workload align.
- [ ] Applicability decisions cover every required §13.1 resource type; an
  omission has an approved outcome/dependency rationale.
- [ ] The hands-on safeguard fields are substantive: real-life question,
  prediction, student action, physical/data evidence, fault/anomaly, design
  decision, and acceptance test.

## Technical and physical-pilot approval

- [ ] A reviewer other than the author independently recomputed equations,
  values, units, limits, expected ranges, and answer keys.
- [ ] Code, numerical examples, simulation, HDL, and PCB hooks pass in the frozen
  environment when applicable; warnings and waivers are dispositioned.
- [ ] Each declared apparatus path has dated physical-pilot evidence, raw
  observations, expected ranges, substitute effects, reset, and safe fallback.
- [ ] Claims register primary sources, versions/retrieval dates, assumptions,
  verification, affected assets, owner, and review-due trigger.

## Safety and responsibility approval

- [ ] Energy/fault sources, authorization, PPE/supervision, inspection points,
  stop conditions, cleanup, incident response, and prohibited modes are explicit
  and consistent in both languages.
- [ ] Safety, security, privacy, ethics, sustainability, accessibility,
  manufacturability, service, and lifecycle are requirements where applicable;
  residual risk has an owner.
- [ ] Deployment/context and local-origin claims cite current approved records;
  no universal content embeds an unversioned jurisdiction assumption.

## Bilingual approval

- [ ] EN and FR preserve outcomes, cognitive demand, figures/data, notation,
  safety meaning, timing, points/rubric totals, support, and release status.
- [ ] Each edition is natural, uses controlled terminology, localizes alt text,
  captions/descriptions, and retains machine/tool tokens unchanged.
- [ ] A technical correction is simultaneous or has a release-blocking paired
  issue with owner and deadline.

## Accessibility approval

- [ ] Semantic headings, keyboard path, reading order, contrast, non-color cues,
  MathML-compatible math, link purpose, and accessible tables pass.
- [ ] Figures/media have localized captions, alt text, long descriptions when
  complex, transcripts/captions, and static/low-bandwidth alternatives.
- [ ] Lab/assessment adaptations preserve the construct and identify essential
  personal decisions separately from one physical method.

## License, originality, and data approval

- [ ] Original work and quotations are lawful; third-party creator/source,
  license, version, modification, attribution, archival permission, retrieval
  date, and checksum are recorded.
- [ ] SPDX identifiers follow the matrix; contributor sign-off and any sponsor,
  student, or partner IP agreement are complete.
- [ ] No live assessment, current solution, protected data, partner secret,
  credential, or restricted link appears in source, history, build, log, cache,
  or offline package.

## Build and release approval

- [ ] EN/FR HTML, printable PDF, and slides build offline from frozen tools;
  links, pagination, fonts/math/schematics, size budget, and visuals pass.
- [ ] Seeded tests fail for the intended reason, including parity,
  accessibility, answer-key, link, KiCad, and restricted-content fixtures.
- [ ] Known limitations, defect dispositions, approvals, change log,
  migration/learner-impact note, manifest, tag/commit, and checksums are complete.
- [ ] Second-instructor rehearsal and formative learners from both language
  pathways are complete before `pilot-ready`; broader cohort evidence is complete
  before `stable`.
