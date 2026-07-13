# Incoming qualification, maintenance, and stock control

**Control ID:** ESE-LAB-PROC-003  
**Status:** procedure ready for deployment execution  
**Authorities:** laboratory director (release), safety officer (safety-critical
release/quarantine), technician (execution), procurement lead (supplier action)

## Chain of custody and incoming inspection

Every delivery enters a physically separated `RECEIVED—QUARANTINE` area. The
receiver records purchase order, supplier/channel, packaging condition, lot/date
code, quantity, MPN/revision, serials, storage exposure, and photographs where
permitted. No delivered item is counted as serviceable or issued before the
applicable checks pass.

1. Reconcile order, invoice, labels, manufacturer markings, revision, and quantity.
2. Screen counterfeit/diversion indicators against authorized-channel records and
   manufacturer documentation. Uncertainty stays quarantined.
3. Inspect damage, corrosion, contamination, bent contacts, swollen cells,
   insulation, plugs, strain relief, fuses, ratings, seals, and accessories.
4. Verify the exact functional specification and approved-substitute decision.
5. Perform the item test method using a known-good reference and record raw results.
6. Assign a durable ID, inventory state, location, and next-check date.
7. Release, rework, return, or quarantine with technician and reviewer signatures.

Sampling is allowed only under an approved incoming-inspection plan that names
lot definition, sample method, acceptance number, critical defects requiring
100% screening, and escalation. Safety controls, protective-earth continuity,
fuses, leads, battery condition, and first-use board recovery are not silently
reduced to cosmetic sampling.

## Instrument checks

`Calibration` is reserved for a documented comparison that establishes a relation
to a reference with stated uncertainty. A function check or adjustment is not
called calibration.

| Asset | Before issue/use | Scheduled check | Quarantine condition |
|---|---|---|---|
| DMM | case/leads/fuse/current-jack visual; known source/resistor check | voltage, resistance, current protection, continuity against traceable or controlled reference | damaged lead/case, wrong fuse, unstable/out-of-tolerance result |
| oscilloscope | earth/lead condition, probe compensation, channel zero and known waveform | amplitude/timebase/channel comparison; USB export; earth continuity by qualified procedure | uncertain earth, cracked probe, compensation impossible, failed reference result |
| bench supply | leads, output-off behavior, set voltage/current limit before load | voltage/current readback, current-limit fold/response, output isolation as specified | overshoot or limit failure, damaged binding post, unsafe earth/isolation result |
| generator | leads, amplitude/offset/frequency into defined load | amplitude, offset, frequency, output impedance behavior | unexpected DC or amplitude capable of exceeding task limit |
| solder station | tip/cord/stand/extraction; temperature setting | protective-earth/tip test and temperature verification under institutional method | failed extraction/earth, damaged cord, uncontrolled temperature |
| debug/logic probe | cable/pinout and known-good target | identity, voltage limits, firmware/tool version, capture/program/recovery test | unknown pinout/voltage, failed known-good target, irreversible setting enabled |
| reference set | seal, environment, due date | external or internal traceability plan with uncertainty fit for teaching claim | expired, damaged, drift beyond control limit |

The asset record contains ID, make/model/MPN/serial, range and ratings, location,
test method/version, reference IDs and due dates, environmental conditions, raw
results, uncertainty where applicable, acceptance band, disposition, technician,
reviewer, and next due date. Overdue or failed items are electronically and
physically blocked from booking.

## Repair and replacement

- De-energize, identify all energy sources, and apply the activity risk assessment.
- Replace tips, probes, leads, fuses, cells, and connectors only with rated and
  approved parts; record part/lot and post-repair checks.
- Never bypass a fuse, protective earth, interlock, current limit, enclosure, or
  isolation barrier to return an item to teaching.
- Repair evidence includes symptom, diagnosis, measurements, parts, work performed,
  function/safety checks, limitations, and release authority.
- A repeated failure triggers supplier, design, handling, storage, training, and
  stock-level review, not only another replacement.

## Battery inspection and quarantine

Only protected/enclosed sources approved for the activity enter ordinary first-year
use. At issue and return, inspect enclosure, swelling, leakage, odor, heat,
connector damage, state-of-charge abnormality, impact/water exposure, and device
reports. Do not charge, press, puncture, short, dismantle, or transport a suspect
source as ordinary stock. Isolate the area, stop work, keep people clear, call the
named safety authority, and follow the institution's chemistry-specific fire,
ventilation, quarantine, transport, and disposal procedure. A generic metal box
is not assumed suitable for every battery or incident state.

## Replenishment and stock floors

At each issue/return cycle, update serviceable, in-use, repair, quarantine,
deliberate-fault, and consumed quantities. The reorder trigger is reached when:

`serviceable + accepted_on_order − reserved_demand <= reorder_floor`

The floor covers forecast demand during supplier lead time, quote approval,
payment, customs, receipt/quarantine, and a documented uncertainty margin. Weekly
alerts apply during teaching; monthly review applies otherwise. Expiry, shelf life,
moisture sensitivity, corrosion, battery condition, and obsolete revisions are
treated as unavailable even if physically present.

## Record minimums and review

No release is valid without the item/asset ID, method revision, raw observation or
measurement, acceptance criterion, result, executor, independent reviewer where
safety/accuracy warrants it, date, and evidence location. The laboratory director
reviews open quarantine and overdue-check lists monthly and before every practical.

