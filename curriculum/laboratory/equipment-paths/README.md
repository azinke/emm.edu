# M03 E4 three-path laboratory validation pack

**Semantic ID:** M03-E4
**Version:** 0.1.0-draft
**Status:** specification and review templates only
**Owner:** laboratory lead
**Required reviewers:** institutional safety lead, instructor representative,
accessibility reviewer, EN reviewer, FR reviewer

This pack turns the Course Master Document's minimal, standard, and advanced
laboratory paths into reviewable operating contracts. It does **not** record a
physical pilot, an apparatus comparison, a fixture verification, a safety
approval, or instructor usability approval. Those claims require dated,
attributable evidence in the approval record.

## Pack contents

| Artifact | Purpose |
|---|---|
| `apparatus-paths.md` | Apparatus and invariant-evidence definitions for five core phenomena |
| `mcu-stimulus-acquisition-spec.md` | Low-energy stimulus/acquisition design contract; not a manufacturing release |
| `physical-access-and-scheduling.md` | Per-learner entitlement, rescheduling, and capacity-test rules |
| `operations-en.md`, `operations-fr.md` | Paired bench maps, quick guides, fault cards, and check-in/out procedure |
| `datasets/` | Prepared raw-format analysis data, conspicuously marked as non-personal and synthetic |
| `safety-usability-approval-template.yml` | Blank, pending-only approval and path-comparison record |
| `later-stage-requalification.md` | Requalification prerequisites for S2 through S6 |

## Evidence boundary

- Prepared data may support modeling, plotting, uncertainty reasoning, anomaly
  detection, and a design decision.
- Prepared data cannot certify that a learner constructed a circuit, selected or
  connected an instrument, made a safe energy-state decision, measured a physical
  quantity, or debugged physical hardware.
- Minimal, standard, and advanced paths use one mastery threshold. Advanced
  resolution is enrichment and does not increase the core grade.
- A learner who misses mandatory personal physical evidence receives another
  physical slot; an analysis substitute does not close that evidence gap.
- Every local deployment must replace proposed limits with approved task limits
  where its institutional safety manual is stricter or more specific.

## Release blockers

This pack remains `draft` until all five configurations have been physically
piloted on each claimed path, uncertainty and access findings have been compared,
the EN/FR procedures have been rehearsed, and independent safety, usability, and
accessibility reviewers have signed a completed approval record. Any unavailable
core physical path blocks the corresponding core laboratory release or requires
an approved outcome-equivalent physical substitute.

SPDX-License-Identifier: CC-BY-SA-4.0
