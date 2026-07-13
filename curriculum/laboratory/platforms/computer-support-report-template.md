# Lowest-supported computer qualification report

**Report ID:** `[M03-E2-COMP-REPORT-DEPLOYMENT-DATE]`  
**Protocol:** M03-E2-COMP-001 v1.0.0  
**Deployment/cohort:** `[pending]`  
**Status:** not run / draft / reviewed / approved  
**Evidence cutoff:** `[YYYY-MM-DD]`  
**Owners and approvers:** `[roles/names or controlled approval record]`

> This blank report contains no benchmark result. Replace every `pending` with
> measured evidence or an explicit unknown. Do not call a profile supported while
> any required workflow remains `not_run`, failed, or lacks independent review.

## Decision summary

| Physical computer profile and exact models | Document | KiCad | Firmware | HDL/FPGA | Numerical | Embedded Linux | Overall |
|---|---|---|---|---|---|---|---|
| `[pending]` | not run | not run | not run | not run | not run | not run | not evaluated |

State the supported/refurbished decision, named cohort, limitations, tasks sent to
a shared builder, and why personal outcome evidence remains intact.

## Frozen environment and method

Record source commit/tag, toolchain lock, offline-bundle version and SHA-256,
installation method, network-unavailable verification, cold/warm definitions,
repetitions, timing/RAM/storage/thermal methods, predeclared acceptance thresholds,
excluded runs, operator, and independent reviewer. Link each
`computer-benchmark-record-template.yml` instance and raw-evidence directory or
controlled ID.

## Machine inventory and condition

| Record ID | Manufacturer/model | Asset reference | Refurbished/repair state | Exact CPU/cores | RAM | Storage/type/health/free | OS/build | Display | Ports/power/thermal notes |
|---|---|---|---|---|---|---|---|---|---|
| `[pending]` | `[pending]` | `[controlled]` | `[pending]` | `[pending]` | `[pending]` | `[pending]` | `[pending]` | `[pending]` | `[pending]` |

Explain sampling limits. Results apply only to the configurations named.

## Offline installation and storage

| Machine record | Install time | Installed bundle | Peak temporary space | Minimum free space | Outputs/log/cache | Period-work + backup need | Fetch/sign-in events |
|---|---:|---:|---:|---:|---:|---:|---|
| `[pending]` | — | — | — | — | — | — | not run |

Record restart/admin requirements, missing packages/licenses/fonts/libraries,
student-work backup/restore, safe cache cleanup, and limitation. Sizes use bytes
or clearly labeled binary units consistently.

## COMP-DOC — Bilingual publications

Report cold and warm full-build times, variation, peak RAM, output bytes/hashes,
EN/FR HTML/PDF/slides/QA/smoke/output-check results, source/generated navigation,
print/visual inspection, keyboard route, and any target comparison from
`toolchain.yml`.

## COMP-KICAD — Schematic and PCB

Report project/open/edit/save, ERC/DRC, fabrication-output times, peak RAM/storage,
local-library integrity, output correctness, display/graphics/interaction behavior,
and defects. Identify project/fixture version without claiming the PCB was
fabricated or electrically validated.

## COMP-FW — Firmware and debug

Report clean/incremental compile, tests, program/verify, debug, bad-image recovery,
peak RAM/storage, driver/permission behavior, exact board/probe/firmware, artifact
hashes, and anomalies. Separate host performance from physical-board qualification.

## COMP-HDL — Simulation and FPGA

Report seeded-failure detection, passing simulations, synthesis/place/route,
timing/resource/bitstream phases, waveform interaction, program/verify/recovery,
peak RAM/temp storage, exact FPGA flow/device/probe, and any vendor-license or
shared-build limitation.

## COMP-NUM — Numerical/data workflow

Report clean script/notebook-equivalent run, library versions, input/output hashes
or numerical tolerance check, plot interaction, time, peak RAM/storage, and
whether every learner can personally inspect, change, rerun, and defend analysis.

## COMP-LINUX — Image, target, and service

Report image/build/write/verify/deploy/recovery phases, peak RAM/temp storage,
safe-media selection, local console/logs, exact target/MCU fixture, artifact hashes,
and anomalies. Keep host-computer and target performance separate.

## Interaction and accessibility findings

Describe startup/response latency at the frozen resolution, keyboard use,
scaling/readability, assistive-technology route tested, time/accommodation impacts,
and unresolved barriers. This section supplements rather than replaces full WCAG
and outcome-equivalence review.

## Loan path

Name owner, quantity/capacity model, eligibility, reservation, pickup/return,
charger/accessories, frozen image, data backup/wipe, breakage help, turnaround,
temporary replacement, accessible alternative, and evidence that demand can be
served. Status: planned / exercised / qualified.

## Repair path

Name intake route, diagnostic/repair roles, spare source, expected response/return,
temporary loan, data protection, evidence retained, end-of-life route, and at
least one exercise record. Status: planned / exercised / qualified.

## Shared-build fallback

Name location/spec/image, permitted tasks, local submission/result transport,
authentication/data isolation, queue capacity and peak wait, hours/monitoring,
failure/retry, output trace, outage/capacity exercise, accessible client, and
owner. List the personal actions that remain local. Status: planned / exercised /
qualified.

## Defects, repairs, anomalies, and limitations

| ID | Observation | Affected machine/workflow | Evidence | Impact | Repair/mitigation | Retest | Owner/due | Status |
|---|---|---|---|---|---|---|---|---|
| `[pending]` | `[pending]` | `[pending]` | `[pending]` | `[pending]` | `[pending]` | not run | `[pending]` | open |

## Approval and rebenchmark triggers

Record each workflow disposition and signatures/dates for toolchain,
accessibility, laboratory/computing, affected courses, and release. State review
due plus event triggers: OS/tool/bundle/firmware/driver/workflow/hardware/storage
change, repeated support incident, or cohort freeze. Link the release/freeze
record; this report alone does not purchase equipment or approve a cohort.

SPDX-License-Identifier: CC-BY-SA-4.0
