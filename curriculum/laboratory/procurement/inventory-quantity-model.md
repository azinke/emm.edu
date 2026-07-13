# Cohort inventory quantity model

**Control ID:** ESE-LAB-PROC-002  
**Applies to:** personal, pair, progression, shared, advanced, consumable, and
spare inventories  
**Release condition:** a named cohort plan and timetable are approved

## Required cohort input

The procurement lead records:

| Field | Meaning | Acceptance rule |
|---|---|---|
| `cohort_id` | stable institutional cohort identifier | not `example`, `TBD`, or a planning scenario |
| `enrolled_students` | funded learners including approved late-entry allowance | integer greater than zero |
| `largest_section` | maximum learners physically present at once | reconciles to timetable and room capacity |
| `pair_size` | learners sharing pair apparatus | normally 2; an exception needs evidence-equivalence approval |
| `rotations` | independently staffed/repeated bench periods | cannot conceal loss of personal practical evidence |
| `weeks` | teaching and assessment weeks requiring stock | includes remediation/rescheduling capacity |
| `attendance_margin` | additional scheduled seats | documented, not used to reduce apparatus below entitlement |
| `deployment_profile` | dated local profile | approved or every unresolved field explicitly dispositioned |

## Quantity classes and formulas

All divisions round upward. `N` is enrolled students, `S` the largest simultaneous
section, `P` the approved pair size, `R` the usable rotation count, and `r` the
item-specific spare fraction.

| Class | Base quantity | Typical contents | Stock rule |
|---|---:|---|---|
| personal | `N` | PPE, tools, breadboards, foundational MCU, storage | issue one traceable set per learner |
| pair | `ceil(N/P)` | progression components and project apparatus | preserve attributable individual evidence |
| simultaneous personal | `ceil(S/R)` | DMM where issued per active learner | timetable must show every learner's access |
| simultaneous pair | `ceil(S/(P*R))` | scope, supply, solder station, debug/logic tools | never exceed validated bench occupancy |
| shared | `ceil(S/ratio)` | generator, reference instruments, advanced tools | queue time must fit the activity plan |
| room | number of qualified rooms | isolation, RCD/GFCI, extraction, emergency systems | no rotation credit across simultaneous rooms |
| consumable | forecast use × sessions × groups | wire, solder, tips, fuses, passives | add loss/rework evidence, shelf life, and reorder floor |
| deliberate fault | planned concurrent stations + known-good controls | seeded-fault boards/cables | segregate from student-use stock |

The order quantity is:

`order = max(0, ceiling(base × (1 + spare_fraction)) + deliberate_fault_reserve − serviceable_on_hand − accepted_on_order)`

Minimum spare fractions from the master contract are 15% for boards, 25% for
high-failure cables/connectors, and 50% for commodity passives/semiconductors.
The item owner may increase these values from observed failure/lead-time data;
decreasing them requires a signed risk disposition and a tested replacement path.

## Inventory families

The catalog must cover, at minimum:

- personal foundation: eye protection, hand tools, breadboards, leads, passives,
  indicators, semiconductors, basic ICs, Pico 2/equivalent, sensors, protected
  low-energy loads, storage, and printed EN/FR safety card;
- pair progression: analog/metrology, professional MCU/debug, digital interfaces,
  lawful communication modules, protected power/control, FPGA, PCB/manufacture,
  and field accessories;
- shared bench: DMM, oscilloscope and compensated probes, current-limited supply,
  generator, grounded temperature-controlled soldering with extraction, debug
  probe, logic analyzer, and locked precision references;
- advanced/shared-regional: spectrum/SDR, electronic load, programmable source,
  microscope/rework, thermal/measurement resources, and any qualified partner
  access needed for a core outcome;
- infrastructure and lifecycle: computer/loan fleet, local server/offline media,
  storage, ESD, power backup, calibration/function-check fixtures, fire/first-aid,
  quarantine, repair, and approved waste routes.

## Bilingual, accessible stock identity

Every physical unit or bin receives a durable ID and a high-contrast label:

`<family>-<item>-<serial> | EN name / nom FR | limit | state | next check`

Color is supplementary only. The printed word and shape/pattern distinguish:

| State | EN / FR label | Pattern |
|---|---|---|
| known good | `KNOWN GOOD / CONFORME` | solid border |
| student use | `STUDENT USE / USAGE ÉTUDIANT` | double border |
| quarantine | `DO NOT USE—QUARANTINE / NE PAS UTILISER—QUARANTAINE` | diagonal stripe |
| deliberate fault | `TRAINING FAULT—DO NOT ISSUE / PANNE DIDACTIQUE—NE PAS DISTRIBUER` | dotted border plus tamper tag |

Labels include an accessible text record; QR codes are optional and never the
only route. Deliberate-fault stock is stored separately from serviceable stock.

## Cohort acceptance review

The laboratory director signs only after the generated plan demonstrates:

1. quantities reconcile to real enrollment, section, room, pair, and rotation data;
2. at least 15% board and required cable/passive reserves are physically serviceable
   or funded with an arrival date before need;
3. the timetable preserves each mandatory personal construction, measurement,
   and debugging event plus remediation/rescheduling capacity;
4. accessibility routes meet the same outcome and independence threshold;
5. stock floors cover lead time plus review, customs, receipt, and quarantine time;
6. no unqualified substitute, expired quote, or unavailable partner resource is
   counted as usable inventory.

