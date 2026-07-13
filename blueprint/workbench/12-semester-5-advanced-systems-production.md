# M12 — Semester 5 Advanced Systems Production

**Goal:** create ESE311, ESE312, ESE313, ESE314, ESE315, PRJ301, program competence gate G7, and secure connected-node Student Project M5.

**Indicative duration:** 8–10 months  
**Primary owners:** RTOS/security, FPGA/architecture, mixed-signal, RF, reliability teams  
**Depends on:** M10; incorporate M11 evidence before release  
**Authoring entry:** approved M10 S4/S5 interface and prerequisite profile plus candidate advanced-tool capability contracts; qualification in E1 precedes dependent course drafting and all physical work\
**Release gate:** applicable M11 findings and supported prerequisite assumptions are dispositioned\
**Exit unlocks:** M13 field-system integration

## Epic E1 — Advanced system contract

- [ ] **M12-E1-T01 [SPEC]** Define shared node timing, power, sensing, communication, programmable-logic, security, reliability, and test requirements; include only technologies justified by Project M5 requirements.
- [ ] **M12-E1-T02 [SPEC]** Freeze a named supported Zephyr release or approved capability-equivalent RTOS, compiler/debug, FPGA simulation/synthesis, RISC-V architecture model, radio, and data-conversion toolchains with offline bundles and migration contracts.
- [ ] **M12-E1-T03 [TEST]** Create golden builds and substitute-platform smoke tests; document migration boundaries.
- [ ] **M12-E1-T04 [SPEC]** Define threat, named-jurisdiction RF authorization/limits, key-handling, security-board reuse, and safe fault-injection constraints.
- [ ] **M12-E1-T05 [SPEC]** Instantiate every canonical §12.2 course/unit manifest, claim register, vertical child backlog, minimal/standard apparatus, hardware variant, context-profile binding, and one-term-early staff-pilot date.

## Epic E2 — Produce course packages

- [ ] **M12-E2-T01 [MAT]** Instantiate full ESE311, including real-time concepts, tasks/threads and synchronization, with scheduling, concurrency, races/deadlocks, IPC, drivers/device tree, memory, networking, secure boot/update, observability, and HIL.
- [ ] **M12-E2-T02 [MAT]** Instantiate full ESE312, including buses/peripherals and caches, with ISA/datapath, assembly, pipeline/hazards, memory hierarchy, privilege/interrupts, RISC-V architecture/RTL, formal/self-checking verification, FPGA implementation/timing, and acceleration.
- [ ] **M12-E2-T03 [MAT]** Instantiate full ESE313, including sampling circuits and isolation, with ADC/DAC architectures, references, jitter, quantization/noise/distortion, aliasing, grounding, calibration, and mixed-signal layout.
- [ ] **M12-E2-T04 [MAT]** Instantiate full ESE314, including EM review, with transmission lines, S-parameters, matching, RF blocks/noise, antennas, propagation, modulation, link budget, SDR, coexistence, regulation, and test.
- [ ] **M12-E2-T05 [MAT]** Instantiate full ESE315, including probability/confidence and reliability models, with DOE, capability, derating, FMEA/FMECA, accelerated tests, fault coverage, production test, and quality/change control.
- [ ] **M12-E2-T06 [MAT]** Produce PRJ301 sprint, architecture/threat/reliability reviews, design history, and retrospectives.
- [ ] **M12-E2-T07 [MAT]** Complete every applicable §13.1 paired resource, professor note, remediation path, practical/design assessment, and QA record at unit level.

## Epic E3 — Verification-rich laboratories and G7

- [ ] **M12-E3-T01 [TEST]** Pilot RTOS race/deadline/brownout/update cases with traces and recovery.
- [ ] **M12-E3-T02 [TEST]** Pilot RISC-V architecture/RTL and FPGA simulation, assertions/formal properties, synthesis, explicit clock/reset/CDC assumptions, constraints, timing reports/closure, and physical I/O evidence.
- [ ] **M12-E3-T03 [TEST]** Pilot converter error/noise budget, engineering link tests conducted within the recorded named-jurisdiction authorization, DOE/reliability, and production-test fixture.
- [ ] **M12-E3-T04 [MAT]** Create G7 individual embedded timing/concurrency debug specification with an unseen live fault or recorded trace variant, rubric, mastery cut, safe equivalents, assessor calibration, remediation/reassessment, appeal, and retained evidence.
- [ ] **M12-E3-T05 [REV]** Confirm no cloud account, irreversible eFuse, unauthorized radio transmission, or FPGA result without declared clock/reset/CDC constraints, timing report, and physical evidence is required.
- [ ] **M12-E3-T06 [TEST]** Staff-pilot every radio, security, converter, FPGA, reliability, and hardware activity at least one teaching term before learner use, not only Project M5.

## Epic E4 — M5 secure connected node

- [ ] **M12-E4-T01 [MAT]** Require authenticated communication, RTOS, power management, converter chain, a programmable-logic element, threat model, reliability plan, and costed architecture.
- [ ] **M12-E4-T02 [TEST]** Test sensor boundaries, deadline overload, lost/corrupt packets, network absence, unauthenticated/replay attempts, unauthorized update, rollback prevention/recovery, key rotation, power interruption during update, long-duration operation, and decommission behavior.
- [ ] **M12-E4-T03 [MAT]** Require controlled release tag—with cryptographic signing only when specified—SBOM, hardware BOM, secrets policy, recovery, credential destruction/decommission, raw test evidence, and limitations.
- [ ] **M12-E4-T04 [TEST]** Build and qualify staff alpha one term early; validate alternate radio/offline path.
- [ ] **M12-E4-T05 [REV]** Conduct architecture, threat, test-readiness, and alpha qualification reviews.
- [ ] **M12-E4-T06 [MAT]** Set Project M5's V2→V3 target and contribution dossier with dated deployment-profile heat/power/connectivity/cost/supply requirements, local/imported security/manufacturing/service boundaries, and capability gaps.

## Epic E5 — Pilot-ready release

- [ ] **M12-E5-T01 [REV]** Audit canonical scope, every unit/resource manifest, claim register, apparatus/hardware paths, G7, Project M5 assurance/local-value evidence, workload, and M11 findings disposition.
- [ ] **M12-E5-T02 [TEST]** Re-pilot every materially corrected safety/security/radio/hardware/assessment/accessibility activity.
- [ ] **M12-E5-T03 [REL]** Independent authority approves the pilot-ready S5 cohort baseline, named supported toolchain/offline bundle, known limitations, and M13/M14 handoff.

## Hands-on and real-life safeguard

Students must see concurrency, timing, RF, conversion, and reliability in traces and measurements. A security checklist without a tested recovery/failure case is insufficient. FPGA work begins with executable verification; a vendor-GUI screenshot is not evidence.

## Required deliverables

- Approved S5 system contract plus six complete course/unit manifests, paired packages, claims, and frozen offline toolchains
- Staff-piloted advanced labs and G7 examiner/remediation/reassessment pack
- Project M5 alpha, threat/assurance/verification and V2→V3 contribution dossier with recovery/decommission evidence
- Signed pilot-ready EN/FR/offline release and M11-findings disposition

## Exit criteria

- [ ] Toolchains and golden projects run offline on supported machines.
- [ ] M5 survives defined communication, power, timing, and update faults.
- [ ] G7 measures individual reasoning under an unseen live real-time fault or an equivalent recorded-trace variant.
- [ ] Every technical claim is traced to calculation, simulation, test, or bounded source.
- [ ] Every G7 decision is recorded per student; external/aggregate sampling only moderates the gate system.
