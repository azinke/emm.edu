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
- [ ] **M03-E4-T04 [MAT]** Create bench setup maps, equipment quick guides, troubleshooting cards, and check-in/out procedure.
- [ ] **M03-E4-T05 [REV]** Obtain safety and instructor usability approval.
- [ ] **M03-E4-T06 [TEST]** Set and test minimum per-student physical-access entitlement; prepared data can preserve an analysis lesson but missed personal construction/measurement/debug evidence is rescheduled.
- [ ] **M03-E4-T07 [SPEC]** Define later safety requalification prerequisites for S2 device/soldering, S3 precision/FPGA, S4 PCB/power, S5 RF/security, and S6 field activities.

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
