# M02 — Content Operations and Repository Foundation

**Goal:** build the Markdown-first, bilingual, testable, offline-capable production system before multiplying course content.

**Indicative duration:** 6–10 weeks  
**Primary owners:** release manager, learning-content architect, tooling engineer, bilingual editors  
**Depends on:** M00; incorporates M01 identifiers and local fields  
**Authoring entry:** M00 approves repository/release authority and M01 supplies deployment-field requirements plus representative records\
**Release gate:** applicable M01 locale, jurisdiction, context, and capability fields are instantiated and validated\
**Exit unlocks:** M04 and all content-production milestones

## Epic E1 — Instantiate canonical curriculum data

- [ ] **M02-E1-T01 [SPEC]** Create `outcomes.yml` with PEO/PLO/course outcome IDs, definitions, progression levels, and evidence mappings.
- [ ] **M02-E1-T02 [SPEC]** Create `prerequisite-graph.yml` with requires, co-requires, unlocks, G1–G9 program competence gates, remediation, and validation against cycles/orphans.
- [ ] **M02-E1-T03 [SPEC]** Create `termbase.yml` from the master glossary with definitions, alternatives, avoided terms, acronym policy, examples, status, and reviewers.
- [ ] **M02-E1-T04 [SPEC]** Create platform, component, project, context, deployment-profile/jurisdiction, local manufacturing capability, supplier/cost, facility, V0–V4 contribution, claim/source, safety, assessment, course-manifest, and unit-manifest schemas.
- [ ] **M02-E1-T05 [TEST]** Add validation for IDs, links, dependency cycles, missing mappings, invalid statuses, and stale paired-language records.
- [ ] **M02-E1-T06 [SPEC]** Generate a child backlog from every canonical course/unit manifest, including each resource, EN/FR edition, approval facet, apparatus path, instructor/learner pilot, defect disposition, evidence link, and approver.
- [ ] **M02-E1-T07 [TEST]** Enforce universal-core versus deployment-profile separation and require context IDs, claim review dates, and contribution/provenance evidence where applicable.

## Epic E2 — Create authoring templates and guides

- [ ] **M02-E2-T01 [MAT]** Implement every §13.1 type: syllabus, prerequisite diagnostic, chapter, lecture/studio plan, slides, demonstration, exploration, pset, solution, lab, MCQ/item, practical/design assessment, professor notes, project, figure/reference-artifact metadata, remediation/enrichment map, claim register, contribution dossier, and QA record; use an approved applicability decision rather than silent omission.
- [ ] **M02-E2-T02 [MAT]** Publish EN and FR style guides, notation rules, schematic conventions, citation/originality rules, and accessible-figure guidance.
- [ ] **M02-E2-T03 [MAT]** Publish author instructions for the hands-on cycle, real-life context briefs, misconception design, seeded faults, and evidence ladders.
- [ ] **M02-E2-T04 [SPEC]** Implement the workbench lifecycle—brief, drafting, technically verified, staff-piloted, formative learner-usability pilot, pilot-ready controlled prerelease, cohort-piloted, release candidate, stable, and retired—while tracking technical, safety, language, accessibility, license, build, apparatus, and approval facets independently.
- [ ] **M02-E2-T05 [MAT]** Provide good/bad examples showing decorative context versus requirement-changing context and recipe lab versus inquiry/design lab.
- [ ] **M02-E2-T06 [MAT]** Publish the claim-verification guide: source hierarchy, independent recomputation, datasheet/standard/regulation versions, historical/context sourcing, expected-range measurement, review-due triggers, and simultaneous EN/FR correction.
- [ ] **M02-E2-T07 [MAT]** Publish the vertical-unit workflow, engagement acceptance criteria, local contribution/origin language guide, and examples of equivalent minimal/standard/advanced evidence.

## Epic E3 — Build publishing and test automation

- [ ] **M02-E3-T01 [TEST]** Configure separate EN/FR HTML, printable PDF, and slide builds from Markdown/Quarto-family source.
- [ ] **M02-E3-T02 [TEST]** Validate paired files, outcomes, equations/values, safety limits, rubric totals, glossary usage, links, alt text, captions, and restricted-content leakage.
- [ ] **M02-E3-T03 [TEST]** Add code, numerical-example, HDL, simulation, and KiCad smoke-test hook interfaces; complete and seed-test the KiCad implementation in T07 before M10 entry.
- [ ] **M02-E3-T04 [TEST]** Create local/offline build path and test it on lowest-supported student hardware and operating systems.
- [ ] **M02-E3-T05 [SPEC]** Define external-link capture, citation metadata, retrieval date, permitted archival copy, checksum, and license handling.
- [ ] **M02-E3-T06 [TEST]** Add bilingual font/math/schematic rendering, print pagination, low-bandwidth size budget, and visual-regression checks on supported devices.
- [ ] **M02-E3-T07 [TEST]** Implement the KiCad/ERC/DRC/release hook contract before M10 entry; name owner, tested version, waiver format, and fixture for a seeded failing project.

## Epic E4 — Versioning, review, and restricted material

- [ ] **M02-E4-T01 [DEC]** Adopt semantic versioning, cohort freezes, change logs, migration notes, urgent safety-correction and learner-impact procedures, and deprecation rules; reserve patch releases for changes that cannot alter a technical or assessment construct.
- [ ] **M02-E4-T02 [SPEC]** Configure a separately permissioned repository/store for solutions, live assessments, student data, and partner-confidential data so restricted content never enters public Git history; expose only controlled artifact references.
- [ ] **M02-E4-T03 [SPEC]** Create pull-request/review checklists for technical, physical-pilot, safety, bilingual, accessibility, license, and build approval.
- [ ] **M02-E4-T04 [TEST]** Perform backup/restore and complete offline-clone drills.
- [ ] **M02-E4-T05 [MAT]** Qualify authors/reviewers through a complete non-assessed vertical sample—claim register through build, physical test, review, revision, and release—and create a train-the-trainer route.
- [ ] **M02-E4-T06 [DEC]** Select licenses and contributor terms for original prose/media, code, HDL, hardware/PCB, data, fonts, and third-party contributions; record SPDX-compatible identifiers where applicable.

## Hands-on and real-life safeguard

The templates and validators must require fields for `real_life_question`, `prediction`, `student_action`, `physical_or_data_evidence`, `fault_or_anomaly`, `design_decision`, and `acceptance_test`. Empty or boilerplate fields fail content review. The build cannot judge pedagogical quality, so reviewers must confirm the context changes calculations, architecture, test, cost, safety, or lifecycle.

## Required deliverables

- Canonical structured curriculum data and schemas
- All teaching-resource templates and style/review guides
- EN/FR web/PDF/slide build and automated QA
- Offline authoring/build bundle
- Version, access, backup, and release workflows

## Exit criteria

- [ ] A new author can create, pair, review, build, and revise a sample unit from documentation alone.
- [ ] The build intentionally catches seeded parity, link, accessibility, answer-key, and restricted-content defects.
- [ ] Offline clone/build/restore works on supported machines.
- [ ] M04 can produce the exemplar without inventing workflow or metadata.
