# Cohort platform freeze and replacement procedure

**Decision control ID:** M03-E2-DEC-001  
**Version:** 1.0.0  
**Owner:** configuration/release manager  
**Decision authority:** laboratory director with safety, platform, toolchain, and
affected course owners  
**Applies:** all teaching boards, probes/programmers, fixtures, offline images, and
assessed platform-bound instructions

## Decision principle

Freeze an exact, qualified configuration six months before teaching where the
planning calendar permits. Freeze makes the evidence baseline auditable; it does
not pretend that an unavailable, unsafe, or defective platform must remain in
service. A mid-cohort change is exceptional and must preserve safety, outcomes,
personal practical evidence, assessment difficulty, accessibility, schedule, and
fairness.

## Reusable-board security prohibition

Ordinary known-good, instructor, loan, spare, substitute, and student-use boards
must remain recoverable. The following operations are prohibited on them even when
a datasheet, tutorial, or teaching tool makes the operation available:

- burning one-time-programmable/eFuse boot, key, encryption, region, voltage,
  anti-rollback, or security state;
- installing a secure-boot root or flash-encryption state that cannot be fully
  returned to the frozen reusable baseline;
- permanent debug/JTAG/SWD disable, irreversible readout protection, or lock state
  whose recovery requires destructive erase not approved by the course contract;
- destroying/replacing a device-unique secret, exhausting a monotonic counter, or
  changing lifecycle state; and
- any command for which reversibility on the exact silicon/board revision has not
  been established from primary documentation and a non-reusable qualification
  path.

Content and scripts use simulation, emulation, reversible configuration, test
keys in volatile/recoverable storage, or explicit demonstration-only output by
default. A course that genuinely assesses permanent security lifecycle behavior
uses separately labeled and inventoried `sacrificial-security` hardware under an
approved activity-specific risk/threat/data procedure, two-person authorization,
non-production test keys, cost/waste disposition, and destruction/quarantine
record. Sacrificial units never return to ordinary stock and are not substitutes
for reusable cohort boards.

Any accidental or suspected irreversible change triggers immediate stop-use and
quarantine. Do not attempt internet-derived unlock commands. Record exact command,
tool log, device/revision, person/role, state evidence, credentials exposure
assessment, and safety/security authority disposition in controlled storage.

## Freeze prerequisites

Before signing the record, verify:

1. the exact manufacturer part number, assembly revision, silicon/package where
   material, markings, and approved procurement channels;
2. completed capability scorecard, abstraction sheet, incoming inspection method,
   golden-project physical pass, and independent review;
3. qualified primary and substitute revisions, with two instructor exemplars of
   each substitute and planned 10–15% board spares;
4. board/probe firmware, drivers, compiler/SDK/RTOS/FPGA/Linux image, USB rules,
   host operating systems, documentation and licenses in the checked offline
   bundle;
5. exact fixtures, cables, adapters, known-good images, current limits, instrument
   requirements, safe handling, recovery and quarantine cards;
6. mapped courses, labs, assessments, EN/FR platform-bound assets, accessibility
   paths, staff qualification, and shared-equipment schedule;
7. dated supply, lifecycle, security-maintenance, total-cost, storage/repair, and
   radio/jurisdiction dispositions; and
8. owners, release/tag/commit, checksums, review date, triggers, notification path,
   and rollback/support end date.

`Pending`, `not_run`, `blocked`, a blank revision, or a manufacturer-only
demonstration cannot be frozen as qualified. Record the gap and keep the decision
open.

## Freeze record

Create one `cohort-freeze-record-template.yml` instance per cohort baseline. Use a
controlled reference rather than publishing serial numbers, supplier quotes,
credentials, keys, personal signatures, or restricted assessment content. The
release manager checks that all platform-bound artifact front matter and course
manifests point to the same baseline.

The approved status is one of:

- `frozen-qualified`: complete primary and substitute evidence;
- `frozen-with-owned-gap`: only a non-safety/non-assessment deployment action is
  pending, with mitigation and expiry before learners use the affected path;
- `not-approved`: the cohort may not use this platform baseline.

No `frozen-with-owned-gap` decision can waive physical qualification, electrical
limits, recovery, offline access, outcome evidence, required personal access,
irreversible-security prohibition, or radio authorization.

## Replacement triggers

Open a replacement decision immediately for:

- safety incident/near miss, damage pattern, overheating, backfeed, battery/storage
  hazard, electrical-limit correction, or new material erratum;
- counterfeit/clone, silent component substitution, inconsistent lot identity, or
  board-revision change;
- failed golden project, unexplained learner/bench failures above the declared
  threshold, corrupted recovery path, or assessment-relevant behavior drift;
- end-of-life/not-recommended status, security support withdrawal, unavailable
  offline tool or driver, host OS incompatibility, license/account restriction, or
  unarchivable dependency;
- supply/lead time no longer supporting cohort plus spares, both approved channels
  failing, or total cost exceeding the approved access model;
- radio law, authority, region, antenna, firmware, network, privacy, or facility
  disposition change;
- inaccessible workflow or disproportionate installation/build time demonstrated
  on the lowest-supported computers; or
- substitute evidence expiry, checksum mismatch, tool image drift, or loss of
  known-good recovery inventory.

Safety and legal triggers invoke stop-work immediately. Other triggers are triaged
against cohort timing and stock; they do not silently change the baseline.

## Replacement decision sequence

1. **Contain.** Identify affected lots/cohorts/assets; stop or quarantine when
   safety, identity, security, or legal status is uncertain. Preserve original
   configuration and evidence.
2. **Describe.** Record observation, source, date, affected revision and channels,
   reproducibility, severity, and whether it affects safety, outcomes, assessment,
   accessibility, schedule, cost, or radio/security.
3. **Evaluate current path.** Independently reproduce the failure, check primary
   sources/errata, inspect lots, and test rollback/workaround on staff samples.
   Never trial an irreversible unlock on reusable stock.
4. **Qualify candidate replacement.** Run the full procurement, abstraction, and
   golden-project protocol. Similarity and prior-family qualification are not
   evidence.
5. **Map equivalence.** For each learning and assessed action, map pins, voltage,
   peripheral semantics, timing, memory/resource limits, debug visibility,
   fixtures, tools, recovery, and evidence. Identify what becomes easier or harder.
6. **Analyze learner impact.** Disposition EN/FR assets, accessibility, staff
   briefing, offline pack, loan/shared access, deadlines, rework, grading, and
   prior evidence using the repository release policy.
7. **Decide.** Choose continue with owned workaround, staged replacement for the
   next cohort, or urgent mid-cohort replacement. State effective time, approvers,
   conditions, expiry, rollback, and effectiveness check.
8. **Release together.** Update both language pathways and all shared platform-
   bound artifacts under one version; issue the new offline bundle and short plain
   notice before affected work.
9. **Verify effectiveness.** Observe the first instructor run and initial learner
   use; compare failure/access/timing evidence to the predeclared rule. Close only
   when affected evidence is valid and old stock is retired, quarantined, or
   relabeled appropriately.

## Mid-cohort fairness rule

Never mix primary and substitute hardware in a common assessment unless moderation
has shown equivalent construct, difficulty, time, visibility, fixtures, and
support. When equivalence cannot be shown, schedule separate calibrated forms or
reschedule; do not lower the threshold. Learners receive adequate practice on the
new route, simultaneous EN/FR notice, access to the correct offline image and
hardware, and explicit disposition of deadlines and prior evidence.

## Decision outputs

- freeze or replacement record with commit/tag and bundle checksum;
- linked primary/substitute scorecards, abstraction sheets, and golden records;
- exact affected artifact and cohort list;
- safety/security/radio, assessment, accessibility, schedule, procurement, and
  total-cost decisions;
- learner-impact choice and EN/FR communication record;
- rollback, stock relabel/quarantine/retirement, and evidence-retention route; and
- first-use effectiveness evidence and next review trigger.

SPDX-License-Identifier: CC-BY-SA-4.0
