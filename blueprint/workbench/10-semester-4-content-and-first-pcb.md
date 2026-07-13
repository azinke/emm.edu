# M10 — Semester 4 Content and First PCB

**Goal:** create ESE221, ESE222, ESE223, ESE224, ESE225, PRJ202, program competence gate G6, and Student Project M4—the first repeatably realizable custom-PCB data-logger product.

**Indicative duration:** 7–10 months, beginning before M09 closes  
**Primary owners:** embedded, control, communication, power, PCB, manufacturing and lab teams  
**Depends on:** M09; M03 platform/tool qualification  
**Authoring entry:** approved M09 S3/S4 interfaces and prerequisite profile plus M03 PCB/platform qualification\
**Release gate:** applicable M09 pilot findings and the one-term-early staff PCB production flow are dispositioned\
**Exit unlocks:** M11 and advanced product work

## Epic E1 — Product thread and interface contracts

- [ ] **M10-E1-T01 [SPEC]** Define M4 power, sensing, control, communication, firmware, PCB, mechanical, test, service, and user interfaces.
- [ ] **M10-E1-T02 [SPEC]** Sequence bare-metal C, timers/ADC/buses/DMA/debug before board freeze.
- [ ] **M10-E1-T03 [SPEC]** Sequence converter/protection, grounding/EMC, communication resilience, control identification, and PCB design reviews.
- [ ] **M10-E1-T04 [SPEC]** Freeze capability contracts and two qualified board/module paths; isolate platform-specific text.
- [ ] **M10-E1-T05 [REV]** Run cross-discipline PDR on the teaching sequence and reference design.
- [ ] **M10-E1-T06 [SPEC]** Instantiate all canonical §12.2 course/unit manifests, vertical child backlogs, claim registers, equipment paths, and one-term-early staff-pilot dates.

## Epic E2 — Produce course packages

- [ ] **M10-E2-T01 [MAT]** Instantiate full ESE221, including C/ABI, GPIO, ADC/DAC, with architecture/memory map, register-level drivers, timers/PWM, interrupts, buses, DMA, low power, debug, and boot/recovery.
- [ ] **M10-E2-T02 [MAT]** Instantiate full ESE222, including transient response, root locus, discretization, with modeling, transfer functions, stability, PID/frequency/state-space design, identification, saturation, and robustness on a physical plant.
- [ ] **M10-E2-T03 [MAT]** Instantiate full ESE223, including information/signals, BER and UART/SPI/I²C, with coding/framing/modulation/noise, CAN/RS-485, networking, lawful jurisdiction-named radio operation/link budget, error handling, and privacy.
- [ ] **M10-E2-T04 [MAT]** Instantiate full ESE224, including losses, buck/boost and isolated-converter overview, with switches/magnetics, gate drive, control, thermal/protection, safe battery boundaries, solar/harvesting, and power integrity.
- [ ] **M10-E2-T05 [MAT]** Instantiate full ESE225, including footprints, with library control, schematic, stack-up, placement, returns/decoupling, SI/PI, EMC/ESD, routing, DFM/DFT, release, assembly, and bring-up.
- [ ] **M10-E2-T06 [MAT]** Produce PRJ202 review clinics and manufacturing/service handoff activities.
- [ ] **M10-E2-T07 [MAT]** Complete every applicable §13.1 paired resource, remediation path, practical/design assessment, professor note, and QA record at unit level.

## Epic E3 — PCB and manufacturing teaching system

- [ ] **M10-E3-T01 [HW]** Develop guided PCB, golden board, known-fault board, assembly variants, test fixture, and component/footprint verification samples.
- [ ] **M10-E3-T02 [TEST]** Automate/reference ERC, DRC, BOM, fabrication, position, and release checks with justified waiver handling.
- [ ] **M10-E3-T03 [MAT]** Create schematic, layout, design-freeze, unpowered inspection, rail-by-rail bring-up, rework, and release practicals.
- [ ] **M10-E3-T04 [TEST]** Complete the entire staff release-to-local-assembly/test flow at least one teaching term before student use; record batch size, observed first-pass/defect/rework results, lead time, deployment/source-currency total cost, and fixes without generalizing beyond the sample.
- [ ] **M10-E3-T05 [MAT]** Create G6 individual PCB release/bring-up specification with unseen safe variants, mastery cut, rubric, assessor calibration, stop conditions, remediation/reassessment, appeal, and retained pass evidence.
- [ ] **M10-E3-T06 [MAT]** Create the institutional V3-readiness teaching pack around Project M4's V2 product: make/buy/local-value map, approved BOM alternates, incoming/ESD inspection, assembly traveler/work instructions, serialization/traceability, checked/calibrated fixture, nonconformance/rework, sample-specific first-pass/defect results, local labor/tooling/scrap, cost, service, and contribution wording.
- [ ] **M10-E3-T07 [TEST]** Have a different local team or technician assemble and test a small controlled batch—at least three nominally identical units or an approved pooled equivalent—from the pack; resolve every process ambiguity, state the sample size, and prohibit generalized yield/process-capability claims from this exercise.

## Epic E4 — M4 resilient data logger

- [ ] **M10-E4-T01 [MAT]** Create need/SRR/PDR/CDR/TRR/release brief with imperfect supply, environment, intermittent link, calibration, repair, and cost requirements.
- [ ] **M10-E4-T02 [MAT]** Require source and power budgets, interface contracts, protection, test points, versioned firmware, board files, and verification matrix.
- [ ] **M10-E4-T03 [TEST]** Inject brownout, sensor open/short, bus lock, reversed connector, wrong footprint, packet loss, and assembly faults safely.
- [ ] **M10-E4-T04 [TEST]** Pilot long-duration logging, recovery, environmental/thermal checks, field-like communication, and another-team reproduction.
- [ ] **M10-E4-T05 [MAT]** Require service notes, approved substitutes, BOM at prototype/100-unit scale, and EN/FR user explanation.
- [ ] **M10-E4-T06 [MAT]** Maintain Project M4's V2 contribution/provenance dossier, distinguishing design, PCB layout/fabrication, firmware, enclosure/harness, assembly, test and service locations plus imported dependencies and lawful origin wording.

## Epic E5 — Pilot-ready release

- [ ] **M10-E5-T01 [REV]** Audit canonical scope, every course/unit manifest, claim register, equipment versus hardware variants, G6, Project M4 verification, local production evidence, workload, and upstream findings.
- [ ] **M10-E5-T02 [TEST]** Re-pilot all safety-, board-, power-, firmware-, accessibility-, assessment-, or process-critical corrections; verify every mandatory safe Project M4 fault/boundary in the traceability matrix.
- [ ] **M10-E5-T03 [REL]** Independent authority approves the pilot-ready S4 cohort baseline, board/process release, offline archive, known limitations, and M11/M12 handoff.

## Hands-on and real-life safeguard

Students personally release and bring up a PCB. A prebuilt module may reduce RF/assembly risk but cannot hide power, protection, connectors, testability, layout reasoning, or firmware interfaces. The system must survive every mandatory realistic power, sensor, or network fault in its approved verification matrix and recover as specified.

Every mandatory safe power, sensor, bus/network, connector/footprint, and assembly fault selected in the approved verification matrix must meet its stated detection, containment, and recovery requirement. An alternate hardware path may change components; it never waives each student's custom-PCB release and bring-up evidence.

## Required deliverables

- Approved S4/product integration contract plus six complete course/unit manifests, paired resources, and claim registers
- Guided/golden/fault PCB source and hardware, KiCad/release automation, G6 pack, and one-term-early staff evidence
- Project M4 design/verification/service pack, V2 contribution dossier, local pilot-production pack and independent small-batch reproduction report
- Signed pilot-ready EN/FR/offline teaching-material, board/process, and cohort releases

## Exit criteria

- [ ] Staff PCB revision completes full release-to-bring-up before student fabrication.
- [ ] The complete staff release-to-local-assembly/test and fixture workflow is executed and corrected at least one teaching term before learner use.
- [ ] M4 has objective manufacturing, firmware, electrical, and resilience evidence.
- [ ] G6 prevents unsafe/untraceable board release.
- [ ] All course resources and two hardware paths are reproducible offline.
- [ ] Every G6 decision is recorded per student; cohort sampling is used only for moderation.
