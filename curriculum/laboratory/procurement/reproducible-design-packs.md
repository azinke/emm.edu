# Locally reproducible laboratory design packs and technician qualification

**Control ID:** ESE-LAB-PROC-005  
**License target:** CERN-OHL-P-2.0 for original hardware source; MIT for test code;
CC-BY-SA-4.0 for instructions  
**Status:** pack contract; individual designs require physical qualification

## Mandatory pack contents

Every cable, fixture, deliberate-fault board, enclosure/harness sample, or test jig
has a stable ID and revision and includes:

- outcome/use contract and prohibited uses;
- editable source plus neutral fabrication/print outputs;
- numbered schematic/wiring diagram, connector pinout, conductor/insulation/rating,
  mechanical dimensions/tolerances, BOM with MPNs and approved alternates;
- make/buy/provenance record naming locally performed and imported work;
- energy-aware risk assessment, limits, guarding, labeling, accessible method,
  cleaning/storage, and end-of-life route;
- assembly traveler with inspection points, tools, skill level, photos/diagrams,
  rework rules, serialization, and configuration record;
- test fixture/method, reference assets, expected bounds, raw record, seeded failure
  proving the test rejects a defect, calibration/function-check interval, and repair;
- controlled change log, independent technical/safety review, license/source notices,
  and release/handover signatures.

## Initial pack specifications

### CAB-LV-001 — fused extra-low-voltage lead

Purpose: connect an approved current-limited source to L1/L2 teaching fixtures.
Use shrouded/touch-safe connectors selected by the institution, keyed polarity,
strain relief, conductor and insulation rated above the approved maximum, and a
replaceable series fuse where the source limit alone does not meet the activity
fault contract. Mark maximum voltage/current/fuse, polarity, revision, and asset ID
in EN/FR. Qualification includes continuity, polarity, insulation/strain inspection,
four-wire voltage drop at rated teaching current, fuse identity, and mating-cycle
inspection. It is never a mains lead.

### FIX-IO-001 — protected MCU I/O stimulus/acquisition fixture

Purpose: provide bounded switches, potentiometer/sensor stimulus, LEDs/test points,
and protected low-energy loads for GPIO/ADC/PWM/bus/debug exercises. Include series
resistance, reverse/back-power analysis, supply/logic test points, replaceable
connectors, and explicit compatible I/O voltage. Qualification exercises every
channel, out-of-range stimulus protection, power sequencing, and known-good firmware.

### FLT-DC-001 — deliberate-fault DC network

Purpose: teach hypothesis-led DMM debugging with switch/jumper-selectable open,
wrong-value, high-contact-resistance, reversed-indicator, and short-to-current-limit
faults. The short is bounded by fixture resistance/fusing and approved source limit;
learners cannot access unbounded energy. Fault selection is concealed from learners
but visible to authorized staff, and a staff key maps fault IDs to expected nodes.
The test must detect every fault and verify the no-fault control.

### ENC-HAR-001 — enclosure and labeled harness sample

Purpose: compare service access, strain relief, connector keying, ingress/dust paths,
thermal clearance, accessible contrast/tactile identification, and replaceability.
The harness uses numbered wires and keyed connectors; color is secondary. Qualification
includes pin-to-pin continuity, isolation, pull/strain inspection, mis-mating attempt,
service-time measurement, and comparison to the wiring table.

### JIG-CBL-001 — cable/harness test jig

Purpose: verify continuity, shorts, crossover, contact resistance where relevant,
and connector identity without relying on visual inspection. Provide a known-good
reference plus seeded open/short/crossover specimens. The jig self-test occurs at
the start and end of a lot; a failed end check quarantines the lot since the last
accepted check.

## Technician qualification

Qualification is per pack family and revision. A candidate must, from the released
source, independently:

1. identify hazards, limits, tooling, references, and stop conditions;
2. build two conforming units without hidden instructor correction;
3. inspect another unit and find all controlled seeded defects;
4. execute the test method, retain raw evidence, and make correct release/quarantine
   decisions including measurement uncertainty where relevant;
5. diagnose and repair a repairable fault, then repeat release tests;
6. explain configuration, alternate, calibration/function-check, record, license,
   and provenance controls in the working language and use the bilingual labels;
7. propose a revision through change control without overwriting prior evidence.

The assessor records pack/revision, attempts, defects, raw results, remediation,
scope authorized, expiry (maximum 24 months; shorter after limited exposure), and
signatures. Requalification follows a safety-critical change, major revision,
serious incident/near miss, lapse, or observed performance concern. A template or
self-declaration is not technician qualification evidence.

