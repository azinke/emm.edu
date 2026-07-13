# ADR-0001 — Content release, access, and licensing baseline

- **Status:** accepted for the repository foundation
- **Date:** 2026-07-13
- **Owners:** program board; configuration/release manager; library/IP steward
- **Applies to:** M02-E4
- **Revisit:** institutional legal review rejects a term; a dependency license is
  incompatible; applicable privacy, assessment, or product-origin law changes

## Decision

1. Use semantic versions and the release classes in Course Master Document
   §14.2. A patch cannot change a technical construct, expected result, safety
   decision, or assessment judgment.
2. Freeze an immutable version for each cohort. Corrections that affect safety
   or learner judgment use the urgent correction and impact process immediately.
3. Keep live assessments, current solutions, protected student data, and
   partner-confidential data in a separately permissioned store outside this
   public repository. Public source stores opaque controlled references only.
4. License original prose, teaching media, and general curriculum data under
   `CC-BY-SA-4.0`; software and HDL under `MIT`; hardware/PCB design source under
   `CERN-OHL-P-2.0`. Fonts retain upstream terms, with `OFL-1.1` preferred.
   Third-party work retains its source license and provenance.
5. Accept contributions under the license declared for the destination using
   Developer Certificate of Origin 1.1 sign-off. Institution, sponsor, capstone,
   participant, or partner work needs a separate agreement when ordinary DCO
   authority is insufficient.

## Rationale

The split preserves the master's open-courseware target while applying licenses
suited to software and physical designs. The public/restricted boundary prevents
access control from depending on a branch, deletion, or later history rewrite.
DCO sign-off creates a durable contributor representation without silently
claiming student, employer, sponsor, or third-party rights.

## Consequences and controls

- Every artifact carries an SPDX identifier in front matter, a manifest, or a
  directory-level license mapping.
- Every external asset records creator, source, version/retrieval date, license,
  modification, attribution, archival permission, and checksum.
- Public pull requests run the restricted-content scan and require facet owners.
- License choice is not legal advice; deploying institutions complete local IP,
  privacy, records, assessment-security, and employment review before release.
- The controlled procedures under `curriculum/governance/` are normative.
