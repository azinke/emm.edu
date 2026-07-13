# Sample procurement and platform qualification protocol

**Protocol ID:** M03-E2-PROC-001  
**Version:** 1.0.0  
**Owner:** procurement lead  
**Technical owner:** platform engineering lead  
**Required independent reviewers:** safety officer and applicable course/toolchain
owner

## Purpose and boundary

Use this protocol to sample and score foundation MCU, professional MCU, wireless,
FPGA, embedded Linux, debug-probe, and programmer candidates. It defines a fair,
traceable method; it contains no supplier quote, purchase authorization, received
sample, physical result, or approved platform decision.

A platform is qualified only for one exact manufacturer part number, assembly
revision, silicon/package where material, frozen environment, probe/programmer,
and procurement-channel risk statement. Similar names and visual clones do not
inherit the result.

## Roles and conflict control

The procurement lead collects comparable commercial records. The platform
engineer freezes test configuration and executes or witnesses technical tests.
The safety officer may stop or quarantine any sample. A course owner judges
learning/action equivalence. A second technical reviewer checks raw evidence and
recomputes scores. Anyone with a supplier, donation, or product conflict records
it and does not solely approve the decision.

Supplier quotes, contacts, serial numbers, credentials, and non-public commercial
terms remain in controlled storage. The public scorecard cites stable record IDs.

## Phase 0 — Freeze the request, not a favorite product

For each category:

1. copy the applicable contract ID from `capability-contracts.yml`;
2. list the courses, assessed actions, cohort quantity, shared ratio, required
   accessories, and latest acceptable delivery date;
3. declare pass/fail gates and scoring rules before opening price information;
4. declare planned sample size and limitations; a small sample supports only the
   stated qualification, not population reliability;
5. freeze the offline environment, host profiles, golden-project version, fixture
   revision, instruments, and evidence directory; and
6. issue the same identity, commercial, documentation, warranty/return,
   lifecycle, and delivery questions to both channels.

## Phase 1 — Establish two-channel evidence

Obtain current comparable offers from at least two independent channels where
practicable. Independence means the purchasing route and custody/provenance risk
are genuinely distinct, not two storefronts fulfilled by the same unknown
seller. For each offer record:

- supplier/channel record ID, manufacturer part number and claimed revision;
- quote date, validity, quantity break, stock basis, and lead-time basis;
- source currency and deployment currency conversion source/date;
- unit, freight, tax, duty, payment, adapter/accessory, warranty/return, and
  estimated landed totals without silently omitting unknowns;
- manufacturer-authorized, regional distributor, reseller, marketplace, donated,
  or other provenance class and counterfeit/clone controls; and
- document links/version, lifecycle statement, country restrictions, radio/module
  identity where applicable, and substitute notice terms.

Mark every unknown as `unknown`; never enter zero. If a second channel cannot be
sampled, the procurement authority records a bounded exception, additional
identity controls, expiry, and replacement-search date. An exception cannot waive
electrical, safety, offline, recovery, or learning gates.

## Phase 2 — Receive, segregate, and identify samples

1. Receive samples into quarantine; preserve packaging and chain-of-custody ID.
2. Photograph or otherwise record product, board revision, device markings,
   connectors, seals, included accessories, and visible damage.
3. Match the physical item to the quotation, manufacturer documentation,
   schematic revision, and advertised programmer/tool requirements.
4. Check for substituted silicon, ambiguous clones, rework, corrosion, bent pins,
   damaged cables, battery/storage damage, or unapproved radios.
5. Do not connect a sample whose identity, power input, I/O domain, battery state,
   or damage status is unresolved. Quarantine and disposition it.
6. Assign an asset/sample ID. Do not publish a serial number when it creates
   warranty, privacy, network, or security exposure.

Samples from each channel are tested separately. Mixed lots do not prove channel
consistency.

## Phase 3 — Document review and abstraction sheet

Complete the full `board-abstraction-sheet-template.yml` for every board candidate
and the applicable interface portions for probes/programmers. Verify facts against
manufacturer primary material, noting exact revisions and errata. Independently
check:

- pin numbering, alternate functions, reset state, pull state, voltage/current
  limits, bank/reference domains, and power/backfeed paths;
- clocks, ADC constraints, timers, buses, memory map, reserved resources, radio,
  boot, debug, and recovery;
- tool, driver, firmware, license/account, host, and offline requirements;
- known failure modes, lifecycle/support notices, and substitute implications; and
- all permanent security/configuration mechanisms, which are marked prohibited on
  reusable boards.

An ambiguous electrical limit or undocumented recovery route is a rejection, not
a request to “try carefully” with learners.

## Phase 4 — Execute qualification

Use the current golden-project specification. Execute every applicable test from
a clean offline installation on each exact sample/revision. At minimum retain:

- operator, witness, date/time, location, ambient conditions where relevant;
- sample/fixture/instrument/cable/probe IDs and function-check/calibration state;
- source and environment commit/hash, commands, raw stdout/stderr, binary hashes,
  build time, storage, memory/resource/timing reports;
- wiring/setup record, current limit, predicted safe state and expected range;
- raw voltage/current/timing/data measurements and uncertainty or resolution;
- boot, interrupted-program, bad-image recovery, and debugger evidence;
- anomaly/fault log, discriminating test, corrective action, retest, and limits; and
- independent reviewer disposition for every test ID.

Wireless tests transmit only under a dated local approval and controlled setup.
Otherwise qualify the non-transmitting path and leave the radio test blocked—not
passed. Never program permanent fuses, keys, secure-boot roots, anti-rollback
counters, readout locks, or permanent debug disable on reusable samples.

## Phase 5 — Score after hard gates

First apply universal and contract-specific rejection gates. A failed hard gate
cannot be averaged away by price or popularity. For candidates that pass, score
each criterion from 0 to 5 using linked evidence:

| Criterion | Weight | Score anchors |
|---|---:|---|
| Transferable learning and hardware visibility | 20 | 0 hides required action; 3 exposes it with bounded gaps; 5 makes registers/interfaces/timing directly inspectable across courses |
| Documentation, schematics, examples, community | 15 | 0 lacks authoritative essentials; 3 complete primary essentials; 5 versioned design files, errata, offline docs, and maintainable examples |
| Local/regional availability and landed cost | 15 | 0 unknown/unobtainable; 3 two dated viable channels with full landed basis; 5 resilient channels and approved cohort TCO with low identity risk |
| Open, offline, cross-platform tool support | 15 | 0 cloud/seat blocks students; 3 frozen offline flow works on required hosts; 5 reproducible open flow, CI and recovery with documented fallback |
| Debug/test access | 10 | 0 no practical fault visibility; 3 required debug/program/test route passes; 5 accessible standard interfaces plus strong measurement/test points |
| Lifecycle and second-source strategy | 10 | 0 unsupported/no migration; 3 reviewable support plus qualified substitute route; 5 strong lifecycle evidence and low-disruption abstraction |
| Electrical robustness and repairability | 10 | 0 unsafe/fragile unresolved; 3 limits, protection, fixtures and repair path are adequate; 5 connectors/protection/replaceable wear parts withstand planned use |
| Accessibility and licensing | 5 | 0 required access excluded; 3 no paid/cloud barrier and usable docs; 5 accessible/offline interfaces and permissive reusable artifacts across supported hosts |

Weighted points equal `score / 5 × weight`; the maximum is 100. Predeclare the
minimum total and any category-specific minimum criterion score in the request
record. The master scorecard weights are fixed; changing them requires a program
decision, not a procurement convenience.

## Phase 6 — Decision, moderation, and release

The reviewer verifies formulas, source links, raw evidence, anomalies, and missing
fields. Then record exactly one decision:

- `qualified-primary`: passes gates and is selected for a named future cohort;
- `qualified-substitute`: passes gates and has a completed equivalence mapping;
- `conditionally-qualified`: only a bounded, non-safety limitation with owner,
  mitigation, expiry, and no lowered outcome/evidence threshold remains;
- `not-qualified`: fails a gate, score, or evidence requirement; or
- `decision-deferred`: required evidence is unavailable.

Qualification is not a purchase order. Procurement authority separately confirms
budget, quote validity, terms, quantity, access model, and institutional approval.
After acquisition, apply incoming inspection to the lot; a passing sample does not
guarantee every unit.

## Required outputs

- one completed scorecard per candidate/channel or a clearly linked channel
  comparison;
- complete abstraction sheet and golden-project evidence per exact revision;
- controlled quotes and landed-cost worksheet;
- anomaly, counterfeit/identity, and quarantine dispositions;
- signed primary/substitute/decline decision with limitations and review triggers;
- board/tool images and offline documentation bundle hashes; and
- trace to the cohort freeze record when a qualified candidate is actually used.

SPDX-License-Identifier: CC-BY-SA-4.0
