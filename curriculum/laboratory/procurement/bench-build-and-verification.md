# Minimal and standard bench build and verification

**Control ID:** ESE-LAB-PROC-004  
**Status:** build specification; no physical bench is released by this document  
**Required release:** named facility inspection, asset checks, activity risk
assessment, and signed bench verification record

## Common safe layout

From learner edge to rear service zone: de-energized build mat and component
storage; DMM and low-voltage connection point; current-limited source; scope and
generator; computer/debug area; staff-controlled isolation and emergency systems.
Keep hot work, battery quarantine, chemicals/coatings, rotating apparatus, mains,
and higher-energy power in separately controlled zones. Cables do not cross exits
or accessible routes. Emergency isolation, stop-work card, limits, exits, and asset
state are visible in EN/FR without depending on color or QR access.

## Minimal path

Per active pair: approved eye protection, hand tools, breadboards/leads, fused or
current-limited extra-low-voltage source, checked DMM, foundation MCU plus known-good
USB data cable, protected low-energy sensor/load fixtures, and offline computer
access. Shared by the validated activity ratio: compensated oscilloscope, generator,
logic/debug probe, and supervised soldering/extraction where the outcome needs it.

The minimal path is accepted only if it produces the same learner decisions and
individual evidence as the standard path. It is not permission to replace personal
measurement/debugging with demonstration or prepared data.

## Standard path

Per pair: checked 0–30 V-class isolated bench supply with visible V/I and adjustable
current limit, 2+ channel 50 MHz-class grounded oscilloscope with compensated probes,
DMM, generator, logic analyzer, debug probe, and temperature-controlled grounded
solder station with effective extraction. Add protected motor/power fixtures,
precision reference access, ESD controls, and progression platform according to the
activity authorization.

## Release tests

All results name asset IDs, method version, reference IDs, acceptance bounds, raw
values, executor, reviewer, and date.

1. **Source current limit:** connect an approved electronic/test load, set voltage
   and low current limit before enabling, step load through the limit, and verify
   output/readback and safe response. Do not use an accidental short as the method.
2. **Fault energy:** for every activity source, calculate maximum steady fault power
   and stored energy (including output capacitors/batteries), verify fuse/current-limit
   rating and clearing/limiting behavior using a safe fixture, and compare conductor,
   connector, probe, component, enclosure, and accessible-temperature ratings.
3. **Probe compensation:** inspect probe rating/ground lead, compensate on the
   scope reference output, record a bounded square-wave capture, and quarantine any
   probe that cannot compensate or has damaged insulation.
4. **Grounded-scope constraint:** prove the bench's protective-earth topology and
   mark scope reference clips as earth-referenced. The activity diagram must show
   prohibited high-side/differential connections and the approved differential or
   isolated measurement method where needed. Never float a protective-earth scope.
5. **Motor/power setup:** use guarded low-energy mechanics, current limit, fuse,
   flyback/driver protection, secure mounting, keep-out zone, emergency stop route,
   thermal stop limit, and a bounded stall test. Record supply/battery chemistry,
   maximum fault/stall energy, rotation hazard, and restart behavior.
6. **Cross-coupling:** verify simultaneous instruments cannot create an unintended
   earth return, back-power a USB host, exceed I/O voltage, or defeat source limits.
7. **Accessibility and egress:** demonstrate reach, control identification, safe
   manipulation/support route, seated clearance, cable management, and unobstructed
   emergency/exit routes without lowering the assessed independence threshold.

## Before every session

Staff confirm room release, RCD/GFCI/emergency status according to institutional
procedure, extraction/ventilation, first-aid/fire response readiness, asset due
dates, quarantine segregation, correct fixtures/fault boards, default source-off
and current limit, expected measurement bounds, learner authorizations, supervision
ratio, accessibility arrangements, and rescheduling capacity. Any failed item stops
the affected station.

