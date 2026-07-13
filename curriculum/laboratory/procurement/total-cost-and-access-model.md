# Total-cost and per-student access model

**Control ID:** ESE-LAB-PROC-006  
**Planning currency for Benin profile:** XOF, with original source currency retained  
**Evidence rule:** blank or expired local quotes keep the budget `quote-required`

## Cost boundary

For each minimal, standard, and advanced/shared-regional path and each named cohort,
calculate:

`TCO = acquisition + landed + enablement + annual_operation + lifecycle + contingency`

where the model separately records:

- boards, components, instruments, fixtures, furniture, storage, computers, local
  server/offline media, networking, and accessible equipment;
- source price/currency; dated exchange rate/source; XOF tax, duty, brokerage,
  freight, insurance, payment/transfer, and local delivery;
- incoming inspection, calibration/reference services, installation, ventilation,
  ESD, fire/first aid, security, and power backup;
- consumables, tips/probes/fuses/leads, batteries, spares, repairs, replacement,
  software/support where unavoidable, and partner/shared-facility fees/travel;
- laboratory director, safety officer, technician, instructor, procurement, IT,
  accessibility, translation, training, setup, issue/return, maintenance, and
  remediation time using institution-approved fully burdened rates;
- storage loss, shelf-life/obsolescence, hazardous/general waste, data sanitization,
  disposal/recycling, and end-of-life transport;
- risk contingency tied to evidence, never an undisclosed percentage used to hide
  missing quotes.

Capital and recurring costs remain separate. Shared equipment uses documented life,
utilization, repair history, residual value policy, and replacement cycle. Per-student
figures state cohort size and allocation method; they do not imply that dividing a
single unavailable instrument creates access.

## Quote and conversion record

For every channel retain supplier identity, exact MPN/revision and quantity break,
quote/invoice, date and validity, source currency, payment terms, Incoterm where
relevant, transport/customs assumptions, exchange-rate publisher and observation
date, conversion formula, each landed-cost component, lead-time basis, authenticity
and lifecycle evidence, warranty/return path, and reviewer. Use at least two viable
channels for critical teaching items. A marketplace listing without fulfillment,
authenticity, revision, and landed-cost evidence is not a qualified channel.

## Access/throughput proof

For every mandatory physical practical create a schedule row with:

| Field | Required proof |
|---|---|
| outcome and personal evidence | exact construction, measurement, instrumentation, debugging, or defense each learner performs |
| authorization | current level/gate, briefing, supervision ratio, accessibility route |
| apparatus | path and quantity of serviceable stations; setup/changeover time |
| demand | learners, attempts, remediation/reschedule reserve, time per attempt |
| capacity | stations × staffed periods × usable minutes minus setup/failure reserve |
| named timetable | room, period, staff, group assignment, and individual evidence capture |
| fallback | repair/spare/rotation/partner route that preserves the same evidence |

Capacity passes only when every learner, including planned remediation, can complete
the personal evidence before progression decisions. Prepared data may preserve an
analysis lesson; it contributes zero capacity toward personal construction,
measurement, or debugging certification.

## Reorder floor and trigger

For consumable or high-failure item `i`:

`floor_i = ceiling(daily_peak_use_i × protected_lead_time_days_i + remediation_reserve_i + uncertainty_reserve_i)`

Protected lead time includes approval, payment, supplier, transport, customs,
incoming quarantine, and test. Trigger ordering when projected serviceable balance
at arrival is at or below the floor. Review weekly during cohort delivery and after
any abnormal failure, substitution, supplier, currency, or timetable change.

## Approval decision

The finance authority, laboratory director, safety officer, and procurement lead
approve a path only when costs are current, the room/facility is qualified, staff
time is funded, physical-access capacity passes, safety-critical spares and disposal
are covered, and unresolved M01 jurisdiction/supply assumptions have written
dispositions. Otherwise state the funded shortfall and affected course/outcome;
do not release the practical on optimism.

