# Versioning, cohort freeze, and release control

**Control ID:** GOV-REL-001
**Owner:** configuration/release manager
**Approvers:** course owner, technical reviewer, EN and FR language editors; add
safety, accessibility, laboratory, license, assessment, and data owners when the
affected facets apply
**Review cadence:** each release and annually

## Version decision

The public program, course, and semantic teaching-unit contract use
`MAJOR.MINOR.PATCH`. EN and FR editions, public student artifacts, and controlled
instructor artifacts carry the same semantic version.

| Change | Increment | Examples | Additional action |
|---|---|---|---|
| No technical or assessment construct can change | PATCH | spelling, formatting, truly equivalent alt text, repaired non-semantic link | paired correction and ordinary regression |
| Compatible capability/content change; or technical correction | MINOR | approved hardware path, new formative items, corrected component value | learner-impact analysis, EN/FR reconciliation, cohort erratum and reassessment disposition |
| Contract change | MAJOR | outcome, prerequisite, credit, mastery rule, safety scope, summative construct | program-board decision, migration plan, revalidation |

A change is never a patch merely because its textual diff is small. Changed
numbers, equations, safety wording, expected ranges, answer keys, rubric rows,
allowed resources, or acceptance limits receive technical/assessment impact
review. Published raw data and evidence are superseded with provenance, never
silently overwritten.

## Lifecycle and release channels

The artifact lifecycle is defined independently from approval facets in the
controlled workbench lifecycle. Git release channels are:

- `workbench`: mutable authoring source; never assigned to a cohort;
- `pilot-ready`: controlled prerelease after the complete unit gate, zero open
  critical defects, second-instructor rehearsal, and formative EN/FR usability;
- `stable`: cohort-piloted, corrected release with declared accessibility and
  apparatus paths exercised;
- `retired`: preserved for reproducibility but excluded from new cohorts.

Tags use `vMAJOR.MINOR.PATCH` for program baselines and
`COURSE-vMAJOR.MINOR.PATCH` for independently released course packages. A tag is
created only from a signed release record containing the commit, manifest
checksum, approvers, known limitations, offline-bundle checksum, and restricted
artifact references—not restricted payload.

## Cohort freeze

Before teaching, record cohort ID, course/version, commit/tag, environment lock,
platform/hardware revisions, deployment profile, release date, owners, and
offline-bundle checksum. Freeze does not prevent corrections; it makes impact
visible. A delivery change states observation; affected assets/languages;
technical, safety, assessment, accessibility, schedule, and fairness impact;
version class/effective time; notice/support route; reassessment/regrading/
deadline disposition; approver; and effectiveness check.

## Urgent safety correction

Anyone may issue stop-work when material could cause harm. The safety owner or
delegate withdraws the affected artifact, identifies cohorts and apparatus,
publishes a plain EN/FR warning through the cohort's working channel, and blocks
energization/use. The release manager records corrected source/version,
incident/change note, evidence recheck, learner impact, replacement offline pack,
and reassessment decision. Safety action is immediate and is not delayed for a
release meeting, translation convenience, or version debate.

## Learner impact and migration

For every minor/major technical correction choose and approve exactly one:
`no_effect`, `clarification_only`, `regrade`, `targeted_reassessment`,
`full_reassessment`, or `evidence_voided_for_safety`. Notify affected EN/FR
pathways simultaneously and preserve original and corrected forms in the
controlled archive. A migration note names changed IDs/paths, required tool or
hardware updates, data transformation, rollback, and end-of-support date.

## Deprecation and retirement

Deprecation states replacement, reason, first warning version, last supported
cohort, safety/security implications, migration route, archive location, and
owner. Preserve source and reproducible outputs for the retention period. Remove
an artifact from navigation only after the active cohort and reassessment window
close; never delete evidence needed to explain a past judgment.

## Release record minimum

```yaml
release_id: ESE111-v1.0.0
channel: pilot-ready
commit: 40-character-git-object-id
cohorts: []
deployment_profile: BEN-EXAMPLE-2026.1
public_manifest_sha256: pending
offline_bundle_sha256: pending
restricted_references: []
facets:
  technical: {status: approved, approver: role-or-name, date: YYYY-MM-DD}
  safety: {status: approved, approver: role-or-name, date: YYYY-MM-DD}
  en: {status: approved, approver: role-or-name, date: YYYY-MM-DD}
  fr: {status: approved, approver: role-or-name, date: YYYY-MM-DD}
known_limitations: []
learner_impact: no_effect
migration_note: null
```
