# Safety requalification prerequisites for S2–S6

**Semantic ID:** M03-E4-REQUAL-01
**Version:** 0.1.0-draft
**Status:** prerequisite specification; no learner authorization or institutional
approval is asserted

Requalification is a pass/fail safety prerequisite independent of course grades.
It confirms only the named task envelope; it does not authorize a learner for all
work at a semester level. The deploying institution maps each row to its adopted
safety manual, exact energy limits, room, supervision, legal requirements, and
assessor. Unmapped or unapproved fields block the activity.

## Common entry and validity rules

Every requalification requires current prerequisite program gates, review of the
task risk assessment and stop conditions, a written/visual knowledge check, a
practical demonstration with an altered setup, correct shutdown/quarantine/
incident response, and an attributable record in the controlled system.

An authorization lasts no longer than one academic semester. Requalification is
required sooner after an incident or near miss, unsafe stop or suspension,
relevant apparatus/fixture/procedure/energy change, material change to accessible
controls or PPE, assessor-observed skill decay, or absence from the authorized
activity for one academic term. A learner never "practises" an expired hazard
unsupervised to regain authorization.

## Stage prerequisites

| Requalification | Entry evidence | Practical check before authorization | Authorized scope boundary | Release blockers |
|---|---|---|---|---|
| **S2-RQ device work and soldering** | Current G1 safe-bench authorization and G2 fundamental measurement evidence; course prerequisite met; task briefing for component polarity, thermal and chemical exposure | Identify iron stand, tip condition/temperature setting, fume extraction, eye protection and hot-item zone; make and inspect one altered through-hole joint; remove one component without pad/lead damage; demonstrate de-energized continuity/short check, handwashing, waste segregation, burn/eye-exposure response | Approved L2 soldering and energy-limited device work only, within named station/task limits; no loose lithium cell, mains, high-energy source, uncontrolled heating or unsupported self-study soldering | Missing ventilation inspection, SDS/local chemical procedure, fire/first-aid route, hot-work limits, current G1/G2, or qualified assessor |
| **S3-RQ precision instrumentation and FPGA** | Current G1/G2/G3 as applicable; ESE121/ESE122 and digital/C prerequisites; current ESD and instrument function-check briefing | Verify signal reference versus protective earth; compensate/check a probe; choose ranges and prevent reference-instrument overload; connect a 3.3 V logic target through approved I/O; identify FPGA bank voltage/pin constraints; diagnose one bounded loading, range, swapped-reference, or logic-level fault; quarantine a suspect precision lead/reference | Named extra-low-voltage precision, analog, ADC and FPGA setups; reference instruments remain staff-controlled; no external I/O until bank voltage and pin map are reviewed | Unknown reference traceability/function status, unqualified logic levels/board revision, scope grounding ambiguity, expired G1/G2, or missing ESD/access route |
| **S4-RQ PCB bring-up and protected DC power** | Current G1–G5 prerequisite evidence; approved schematic/PCB review and bring-up plan; task-specific stored-energy/current/fault-power calculations | Inspect unpowered PCB against release revision; test shorts/polarity/protective parts; set supply and current limit with output off; use staged power-rail bring-up and thermal/current stop criteria; safely command an approved low-energy motor/load; isolate/quarantine a board with an unexpected current or temperature signature | Named PCB and protected DC converter/motor setup under approved L2/L3 supervision; task limits govern voltage, current, power, capacitance, battery state, temperature and rotation separately | Missing release/configuration identity, fuse/protection or enclosure, unknown supply isolation/earth relation, absent energy calculation, prohibited battery condition, or no direct qualified supervision where L3 is assigned |
| **S5-RQ RF and security laboratories** | Current G1–G6; exact board/radio/firmware frozen; deployment-specific radio/legal and exposure approval; current threat/data-handling briefing | Confirm lawful band/channel/power/test mode and approved antenna/load before transmit; demonstrate RF stop/disable; inspect battery/power/thermal limits; recover a board using reversible credentials/configuration; diagnose one bounded interface/security-state fault without exposing a secret or changing irreversible security fuses | Approved low-power radio or shielded/dummy-load task and reversible security laboratory only; no RF-power work, jamming, unauthorized network access, credential publication, or irreversible lock/fuse operation on reusable boards | Missing jurisdiction/facility authorization, exposure calculation/control, antenna/load approval, restricted-data route, recovery image, or task-specific supervisor |
| **S6-RQ field activity** | Current G1–G7 and passed G8 before any student-led stakeholder research, personal-data collection, site access or deployment; institutional/partner ethics and site permissions remain separate; current equipment-specific qualifications | Rehearse site sign-in/out, buddy/check-in and missed-contact escalation; identify permitted zones, emergency isolation, first-aid/evacuation and weather/traffic/mechanical/biological hazards; inspect enclosure/cables/power state; demonstrate safe rollback, data minimization, offline operation, incident reporting, asset recovery and leave-safe handover | Only the named approved site, date window, equipment configuration, participants, data plan and field risk assessment; no improvised mains connection, high-energy battery access, RF-power work, high voltage, medical/safety-critical claim, lone work, or unapproved human-participant activity | Any missing G8, ethics/partner/site permission, named host/supervision, communications/emergency route, weather/transport go/no-go check, lawful radio/data approval, service/rollback owner, or current technical authorization |

## Required controlled record

Record learner reference, stage ID, exact task/envelope, prerequisite gate
versions, assessor and authority, written/practical variants, observed decisions,
stop/quarantine/incident response, accommodations, result, remediation, issue and
expiry dates, suspension/requalification triggers, and appeal/moderation route.
Personal, accessibility, incident, and assessment details must not be committed to
public Git.

The assessor must vary component values, fault, setup, or scenario on reassessment
so the check tests transfer rather than rehearsal. Unsafe behavior stops the
attempt immediately; remediation does not waive the dependent prerequisite.

SPDX-License-Identifier: CC-BY-SA-4.0
