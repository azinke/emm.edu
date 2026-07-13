---
semantic_id: ESE-SAF-001
id: ESE-SAF-001-en
language: en
paired_with: ESE-SAF-001-fr
version: 0.1.0
status: draft
safety_level: L0-L4
localization_layer: universal-core
---

# Laboratory safety manual

Read this manual with the [shared technical contract](../shared/technical-contract.md).
The contract controls numeric limits and gate relationships. This edition controls
English operating language. An institution must complete the deployment fields,
cite applicable rules, inspect the facility, train staff and approve the system
before use.

## 1. Roles, authority and supervision

The institutional safety authority approves the manual, activity risk assessments,
L3/L4 permits, quarantine release and corrective actions. The laboratory owner
maintains rooms and records. The activity owner writes the procedure and expected
bounds. The instructor confirms readiness and controls energization. The technician
maintains equipment and segregated stores. Every learner checks the task, reports
uncertainty, uses stop-work authority and preserves honest evidence.

One author cannot solely approve a hazardous activity or high-stakes gate. Use the
contract ratios: at least 1 trained instructor/assistant per 12 learners in L1/L2
and per 8 learners in unfamiliar L3 work. L3/L4 and specified first exposures need
direct supervision: the controller is close enough to see the work, intervene and
isolate energy immediately. Unsupported self-study never includes mains, high
voltage, high-energy batteries, RF power or any L3/L4 activity.

## 2. Authorization levels

- **L0:** induction, observation, simulation, verified de-energized assembly.
- **L1:** approved current-limited core work inside the shared L1 envelope. G1 is
  required before independent energization.
- **L2:** approved extra-low-voltage bench instruments, soldering, protected
  batteries and bounded rotation inside the shared L2 envelope.
- **L3:** institution-controlled higher fault energy, power conversion, battery
  packs, thermal/rotating hazards, chemicals/coatings or lawful RF.
- **L4:** mains, high voltage, high-energy storage, lasers or safety-critical equipment.

An activity receives the highest triggered level. Authorization is personal,
level/task-specific, dated and expiring; it is not transferable between people,
equipment or activities. The instructor checks the authorization record before work.

## 3. Daily entry and bench rules

1. Enter only for scheduled/authorized work; identify the instructor, isolation,
   exits, assembly point, first aid, fire response and quarantine point.
2. Tie back hair; secure loose clothing and jewelry; use closed footwear where the
   activity requires it. Keep food, drink and unauthorized chemicals outside.
3. Inspect the bench, cables, tools, ventilation and emergency access. Tag and
   quarantine damage; do not improvise repairs.
4. Keep bags and cables out of exits and access routes. Arrange tools so a stop or
   withdrawal does not cross the apparatus.
5. Record equipment IDs, function/calibration status, activity revision, expected
   ranges and energy limits before connecting a source.
6. Follow the contract's pre-energization sequence every time the circuit changes.
7. Work only on one energized configuration at a time. Never make a wiring change
   while energized. Never bypass an interlock, RCD/GFCI, earth, fuse or guard.
8. A peer check supplements but never replaces the required instructor checkpoint.

## 4. PPE and engineering controls

The activity risk assessment selects controls in this order: remove/substitute the
hazard, isolate or guard it, limit energy and exposure, use a controlled procedure,
then add personal protective equipment (PPE). Safety glasses are the default for
construction, cutting, soldering, rotating apparatus and energization where parts
may eject. Select heat-resistant, chemical, face, hearing or respiratory protection
only from the assessed exposure and manufacturer/SDS requirements. Gloves can create
entanglement or loss-of-dexterity risks and are never a generic electrical control.

Use local exhaust ventilation for solder fumes and assessed chemical processes.
Check capture at the source before heating. Use ESD controls to protect equipment;
remove a wrist strap whenever the activity or instrument could expose the wearer to
an electrical hazard not covered by the approved ESD method.

## 5. Energization, measurement and shutdown

Predict normal voltage, current, power, temperature and motion. Calculate capacitor
and battery energy. Confirm ratings for the weakest conductor, probe and component.
Set the current limit with supply output off. Connect the circuit, obtain the required
checkpoint, clear hands, energize and compare the first observation with the expected
range. An unexplained difference is a stop condition, not a reason to increase the limit.

Use a de-energized continuity/resistance check. Connect current meters only through
the correct fused input and range; never place a current input across a source. Keep
probe fingers behind guards. Conventional grounded oscilloscopes never have their
protective earth defeated and are used only as described by the shared contract.

To adjust: switch off, isolate every source, wait the labeled discharge time, verify
zero energy with a suitable instrument, then touch. Shutdown includes batteries,
USB, programmers, external signals and mechanical/pneumatic sources, not only the
bench supply.

## 6. Soldering, batteries, movement, chemicals and RF

Place a soldering iron in its stable stand, verify extraction, keep the hot zone
clear, and treat the tip and recent joints as hot. Wash hands after solder/flux work;
do not eat or touch the face. Collect dross, contaminated wipes and lead-bearing
material in the assigned waste stream. A burn, failed extraction or unstable stand
stops the station.

Inspect batteries before issue and return. Stop for swelling, denting, puncture,
corrosion, leakage, unusual odor/heat, damaged insulation or unknown provenance.
Do not charge, short, crush, open or transport a suspect battery. Isolate equipment
only when this can be done without contact or escalation; otherwise evacuate the
immediate area and call the trained response. Use the approved nonconductive,
chemistry-compatible quarantine container and keep terminals separated. A fire or
thermal event uses the adopted fire-response plan—not an improvised extinguisher choice.

Guard, restrain and create an ejection-free zone around moving parts. Remove power
before clearing a jam. For chemicals, read the SDS, label the working quantity and
prepare spill/waste controls before opening. For RF, use only the approved frequency,
power, antenna, separation and location. Stop if a configuration or authorization is uncertain.

## 7. Stop work and emergencies

Anyone may say **STOP** without penalty. Repeat it, remove your hands and follow the
controller's isolation/evacuation instruction. If safe, the designated person presses
the emergency disconnect. Never touch a person who may remain energized. Raise the
alarm, contact the locally posted response, provide only trained first aid, evacuate
and account for people. Do not re-enter or reset equipment until the responsible
authority releases it.

After immediate care, preserve the scene and configuration when safe. Record facts,
not blame or speculation. Reporting an incident or near miss does not reduce a grade;
concealment or evidence alteration is a serious professional violation.

## 8. Incident, near-miss and quarantine workflow

1. **Protect:** stop, isolate/evacuate, call response and give trained aid.
2. **Notify:** tell the instructor and safety authority promptly using the local route.
3. **Segregate:** attach a bilingual `DO NOT USE / NE PAS UTILISER` tag; record unit,
   energy state and access restriction; move it only under an approved safe method.
4. **Record:** use `ESE-SAF-FRM-005` for injury/illness, release, property damage,
   unsafe condition, near miss, battery/equipment damage and waste disposition.
5. **Investigate:** identify causal conditions, failed controls, evidence limits and
   affected activities. A near miss receives the same learning focus as an incident.
6. **Decide:** only the named authority may release, repair/retest, return, recycle or
   dispose. Never return quarantined material directly to student-use stock.
7. **Improve:** assign owner/date/effectiveness check; reconcile EN/FR procedures and
   suspend affected authorizations/content when necessary.

## 9. Cleanup, storage and waste

De-energize and verify zero energy. Return instruments to safe settings; inspect and
count leads, guards and tips. Allow hot items to cool in a marked area. Clean the bench
using the approved method; wash hands. Sort reusable known-good parts, student-use
parts, failed-for-debugging artifacts and quarantine—never mix these states.

Use labeled, closed and compatible containers for solder waste, sharps, batteries,
electronic waste, solvents/coatings and ordinary waste. Never put batteries, chemical
liquid, contaminated wipes, solder/metal dross or sharp leads in ordinary waste unless
the approved local waste plan explicitly permits it. Record transfer, mass/count,
handler and destination. Unknown material is quarantined, not guessed.

## 10. Accessibility and safe participation

Provide a clear route, reachable isolation, adjustable bench/seat, non-color-only and
high-contrast/tactile labels, safe probe holders, advance instructions and an accessible
communication route. When dexterity is not the construct, an assistant may manipulate
under the learner's explicit direction; the learner still chooses the setup, predicts,
controls energization decisions, interprets evidence and invokes stop work. An access
adaptation never lowers the safety or evidence threshold.

## 11. Activity approval and records

Every new lab domain or material change completes `ESE-SAF-FRM-001` before learners
encounter the hazard. Approval covers one identified revision, room, equipment path,
population and period. The record includes emergency response, accessible safe methods,
stop conditions, residual-risk owner, validation evidence and re-review triggers.

Use `ESE-SAF-FRM-002` for personal authorization, `ESE-SAF-FRM-003` for competent
facility inspection, `ESE-SAF-FRM-004` for planned exercises and `ESE-SAF-FRM-005`
for events/quarantine/waste. Blank forms are not evidence. Retain records under the
institutional privacy and retention schedule and restrict personal/medical details.

