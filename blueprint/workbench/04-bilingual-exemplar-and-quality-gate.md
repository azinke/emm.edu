# M04 — Bilingual Exemplar and Quality Gate

**Goal:** produce and pilot one complete EN/FR unit—ESE111 Chapter 4, Kirchhoff Models—to prove technical, pedagogical, laboratory, assessment, accessibility, and publishing workflows.

**Indicative duration:** 8–12 weeks  
**Primary owners:** exemplar course author, lab instructor, EN/FR editors, assessment and accessibility reviewers  
**Depends on:** M02–M03  
**Authoring entry:** draft M02 templates/build smoke test and the specific M03-approved exemplar bench/safety route exist\
**Release gate:** the M02 production workflow and M03 exemplar equipment/safety paths are approved, versioned baselines\
**Exit unlocks:** scaled course production

## Epic E1 — Unit design brief

- [x] **M04-E1-T01 [SPEC]** Define outcomes, prerequisites, misconceptions, vocabulary, model limits, safety, evidence, and downstream dependencies.
- [ ] **M04-E1-T02 [SPEC]** Select an approved, versioned M01 context brief such as diagnosing a repairable low-voltage lighting or sensor network; provide a portable alternative that preserves the engineering decision.
- [x] **M04-E1-T03 [SPEC]** Write measurable acceptance: students predict, solve, measure, quantify disagreement, localize a seeded fault, redesign one branch, and verify the changed result.
- [x] **M04-E1-T04 [MAT]** Create shared schematics, parameter sets, simulations, raw-data schema, rubrics, and expected ranges.
- [ ] **M04-E1-T05 [REV]** Review construct, workload, safety, and EN/FR terminology before prose expands.
- [x] **M04-E1-T06 [SPEC]** Instantiate the unit manifest and claim/source register, classifying every derivation, component behavior, instrument limit, historical/context statement, and version-bound source.

### E1 implementation record — 2026-07-14

The versioned design contract, parameter set, analytical oracle, exhaustive
tolerance/meter corner model, raw-data schema, rubric, editable accessible
schematic, artifact metadata, unit manifest, and claim/source register are under
[`curriculum/courses/ESE111/shared/`](../../curriculum/courses/ESE111/shared/).
The model deliberately labels calculated bounds as simulation, not physical
expected ranges or golden data.

T02 remains open because `CTX-BJ-ENERGY-001` is at `review`, not approved, and
M01-E2-T04 has not produced an approved measurable context brief. Draft teaching
uses the design brief's deployment-neutral repair fixture; it makes no Benin,
stakeholder, availability, or origin claim. T05 remains open until reviewers
independent of the author accept construct, workload, safety, and natural EN/FR
terminology. Authoring checks and automated tests do not impersonate those roles.

## Epic E2 — Complete teaching package

- [x] **M04-E2-T01 [MAT]** Author natural EN and FR chapters following Discover → Understand → Experiment → Analyze → Design.
- [x] **M04-E2-T02 [MAT]** Create claim-titled slides, speaker notes, prediction poll, board plan, demonstration, and static fallback.
- [ ] **M04-E2-T03 [MAT]** Create pset with estimation, nodal/Kirchhoff modeling, simulation, datasheet/measurement, fault diagnosis, and design; create restricted solutions.
- [x] **M04-E2-T04 [MAT]** Create guided lab in minimal and standard paths with setup inspection, raw-data table, uncertainty, seeded open/incorrect-value fault, and redesign.
- [ ] **M04-E2-T05 [MAT]** Create 8–12 independently reviewed pilot-ready MCQs across levels with plausible misconceptions and explanations in both languages; publish a post-pilot item-analysis plan for growing the mature bank to 20+ without filler.
- [x] **M04-E2-T06 [MAT]** Create professor notes, remediation, enrichment, editable figures, alt/long descriptions, and low-bandwidth files.

### E2 implementation record — 2026-07-14

The paired package now contains a unit guide, prerequisite diagnostic, natural EN
and FR chapter editions, claim-titled slides with speaker notes, lecture/board
plan, loading demonstration and static recovery, guided exploration, all-category
problem set, two-path laboratory, public practical construct, repair-handoff design
clinic, professor notes, remediation/enrichment, accessible source figure,
reference artifacts, prepared analysis fallback, contribution boundary, open QA
record, and an offline/low-bandwidth inventory. Artifact IDs and the shared
technical contract are structurally paired; calculated and prepared values retain
their provenance.

T03 remains open: the public problem set is complete, but M02-E4-T02 has not
configured the separately permissioned production store, so the current worked
solution cannot lawfully be created or committed here. T05 remains open: the
ten-item bilingual construct and post-pilot growth/analysis plan exist, but actual
pilot items, keys, explanations, independent reviews, and later statistics belong
to that controlled store. Public opaque references expose none of those contents.

## Epic E3 — Technical and physical pilot

- [ ] **M04-E3-T01 [TEST]** Independently recompute every circuit, inspect units/notation/schematics and primary-source versions, simulate tolerances, compile/run applicable assets, and verify answer keys/restricted views.
- [ ] **M04-E3-T02 [TEST]** Run lab with primary and substitute components on minimal and standard equipment; record golden raw data and realistic ranges.
- [ ] **M04-E3-T03 [TEST]** Seed faults without telling pilot instructors; verify the diagnostic tree distinguishes them.
- [ ] **M04-E3-T04 [TEST]** Rehearse lecture/demo timing, equipment failure, power interruption, absent internet, and recovery.
- [ ] **M04-E3-T05 [REV]** Complete technical, lab safety, accessibility, license, and instructor-usability reviews.

### E3 control implementation record — 2026-07-14

The repository now provides an independent-recomputation/source/build protocol,
a primary/substitute × minimal/standard physical-pilot matrix, strict raw-data and
golden-data provenance rules, blind-fault custody and redacted reporting controls,
a timed second-instructor/failure-recovery rehearsal, and five independent review
briefs under [`shared/pilots/`](../../curriculum/courses/ESE111/shared/pilots/).
An executable evidence gate rejects completion without attributable evidence,
rejects prepared/simulated data as a physical pilot, and rejects release approval
while a task or facet is pending.

All E3 boxes remain open. Automated authoring checks cannot close T01 without a
qualified reviewer and controlled answer views; no approved exact apparatus has
produced T02 physical/golden data; no blind instructors have executed T03; no
second instructor has rehearsed T04; and none of the named independent authorities
has approved T05. The protocols name the exact evidence required to close each task.

The E3 authoring audit independently recomputed the published nominal and corner
values, then triggered corrections before this control commit: valid inline math
plus a rendered regression, explicit KVL residuals, reproducible prepared data,
expanded-uncertainty/coverage semantics with guard bands, a Boolean continuity
schema, stable unit-outcome traceability, and an unclipped convention-labeled
schematic. Pandoc produced all 24 HTML documents and both static slide decks, and
the rendered-output gate passed. Full PDF/Quarto evidence remains open because the
frozen host lacks Quarto, `footnote.sty`, and `rsvg-convert`; partial PDFs also
fail the embedded-font gate, and build warnings remain failures rather than being
waived.

## Epic E4 — Learner and parity pilot

- [ ] **M04-E4-T01 [TEST]** Pilot with consented small EN-dominant and FR-dominant learner groups representing target readiness and access needs; predefine sample rationale, qualitative stopping rule, and acceptance thresholds.
- [ ] **M04-E4-T02 [TEST]** Observe predictions, wiring, instrument use, discussion, debugging, cognitive load, time, and design transfer.
- [ ] **M04-E4-T03 [TEST]** Compare learning and item behavior by language without overinterpreting small samples; log wording versus conceptual issues.
- [ ] **M04-E4-T04 [REV]** Revise both editions, expected ranges, professor notes, hints, and timing from evidence.
- [ ] **M04-E4-T05 [REL]** Tag exemplar release and publish its QA record and known limitations.

### E4 control implementation record — 2026-07-14

The learner-pilot controls under
[`shared/pilots/`](../../curriculum/courses/ESE111/shared/pilots/) now preregister
matched EN-dominant and FR-dominant formative routes, a bounded 6-per-route sample
rationale, qualitative stopping and hard-ceiling rules, readiness/access accounting,
conjunctive safety and reasoning thresholds, and explicit prohibitions on efficacy,
causal language-effect, demographic, or small-sample equivalence claims. A paired
participant-information draft states voluntariness, withdrawal, privacy, access,
burden, and stop conditions, but is visibly unusable until the deploying authority
inserts and approves accountable contacts and the consent/data route.

The observation instrument records committed predictions, representation/model
work, wiring and instrument choices, discussion, uncertainty, debugging, prompt
level, cognitive-load indicators, time, and design transfer without treating group
work as individual competence. The frozen parity plan uses counts, individual
values, conservative wording-versus-concept adjudication, and controlled item-slot
review; it forbids significance, DIF, causal, or powered-equivalence claims at the
planned scale. The paired-revision/release control links every change to evidence,
reopens affected pilots, distinguishes simulated from physical expected ranges,
requires production-effort metrics and known limitations, and prohibits a tag
until every task/facet is accepted by the independent release authority.

All E4 boxes remain open: no human-participant authority has approved recruitment
or consent; no consented learners, observers, controlled items, or pilot records
exist; therefore there is no parity result or evidence-based revision to claim.
The evidence gate now rejects learner-task completion without deidentified human
provenance, an authority record, and recorded authorized consent. No release tag
was created.

## Hands-on and real-life safeguard

Students must confront at least one measurement that disagrees with the ideal calculation because of tolerance or meter/loading effects. The design extension must change a real requirement—brightness balance, sensor threshold, current budget, or fault tolerance—and require post-change verification.

## Required deliverables

- Approved applicability/unit manifest and claim/source register
- Paired EN/FR teaching/source pack with restricted artifacts referenced separately
- Independent technical/safety/accessibility/license/build review record
- Minimal/standard physical data plus second-instructor and learner-pilot evidence
- Defect disposition, QA record, release tag, offline outputs, and measured production effort

## Exit criteria

- [ ] Every applicable unit resource in §13.1 is represented; non-applicability is approved rather than manufactured as filler.
- [ ] Both language editions pass the same technical and cognitive threshold.
- [ ] A second instructor can teach the unit and recover the demo using the notes.
- [ ] The physical lab produces reproducible evidence on both equipment paths.
- [ ] Production metrics from the exemplar update later milestone estimates.
- [ ] Independent release authority approves zero open critical defects and time-bounded owners for accepted residual defects.
