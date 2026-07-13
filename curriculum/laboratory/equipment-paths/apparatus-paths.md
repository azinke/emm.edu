# Apparatus contracts for five core phenomena

**Semantic ID:** M03-E4-APPARATUS-01
**Version:** 0.1.0-draft
**Validation state:** not physically piloted; all capability values are design
requirements to verify, not claims about stocked equipment

## Invariant evidence contract

For every path, the learner must predict before energizing, inspect the setup,
calculate the task's fault-energy/current limit, configure the acquisition,
retain raw readings and settings, state an uncertainty contribution, diagnose an
assigned anomaly, and make the same acceptance decision. The instructor records
apparatus identity and function-check status. Prepared data never replaces the
actions marked **personal physical evidence**.

### DC networks

**Core question:** Does a loaded resistor network meet its specified output and
power limits, and which fault best explains an out-of-range node?

| Path | Apparatus definition | Same required learner evidence | Path boundary |
|---|---|---|---|
| Minimal | Current-limited, approved extra-low-voltage source; fused DMM with known input resistance and resolution; breadboard; 1% resistors; optional continuity tester | Personally construct and inspect the network; choose reference node/range/test points; measure source and at least three nodes; calculate loading and resistor power; locate one open, wrong-value, or misplaced connection | No current-input use unless separately qualified. Select circuit values so meter resolution and input loading permit the common uncertainty target. |
| Standard | Bench supply with visible V/I and current limit; two DMMs or DMM plus oscilloscope for static checks | Same core evidence; record supply limit and observed current; independently verify one node with a second channel | Scope protective-earth constraints must be briefed before connection. A screenshot alone is not evidence. |
| Advanced | Programmable source/DMM or source-measure capability with independently checked leads and limits | Same core evidence; an automated sweep may add repeatability/linearity analysis | Automation cannot choose nodes, inspect wiring, explain loading, or diagnose for the learner. |

**Physical access required:** construction, pre-energization check, instrument
connection/ranging, personal readings, and fault localization.

### RC response

**Core question:** Does a first-order RC network agree with its predicted time
constant within a declared uncertainty, including source and input loading?

| Path | Apparatus definition | Same required learner evidence | Path boundary |
|---|---|---|---|
| Minimal | DMM for static checks; characterized MCU stimulus/acquisition fixture; breadboard; 1% resistor and characterized capacitor | Personally construct; choose acquisition interval and duration; acquire charge/discharge samples; fit or estimate `tau`; account for source/input loading; diagnose a wrong capacitor or acquisition-rate fault | Use at least 20 sample intervals per predicted `tau` and observe at least 5 predicted `tau`. If the fixture cannot meet this after values are redesigned, this path is not eligible. |
| Standard | Bench generator and two-channel oscilloscope with function-checked, compensated probes | Same core evidence; choose amplitude, offset, coupling, timebase, trigger and probe point; export recoverable samples/settings | Grounded-scope connection must stay inside the approved isolated extra-low-voltage setup. |
| Advanced | Automated oscilloscope sweep or frequency-response instrument with fixture/reference-plane check | Same core evidence plus optional dense frequency or parasitic analysis | The learner must independently validate an automated result against a raw time-domain or point measurement. |

**Physical access required:** construction, static safety checks, instrument/probe
choice and connection, acquisition, and physical anomaly diagnosis.

### Sensor calibration

**Core question:** What calibration model and uncertainty statement are justified
for a low-voltage sensor over the declared teaching range?

| Path | Apparatus definition | Same required learner evidence | Path boundary |
|---|---|---|---|
| Minimal | Approved low-voltage sensor, MCU ADC or DMM, and at least five staff-prepared comparison states with a traceable reference record | Personally wire and read the sensor at five or more randomized states; retain repeats; choose a model; inspect residuals; identify a swapped-point or saturation anomaly | Comparison states must not use a person as a research participant. Reference uncertainty must be small enough for the common decision threshold; otherwise narrow the claim. |
| Standard | Bench DMM/data acquisition plus controlled source or environmental fixture and recorded reference instrument | Same core evidence with instrument configuration and repeat observations | More digits do not justify an unsupported calibration claim. |
| Advanced | Calibrated reference chain and automated multi-point fixture | Same core evidence plus optional hysteresis, drift, or between-unit analysis | A calibration certificate does not remove setup, range, repeatability, and model-validity checks. |

**Physical access required:** wiring, reference/sensor placement, personal raw
readings, repeat choice, and response to a physical anomaly. Prepared values may
support only the analysis construct.

### Digital timing

**Core question:** Does a low-voltage GPIO or serial transaction meet its timing
contract, and what causes an intermittent timing failure?

| Path | Apparatus definition | Same required learner evidence | Path boundary |
|---|---|---|---|
| Minimal | Characterized low-cost logic analyzer or MCU timer/capture input; approved 3.3 V logic target; DMM for static level check | Personally connect signal reference and channel; set sample rate/trigger; capture repeated events; cross-check one interval by a second method; diagnose an injected period, polarity, or scheduling fault | Sampling must provide at least 10 samples across the shortest interval being judged. This path cannot certify rise time, overshoot, or analog threshold margin. |
| Standard | Oscilloscope and/or bench logic analyzer with selectable thresholds and recoverable trace export | Same timing prediction, configuration, repeated transactions, hypothesis table, correction, and acceptance evidence | `Auto` settings and protocol-decoder text without raw timing are insufficient. |
| Advanced | Mixed-signal or higher-bandwidth instrument with protocol decode | Same core evidence plus optional jitter or signal-integrity enrichment | The learner validates decoder output against raw edges and electrical levels. |

**Physical access required:** connection, acquisition configuration, repeated
capture, and fault localization on a target.

### MCU debugging

**Core question:** Can the learner recover a low-voltage board and localize a
seeded hardware/firmware interface fault by discriminating tests?

| Path | Apparatus definition | Same required learner evidence | Path boundary |
|---|---|---|---|
| Minimal | Recoverable MCU board; offline build/recovery bundle; UART or GPIO diagnostics; DMM; low-cost logic analyzer or capture fixture | Personally inspect, recover, build/flash, predict checkpoints, record hypotheses, run discriminating tests, isolate and correct one configuration/interface fault, and repeat an acceptance test | Fault must remain reversible; no irreversible security configuration. Logs alone cannot prove connection or physical isolation work. |
| Standard | Same target plus known-good SWD/JTAG debug probe, bench supply/current limit, oscilloscope or logic analyzer | Same core evidence, including breakpoint/watch or register evidence and one electrical cross-check | Debugger status does not replace checking reset, power, clock, pin mux, and signal reference. |
| Advanced | Trace-capable target/probe or mixed-signal correlation setup | Same core evidence plus optional execution/timing correlation | Trace automation cannot replace the hypothesis table and a learner-selected discriminating test. |

**Physical access required:** board inspection and connection, recovery, probe or
diagnostic configuration, physical/electrical cross-check, and seeded-fault
localization. A prepared debug log supports interpretation only.

## Comparison acceptance criteria

A reviewer may mark paths equivalent only after physical pilots show, for every
row above, the same construct, independence, raw evidence, decision threshold,
safety stop behavior, reasonable completion burden, and accessible route. Record
observed range, uncertainty, completion time, access defect, and anomaly outcome
in `safety-usability-approval-template.yml`. Until then the comparison status is
`pending`.

SPDX-License-Identifier: CC-BY-SA-4.0
