# Cross-platform golden-project qualification specification

**Specification ID:** M03-E2-GOLDEN-001  
**Version:** 1.0.0  
**Owner:** platform engineering lead  
**Safety authority:** laboratory safety officer  
**Review:** every environment, board/tool revision, fixture, driver, or test change

## Intent

The golden project is a small set of inspectable tests used to decide whether an
exact primary or substitute platform can support planned teaching actions. It is
not one “blink” demonstration and it does not replace later course laboratories.
The same test IDs and evidence rules are applied to every candidate; adapters may
change, but the outcome and decision threshold may not.

Passing simulation proves only the design-side behavior covered by that
simulation. Every board qualification requires physical execution on the named
sample, and every offline claim requires a clean run with networking disabled or
isolated after bundle installation.

## Safety and configuration prerequisites

- Approved abstraction sheet identifies exact board revision, pin map, voltage
  and current limits, reset state, backfeed paths, boot/recovery, and errata.
- A safety reviewer approves the fixture calculation, current limit, leads,
  instrument/probe ratings, setup sequence, stop conditions, and accessible
  temperature/energy scope.
- The operator predicts the de-energized and energized safe state before wiring.
- Connections change only while de-energized unless the approved method explicitly
  requires and controls live work.
- Wireless transmission is disabled unless an exact configuration has dated
  jurisdiction and facility approval.
- Reusable boards may not receive permanent debug locks, secure-boot roots,
  one-time fuses, anti-rollback counters, destructive keys, or other irreversible
  security/configuration state.

## Required evidence package

Retain source commit, test/fixture/environment versions, offline bundle checksum,
candidate and sample asset IDs, board abstraction sheet ID, programmer/probe,
host profile, commands and complete logs, binary/bitstream/image hashes, build
times and resource reports, setup/wiring evidence, predicted values/bounds, raw
measurements with instrument resolution/uncertainty, anomalies, recovery attempts,
and independent review. Use `evidence-record-template.yml`.

No test passes from a screenshot alone. A retest retains the original failure and
links the correction; do not overwrite contrary evidence.

## Common test sequence

### GP-00 — Identity, source, and offline environment

**Applies to:** all categories.

Verify the received item against manufacturer part number, board/tool revision,
silicon/package where relevant, schematic and errata. Verify source and dependency
hashes, licenses, host identity, environment lock, USB driver/probe firmware, and
offline bundle manifest. Disable or isolate network interfaces before the cold
build and retain how this was verified.

**Pass:** identity has no unresolved ambiguity; every input needed for applicable
tests is archived and license-usable; commands do not fetch; the evidence record
can reproduce the configuration. An unresolved clone/revision or undeclared
network access fails the test.

### GP-01 — Boot, programming, and recovery

**Applies to:** all boards/targets; programmer self-recovery is separately checked
for probe/programmer candidates.

Record normal boot. Load a known-good minimal artifact, then a deliberately
non-working but electrically safe artifact. Exercise documented bad-image
recovery. Where the documented method and fixture safely permit, simulate an
interrupted program operation and recover using the normal staff route. Restore
the known-good artifact and verify its hash/readback or functional signature.

**Pass:** each declared recovery route is repeatable, documented, offline, and
reversible; no permanent state or undocumented vendor service is required. One
operator mistake may be diagnosed and corrected, but the final record must retain
it.

### GP-02 — GPIO visibility, direction, and safe fault

**Applies to:** MCU, wireless, FPGA, and protected embedded-Linux GPIO.

Use the approved current-limited loopback fixture. Verify reset state before the
student artifact takes control. Drive a low-rate deterministic pattern, observe it
with an independent instrument/input, read a loopback, and exercise input pulls.
Introduce only the fixture-declared safe open connection or swapped logical
mapping; locate it from symptoms without exceeding drive or bank limits.

**Pass:** levels and timing remain within precomputed bounds; reset state and pulls
match the abstraction sheet; the safe fault is localized; output contention,
backfeed, and incompatible domains are absent. GPIO counts only if learners can
inspect mapping and behavior rather than call an unexamined service.

### GP-03 — ADC acquisition and evidence

**Applies to:** foundation/professional MCU and any wireless board whose ADC is
used for assessed work. Not required for FPGA/Linux when an external qualified
measurement bridge is the declared route.

Apply at least three safe, independently measured input levels spanning the
approved teaching range using the board-specific source network. Include repeated
samples, reference/range configuration, acquisition timing/source-impedance check,
raw codes, physical input measurement, and an expected quantization/uncertainty
bound. Include one recognized saturation or out-of-range-near-boundary case only
within recommended operating conditions.

**Pass:** monotonic ordering and conversion relation match predeclared bounds;
repeatability and bias are reported honestly; reference, resolution, scaling, and
source effects are visible. Typical single-unit behavior is not relabeled as a
guaranteed board specification.

### GP-04 — Timer, PWM, capture, and clock evidence

**Applies to:** MCU/wireless/FPGA; Linux only through its declared MCU/FPGA bridge
when deterministic timing is an outcome.

Generate at least two periods and duty cycles derived from an explicit clock and
divider model. Measure period, high/low time, edge behavior, and update behavior
with an independent instrument or qualified capture input. Where available, close
the loop through capture/compare and compare reported and independent results.

**Pass:** frequency/duty error is within predeclared clock, quantization,
instrument, and configuration bounds; resource and pin conflicts are recorded;
learners can trace the result to clock/timer/RTL decisions.

### GP-05 — UART and serial buses

**Applies to:** all board categories, using only interfaces required by the
capability contract.

Run framed UART loopback with error detection and one invalid-frame case. Exercise
SPI and I2C (or the approved equivalent required by the category) against a known
fixture/target, reading an identity register or deterministic fixture response and
performing a reversible write/readback where safe. Capture logic timing and check
voltage domain, pullups, mode, bit order, rate, addressing, and bus-idle state.

**Pass:** expected transactions and invalid-case diagnosis are reproducible;
captured timing/protocol agrees with configuration; bus contention, missing
pullups, and pin-map errors can be distinguished.

### GP-06 — Hardware debug and probe/programmer behavior

**Applies to:** MCU/wireless boards with declared wired debug and all applicable
probe/programmer candidates. FPGA uses GP-10 programming/observability; Linux uses
GP-11 console/service diagnosis.

Connect only after target-voltage and orientation checks. Demonstrate halt, source
or instruction step, hardware/software breakpoint as supported, register and
memory inspection, controlled variable modification, reset, and recovery under
reset. Verify that target powering and probe powering cannot contend. Record any
breakpoint, trace, low-power, optimization, or RTOS limitation.

**Pass:** all contract-required operations work offline on the exact target; probe
voltage behavior is safe; a wedged application is recoverable; debug visibility is
adequate for planned fault-localization evidence.

### GP-07 — Power, reset, brownout, and ordinary robustness

**Applies to:** all boards/targets; values and perturbations are candidate-specific.

With an approved current-limited source or USB measurement arrangement, record
off, boot, idle, and representative-load current under defined conditions. Verify
reset and power-cycle behavior. Exercise only a preapproved benign supply ramp or
brownout case inside the fixture and manufacturer operating/survival constraints;
then verify recovery and storage/configuration integrity. Observe accessible
temperature where material.

**Pass:** no backfeed, unexpected powering, unsafe heating, corrupted persistent
state, or recovery failure occurs; measured bounds and limitations support the
planned bench/access model. This is a classroom robustness screen, not compliance
or reliability certification.

### GP-08 — Clean offline build and artifact trace

**Applies to:** all categories.

From a clean user profile/cache state in each required lowest-supported host
profile, with networking unavailable, build all applicable golden artifacts,
program/configure the target, start the debugger or local diagnostic route, and
run automated host/simulation tests. Record cold/warm time, peak memory when the
benchmark protocol requires it, output hash/size, warnings, licenses, and any
shared-build dependency.

**Pass:** no fetch or account occurs; build/test/program/debug steps succeed from
archived inputs; warnings meet the frozen policy; generated artifacts trace to
source and environment. A pass on a staff workstation does not qualify a lowest-
supported host.

### GP-09 — Radio disabled state and approved wireless behavior

**Applies to:** wireless candidates.

First verify a non-transmitting default/off state. If and only if dated local
approval identifies band, region, firmware, configured power, antenna, facility,
and test method, run the bounded telemetry/security/power cases and retain the
approval ID. Test recovery from malformed local configuration without exposing
real credentials or uncontrolled networks.

**Pass:** disabled state is demonstrable and does not depend on an undocumented
cloud service. The active-radio portion passes only with approval and raw evidence;
otherwise record `blocked-jurisdiction`, never `pass`.

### GP-10 — FPGA simulation, synthesis, timing, configuration, and recovery

**Applies to:** FPGA candidates.

Run self-checking RTL tests including at least one injected failing vector, then
synthesize/place/route with explicit device/package, pin, clock, and I/O
constraints. Review warnings, utilization, and timing. Program volatile and/or
nonvolatile configuration as declared, verify measured GPIO/timer/bus behavior,
load a safe invalid/non-working design, and recover the known-good image.

**Pass:** tests detect the seeded failure; approved design tests pass; every
external pin/clock is constrained; timing and predeclared resource headroom pass;
physical behavior agrees with the model; recovery does not depend on permanent
state or online tooling.

### GP-11 — Embedded-Linux image, service, device link, and recovery

**Applies to:** embedded-Linux candidates.

Verify image and package hashes, provision replaceable storage, boot without
internet, obtain local console/log access, run the golden service, exchange a
versioned/error-checked message with the MCU or deterministic fixture, exercise a
service/process/network-unavailable failure, and restore a known-good image and
configuration backup. Record RAM, storage, startup, and thermal/power observations
under declared load.

**Pass:** boot/service/device path and diagnosis are reproducible offline; no real
credential is embedded; update/recovery and storage replacement are documented;
resource headroom and shared-access timing satisfy predeclared cohort thresholds.

## Category applicability matrix

| Test | Foundation MCU | Professional MCU | Wireless | FPGA | Embedded Linux | Probe/programmer |
|---|:---:|:---:|:---:|:---:|:---:|:---:|
| GP-00 | R | R | R | R | R | R |
| GP-01 | R | R | R | R | R | R |
| GP-02 | R | R | R | R | R* | — |
| GP-03 | R | R | C | — | — | — |
| GP-04 | R | R | R | R | C* | — |
| GP-05 | R | R | R | R | R | — |
| GP-06 | R | R | R | — | — | R |
| GP-07 | R | R | R | R | R | C |
| GP-08 | R | R | R | R | R | R |
| GP-09 | — | — | R | — | — | — |
| GP-10 | — | — | — | R | — | C |
| GP-11 | — | — | — | — | R | — |

`R` is required; `C` is required when the capability is claimed or used; `*`
uses the approved protected or deterministic bridge. A test may be marked not
applicable only with contract trace and reviewer approval.

## Qualification decision rule

Every required test must be `pass`; `blocked`, `not_run`, `inconclusive`, or a
missing raw record cannot qualify a candidate. A conditional qualification is
allowed only for a bounded non-safety capability not used by the named courses,
with explicit content/assessment disposition, owner, expiry, and substitute. A
safety, electrical, recovery, offline, identity, irreversible-state, or required-
learning-action defect is not conditionally waivable.

SPDX-License-Identifier: CC-BY-SA-4.0
