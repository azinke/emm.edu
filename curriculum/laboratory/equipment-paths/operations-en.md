# Bench operations cards — English

**Semantic ID:** M03-E4-OPS-01
**Language:** en
**Version:** 0.1.0-draft
**Paired artifact:** `operations-fr.md`
**Status:** not rehearsed or safety-approved

These cards apply only to the locally approved, energy-limited task envelope and
current learner authorization. Stop if a label, limit, source, lead, protective
part, or authorization is missing or unclear.

## Shared setup map

```text
BACK / fixed services
+------------------------------------------------------------------+
| [A] approved source, OUTPUT OFF  [B] instrument  [C] data PC      |
|                                                                  |
| [D] de-energized DUT zone       [E] probe/lead parking            |
|     inspection card here            no loose metal                |
|                                                                  |
| [F] evidence/notebook zone      [G] parts: GOOD / RETURN /        |
|                                     QUARANTINE (separate bins)    |
+------------------------------------------------------------------+
FRONT / learner escape path                    [H] emergency stop
```

Keep liquids, bags, and unrelated metal outside the map. The emergency stop and
exit remain reachable. `0V_REF` means signal reference, not protective earth.

## Path overlays

| Zone | Minimal | Standard | Advanced |
|---|---|---|---|
| A | approved current-limited extra-low-voltage source | bench supply, output off, limit preset | programmable source, output locked off until review |
| B | DMM plus characterized logic analyzer/MCU fixture | DMM, oscilloscope/generator, logic analyzer/debug probe as assigned | precision/automated instrument with fixture/reference-plane record |
| C | offline capture device; network not required | offline instrument export/build device | offline automation controller and raw export destination |
| D | breadboard/low-voltage board only | same DUT with probe clearance | reviewed fixture with guarded/keyed connections where applicable |

Advanced equipment is not permission for higher energy or unsupervised work.

## Quick guide QG-01 — Check before energy

1. Confirm your learner authorization, task ID, apparatus path, and approved
   envelope with the instructor.
2. Read source, instrument, lead, probe, fixture, and DUT labels. Move any damaged,
   overdue, unknown, or mismatched item to `QUARANTINE`; do not test it on a DUT.
3. With all sources off and stored energy discharged by the approved method,
   inspect polarity, component values, exposed conductors, signal reference, and
   possible shorts.
4. Calculate or identify the task's maximum fault current, power, stored energy,
   and accessible temperature. Stop if the approved limit is absent.
5. Set voltage and current limit with output off. Select the instrument function,
   terminal, range, probe attenuation, threshold, and signal reference.
6. Ask for the required peer/instructor checkpoint. Keep one hand ready to switch
   off without reaching across the circuit.

## Quick guide QG-02 — Energize, observe, stop

1. Announce energization and switch on only the approved source.
2. Observe current, temperature indicators, smell, sound, and expected first test
   point before proceeding.
3. Stop immediately for unexpected heat, smell, smoke, sound, unstable supply,
   damaged insulation, current limit activation not predicted by the method, an
   out-of-bounds reading, lost signal reference, or any uncertain condition.
4. Switch off; do not touch until stored energy and temperature are safe by the
   approved method. Notify the instructor and preserve configuration/evidence.
5. Record the stop as evidence. Do not hide a near miss or change the setup before
   the instructor decides whether inspection or quarantine is required.

## Quick guide QG-03 — DMM

- Inspect body, leads, insulation, terminals, fuse/function label, and check-due
  date. Confirm the meter is approved for the task; category markings do not
  expand this course's task envelope.
- For voltage/resistance, use the common and voltage/resistance terminals. Never
  measure resistance or continuity on an energized circuit.
- Current-input work is excluded from these cards unless a separate task briefing
  and qualification explicitly permit it.
- Prove a plausible reading on a known, approved source or check fixture before
  and after a safety-relevant measurement.
- Retain value, unit, range, stable/unstable state, test points, polarity, meter ID,
  and relevant resolution/input-resistance contribution.

## Quick guide QG-04 — Oscilloscope and logic analyzer

- Identify protective earth, chassis, signal reference, and DUT `0V_REF`; never
  assume they are isolated.
- Function-check the probe, attenuation setting, compensation, channel, threshold,
  sample rate, timebase, and trigger on an approved check signal.
- Attach the signal-reference lead first and remove it last with the DUT
  de-energized. Use short ground connections approved for the fixture.
- Save raw samples or an open trace plus instrument ID and all acquisition
  settings. A screenshot or decoder label alone is insufficient.
- Do not infer rise time, overshoot, or analog margin from a digital-only analyzer.

## Quick guide QG-05 — Supply, generator, and MCU fixture

- Set amplitude/voltage, offset, frequency, waveform, and current limit while the
  output is off. Verify these settings at an approved unloaded checkpoint.
- Confirm there is only one DUT power source or an approved anti-back-feed design.
- The MCU fixture starts safe, requires `ARM`, and returns to safe on timeout or
  disconnect. If identification/profile/status is missing, do not connect it.
- Never use the draft fixture outside 0 V/3.3 V energy-limited teaching circuits;
  in fact, no unit may be used until its approval record says `approved`.

## Troubleshooting cards

### TC-01 No expected DC value

1. Switch off and confirm discharge.
2. Check the model's reference node and predicted values.
3. Inspect source polarity/limit, DMM terminals/function, continuity, breadboard
   row placement, component values, and one node at a time.
4. Change one discriminating condition and predict its result before re-energizing.
5. Quarantine any lead or part that fails a known-good cross-check.

### TC-02 Flat, clipped, or noisy capture

1. Stop output; check common signal reference and allowed voltage range.
2. Compare predicted `tau` or shortest timing interval with sample interval,
   duration, bandwidth, probe attenuation, and trigger.
3. Check for ADC saturation, generator offset, wrong coupling, dropped samples,
   floating input, or input loading.
4. Cross-check one static level or interval by an independent method.

### TC-03 MCU does not boot or debug

1. Disconnect loads; inspect supply, current limit, cable, orientation, reset/boot
   state, signal reference, and visible damage.
2. Use the approved recovery image and known-good cable/probe. Record exact tool
   output; do not perform irreversible security operations.
3. Test power, reset, clock symptom, firmware identity, pin mux, and interface in
   an order that discriminates hypotheses.
4. Change one variable at a time. Restore the seeded fault after assessment only
   if the instructor's configuration-control procedure requires it.

### TC-04 Stop and escalate

Stop and call the instructor for an unknown energy source, unexpected heating or
odor, damaged insulation, repeated overcurrent, lost protective part/interlock,
liquid, injury, smoke, fire, or uncertainty about protective earth. De-energize
only if the approved emergency procedure makes that action safe. Follow the room
incident/near-miss and evacuation procedure; these cards do not replace it.

## Check-in CI-01

1. Sign out the bench/configuration ID and each serialized instrument/accessory.
2. Confirm current authorization and accessible controls/labels.
3. Inspect and function-check items; record status and due dates.
4. Count leads/probes/adapters; confirm correct ratings and compensation pieces.
5. Record pre-existing defects. Place failed items directly in `QUARANTINE` and
   obtain a qualified replacement.
6. Load only the instructor-approved firmware/configuration and create a new raw
   evidence folder named by pseudonymous learner, task, date, and attempt.

## Check-out CO-01

1. Stop stimulus, switch source output off, disconnect source power, and confirm
   discharge/cooling using the approved method.
2. Remove signal leads, return controls to the local default, and save raw data,
   configuration, hashes where supplied, and notebook references.
3. Inspect, count, clean by the approved dry method, cap probes, and coil leads
   without stress.
4. Return known-good items to `RETURN`; never move an unverified item into `GOOD`.
   Label failures with symptom, setup, date, reporter, and last safe state, then
   place them in `QUARANTINE`.
5. Clear scraps and restore the bench map. Sign out with the instructor/technician;
   record incident, near miss, missing item, or unresolved physical evidence.

SPDX-License-Identifier: CC-BY-SA-4.0
