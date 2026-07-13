# Laboratory inventory and procurement control

**Document set:** ESE-LAB-PROC-001  
**Status:** controlled planning baseline; deployment qualification pending  
**Owner:** procurement lead  
**Required approvers:** laboratory director, safety officer, finance authority  
**Review cycle:** before every cohort freeze and whenever a quote, board revision,
supplier, safety limit, or cohort size changes

This directory implements the inventory, bench, maintenance, design-pack, and
total-cost controls required by M03-E3. It is a universal process layer. It does
not assert that a Benin supplier, facility, instrument, technician, or price has
been qualified.

## Controlled workflow

1. Name the real cohort and simultaneous laboratory-section sizes in an approved
   cohort plan. A planning scenario is never relabeled as an enrolled cohort.
2. Select items by functional specification. Record manufacturer part number
   (MPN) and revision where performance, safety, tooling, or interchangeability
   depends on the exact item.
3. Obtain independent quotes from at least two viable channels. Preserve the
   source currency, XOF landed value, exchange-rate source/date, tax, duty,
   freight, payment constraints, lead time, and quote validity.
4. Qualify samples and substitutes before freezing the cohort BOM. A lower price
   cannot override learning visibility, safe fault energy, repairability, offline
   operation, debug access, or counterfeit risk.
5. Generate quantities and the total-cost model. Review bench throughput and
   each learner's physical-access entitlement, not only total item count.
6. Receive into quarantine, inspect, function-check, label, and release to the
   appropriate inventory state.
7. Track calibration/function-check due dates, repairs, consumption, reorder
   floors, battery condition, and disposal.

## Files and evidence boundaries

- [inventory-quantity-model.md](inventory-quantity-model.md) defines quantity
  classes, formulas, labels, stock states, and cohort acceptance.
- [procurement-register-template.csv](procurement-register-template.csv) contains
  every required item, source, lifecycle, cost, and test field.
- [qualification-maintenance-and-stock-control.md](qualification-maintenance-and-stock-control.md)
  controls receipt, calibration/function checks, repair, batteries, and stock.
- [bench-build-and-verification.md](bench-build-and-verification.md) specifies
  minimal and standard bench assembly and release tests.
- [reproducible-design-packs.md](reproducible-design-packs.md) defines locally
  reproducible cables, fixtures, deliberate-fault boards, harnesses, enclosure
  samples, and jigs plus technician qualification.
- [total-cost-and-access-model.md](total-cost-and-access-model.md) defines the
  full-cost and per-student scheduling model.
- `curriculum/scripts/plan_lab_inventory.py` produces deterministic quantities
  from a reviewed cohort input and catalog.

Templates and passing software tests establish the control system only. The
following remain deployment evidence: named cohort approval, supplier quotes,
sample inspection, physical bench verification, calibration traceability,
technician performance, funded purchase order, and disposal agreement.

