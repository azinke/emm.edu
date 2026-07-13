# Content workbench lifecycle and approval facets

This specification controls curriculum resources from first brief to retirement.
It implements the Course Master Document §§11 and 13.12–13.13 and the M02 workbench
contract. It applies to EN/FR editions, shared assets, instructor-only annexes, and
offline outputs.

## Two independent dimensions

`lifecycle` answers “how much production and real-use evidence does this artifact
have?” Approval facets answer “which authorities have accepted this exact
configuration for a stated purpose?” Advancing a lifecycle state never changes a
facet automatically. A facet can expire or reopen while the lifecycle remains the
same; a consequential defect can move an artifact back to an earlier state.

Use these machine-safe values:

```yaml
lifecycle: drafting
approval_facets:
  technical:
    status: pending # pending | in-review | approved | approved-with-conditions | rejected | expired | not-applicable
    reviewer: "[name and qualified role]"
    evidence: "[controlled record ID/link]"
    reviewed_on: YYYY-MM-DD
    review_due: YYYY-MM-DD
    conditions: []
```

## Lifecycle states and gates

| Order | Value | Meaning and minimum entry evidence | Exit authority |
|---:|---|---|---|
| 1 | `brief` | Stable semantic ID; audience; outcomes/prerequisites/downstream use; authentic question; misconceptions; safety/context layer; workload; required evidence; §13.1 applicability inventory and owners. | Content owner accepts the design brief. |
| 2 | `drafting` | At least one artifact is being authored against the shared technical contract; claims, equations/values, figures/data/code, apparatus capability, expected ranges, fault, decision, acceptance test, and EN/FR pairing are identified. | Content owner confirms a reviewable vertical slice. |
| 3 | `technically-verified` | A person other than the author independently recomputes/checks major claims; code/simulation/HDL/PCB checks run as applicable; citations/license candidates are inspected; safety limits and expected ranges are checked; both languages and shared assets are listed in the claim register. No unresolved critical technical or safety defect. | Qualified technical reviewer; safety approval remains a separate facet. |
| 4 | `staff-piloted` | A second prepared instructor rehearses the teaching sequence. Every claimed demo/lab/apparatus/substitute path has a physical pilot with configuration, raw data, expected range, setup/reset time, fault recovery, and safe-stop evidence. Simulation/prepared data does not certify personal physical competence. | Pilot lead accepts the staff-pilot record; apparatus and safety facets remain independent. |
| 5 | `formative-learner-usability-pilot` | Formative, non-cohort release with learners representing both intended EN and FR pathways. Evidence covers prerequisites, wording, timing, cognitive load, engagement, misconception movement, accessibility routes, equipment paths, and individual learner action. Exceptions are pre-release, owned, time-bounded, and block unrestricted use. | Pilot lead plus language/access reviewers accept the formative evidence. |
| 6 | `pilot-ready` | Controlled prerelease only. Vertical package is paired, reviewable, offline-buildable, physically tested, second-instructor rehearsed, and corrected after the formative usability pilot. Eight facets are approved or approved-with-conditions for the limited channel; zero open critical defects. A named authority approves version, cohort/scope, expiry, known limitations, archive/checksum, and support route. | Independent release authority. |
| 7 | `cohort-piloted` | The controlled baseline was used by a broader small cohort. Declared EN/FR, accessibility, and equipment routes were exercised; attainment/engagement, workload, incidents, apparatus failures, item behavior, support load, and defects were analyzed without overinterpreting small samples. | Cohort-pilot owner accepts findings and dispositions. |
| 8 | `release-candidate` | Cohort findings and consequential paired corrections are resolved or explicitly accepted; all affected tests/pilots/facets are rerun; full manifest, change log, migration notes, known limitations, offline archive, and stable-support dates are ready. Zero open critical defects. | Release manager nominates an immutable candidate. |
| 9 | `stable` | Independent authority approves the candidate for ordinary supported teaching. Both editions share semantic version and maturity; all required facets are current; broader cohort evidence covers declared paths; reproducible/offline outputs and support/review dates are published. | Stable-release authority. |
| 10 | `retired` | Use has ended because of supersession, hazard, unsupported dependency, invalid claim, license/access issue, or policy decision. The record states reason/effective date, replacement/remediation, affected cohorts, archive/retention rules, link behavior, and urgent safety communication if needed. Retired is terminal; revision receives a new version/state. | Release and records authority; safety authority joins urgent retirements. |

`pilot-ready` is not evidence of cohort success and must never be advertised as
`stable`. A state is recorded per exact version/configuration, not inherited by a
fork, translation, apparatus substitution, or changed assessment.

## Approval facets

| Facet | What must be accepted | Typical evidence and reopening triggers |
|---|---|---|
| `technical` | Claims, derivations, equations/values, code/HDL/simulation/PCB behavior, data interpretation, answer keys, model limits. | Independent check and claim register. Reopen for technical correction, source/version change, contradiction, failed expected range, or construct change. |
| `safety` | Hazard boundary, authorization/PPE, ratings, setup inspection, stop/recovery, substitutions, disposal, instructor competence. | Risk review and physical pilot. Reopen for incident/near miss, equipment/energy/procedure/site/standard change. |
| `language` | Natural EN and FR, controlled terms, identical technical contract/cognitive demand/points/timing, simultaneous correction. | Fluent pedagogical plus technical review, parity report, learner pilot. Reopen whenever meaning-bearing content changes. |
| `accessibility` | Semantic structure, keyboard/print/offline routes, alt text/captions/transcripts/long descriptions, non-color encoding, outcome-preserving accommodations. | Accessibility review and representative pathway pilot. Reopen for media/layout/apparatus/task change or reported barrier. |
| `license` | Originality/provenance, attribution, compatible permission/license, permitted archival/distribution, contributor/tool-output record. | Source/permission ledger and scans. Reopen for source replacement, license/terms change, new media/code/data, or dispute. |
| `build` | EN/FR HTML/PDF/slides and offline outputs reproducibly build; links/assets/restricted-content boundaries pass. | CI/local build logs, tagged environment, archive checksum. Reopen for dependency/config/source/format change or failed build. |
| `apparatus` | Each declared minimal/standard/advanced capability path is available, function-checked, physically piloted, safe, and outcome-equivalent; substitutes have measured effects. | Pilot data, inventory/profile IDs, calibration/function checks. Reopen for substitution, lifecycle/supply failure, lab move, or expected-range miss. |
| `approval` | Authorized scope, release channel/cohort, version, conditions, residual risk/defects, support and expiry are accepted. | Signed decision/QA record. Reopen when another facet expires/rejects, conditions fail, scope expands, or a critical defect appears. |

Use `not-applicable` only with an approved applicability decision that explains why
the concern cannot affect the artifact and names an expiry/review trigger. For
example, an apparatus facet may be not applicable to a prose-only course guide,
but not to a lab simply because equipment has not arrived.

## Transition procedure

1. The owner requests one target state for an immutable baseline and links the QA
   record, manifest, paired assets, claim register, build/archive IDs, and defects.
2. Reviewers decide their facet independently; conditions state owner, due date,
   scope, expiry, and learner/safety impact.
3. The transition authority checks the state gate and facet requirements. It never
   accepts a majority vote over a rejected safety, technical, or release approval.
4. The release manager records old/new state, version/commit, authority/date,
   evidence, conditions, and change log. EN and FR advance together.
5. Any affected automated and human check is rerun after correction. A technical
   correction opens a paired-language issue even if only one edition revealed it.

## Defects, rollback, and WIP limits

- Critical means risk of harm, invalid construct/answer, dishonest attribution or
  provenance, exposed restricted content, unusable required access path, or a
  materially wrong engineering claim. Target release gates require zero open
  critical defects.
- High/medium/low residual defects may be accepted only by named authority with
  impact, workaround, owner, due date, and expiry. Silence is not disposition.
- Reopen the earliest state whose evidence is invalidated. Examples: changed lab
  hardware usually returns to `technically-verified` before a new staff pilot; a
  prose typo can remain stable after paired correction and proportional checks.
- Stop opening new units when technical review, translation, physical pilot,
  accessibility, or defect queues cannot keep pace. Finish a defensible vertical
  unit before expanding horizontal inventory.

## Minimum audit event

Every transition record contains artifact and semantic IDs, old/new state,
version/commit/archive checksum, EN/FR parity version, requested/decided dates,
requester and authority, each facet status/evidence, open defects/conditions,
context/equipment profiles, review/expiry triggers, and links to superseded events.
