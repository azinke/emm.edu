# Restricted-material boundary and access control

**Control ID:** GOV-SEC-001
**Public owner:** configuration/release manager
**Restricted-store owners:** assessment authority and data steward
**Principle:** classification occurs before creation, import, or export

## Boundary

This public repository may contain released exemplars, rubrics, construct
specifications, and opaque artifact references. It must never contain:

- live/embargoed prompts, answer keys, current solutions, setup variants,
  examiner calibration details, or item statistics that expose keys;
- identifiable student records, accommodations, grades, submissions, images,
  voices, consent records, or incident/appeal files;
- partner-confidential needs, sites, contacts, credentials, network details,
  unpublished product/IP data, or human-participant research records;
- secrets, tokens, private keys, raw access logs, or decryption material.

Branches, pull requests, Git LFS, encrypted blobs, deletion, and `.gitignore` do
not make public history an acceptable restricted store. If restricted content is
committed, stop distribution, notify the data/assessment owner, rotate exposed
secrets, preserve a controlled incident record, assess notification duties, and
follow an approved history-remediation plan. Do not improvise a history rewrite.

## Separate store

Create the restricted store outside the public checkout with
`python3 curriculum/scripts/initialize_restricted_store.py PATH --remote URL`.
Production use requires a private remote with named accounts, MFA where
available, protected default branch, reviewed access, encrypted transport,
encrypted managed storage/backups, and audit events. Local permissions are
defense in depth, not the authority system.

| Area | Read | Write/approve | Default retention |
|---|---|---|---|
| current assessments | named teaching/exam team | assessment owner; two-person release for high stakes | through challenge/reassessment window plus institutional rule |
| restricted solutions | named instructors/reviewers | course and assessment owners | while supported, then controlled release/archive |
| student data | minimum named education staff | data steward under institutional policy | purpose-limited schedule |
| partner-confidential | agreement-named team | partner liaison/data steward | contract/consent schedule and handover |

Access is least privilege, time bounded, reviewed each term and on role change,
and revoked promptly. No author solely approves their own high-stakes assessment.

## Controlled public reference

```yaml
reference_id: RST-ESE111-PS04-SOL-001
classification: restricted-solution
semantic_asset_id: ESE111-PS04
approved_version: 1.0.0
store_namespace: solutions/ESE111/PS04
owner_role: assessment-owner
release_condition: after-cohort-and-reassessment-window
integrity_sha256: supplied-by-restricted-store
```

The public reference reveals no answer, participant identity, partner secret,
private URL, storage credential, or internal access-control identifier.

## Transfer, backup, destruction, and checks

Use approved encrypted channels and verify recipient, classification, checksum,
purpose, and expiry. Never paste restricted material into public issues,
translation services, or unapproved AI tools. Backups inherit classification,
access, encryption, retention, and deletion duties. Destruction is authorized
and logged; deleting a commit alone is not destruction.

Reachable Git history is scanned for prohibited restricted-store payload paths
and high-confidence private-key/token patterns. Course-source QA separately
checks restricted path/front-matter/content markers and links. Generated-product
QA checks its declared leakage patterns. A match blocks release and requires
human classification; any suppression names the rule, file, reviewer, expiry,
and rationale. Reviewers still inspect generated HTML/PDF/slides and offline
bundles because automated patterns cannot prove that a clean tree is lawful or
properly classified.
