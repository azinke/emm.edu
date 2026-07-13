# Curriculum author quickstart

This path takes a new author from an approved manifest to a reviewed bilingual
workbench unit. It does not waive the physical, human, safety, language, or
release approvals in the master document.

## 1. Confirm authority and scope

Read the Course Master Document invariants, the current workbench milestone,
`data/course-manifests.yml`, `data/unit-manifests.yml`, and the applicable dated
deployment profile. Do not invent a jurisdiction, supplier, price, facility,
participant, or local-origin fact when its mapping is pending.

Select a stable unit/resource child from
`backlog/canonical-child-backlog.yml`. Confirm its outcome, prerequisites,
downstream use, resource applicability, language pair, apparatus path, owners,
and approval facets. Restricted work is created only in the separately
permissioned store.

## 2. Brief before drafting

Use `templates/README.md` to select every required §13.1 resource type and record
an approved applicability decision for any omission. Complete the authentic
question and all hands-on safeguard fields with substantive, reviewable content:

- `real_life_question`
- `prediction`
- `student_action`
- `physical_or_data_evidence`
- `fault_or_anomaly`
- `design_decision`
- `acceptance_test`

Open the claim register before exposition. A dated/current claim needs a primary
source, version/retrieval date, owner, verification, affected EN/FR assets, and
review trigger. Universal content cannot carry an unversioned deployment fact.

## 3. Build one vertical bilingual unit

Follow `guides/vertical-unit-workflow.md`: design the evidence and exit check,
freeze the shared technical contract, then author natural EN and FR explanations
with shared equations, values, safety limits, ranges, figures, data, and rubric.
Use the style guides and termbase; do not translate code/tool tokens. Include
prediction, observable action, anomaly diagnosis, evidence-driven decision, and
acceptance test rather than a passive recipe.

Advance the lifecycle state only when its prerequisites are true. Technical,
safety, language, accessibility, license, build, apparatus, and approval facets
remain independent; a strong facet cannot compensate for a failed safety or
parity facet.

## 4. Validate locally without network

```sh
python3 curriculum/scripts/validate_canonical.py --as-of 2026-07-13
python3 curriculum/scripts/qa_content.py --offline
python3 curriculum/scripts/build_publications.py --engine auto --offline
python3 curriculum/scripts/run_smoke_hooks.py
python3 curriculum/scripts/check_outputs.py
```

Use the locked Pandoc route as offline recovery when Quarto is unavailable. A
release still requires the declared Quarto build. Never weaken a failing check
to make content appear complete; correct the source or record a narrowly scoped,
owned, expiring waiver where policy explicitly permits one.

## 5. Review, pilot, revise, and release

Complete `governance/review-checklist.md`. Independently recompute technical
work; physically test every declared apparatus path; run EN and FR technical and
pedagogical review; inspect accessibility, licensing, generated output, offline
size, and restricted leakage. A second prepared instructor and formative
learners from both intended language pathways are required before `pilot-ready`.
A broader cohort exercises declared accessibility/apparatus paths before
`stable`.

Disposition every defect with impact, owner, due date, evidence, and authority.
Rerun affected checks, update the paired edition, claims, change log, learner-
impact/migration note, manifest and checksums, then create the controlled release
record. Version and freeze the cohort according to
`governance/versioning-and-release.md`.

## Recovery

If the network is unavailable, all ordinary authoring, canonical QA, build,
smoke hooks, and internal-link checks use the installed bundle. External link
health is a scheduled networked check; source metadata and permitted archival
copies keep ordinary builds independent of it. Recovery drills follow
`governance/backup-restore.md`.
