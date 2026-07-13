# M02 — Content Operations and Repository Foundation

**Goal:** build the Markdown-first, bilingual, testable, offline-capable production system before multiplying course content.

**Indicative duration:** 6–10 weeks  
**Primary owners:** release manager, learning-content architect, tooling engineer, bilingual editors  
**Depends on:** M00; incorporates M01 identifiers and local fields  
**Authoring entry:** M00 approves repository/release authority and M01 supplies deployment-field requirements plus representative records\
**Release gate:** applicable M01 locale, jurisdiction, context, and capability fields are instantiated and validated\
**Exit unlocks:** M04 and all content-production milestones

## Epic E1 — Instantiate canonical curriculum data

- [x] **M02-E1-T01 [SPEC]** Create `outcomes.yml` with PEO/PLO/course outcome IDs, definitions, progression levels, and evidence mappings.
- [x] **M02-E1-T02 [SPEC]** Create `prerequisite-graph.yml` with requires, co-requires, unlocks, G1–G9 program competence gates, remediation, and validation against cycles/orphans.
- [x] **M02-E1-T03 [SPEC]** Create `termbase.yml` from the master glossary with definitions, alternatives, avoided terms, acronym policy, examples, status, and reviewers.
- [x] **M02-E1-T04 [SPEC]** Create platform, component, project, context, deployment-profile/jurisdiction, local manufacturing capability, supplier/cost, facility, V0–V4 contribution, claim/source, safety, assessment, course-manifest, and unit-manifest schemas.
- [x] **M02-E1-T05 [TEST]** Add validation for IDs, links, dependency cycles, missing mappings, invalid statuses, and stale paired-language records.
- [x] **M02-E1-T06 [SPEC]** Generate a child backlog from every canonical course/unit manifest, including each resource, EN/FR edition, approval facet, apparatus path, instructor/learner pilot, defect disposition, evidence link, and approver.
- [x] **M02-E1-T07 [TEST]** Enforce universal-core versus deployment-profile separation and require context IDs, claim review dates, and contribution/provenance evidence where applicable.

## Epic E2 — Create authoring templates and guides

- [x] **M02-E2-T01 [MAT]** Implement every §13.1 type: syllabus, prerequisite diagnostic, chapter, lecture/studio plan, slides, demonstration, exploration, pset, solution, lab, MCQ/item, practical/design assessment, professor notes, project, figure/reference-artifact metadata, remediation/enrichment map, claim register, contribution dossier, and QA record; use an approved applicability decision rather than silent omission.
- [x] **M02-E2-T02 [MAT]** Publish EN and FR style guides, notation rules, schematic conventions, citation/originality rules, and accessible-figure guidance.
- [x] **M02-E2-T03 [MAT]** Publish author instructions for the hands-on cycle, real-life context briefs, misconception design, seeded faults, and evidence ladders.
- [x] **M02-E2-T04 [SPEC]** Implement the workbench lifecycle—brief, drafting, technically verified, staff-piloted, formative learner-usability pilot, pilot-ready controlled prerelease, cohort-piloted, release candidate, stable, and retired—while tracking technical, safety, language, accessibility, license, build, apparatus, and approval facets independently.
- [x] **M02-E2-T05 [MAT]** Provide good/bad examples showing decorative context versus requirement-changing context and recipe lab versus inquiry/design lab.
- [x] **M02-E2-T06 [MAT]** Publish the claim-verification guide: source hierarchy, independent recomputation, datasheet/standard/regulation versions, historical/context sourcing, expected-range measurement, review-due triggers, and simultaneous EN/FR correction.
- [x] **M02-E2-T07 [MAT]** Publish the vertical-unit workflow, engagement acceptance criteria, local contribution/origin language guide, and examples of equivalent minimal/standard/advanced evidence.

## Epic E3 — Build publishing and test automation

- [x] **M02-E3-T01 [TEST]** Configure separate EN/FR HTML, printable PDF, and slide builds from Markdown/Quarto-family source.
- [x] **M02-E3-T02 [TEST]** Validate paired files, outcomes, equations/values, safety limits, rubric totals, glossary usage, links, alt text, captions, and restricted-content leakage.
- [x] **M02-E3-T03 [TEST]** Add code, numerical-example, HDL, simulation, and KiCad smoke-test hook interfaces; complete and seed-test the KiCad implementation in T07 before M10 entry.
- [ ] **M02-E3-T04 [TEST]** Create local/offline build path and test it on lowest-supported student hardware and operating systems.
- [x] **M02-E3-T05 [SPEC]** Define external-link capture, citation metadata, retrieval date, permitted archival copy, checksum, and license handling.
- [x] **M02-E3-T06 [TEST]** Add bilingual font/math/schematic rendering, print pagination, low-bandwidth size budget, and visual-regression checks on supported devices.
- [x] **M02-E3-T07 [TEST]** Implement the KiCad/ERC/DRC/release hook contract before M10 entry; name owner, tested version, waiver format, and fixture for a seeded failing project.

## Epic E4 — Versioning, review, and restricted material

- [x] **M02-E4-T01 [DEC]** Adopt semantic versioning, cohort freezes, change logs, migration notes, urgent safety-correction and learner-impact procedures, and deprecation rules; reserve patch releases for changes that cannot alter a technical or assessment construct.
- [ ] **M02-E4-T02 [SPEC]** Configure a separately permissioned repository/store for solutions, live assessments, student data, and partner-confidential data so restricted content never enters public Git history; expose only controlled artifact references.
- [x] **M02-E4-T03 [SPEC]** Create pull-request/review checklists for technical, physical-pilot, safety, bilingual, accessibility, license, and build approval.
- [x] **M02-E4-T04 [TEST]** Perform backup/restore and complete offline-clone drills.
- [ ] **M02-E4-T05 [MAT]** Qualify authors/reviewers through a complete non-assessed vertical sample—claim register through build, physical test, review, revision, and release—and create a train-the-trainer route.
- [x] **M02-E4-T06 [DEC]** Select licenses and contributor terms for original prose/media, code, HDL, hardware/PCB, data, fonts, and third-party contributions; record SPDX-compatible identifiers where applicable.

## Implementation and verification record — 2026-07-13

**Implementation commit:** `bef01747883c0982b2b68f5ece1f7d77f5a7e528`
**Evidence rule:** a checked item has committed repository evidence and its stated
automated/specification result. Physical, institutional, production-access, or
human qualification evidence is not inferred from a template, synthetic fixture,
CI configuration, or high-capacity development host.

### E1 — Canonical data

- `curriculum/data/outcomes.yml` contains 5 PEOs, 14 PLOs, 46 course outcomes,
  progression levels, evidence, and mappings.
- `curriculum/data/prerequisite-graph.yml` contains 64 nodes, 134 `requires`
  relations, co-requisites, unlocks, remediation, and G1–G9.
- The sole authoritative `curriculum/i18n/termbase.yml` contains 147 controlled
  concepts derived from the master glossary. Twenty Draft 2020-12 schemas cover
  outcomes, prerequisite graph, termbase, manifests, deployment/context,
  platform/component/project, manufacture/cost/facility, contribution/provenance,
  claim/source, safety, assessment, and backlog records.
- The deterministic child backlog contains 940 resource children with EN/FR
  editions, eight independent approval facets, apparatus routes, instructor and
  learner pilots, defects, evidence links, and approvers.
- Generator drift, canonical validation, and three unit tests pass. Seven seeded
  records prove detection of a dependency cycle, unknown mapping, invalid status,
  stale language pair, missing context, unsupported origin/provenance, and a
  boilerplate hands-on contract. The dated Benin profile remains explicitly
  `mapping-in-progress` rather than asserting unsupported local facts.

### E2 — Authoring system

- Twenty templates implement every §13.1 type plus the mandatory applicability
  decision. Templates and guides require substantive hands-on safeguard fields,
  shared technical contracts, natural paired editions, claims, evidence,
  apparatus equivalence, accessibility, licensing, pilots, and independent
  facets.
- The EN/FR style guides, technical conventions, learning-experience guide,
  good/bad context and lab examples, claim-verification guide, vertical workflow,
  engagement acceptance, apparatus evidence, local contribution/origin language,
  and ten-state lifecycle are published under `curriculum/`.
- YAML/front matter parses, local links resolve, offline course-source QA reports
  zero errors/warnings, and `git diff --check` passes.

### E3 — Publishing and automated QA

- Quarto configuration and the locked Pandoc/XeLaTeX recovery path produce
  separate EN/FR HTML, PDF, and repository-local HTML slides. Remote images,
  scripts, styles, and CSS imports are rejected before offline render.
- Nine automated tests pass: six paired publication products, parity/technical
  contract/rubric/glossary/link/accessibility defects, explicit answer-key drift,
  source and rendered HTML/PDF restricted leakage, five smoke-hook interfaces,
  visual regression, and a real KiCad 9.0.9 seeded short-circuit failure.
- External-source capture, checksum/license metadata, print/font/math/schematic,
  size budgets, visual viewports, hook contracts, CI, owner/versioned KiCad
  waivers, and benchmark templates are committed. Quarto 1.7.33 is frozen in CI;
  it was not present on the implementation host.
- **Open M02-E3-T04 evidence:** run the full offline bundle on both declared
  4 GiB, two-core Linux and Windows profiles, record cold/warm time, outputs,
  failures and reviewer, and change each `requires_physical_benchmark` status
  only after approval. The Fedora implementation host has 35 GiB RAM and cannot
  substitute for either result. **Owner:** toolchain owner with learner-device/IT
  reviewer.

### E4 — Release, access, recovery, and licensing

- ADR-0001 and `curriculum/governance/` control semantic versions, cohort freeze,
  urgent safety correction, learner impact, migration, deprecation, independent
  review facets, restricted classification, backup/restore, license/provenance,
  and DCO 1.1 contributor terms. Defaults are `CC-BY-SA-4.0` for original
  courseware, `MIT` for software/HDL, `CERN-OHL-P-2.0` for hardware source, and
  upstream terms for fonts/third-party work.
- The 2026-07-13 drill bundled every ref from the clean implementation commit and
  a separate synthetic restricted store, disabled network-capable Git paths,
  verified bundles/checksums, restored and `fsck`-checked both clones, compared
  refs/HEAD/tree, checked the public boundary/canary, and ran all nine E3 tests
  offline inside the restored public clone. See
  `curriculum/governance/drill-records/2026-07-13-offline-clone-and-restore.md`.
- Reachable-history scanning, current-source QA, and rendered HTML/PDF leakage
  tests implement complementary controls; manual classification remains required.
- **Open M02-E4-T02 evidence:** provision the production private remote and record
  an opaque approved attestation for named accounts, MFA where available,
  protected branch, transport/storage/backup encryption, audit events, term
  access review, retention, and restoration authority. The initializer and
  synthetic store prove the mechanism only. **Owners:** assessment authority,
  data steward, institutional IT/security.
- **Open M02-E4-T05 evidence:** a real candidate must complete the non-assessed
  bilingual vertical sample including safe physical execution, independent
  review, authentic revision, release, teach-back, and trainer authorization.
  The route and controlled record template exist; no person is represented as
  qualified. **Owners:** faculty-development lead and learning-content architect.

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
- [x] The build intentionally catches seeded parity, link, accessibility, answer-key, and restricted-content defects.
- [ ] Offline clone/build/restore works on supported machines.
- [x] M04 can produce the exemplar without inventing workflow or metadata.

The first open exit criterion requires an observed new-author exercise through
revision, not a self-review of documentation. The third remains open until the
minimum-profile Linux and Windows benchmark records close E3-T04. The successful
Linux implementation-host restore/build drill closes E4-T04 but is not promoted
to unsupported device evidence.
