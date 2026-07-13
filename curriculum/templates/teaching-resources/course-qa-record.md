---
qa_record_id: COURSE-RELEASE-QA-001
scope_id: COURSE-OR-UNIT-ID
resource_type: qa-record
version_under_review: 0.1.0
target_lifecycle: pilot-ready
record_status: open # open | approved | rejected | superseded
release_authority: "[role/name]"
opened_on: YYYY-MM-DD
closed_on: null
---

# Course/unit QA record

## Baseline and package completeness

Record commit/tag/archive checksum, EN/FR/offline build IDs, environment/tool
versions, manifest, full §13.1 inventory, artifact links, and approved
non-applicability decisions. State known limitations and supported deployment/
context/equipment/accessibility paths.

## Alignment and hands-on safeguard

| Outcome | Prerequisite | Learning activity | Individual/team evidence | Assessment/rubric | Result/evidence |
|---|---|---|---|---|---|
| [ID] | [IDs] | [artifact] | [artifact] | [rows] | [pass/defect] |

Confirm that applicable resources contain specific `real_life_question`,
`prediction`, `student_action`, `physical_or_data_evidence`, `fault_or_anomaly`,
`design_decision`, and `acceptance_test` content, and that context changes an
engineering requirement or decision.

## Lifecycle evidence

| State/gate | Required evidence | Evidence ID/date | Reviewer | Result/conditions |
|---|---|---|---|---|
| technically-verified | independent recomputation/source/code/simulation checks | [ID] | [name] | [result] |
| staff-piloted | second-instructor rehearsal and every physical path tested | [ID] | [name] | [result] |
| formative learner-usability pilot | intended EN/FR pathway learners; timing/language/cognitive load/access/apparatus | [ID] | [name] | [result] |
| cohort-piloted | broader small cohort including declared access/equipment paths | [ID] | [name] | [result] |

## Independent approval facets

| Facet | Status | Reviewer/qualification | Evidence/date | Defects/conditions | Expiry/trigger |
|---|---|---|---|---|---|
| technical | pending | | | | |
| safety | pending | | | | |
| language | pending | | | | |
| accessibility | pending | | | | |
| license | pending | | | | |
| build | pending | | | | |
| apparatus | pending | | | | |
| approval | pending | | | | |

No lifecycle transition makes a facet pass. `not-applicable` requires a linked
approved decision.

## Verification and pilots

Link claim register; independent calculations; compile/simulation/HDL/KiCad tests;
physical expected-range data for each apparatus path; safety review; EN/FR parity;
termbase/notation; accessible figures/media; licenses/originality; restricted-
content scan; offline build; engagement observations; instructor/learner/cohort
pilot protocols; defects and reruns.

## Defect and change disposition

| Defect/change ID | Severity | Affected EN/FR/shared assets | Construct/safety/access impact | Owner/due | Disposition and retest evidence | Approver |
|---|---|---|---|---|---|---|
| [ID] | critical/high/medium/low | [IDs] | [impact] | [owner/date] | [resolved/accepted/time-bounded] | [role] |

Target gates have zero open critical defects. Accepted residual defects state
impact, workaround, owner, due date, and authorized acceptance. Corrections to
technical contracts open paired-language issues and rerun affected approvals.

## Release decision

State approved/rejected target state, controlled channel, conditions, version/tag,
archive location/checksum, approver/date/signature reference, next review date/
trigger, and retirement/migration obligations if applicable.
