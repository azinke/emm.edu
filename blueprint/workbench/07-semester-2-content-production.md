# M07 — Semester 2 Content Production

**Goal:** create the coordinated S2 package for MAT102, PHY102, ESE121, ESE122, CSC102, DES102, program competence gates G3 and G4, and Student Project M2.

**Indicative duration:** 5–7 months  
**Primary owners:** S2 course team and Year-1 integration lead  
**Depends on:** approved M06 interfaces; exemplar production system  
**Authoring entry:** named M06 S1 interface baseline—outcomes, gates, notation, data, platforms, workload, and remediation—is approved\
**Release gate:** the approved S1→S2 prerequisite contract and applicable M06/M05 prerelease defects are dispositioned; actual S1 learner evidence is checked at the M08 S2 go/no-go\
**Exit unlocks:** M08 and M09

## Epic E1 — Sequence dynamics, devices, and C

- [ ] **M07-E1-T01 [SPEC]** Coordinate complex numbers/ODEs with RC/RL/RLC, phasors, filters, semiconductor behavior, and waveform measurement.
- [ ] **M07-E1-T02 [SPEC]** Coordinate fields/material physics with capacitance, induction, devices, thermal limits, and safe component selection.
- [ ] **M07-E1-T03 [SPEC]** Place C types, bitwise work, memory, modularity, tests, and debugger practice before embedded prerequisites.
- [ ] **M07-E1-T04 [SPEC]** Thread stakeholder, repairability, accessibility, lifecycle, cost, and requirements work into M2 rather than isolate it in DES102.
- [ ] **M07-E1-T05 [REV]** Review workload, terminology, notation, and S1 remediation dependencies.
- [ ] **M07-E1-T06 [SPEC]** Instantiate the six named S2 course/unit manifests—MAT102, PHY102, ESE121, ESE122, CSC102, and DES102—and their child backlogs; preserve canonical scope or approve an explicit outcome/dependency disposition.

## Epic E2 — Produce six complete course packages

- [ ] **M07-E2-T01 [MAT]** Produce MAT102 with measured transient and sinusoidal examples, linear algebra, ODEs, and numerical checks.
- [ ] **M07-E2-T02 [MAT]** Produce PHY102 with field, wave, material, semiconductor, and thermal/electrical experiments.
- [ ] **M07-E2-T03 [MAT]** Instantiate the full ESE121 contract, including transformer/coupling and Fourier/sampling preview, with capacitors/inductors, transient/frequency models, AC power, resonance, filters, and nonidealities.
- [ ] **M07-E2-T04 [MAT]** Instantiate the full ESE122 contract, including the op-amp preview, with diode protection, BJT/MOSFET switch/amplifier operation, bias, thermal/SOA, and datasheet decisions.
- [ ] **M07-E2-T05 [MAT]** Instantiate the full CSC102 contract with Boolean/truth-table foundations, defensive C, data structures, memory/bit operations, modular builds, unit tests, debugger work, and a scaffolded provided-driver MCU practical; register-level embedded design remains in ESE221.
- [ ] **M07-E2-T06 [MAT]** Produce DES102 with observed needs, measurable requirements, accessible prototypes, repair/lifecycle, local sourcing, economics, and verification.
- [ ] **M07-E2-T07 [MAT]** Complete paired chapters, notes, slides, labs/explorations, psets, solutions, MCQs, practicals, and QA records.
- [ ] **M07-E2-T08 [REV]** Complete unit claim/source registers and independent calculation/code/physical/context checks before staff pilot.

## Epic E3 — Laboratory and competence gates

- [ ] **M07-E3-T01 [TEST]** Pilot the required ESE121 circuit experiments plus the required ESE122 device experiments—at least nine across the coordinated set—including scope/probe errors, component tolerance, clipping, heating, and seeded faults; retain each course's declared practical evidence.
- [ ] **M07-E3-T02 [MAT]** Create individual “switch versus amplifier” and filter/transient design practicals.
- [ ] **M07-E3-T03 [MAT]** Create G3 solder/rework specification using inspectable through-hole and accessible hand-solderable SMD practice, with package/inspection criteria, safe variants, mastery cut, accessible route, remediation and reassessment.
- [ ] **M07-E3-T04 [MAT]** Create G4 C/source-control specification with compile, test, debugger, change, commit, and explanation tasks plus unseen variants, mastery cut, assessor calibration, remediation/reassessment and evidence retention.
- [ ] **M07-E3-T05 [TEST]** Calibrate assessors and verify safe equipment pathways.

## Epic E4 — M2 calibrated environmental monitor

- [ ] **M07-E4-T01 [SPEC]** Select a context where calibration, enclosure, drift, and user interpretation matter; avoid uncritical DHT11/resistive-soil-probe demos.
- [ ] **M07-E4-T02 [MAT]** Require an analog interface, protected logic/load drive, scaffolded MCU-C implementation using provided drivers/HAL, two-variable measurement, calibration reference and uncertainty chain, logging/display, and requirements trace; do not assess untaught register-level embedded skills.
- [ ] **M07-E4-T03 [HW]** Build variants with known sensor and component differences; characterize reference ranges and environmental limitations.
- [ ] **M07-E4-T04 [MAT]** Add seeded sensor-open, aliasing/noise, wrong transistor, and power faults with a debugging decision tree.
- [ ] **M07-E4-T05 [TEST]** Pilot user test, calibration, repairability, cost, and individual oral/practical defense.
- [ ] **M07-E4-T06 [MAT]** Set Project M2's V1 target and contribution/provenance dossier: interface/enclosure/harness and calibration work, locally feasible assembly/service steps, local/imported dependencies, deployment-currency cost, make/buy/substitutes, repair, and bounded origin wording.

## Epic E5 — Pilot-ready release

- [ ] **M07-E5-T01 [REV]** Audit every unit manifest, canonical scope, workload, EN/FR/accessibility facet, claim register, apparatus path, gate pack, Project M2 evidence, and open defect.
- [ ] **M07-E5-T02 [TEST]** Complete second-instructor and representative learner rehearsal plus one-term-early staff pilots of every physical/project activity; re-pilot material corrections.
- [ ] **M07-E5-T03 [REL]** Independent authority approves the pilot-ready S2 cohort baseline, offline archive, known limitations, and M08/M09 interface handoff.

## Hands-on and real-life safeguard

Students must use devices beyond ideal symbolic behavior: actual forward drop, threshold/gate-drive suitability, saturation/headroom, tolerance, thermal response, sensor drift, and sampling artifacts. M2 must include a decision where a cheaper or simpler sensor loses against calibration, durability, or maintenance evidence—or wins with explicitly bounded limitations.

## Required deliverables

- Approved S2 integration contract plus six complete course/unit manifests, claim registers, and paired packages
- Physical lab/equipment-path evidence and G3/G4 examiner, remediation, reassessment, and retention packs
- Project M2 brief, calibration/uncertainty and fault evidence, V1 contribution dossier, user/service and individual-defense pack
- Staff/second-instructor/representative-learner pilot evidence and signed pilot-ready EN/FR/offline release

## Exit criteria

- [ ] All S2 packages meet resource and parity definitions.
- [ ] G3/G4 assessments are safe, reliable, and individually administered.
- [ ] M2 closes the Year-1 observe–model–build loop with verified performance.
- [ ] ESE211/ESE212/ESE221 prerequisite evidence is explicit.
- [ ] MCU C in Project M2 is bounded to taught CSC102 skills and provided drivers; ESE221 does not inherit a hidden register-level prerequisite.
