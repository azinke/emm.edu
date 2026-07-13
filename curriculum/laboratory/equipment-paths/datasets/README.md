# Prepared raw-format analysis datasets

**Semantic ID:** M03-E4-DATA-01
**Version:** 0.1.0-draft
**Evidence class:** prepared, synthetic, non-personal; not physical measurement

Every CSV in this directory is deterministic teaching data created from a stated
idealized model or scripted event scenario. No learner, staff member, instrument,
physical fixture, sensor, MCU, or laboratory produced these values. The files use
a raw-record shape so learners can practise import, plotting, model fitting,
uncertainty reasoning, anomaly detection, and design decisions during rotation or
as an accessible analysis route. They must never be relabeled as raw physical
measurement, calibration evidence, path-comparison evidence, apparatus
qualification, or personal practical evidence.

The fields `record_class` and `provenance` repeat this boundary on every row so it
survives extraction from this README. The `.csv` decimal separator is a point in
both language pathways because it is machine data.

| Dataset | Scenario/model | Deliberate analysis feature | Constructs it cannot certify |
|---|---|---|---|
| `dc-network-prepared.csv` | 5.0 V divider; ideal nominal values with rounding | one wrong-value lower resistor in run `DC-B` | wiring, DMM choice/connection, safe energization, physical fault localization |
| `rc-response-prepared.csv` | `v(t)=3.3(1-exp(-t/tau))`; `tau=0.100 s` nominal | run `RC-B` represents `tau=0.047 s` | RC construction, probe choice, acquisition configuration, loading diagnosis |
| `sensor-calibration-prepared.csv` | linear `V=500+10T` mV plus deterministic offsets | one displaced 30 °C point | sensor/reference placement, physical repeats, calibration execution |
| `digital-timing-prepared.csv` | nominal 1000 µs event period | one 1600 µs scheduling delay | analyzer connection/threshold, live capture, physical timing debug |
| `mcu-debug-prepared.csv` | ordered boot/interface checkpoints | seeded wrong pin-multiplexing state | board recovery, flashing/probing, electrical cross-check, physical debugging |

Learners must cite the dataset ID/version and write **prepared synthetic
non-personal data** on plots, tables, and conclusions. The instructor marks the
associated physical construct `outstanding` until separately observed.

SPDX-License-Identifier: CC-BY-SA-4.0
