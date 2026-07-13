# Platform qualification control pack

**Control ID:** M03-E2-CTRL-001  
**Scope:** M03 Epic E2 platform capability qualification  
**Owner:** platform engineering lead  
**Approvers:** laboratory director, safety officer, procurement lead, toolchain
owner, course owners, and release manager  
**Review:** at every cohort freeze and at least annually

This directory turns the Course Master Document platform strategy into auditable
contracts and blank execution records. It deliberately separates a specified
method from evidence that the method was executed. A template, candidate name,
manufacturer statement, or successful simulation is never a procurement,
physical-board, or low-specification-computer result.

## Artifact map and present evidence state

| M03 task | Artifact | What this repository establishes | What still requires execution |
|---|---|---|---|
| E2-T01 | `capability-contracts.yml` | Required capabilities and rejection gates for every planned category | Candidate-specific source review and measured qualification |
| E2-T02 | `procurement-qualification-protocol.md`, `procurement-scorecard-template.yml` | Two-channel sampling, identity, inspection, scoring, and decision protocol | Quotes, sample purchases, incoming inspection, tests, and approved scores |
| E2-T03 | `golden-project/qualification-spec.md`, fixture and evidence templates | Common test IDs, applicability, method, and acceptance rules | Builds and physical runs on each exact primary and substitute revision |
| E2-T04 | `board-abstraction-sheet-template.yml` and `board-sheets/` | Required sheet structure plus a pending sheet for each planned board category | Exact pin/electrical/errata data verified against primary documents and samples |
| E2-T05 | `cohort-freeze-and-replacement.md`, `cohort-freeze-record-template.yml` | Freeze, change, equivalence, rollback, and irreversible-security-operation controls | A signed record for each real cohort and any replacement decision |
| E2-T06 | `computer-benchmark-protocol.md`, benchmark/report templates | Repeatable offline workload and support-path protocol | Runs on named physical/refurbished computers and an approved published report |

All records start as `not_run`, `pending`, or `qualification-pending`. Only an
authorized reviewer may advance them after linking attributable evidence. Do not
copy a result between revisions, supplier channels, operating systems, or board
variants.

## Governing rules

- Capability comes before brand. Reference names in the master document identify
  a ladder to qualify, not blanket approval of every product carrying that name.
- Exact board, assembly revision, tool image, driver, programmer, and permitted
  documentation bundle are frozen together.
- Required work builds without a network after installation of the frozen bundle.
- A substitute must preserve outcome, practical action, debug visibility, safety,
  assessment difficulty, and access; matching a connector or example sketch is
  insufficient.
- Radio use remains disabled until the deployment jurisdiction and exact radio
  configuration are approved.
- Ordinary reusable teaching boards never undergo irreversible security
  operations. Security exercises needing permanent state use simulation or
  separately controlled sacrificial hardware.
- Procurement and benchmark facts are deployment-bound records: include source,
  date, currency, conditions, limitations, and reviewer.

## Evidence storage

Completed public records may live beside this pack when they contain no personal,
commercially restricted, credential, key, network, or assessment-sensitive data.
Use controlled storage for supplier quotations, serial-number registers, security
keys, personal approvals, and restricted test material. A public decision record
may cite a controlled-store ID without copying the protected payload.

SPDX-License-Identifier: CC-BY-SA-4.0
