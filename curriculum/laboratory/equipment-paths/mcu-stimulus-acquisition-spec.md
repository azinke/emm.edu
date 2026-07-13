# Safe MCU stimulus/acquisition fixture specification

**Semantic ID:** M03-E4-MCU-FIXTURE-01
**Version:** 0.1.0-draft
**Artifact class:** design specification only
**Hardware/firmware status:** not built, not reviewed, not electrically tested,
not approved for learner use

The fixture is intended to expose timing and acquisition decisions on
energy-limited 3.3 V teaching circuits. It is not an instrument, calibration
reference, protective device, or substitute for an approved bench supply. Exact
board, component ratings, firmware, enclosure, and task limits must be frozen and
verified before manufacture or use.

## Functional channels

| Channel | Proposed function | Fail-safe design requirement |
|---|---|---|
| `STIM_A` | 0 V/3.3 V step or square output for RC/timing work | 1 kΩ series resistor at connector; output low during reset; no pull-up to an external rail |
| `STIM_B` | second GPIO timing marker | 1 kΩ series resistor; output low during reset |
| `CAP_A`, `CAP_B` | timer capture for 3.3 V digital edges | 10 kΩ series resistance, Schmitt input or verified threshold behavior, and clamp network whose current is bounded for the approved envelope |
| `ADC_A`, `ADC_B` | acquisition of nonnegative low-energy analog nodes | input divider/buffer chosen only after ADC limits are frozen; series resistance and bounded clamp current; test point before protection |
| `0V_REF` | signal reference | visually and tactilely distinct; never labeled protective earth |
| `DUT_PWR_SENSE` | optional observation of fixture-issued DUT rail | sense-only path; cannot back-power an externally powered DUT |

Only one power source may energize a DUT unless an approved power-OR/isolation
design prevents back-feed. The fixture must not connect to mains, high-energy
batteries, negative inputs, unknown sources, motors, relays, RF power stages, or
any node outside the approved task envelope.

## Proposed connection architecture

```text
USB isolated/approved source -> resettable current limit -> 3V3 fixture rail
                                             |
MCU GPIO -> 1 kΩ -> STIM_A ------------------+--> approved passive DUT
MCU GPIO -> 1 kΩ -> STIM_B ------------------+

approved DUT node -> bounded input network -> ADC_A / CAP_A
DUT signal reference ----------------------> 0V_REF
```

The final drawing must include connector pin numbers, net labels, polarity,
component tolerances/ratings, clamp-current calculation, maximum capacitor stored
energy, fault-current cases, creepage/clearance appropriate to the actual approved
envelope, test points, revision, and an enclosure/strain-relief design. Keyed or
shrouded connectors and a physical output-enable control are preferred. Color
must not be the sole identification method.

## Firmware behavior contract

Firmware must:

1. start with stimulus pins as inputs or driven low and require an explicit
   `ARM` command before output;
2. reject frequency, duty-cycle, amplitude-mode, sample-rate, sample-count, and
   duration requests outside a compile-time approved profile;
3. report board ID, fixture revision, firmware commit, clock source, configured
   sample interval, channel, range profile, dropped samples, overflow, reset
   cause, and data checksum with every capture;
4. use timer/DMA acquisition where available and expose timing quantization;
5. stop output on command timeout, USB loss, watchdog reset, buffer overflow, or
   invalid configuration;
6. keep stimulus and acquisition raw records in open CSV or newline-delimited
   JSON without cloud dependency;
7. include a self-test that checks firmware state and loopback timing, while
   stating that self-test does not prove analog scale, input protection, or
   external wiring safety.

Suggested command semantics are `ID?`, `PROFILE?`, `ARM`, `STIM`, `CAPTURE`,
`STOP`, and `SAFE`. This is a protocol sketch, not released firmware.

## Required verification before learner use

- Independent schematic/layout review and task risk assessment.
- Worst-case fault analysis for every pair of connector pins and every allowed
  external source; verify current, power, stored energy, temperature, and clamp
  current against approved component and institutional limits.
- Measure output levels, series resistance, reset/boot state, timeout shutdown,
  back-feed, input impedance, ADC transfer, timer clock/error, sample loss, and
  timestamp quantization on each manufactured revision.
- Compare one DC level and one interval against suitable reference instruments;
  retain raw readings and an uncertainty budget. This is a function/
  characterization check, not a calibration claim unless the full metrological
  chain is established.
- Seed invalid commands, disconnects, brownouts, reset, overflow, swapped signal
  reference, and a bounded over-range input; confirm safe state and useful error.
- Rehearse the EN and FR guides with intended users and an accessible route.
- Label each unit with configuration ID, revision, approved envelope, function-
  check due date, owner, and quarantine route.

Until all checks and approvals are recorded, the fixture configuration status is
`design-only-do-not-connect`.

SPDX-License-Identifier: CC-BY-SA-4.0
