# ESE-SAF-TC-001 — Shared laboratory safety technical contract

**Version:** 0.1.0  
**Status:** draft; numeric defaults require local safety-authority review  
**Applies to:** `ESE-SAF-001` and `ESE-SAF-002` in EN and FR

This is the language-neutral safety contract. Values are conservative curriculum
defaults, not a claim of compliance with an unnamed standard. A deployment must
replace them when a cited applicable rule is stricter and record that decision in
the activity risk assessment. Classification uses the highest level triggered by
any energy, fault, chemical, mechanical, RF, environmental or use condition.

## L0–L4 authorization envelope

| Level | Permitted envelope only after activity approval | Default supervision | Evidence |
|---|---|---|---|
| L0 | Observe; simulate; inspect or assemble only after every source and stored-energy element is removed, discharged, verified and controlled | staff present or an approved low-risk plan; no energization | induction acknowledgement |
| L1 | Current-limited, extra-low-voltage core work, normally no more than 12 V DC, 1 A source limit, 12 W fault power and 0.25 J exposed capacitor energy; protected/enclosed energy sources only; no soldering or deliberate rotation | at least one trained instructor/assistant per 12 learners; trained staff immediately available; pre-G1 work is direct-supervised at instructor-controlled stations | G1 written and practical evidence before independent L1 energization |
| L2 | Approved extra-low-voltage work, normally no more than 24 V DC, 2 A and 48 W; soldering, bounded low-energy motors, protected batteries and bench instruments within the activity limits | at least 1:12; direct supervision for first exposure, soldering, hot work, batteries and rotating setups until the task briefing permits close supervision | current G1 plus task qualification; solder instruction may start before G3 under direct supervision |
| L3 | Any work outside L2 but not assigned to L4: higher fault-energy DC, converters, accessible heat/rotation, battery packs, chemicals/coatings or lawful RF transmission | qualified local controller; at least 1:8 for unfamiliar work; direct supervision whenever the risk assessment requires | activity-specific risk assessment, current task authorization and instructor sign-off |
| L4 | Mains, high voltage, high-energy storage, lasers or safety-critical equipment | advanced course only, continuous direct supervision under an adopted institutional procedure | named institutional approval and task permit; prohibited in unsupported self-study |

“Normally” is not permission to exceed a value. The activity record must state
each actual limit. `SELV` may be used only when the adopted standard's full
source/system definition is satisfied. Voltage never reduces a higher level
triggered by available current, fault power or stored energy.

## Mandatory energy-aware classification

The author records the source open-circuit voltage; normal and current-limit
current; available/fault power; upstream protection and clearing behavior;
conductor, connector, fuse and probe ratings; and stored-energy calculations.

- Capacitor energy: `E = 1/2 C V²`. L1 permits at most 0.25 J accessible before
  discharge controls. L2 requires an approved discharge path and verification;
  exposed energy above 5 J is L3. Any energy that remains at a hazardous value
  after shutdown requires a bleed-time label and measured zero-energy check.
- Batteries: record chemistry, cell count, nominal/maximum voltage, capacity,
  watt-hours, state-of-charge bound, protection/BMS, prospective short-circuit
  behavior, connectors, charger and damaged-pack route. L1 uses only protected,
  enclosed institution-approved sources. Loose rechargeable lithium cells are
  excluded from L1. Opening, spot-welding, bypassing protection, charging an
  unknown/damaged cell, or pack construction is L3/L4 as institutionally assigned.
- Fusing and wiring: protection must interrupt the credible source fault before
  the lowest-rated conductor, connector, switch, PCB trace or probe is damaged.
  A current limit is not treated as a fuse unless its credible single fault and
  behavior have been verified. Never replace a fuse with foil, wire or a higher
  rating without engineering approval.
- Temperature: L1/L2 activities set a predicted accessible-temperature limit,
  normally no more than 45 °C in steady learner contact, and stop on an unexpected
  rise, odor, discoloration or any measured value above the activity limit.
  Intended hot tools/surfaces require guarding, a stand, heat-resistant placement,
  explicit briefing and direct supervision. Do not infer safety from temperature alone.
- Rotation/mechanics: record speed, moving mass/inertia, stored mechanical energy,
  pinch/entanglement/ejection zones, stall current and restraint. L2 permits only
  a restrained low-energy rig with guarded coupling and no exposed blade, flywheel
  or projectile path. Otherwise use L3 controls.
- Chemicals, solder, flux and coatings: identify product and safety data sheet
  (SDS), route of exposure, quantity, ventilation/extraction, incompatible
  materials, spill/first-aid method and waste stream. Ordinary institution-approved
  solder/flux may be L2 with extraction and hygiene; unknown substances, bulk
  solvents, coatings, etchants or sensitizers are L3 until assessed.
- Oscilloscopes: document protective-earth bonding, input maximum, probe rating,
  common-mode limit and measurement category. A conventional earth-referenced
  probe ground connects only to a verified safe reference of an isolated L1/L2
  circuit. Never float the oscilloscope, defeat protective earth, or clip its
  ground to an unverified live node. Mains/category measurements are L4 and use
  institution-approved differential/isolation methods and qualified personnel.
- RF: record frequency, mode/duty cycle, antenna gain/separation, conducted and
  radiated power, exposure calculation, spectrum authorization and interference
  controls. L2 is limited to unmodified institution-approved low-power equipment
  operated within its lawful configuration. Amplifiers, changed antennas,
  intentional RF power tests or uncertain exposure/regulatory status are L3/L4
  and remain off until approved.
- Field conditions: assess weather, wetness, heat, dust, lighting, traffic,
  heights, animals/insects, public access, security, communications, travel,
  lone work, emergency response, data/participant boundaries and safe withdrawal.
  Field work also requires G8 and institutional/partner approval where applicable.

## Universal pre-energization sequence

1. Identify the activity revision, authorization level and stop conditions.
2. Remove power; inspect enclosure, leads, polarity, component orientation,
   insulation, ratings and mechanical restraint.
3. Check for unintended shorts and protective-earth/reference errors.
4. Calculate maximum current, fault power and stored energy; compare every part
   and probe with its rating.
5. Set voltage and current limit with output off; select and verify the fuse.
6. Obtain the peer/instructor checkpoint required by the activity.
7. Clear the work area, secure PPE, identify isolation and keep an escape path.
8. Energize without touching the circuit; monitor current, voltage, sound, smell,
   motion and temperature against expected bounds.
9. Stop, isolate, wait/discharge and verify zero energy before adjustment.

## Stop-work and emergency priorities

Anyone may say **STOP / ARRÊT**. Stop on unknown configuration; missing
authorization, PPE, guard, extraction or supervisor; damaged insulation/battery;
unexpected current, heat, odor, smoke, arcing, noise, motion or RF behavior;
liquid ingress; exposed conductor; loss of communications; illness/injury; fire;
or a measurement outside the approved envelope. Do not touch a casualty or
apparatus until the energy is isolated. Raise the alarm, use the emergency
isolation only when safe, call the locally posted response, give first aid only
within training, evacuate when required, preserve evidence and report promptly.

## G1/G3 and prior-competence crosswalk

| State | Allowed practice | Independence claim |
|---|---|---|
| Induction complete, pre-G1 | L0 and direct-supervised instructor-controlled L1 stations; instructor controls source and authorizes each energization | none |
| G1 current | independent energization only within an approved L1 activity; L2/L3/L4 still need their own controls | safe bench user within stated scope |
| L2 solder briefing, pre-G3 | solder training may begin under direct supervision after tool/SDS/PPE/stop briefing | no independent solder/rework claim |
| G3 current | independent progression in approved L2 solder/rework tasks, subject to local supervision and activity authorization | solder/rework gate met; not permission for every hot-work task |
| Prior equivalent competence | candidate may challenge G1/G3 using an unseen equivalent practical and the same conjunctive safety/evidence threshold | no waiver, automatic credit or energization before the result is formally recorded |

Default authorization validity is one academic year and ends sooner at the date
set by the institution. Requalification is required after expiry, material
procedure/equipment change, six months without the competence (unless the local
period is shorter), an unsafe act, relevant incident/near miss, medical/access
change affecting controls, or safety-authority suspension.

