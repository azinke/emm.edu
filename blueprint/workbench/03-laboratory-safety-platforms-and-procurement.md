# M03 — Laboratory Safety, Platforms, and Procurement

**Goal:** qualify safe, repairable, locally procurable hardware and three equipment paths that can support the planned hands-on curriculum.

**Indicative duration:** 8–14 weeks; procurement continues thereafter  
**Primary owners:** laboratory director, safety officer, technician, procurement lead, platform engineers  
**Depends on:** M00–M01  
**Authoring entry:** M00 names safety/procurement authority and M01 supplies draft infrastructure, supply, and jurisdiction constraints\
**Release gate:** applicable M01 safety, infrastructure, sourcing, and local-capability findings are approved or explicitly dispositioned\
**Exit unlocks:** M04 physical pilot, M06 onward laboratory production

## Epic E1 — Laboratory safety system

- [ ] **M03-E1-T01 [SPEC]** Publish L0–L4 authorization, supervision ratios, PPE, stop-work, energization, cleanup, incident, near-miss, quarantine, and waste procedures in EN/FR.
- [x] **M03-E1-T02 [SPEC]** Define energy-aware limits: voltage plus current/fault power, capacitor/battery stored energy and chemistry, fusing, conductor/probe ratings, accessible temperature, rotating energy, chemicals/coatings, oscilloscope grounding/measurement category, RF exposure, and field conditions; retain current-limited extra-low-voltage core work and institution-controlled higher hazards.
- [x] **M03-E1-T03 [MAT]** Create safety induction, quizzes, practical stations, instructor calibration, remediation, and authorization records.
- [ ] **M03-E1-T04 [HW]** Inspect RCD/GFCI, emergency isolation, fire response, first aid, ventilation/fume extraction, ESD, storage, exits, accessibility, and signage.
- [ ] **M03-E1-T05 [TEST]** Run incident-response and damaged-battery/equipment quarantine drills.
- [x] **M03-E1-T06 [SPEC]** Require activity-specific risk assessment and safety-authority approval for each new lab domain, with authorization expiry/requalification, emergency response, accessible safe methods, and stop conditions.
- [x] **M03-E1-T07 [SPEC]** Crosswalk practice to program gates: G1 is required for independent L1 energization, while pre-G1 practice is limited to direct-supervised instructor-controlled stations; solder training may begin at L2 after task briefing under direct supervision, while G3 certifies independent progression rather than first exposure; allow formally assessed prior equivalent competence to challenge a gate without waiving its evidence threshold.

## Epic E2 — Platform capability qualification

- [x] **M03-E2-T01 [SPEC]** Convert each planned board use into capability contracts: I/O voltage, ADC, timers, buses, memory, debug, radio, logic, toolchain, recovery, lifecycle, and cost.
- [ ] **M03-E2-T02 [TEST]** Procure samples from at least two channels and score Pico 2/equivalent, professional MCU, wireless board, FPGA, Linux target, probes, and programmers.
- [ ] **M03-E2-T03 [TEST]** Run golden projects for boot/recovery, GPIO, ADC, timer/PWM, serial buses, debug, power, and offline build on primary and substitute boards.
- [ ] **M03-E2-T04 [SPEC]** Publish board abstraction sheets with pins, electrical limits, boot/debug, errata, known failure modes, substitute mapping, and safe handling.
- [ ] **M03-E2-T05 [DEC]** Freeze exact cohort boards/revisions and replacement triggers; prohibit irreversible security operations on ordinary reusable boards.
- [ ] **M03-E2-T06 [TEST]** Benchmark document, KiCad, firmware, HDL/FPGA, numerical, and Linux workflows on named lowest-supported/refurbished computers; publish build times, offline storage, loan/repair path, and shared-build fallback.

## Epic E3 — Inventory and bench build-out

- [ ] **M03-E3-T01 [SPEC]** Convert personal, pair, progression, shared-bench, advanced, consumable, and spare inventories into quantities for actual cohorts.
- [ ] **M03-E3-T02 [SPEC]** Add manufacturer part number, functional spec, approved substitutes, source, deployment/source-currency landed cost and date (XOF for Benin), lead time, lifecycle, storage, and test method.
- [ ] **M03-E3-T03 [HW]** Build known-good, student-use, quarantine, and deliberate-fault inventories with bilingual/high-contrast labels.
- [ ] **M03-E3-T04 [HW]** Establish incoming inspection, instrument function/calibration checks, repair, tip/probe/fuse replacement, battery inspection, and consumable replenishment.
- [ ] **M03-E3-T05 [HW]** Assemble minimal and standard benches; verify current limits, fault energy, probe compensation, grounded-scope constraints, and safe motor/power setups.
- [ ] **M03-E3-T06 [HW]** Release locally reproducible design packs for cables, fixtures, deliberate-fault boards, enclosure/harness samples, and test jigs; qualify technicians to build, inspect, repair, calibrate/function-check, and revise them.
- [ ] **M03-E3-T07 [SPEC]** Budget total cost by cohort/equipment path: computers, tax/duty/freight, calibration, consumables, storage, power backup, staff/technician time, spares, repair, replacement, disposal, and stock-floor/reorder triggers.

## Epic E4 — Three-path laboratory validation

- [ ] **M03-E4-T01 [TEST]** Define minimal, standard, and advanced apparatus for core phenomena and identify outcomes that require physical access.
- [ ] **M03-E4-T02 [HW]** Develop safe MCU-based stimulus/acquisition and prepared raw datasets for rotation or accessibility, without misrepresenting them as personal measurement.
- [ ] **M03-E4-T03 [TEST]** Compare evidence quality and uncertainty across paths on at least DC networks, RC response, sensor calibration, digital timing, and MCU debugging.
- [x] **M03-E4-T04 [MAT]** Create bench setup maps, equipment quick guides, troubleshooting cards, and check-in/out procedure.
- [ ] **M03-E4-T05 [REV]** Obtain safety and instructor usability approval.
- [ ] **M03-E4-T06 [TEST]** Set and test minimum per-student physical-access entitlement; prepared data can preserve an analysis lesson but missed personal construction/measurement/debug evidence is rescheduled.
- [x] **M03-E4-T07 [SPEC]** Define later safety requalification prerequisites for S2 device/soldering, S3 precision/FPGA, S4 PCB/power, S5 RF/security, and S6 field activities.

## Implementation and verification record — 2026-07-14

**Evidence rule:** a checked item has committed repository evidence for the stated
specification, material, decision, or test result. A procedure, template, planning
scenario, synthetic dataset, or development-host run is not represented as a
physical inspection, procurement, human qualification, institutional approval,
learner authorization, or deployment result.

### E1 — Laboratory safety system

- The paired [English safety manual](../../curriculum/laboratory/safety/en/safety-manual.md)
  and [French safety manual](../../curriculum/laboratory/safety/fr/manuel-de-securite.md)
  share one language-neutral technical contract. The manual covers L0–L4,
  supervision, PPE, stop work, energization, cleanup, incidents, near misses,
  damaged-equipment/battery quarantine, waste, emergency response, and accessible
  safe participation. It remains draft until named technical, language, safety,
  and institutional authorities approve and publish it; therefore T01 is open.
- The technical contract defines task-specific voltage, current/fault-power,
  capacitor/battery energy and chemistry, fuse/conductor/probe, temperature,
  rotation, chemical/coating, grounded-scope/category, RF, and field-condition
  controls. Planning caps are explicitly not a safe harbor and require local
  safety-authority review against the applicable rules.
- Paired induction packages provide formative questions, practical stations,
  assessor calibration, conjunctive pass rules, remediation, accessible methods,
  expiry/requalification, and prior-equivalence challenge rules. Controlled blank
  records cover activity approval, individual authorization, facility inspection,
  drills, events, quarantine, and waste.
- `curriculum/data/safety.yml` now exposes L0–L4 and the G1/G3 relationships instead
  of the earlier simplified L0–L2 draft. Canonical validation, offline content/output
  QA, publication build, JSON parsing, EN/FR structural checks, and `git diff --check`
  passed during implementation.
- **Open M03-E1-T04 evidence:** a competent person must inspect the named facility,
  test applicable RCD/GFCI and emergency systems by the adopted method, disposition
  every defect, and sign the record. **Owners:** laboratory director and safety officer.
- **Open M03-E1-T05 evidence:** trained participants must execute and debrief both
  incident-response and damaged-battery/equipment quarantine drills in the named
  facility, including accessibility, communications, timing, observed actions,
  corrective owners, and a successful effectiveness check. **Owner:** safety officer.

### E2 — Platform capability qualification

- [Capability contracts](../../curriculum/laboratory/platforms/capability-contracts.yml)
  now cover foundation MCU, professional MCU/RTOS, wireless, FPGA, embedded Linux,
  and debug/programming tools across electrical domains, ADC, timers, buses, memory,
  debug, radio, logic, offline toolchain, recovery, lifecycle, and total cost. The
  canonical platform matrix carries all seven categories and truthfully marks
  untested hardware `qualification-pending`.
- The platform control pack provides two-channel procurement and weighted scorecard
  records; a common golden-project contract for boot/recovery, GPIO, ADC, timers/PWM,
  buses, debug, power, and offline build; abstraction-sheet fields and pending
  category sheets; cohort freeze/replacement and irreversible-security controls;
  and full-workflow lowest-supported/refurbished-computer benchmark records.
- Exact pins, electrical limits, errata, MPN/revision, supplier provenance, and
  measured results are intentionally blank until verified against primary documents
  and received samples. A category sheet is not a qualified board.
- Canonical validation, generator equality, YAML parsing, offline content QA,
  automated script tests, and `git diff --check` passed during implementation.
- **Open M03-E2-T02/T03 evidence:** procure exact samples through at least two viable
  channels, authenticate/inspect them, run and independently review every applicable
  golden test on each primary and substitute revision, and publish the resulting
  scores, raw logs, measurements, limitations, and landed costs. **Owners:** platform
  engineering and procurement leads.
- **Open M03-E2-T04 evidence:** complete and approve exact abstraction sheets from
  authoritative documents plus sample measurements and failure/recovery evidence.
  **Owner:** platform engineering lead.
- **Open M03-E2-T05 evidence:** sign a real cohort freeze naming every orderable part,
  assembly revision, tool image, driver, programmer, substitute, spare quantity, and
  trigger. **Approvers:** course owners, laboratory director, safety/procurement,
  toolchain owner, and release manager.
- **Open M03-E2-T06 evidence:** execute all six workflow classes on named minimum
  Linux and Windows/refurbished candidates; publish cold/warm times, failures,
  offline storage, repair/loan route, and shared-build fallback after review. The
  development host is not promoted to minimum-profile evidence. **Owners:** toolchain
  owner, IT/loan-fleet owner, and learner-device reviewer.

### E3 — Inventory and bench build-out

- The [inventory and procurement control set](../../curriculum/laboratory/procurement/README.md)
  defines personal, pair, progression, simultaneous/shared, advanced, consumable,
  deliberate-fault, and spare classes; actual-cohort input; upward-rounded quantity
  formulas; the master-document spare floors; accessible EN/FR high-contrast stock
  states; and acceptance review.
- The procurement register includes functional specification, manufacturer/MPN and
  revision, substitutes, source/channel, source-currency and XOF landed-cost fields,
  exchange source/date, tax/duty/freight, quote validity, lead time, lifecycle,
  storage, inspection/test, calibration/function-check, repair, disposal, quantity,
  stock floor, reorder trigger, evidence, owner, and reviewer. Its sole example row
  is unambiguously `EXAMPLE-DO-NOT-PROCURE` and contains no invented price.
- Incoming quarantine, identity/counterfeit screening, function/calibration checks,
  tip/probe/fuse replacement, battery handling, repair release, consumable control,
  and known-good/student-use/quarantine/deliberate-fault segregation are specified.
  Minimal and standard bench specifications include safe current-limit/fault-energy,
  probe-compensation, grounded-scope, motor/power, cross-coupling, accessibility,
  and daily-release tests.
- Reproducible pack contracts cover a fused low-voltage cable, protected MCU I/O
  fixture, deliberate-fault DC network, enclosure/harness sample, and cable tester,
  with editable sources, provenance, travelers, seeded-defect tests, revision,
  repair, license, and technician build/inspect/repair/revise qualification criteria.
- The total-cost model includes computers, landed acquisition, facilities, calibration,
  consumables, power backup, storage, staff/technician/IT/accessibility time, spares,
  repair, replacement, partner access, risk, and disposal, plus per-student schedule
  capacity and stock-floor/reorder formulas for minimal/standard/advanced paths.
- `plan_lab_inventory.py` rejects non-approved cohort inputs by default and calculates
  quantities only when given a reviewed cohort record (or an explicit non-evidence
  scenario flag). Four unit tests cover rounding, spare/reserve/stock arithmetic,
  planning-scenario rejection, and invalid capacity. The documented 24-learner input
  remains a planning scenario and is not a Benin procurement claim.
- **Open M03-E3-T01/T02/T07 evidence:** approve the actual cohort/section/timetable;
  qualify exact MPNs and substitutes; obtain two-channel dated quotes and landed XOF
  costs; populate serviceable stock, lifecycle, lead time, staff/time, disposal, and
  access data; then approve the funded TCO and order quantities. **Owners:** laboratory
  director, procurement/finance, course owners, and timetable owner.
- **Open M03-E3-T03/T04/T05 evidence:** receive, label, segregate, inspect, function-
  check/calibrate, assemble, and physically verify the named stock and benches;
  disposition every defect and retain signed raw records. **Owners:** technician,
  safety officer, laboratory director, and metrology owner.
- **Open M03-E3-T06 evidence:** complete editable fabrication files and physical
  qualification for each pack revision, execute repeat builds and seeded-defect
  tests, and authorize named technicians from attributable performance. A pack
  contract is not a released design or human qualification. **Owners:** fixture
  engineer, technician qualification assessor, safety officer, and release manager.

### E4 — Three-path laboratory validation

- The [equipment-path pack](../../curriculum/laboratory/equipment-paths/README.md)
  defines minimal, standard, and advanced configurations for DC networks, RC
  response, sensor calibration, digital timing, and MCU debugging. Every construct
  identifies the personal physical construction, connection, configuration,
  measurement, recovery, and fault-localization evidence that prepared data cannot
  certify. Because no physical path pilot has run, T01 remains open.
- The safe MCU stimulus/acquisition artifact is a design-only 3.3 V fixture and
  fail-safe firmware contract. Five prepared CSV datasets are openly identified in
  every row as synthetic/non-personal and produced without physical apparatus; they
  support analysis continuity only. Physical construction, characterization,
  firmware implementation, independent review, and approval remain open under T02.
- Paired EN/FR operations materials provide bench maps, quick guides, troubleshooting
  cards, and issue/return controls. They use the same safety and evidence contract
  and do not turn advanced automation into a higher core threshold.
- The proposed entitlement reserves one 75-minute active-learner block for each of
  five physical constructs plus one remediation/reassessment block; it defines
  attributable pair-role rotation, accessibility, missed-evidence rescheduling,
  a failure reserve, and a capacity formula. The illustrative 24-learner calculation
  is not a deployment result, so T06 remains open until a real timetable and pilot pass.
- S2–S6 requalification specifications require current prerequisite gates, altered
  practical checks, exact task envelopes, expiry/suspension triggers, incident/
  quarantine response, and separate institutional, radio/legal, ethics, site, and
  partner approvals. No learner authorization is inferred.
- The pending-only approval record captures five-construct path results, raw ranges,
  uncertainty, completion/reset time, anomalies, physical actions, stops, access,
  capacity, technical/safety/usability/accessibility/EN/FR review, defects, limits,
  expiry, and re-pilot triggers. CSV/YAML parsing, offline QA, EN/FR review structure,
  provenance checks, and `git diff --check` pass.
- **Open M03-E4-T03/T05 evidence:** physically run all five constructs on each claimed
  path, compare uncertainty and evidence quality against one common mastery decision,
  disposition defects, rehearse EN/FR/access routes, and obtain independent safety
  and instructor-usability approval. **Owners:** laboratory lead, safety authority,
  second instructor, metrology owner, accessibility reviewer, and bilingual reviewers.
- **Open M03-E4-T06 evidence:** freeze the actual cohort/timetable/room/staff/equipment,
  pass the capacity calculation with at least 20% failure/remediation reserve, and
  confirm setup/reset and personal completion times in a physical pilot. Missed
  personal evidence is rescheduled even when prepared data preserves analysis.
  **Owners:** timetable owner, laboratory lead, course owners, and accessibility lead.

## Hands-on and real-life safeguard

Qualification uses authentic loads, sensors, noise, wiring mistakes, brownouts, temperature, and replacement parts—not only “blink.” Each reference platform must expose enough of the system for learners to measure and debug. Reject a cheaper board if undocumented behavior, fragile connectors, cloud dependency, counterfeit risk, or lack of debug makes practical learning unreliable.

## Required deliverables

- Adopted EN/FR safety manual and authorization assessments
- Qualified platform matrix, golden projects, and substitute sheets
- Costed inventory/procurement plan and functioning bench pool
- Calibration/maintenance/quarantine system
- Three-equipment-path equivalence report
- Lowest-supported computer report, locally reproducible fixture packs, and technician qualification evidence

## Exit criteria

- [ ] Staff can safely run the M04 exemplar using minimal and standard paths.
- [ ] Primary and substitute boards build, recover, and debug offline.
- [ ] Required first-year quantities plus spares are funded or a documented rotation plan preserves outcomes.
- [ ] No unresolved safety or radio/legal assumption is embedded in student work.
- [ ] Voltage is never used as the sole hazard classifier; energy-aware limits, expiry/requalification, and incident response are approved.
- [ ] Total-cost and per-student access models show that each mandatory personal practical can actually be scheduled.
