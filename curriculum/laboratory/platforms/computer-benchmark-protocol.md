# Lowest-supported computer benchmark and support protocol

**Protocol ID:** M03-E2-COMP-001  
**Version:** 1.0.0  
**Owner:** toolchain owner  
**Approvers:** accessibility reviewer, laboratory/computing lead, course owners,
and release manager  
**Execution state:** not run

## Purpose

This protocol determines whether actual lowest-supported and refurbished computers
provide a workable offline student experience for document, KiCad, firmware,
HDL/FPGA, numerical, and embedded-Linux workflows. Marketing minimum
specifications, a virtual-machine estimate, and a successful staff workstation run
are not acceptable substitutes for a named physical-machine record.

The canonical proposed profiles currently live in
`curriculum/environments/toolchain.yml`. They remain
`requires_physical_benchmark` until completed records and the deployment report
are approved. This protocol does not report any performance result.

## Freeze before measuring

Create a benchmark plan that names:

- deployment/cohort ID; physical manufacturer/model and asset ID; refurbished
  status and repair history relevant to performance;
- CPU exact model/architecture/physical cores, RAM, storage type/capacity/free
  space/health, graphics/display, ports, battery/power state, and thermal condition;
- OS edition/version/build, firmware, filesystem, locale, encryption/antivirus
  conditions, user privilege, and accessibility configuration;
- source commit, tool/environment lock, offline bundle version/manifest checksum,
  licenses, fixture/board/probe versions, and prepared caches;
- clean/cold and ordinary/warm definitions, repetitions, timing method, memory and
  storage measurement method, expected outputs/checksums, and acceptance rules;
- repair/loan/shared-build routes, service hours, capacity, queue assumptions, and
  student data/credential handling; and
- independent operator/reviewer and any conflict with hardware/tool selection.

Predeclare workflow-specific maximum completion/interaction times, minimum free
space after install, and failure rule before running. Preserve the publication full
build targets already declared in `toolchain.yml`; do not silently relax them
after observing a slow result. Course owners set task thresholds from real contact
and assessment time, then accessibility and timetable owners approve them.

## Machine preparation

1. Function-check storage health, memory, cooling, display, keyboard/pointing and
   required USB ports. Record defects; do not tune away a representative
   refurbished-machine condition without reporting the repair.
2. Restore the declared OS image or document the existing controlled image.
   Apply only frozen updates. Record background-service and power-mode choices.
3. Install the offline bundle without network access if installation is part of
   the support promise. Hash the installed manifest and record install time, peak
   storage, warnings, restart, and privilege needs.
4. Create a non-administrator student account. Confirm keyboard-only access,
   display at the profile resolution, readable scaling, and relevant assistive-
   technology route; benchmark does not replace a full accessibility review.
5. Disable or isolate network interfaces and verify using the approved local
   method. A tool that stalls, fetches, signs in, checks a license online, or hides
   missing packages fails the offline case.
6. Reboot and settle for the predeclared interval. Record initial free storage and
   idle RAM/CPU. Do not include an unreported compiler or package cache.

## Common execution method

Run each workload at least three times when practical: one clean/cold run and two
ordinary/warm runs. If a destructive clean state is impractical, use three
equivalent imaged machines or approved snapshot/reimage procedure and document the
limitation. Randomize workload order across machines when thermal or caching order
could bias comparison.

For every step capture wall time, success/exit status, peak RAM, CPU saturation,
storage growth/free space, output size/hash, warnings/errors, application startup
and meaningful interaction latency, crash/hang/thermal throttling, and operator
interventions. Keep full logs. Check output correctness separately from speed.

An operator may repeat after a documented mistake; both records remain. A tool
failure is not deleted as an outlier without a predeclared exclusion rule and
reviewer approval.

## Workload suite

### COMP-DOC — Bilingual document workflow

From a clean source tree run canonical validation, offline QA, complete EN and FR
HTML/PDF/slides publication, smoke hooks, and output checks using the repository
commands. Open representative source, generated HTML and PDF; navigate by keyboard,
search, zoom/reflow where supported, inspect figures/tables/code, and print-preview.

Record cold/warm full-build time against the named profile target in
`toolchain.yml`, peak RAM, installed bundle and generated-output storage, failed
format targets, and visual/accessibility inspection disposition.

### COMP-KICAD — Schematic and two-layer PCB workflow

Open the frozen representative project, pan/zoom/edit a component/value and track,
run ERC/DRC, update from schematic if in scope, generate the approved manufacturing
outputs, close/reopen, and verify native source/output hashes or declared expected
differences. Use local frozen symbol/footprint/3D/model libraries with network off.

Record startup/open/save interaction, ERC/DRC and fabrication-output times, peak
RAM/storage, display/graphics defects, missing libraries/fonts/models, and whether
essential work remains usable at the lowest resolution.

### COMP-FW — Firmware build, test, program, and debug

Build clean and incremental foundation-MCU and professional-MCU golden artifacts;
run host/unit tests; report binary and memory usage; connect the frozen probe;
program/verify a known-good board; halt, inspect and resume; and perform the
approved recovery path. Run without any package/board-manager fetch.

Record compile/test/program/debug/recovery times separately, peak RAM/storage,
USB/driver/permission issues, artifact hashes, warnings, and whether attached
hardware changes the host profile result.

### COMP-HDL — HDL simulation and FPGA flow

Run self-checking HDL simulation with a detected seeded failure, then the passing
suite. Synthesize, place/route, generate timing/resource reports and bitstream for
the frozen candidate; program/verify hardware and recover the known-good image.
If a vendor flow is a fallback, benchmark it separately and include license/startup
conditions.

Record each phase, peak RAM/temp storage, waveform-viewer responsiveness, output
hashes, timing/resource result, programmer path, and any shared-build need. A
simulation-only local pass cannot be reported as a complete FPGA workflow.

### COMP-NUM — Numerical/data analysis workflow

Run the frozen script/notebook-equivalent workload from raw local data to tables
and plots: parse, validate, perform representative vector/matrix/numerical
operations, fit/analyze, and regenerate deterministic outputs. Use scripts as the
reproducible authority; any notebook is restarted and run clean.

Record cold/warm time, peak RAM/storage, numerical library versions, output hashes
or tolerance comparison, plot interaction, and whether a shared-build route would
undermine individual analysis/debug evidence.

### COMP-LINUX — Embedded-Linux image and target workflow

On the student computer, verify or build the frozen image/service as declared,
write the known-good image to replaceable media through an approved safe device-
selection method, obtain local console access, cross-compile/deploy the service,
exchange a checked message with target/MCU fixture, retrieve logs, and execute
recovery. Keep target performance separate from host-computer performance.

Record image/build/write/verify/deploy times, peak RAM/storage and temporary space,
USB/media risks, local console usability, artifact hashes, and any task assigned to
a shared build machine.

## Cross-cutting offline and storage audit

After all workloads, search logs for attempted fetch/sign-in/license calls, record
bundle installed size, peak temporary space, per-workflow outputs, log growth,
minimum free-space point, cache cleanup that is safe for learners, and space needed
for one academic period of work plus backups. Do not report only compressed
download size.

Run the declared backup/restore of a student work directory. Verify that personal
files and credentials are not copied into shared build queues or golden images.

## Loan, repair, and shared-build fallback qualification

The report names an operational route, not “ask IT”:

- loan-pool quantity, eligibility, reservation, pickup/return, charger/accessories,
  image, data wipe/backup, breakage support, turnaround, and accessible alternatives;
- local repair intake, diagnostic owner, spare/part route, target response and
  return time, temporary replacement, evidence retention, and end-of-life disposal;
- shared builder location/spec/image, supported tasks, local submission/result
  transport with intermittent internet, authentication/data isolation, queue
  capacity, expected wait at peak cohort load, hours, monitoring, failure/retry,
  artifact trace, and accessible client route; and
- an outage exercise or capacity model showing that mandatory personal work can be
  scheduled. Shared compute may accelerate synthesis/image builds, but it cannot
  replace personal editing, reasoning, measurement, programming, debugging, or
  defense evidence.

A fallback that exists only on paper is `planned`, not `qualified`.

## Decision and publication

For each profile and workflow choose `pass`, `conditional`, `fail`, or `not_run`.
All required workflows must pass for the profile to be named fully supported. A
conditional result needs a bounded task routed to a tested shared builder or a
time-limited repair/loan mitigation; it cannot hide loss of personal outcome
evidence, inaccessible essential operation, offline failure, unsafe media/hardware
handling, or unmet assessment timing.

Publish the redacted report using `computer-support-report-template.md`, naming
exact models and measured times/storage, repetitions and variation, failures,
repairs, limitations, loan/repair route, and shared-build route. Link raw records
or controlled evidence IDs. Never generalize from a different CPU name, RAM size,
virtual machine, or newer board image.

Rebenchmark on material OS, tool, bundle, firmware/driver, workflow, hardware,
storage-health, or profile change; after a repeated support incident suggesting the
threshold is unrealistic; and at least at each cohort freeze.

SPDX-License-Identifier: CC-BY-SA-4.0
