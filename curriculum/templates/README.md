# Teaching-resource templates

These templates instantiate the complete-course package in Course Master Document
§13.1. Copy a template; do not edit the template in place for a course. Every
course or unit manifest must list every resource type below and link either to an
artifact or to an approved
[`applicability-decision`](teaching-resources/applicability-decision.md). Absence
is not an applicability decision.

## Shared authoring contract

Every instantiated artifact starts with these fields (YAML front matter or the
equivalent structured record):

```yaml
semantic_id: ESE111-U04-LAB01
id: ESE111-U04-LAB01-en
resource_type: laboratory
language: en                     # en | fr | shared
paired_with: ESE111-U04-LAB01-fr # null only for language-neutral shared assets
title: "[descriptive title]"
version: 0.1.0
lifecycle: drafting
owners:
  content: "[name or accountable role]"
  technical: "[name or accountable role]"
  language: "[name or accountable role]"
outcomes: [ESE111-LO04]
prerequisites: [ESE111-LO03]
estimated_student_time_min: 120
safety_level: L1
localization_layer: universal-core # universal-core | deployment-pack | project-context
context_ids: []
claim_register: "[path or controlled ledger ID]"
contribution_dossier: null
license: CC-BY-SA-4.0
approval_facets:
  technical: {status: pending, evidence: null, reviewer: null, reviewed_on: null}
  safety: {status: pending, evidence: null, reviewer: null, reviewed_on: null}
  language: {status: pending, evidence: null, reviewer: null, reviewed_on: null}
  accessibility: {status: pending, evidence: null, reviewer: null, reviewed_on: null}
  license: {status: pending, evidence: null, reviewer: null, reviewed_on: null}
  build: {status: pending, evidence: null, reviewer: null, reviewed_on: null}
  apparatus: {status: pending, evidence: null, reviewer: null, reviewed_on: null}
  approval: {status: pending, evidence: null, reviewer: null, reviewed_on: null}
```

Use `not-applicable` on a facet only with a linked, approved rationale. Lifecycle
and facets follow [`content-lifecycle.md`](../workflows/content-lifecycle.md).
Technical values, equations, expected ranges, figures, rubrics, and safety limits
belong to the shared technical contract and must agree across languages.

## Required package inventory

| §13.1 type | Template |
|---|---|
| course guide/syllabus | [`course-syllabus.md`](teaching-resources/course-syllabus.md) |
| diagnostic/prerequisite check | [`prerequisite-diagnostic.md`](teaching-resources/prerequisite-diagnostic.md) |
| chapter | [`chapter.md`](teaching-resources/chapter.md) |
| lecture/studio plan | [`lecture-studio-plan.md`](teaching-resources/lecture-studio-plan.md) |
| slides | [`slides.md`](teaching-resources/slides.md) |
| demonstration | [`demonstration.md`](teaching-resources/demonstration.md) |
| guided exploration | [`guided-exploration.md`](teaching-resources/guided-exploration.md) |
| problem set | [`problem-set.md`](teaching-resources/problem-set.md) |
| worked solution | [`worked-solution.md`](teaching-resources/worked-solution.md) |
| laboratory experiment | [`laboratory.md`](teaching-resources/laboratory.md) |
| MCQ/item | [`mcq-item.yml`](teaching-resources/mcq-item.yml) |
| practical/design assessment | [`practical-design-assessment.md`](teaching-resources/practical-design-assessment.md) |
| professor notes | [`professor-notes.md`](teaching-resources/professor-notes.md) |
| milestone/project brief | [`project-brief.md`](teaching-resources/project-brief.md) |
| figure/source pack and reference artifacts | [`reference-artifact-metadata.yml`](teaching-resources/reference-artifact-metadata.yml) |
| remediation/enrichment paths | [`remediation-enrichment-map.md`](teaching-resources/remediation-enrichment-map.md) |
| technical claim/source register | [`claim-register.yml`](teaching-resources/claim-register.yml) |
| contribution/provenance dossier | [`contribution-dossier.md`](teaching-resources/contribution-dossier.md) |
| course QA record | [`course-qa-record.md`](teaching-resources/course-qa-record.md) |

The hands-on safeguard fields—`real_life_question`, `prediction`,
`student_action`, `physical_or_data_evidence`, `fault_or_anomaly`,
`design_decision`, and `acceptance_test`—must contain specific, reviewable
content wherever the resource teaches or assesses engineering action. Copying the
field names or writing “TBD” does not pass review.
