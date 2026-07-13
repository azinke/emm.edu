# Technical and contextual claim-verification guide

Every consequential curriculum claim must be derivable, testable, or cited and
must state its domain. This guide governs authoring, independent review, pilot
measurements, currency review, and paired EN/FR correction. Use the
[`claim-register`](../templates/teaching-resources/claim-register.yml) for records.

## Classify before verifying

| Claim class | Examples | Minimum verification pattern | Currency rule |
|---|---|---|---|
| `concept-stable` | KCL derivation under lumped-circuit assumptions; dimensional relation | Independent derivation/recomputation; authoritative reference when attribution/history matters | Review when model/domain or pedagogy changes |
| `platform-bound` | pin function, SDK support, board ADC behavior, tool command | Exact manufacturer/project primary documentation plus test on named hardware/tool version | Dated review and trigger on hardware/tool/firmware revision, support or lifecycle change |
| `standard-bound` | symbol convention, test method, EMC limit | Applicable official standard edition and scope; qualified interpretation where needed | Edition/amendment/withdrawal trigger; never imply certification from teaching alignment |
| `regulation-bound` | radio, electrical, data, product-origin requirement | Current official legal/regulatory text and qualified local applicability decision | Jurisdiction and effective-date record; trigger on law/guidance/authority/scope change |
| `contextual-empirical` | local supply, cost, environment, user/service constraint, historical event | Approved context method/source, dated bounded sample/record, uncertainty and non-generalization | Context owner, review date, new field/supplier/price/event evidence trigger |
| `frontier-annual` | state-of-practice capability, emerging research/tool claim | Primary research/official project evidence, comparison/replication where feasible, limitations | At least annual review and trigger on contradictory or superseding evidence |

Claim consequence controls rigor. A safety limit, live assessment answer, public
origin statement, or field-fitness claim needs stronger independent authority and
evidence than a low-stakes illustrative estimate.

## Source hierarchy

Use the closest authoritative source that can support the exact wording:

1. applicable official law/regulator publication, current standard, manufacturer
   datasheet/errata/reference manual, protocol specification, original dataset,
   source repository/release, or primary research;
2. authoritative institutional technical guidance or well-documented replication;
3. scholarly review, specialist handbook, or textbook for synthesis/pedagogy;
4. distributor pages, tutorials, media, community discussion, or generated text
   only as discovery leads or clearly bounded experience—not authority for device
   limits, regulation, safety, or current support.

Authority is not enough: verify jurisdiction/device/revision, applicability,
conditions, exact table/section/page, effective date, and whether later errata or
amendments exist. Record access/license terms; an archived copy is kept only when
permitted, with checksum.

## Independent recomputation and technical reproduction

The checker is not the original author and does not begin from the author's final
number alone. They:

1. restate the claim and decision consequence;
2. recover inputs from cited primary material/raw data and verify units,
   transcription, configuration, and version;
3. select/derive the model independently, name assumptions and domain, and compute
   with a separate method or implementation where practical;
4. test limiting cases, sign/polarity, dimensional consistency, order of magnitude,
   tolerance/worst case, numerical precision, and sensitivity;
5. compare result and discrepancy against a predeclared acceptance rule;
6. compile/run/simulate/measure on the named environment or hardware where the
   claim depends on behavior, retaining logs/raw data;
7. record pass, qualified pass, or defect plus limitations and affected assets.

“Looks reasonable,” peer proofreading, or rerunning the author's opaque spreadsheet
is not independent recomputation.

## Datasheets, standards, and regulations

- Record manufacturer/issuer, title, device/document ID, revision/edition,
  publication/effective date, exact locator, retrieval date, and errata/amendments.
- Distinguish absolute maximum from recommended operating conditions and typical
  from guaranteed values. Capture test conditions, temperature, supply, load,
  frequency, package, grade, and population basis.
- Do not cite a distributor summary when the current manufacturer document is
  available. Qualify clone/variant devices separately.
- For standards, distinguish “informed by,” “tested using,” “conforms to,” and
  “certified to.” A classroom exercise normally supports only the first two unless
  competent authority and full scope establish more.
- For regulations, record jurisdiction, product/activity/data category, actor,
  effective date, exemptions, responsible authority, and a qualified applicability
  decision. Do not transplant one country's conclusion to another.
- Avoid reproducing restricted standards or copyrighted tables beyond permission;
  cite the controlled copy and provide author instructions that remain usable by
  authorized readers.

## Historical and context sourcing

Source claims about inventors, dates, communities, industry, costs, infrastructure,
needs, customary practice, and local capability. Separate:

- observed/measured fact with method/date/sample;
- stakeholder statement and speaker/consent context;
- documented historical interpretation;
- engineering assumption to test;
- illustrative fictional scenario clearly labeled as such.

Triangulate consequential contextual claims and preserve disagreement. Do not
generalize a site, partner, small sample, or country to a continent or population.
Context should change a requirement; it must not become decorative deficit
narrative. Price/supply claims record currency, tax/shipping/landed-cost basis,
supplier, date, quantity, and uncertainty.

## Expected-range measurement

Instructor materials use a range derived before the pilot—not a fictitious exact
number reverse-engineered from one “golden” unit.

1. Define measurand, configuration, method, instruments/probes, function checks or
   calibration status, environment, sample/repetition, and acceptance decision.
2. Predict nominal and bounds from model, guaranteed/characterized component
   limits, source/load/probe effects, tolerance, quantization, repeatability, and
   relevant uncertainty.
3. Pilot every declared minimal/standard/advanced and substitute path. Retain raw
   results, configuration, anomalies, units, sample count, and processed method.
4. Compare observed distribution/range with prediction. Investigate outliers;
   revise model, procedure, apparatus, or acceptance rule with documented reason.
5. Publish an honest instructor range and conditions. Do not imply population
   yield, reliability, or field qualification from a small teaching pilot.

## Review-due dates and event triggers

Set both a scheduled date and meaningful event triggers for platform-, standard-,
regulation-, price-, context-, and frontier-bound claims. Triggers include:

- new datasheet/erratum/hardware/tool/firmware revision or end-of-support notice;
- standard amendment, withdrawal, or interpretation; law/regulator/jurisdiction or
  product-scope change;
- supplier, price, currency, tax/shipping, availability, facility, context, or
  deployment-profile change;
- measured result outside expected range, reproducibility failure, incident/near
  miss, learner report, external contradiction, or upstream claim correction;
- change in product configuration, contributor/process/location, or origin law;
- annual frontier scan or ordinary scheduled review, whichever occurs first.

An overdue claim blocks the release gate that depends on it. “Reviewed once” is not
a permanent status.

## Simultaneous EN/FR correction

1. Open one paired issue listing claim ID and every affected EN, FR, and shared
   artifact—including answers, captions, alt text, data, slides, rubrics, and
   offline outputs.
2. Quarantine or visibly qualify the unsafe/materially wrong artifact; use urgent
   learner-impact/safety communication when required.
3. Correct the shared technical contract first, then author natural corrections in
   both languages. Do not patch only the edition where the defect was reported.
4. Rerun independent technical, safety, parity, build, apparatus, and assessment
   checks proportional to the change. Re-pilot when construct, safety, apparatus,
   access, language clarity, or timing may have changed.
5. Release both editions under one version, update register/change log/offline
   archive, notify affected cohorts/instructors, and record superseded evidence.

## Claim reviewer decision

A claim passes only when wording matches evidence, source/version and conditions
are traceable, independent verification is complete, limitations are visible,
context/contribution records are linked where applicable, both languages are
covered, and review due/trigger and accountable owner are present.
