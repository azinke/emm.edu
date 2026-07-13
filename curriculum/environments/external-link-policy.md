# External-link capture and citation contract

Every external URL used by released courseware has one entry in
`external-links.yml`. A bare hyperlink is not a durable source. The entry records:

- stable `id`, exact `url`, `title`, `publisher_or_author`, `source_kind`, and
  `edition_or_version`;
- ISO 8601 `retrieved_on`, `review_due`, responsible `owner`, and the affected
  artifact IDs;
- `citation_text` and, for technical claims, the primary-source status and
  claim/register IDs;
- `archive_permission`: `permitted`, `prohibited`, or `unknown`, plus the
  permission/license evidence and `license_or_terms` (an SPDX expression where
  one exists, otherwise an owned `LicenseRef-*`/terms reference);
- if redistribution is permitted, a repository-relative `archive_path`, media
  type, byte count, and `sha256` checksum; if it is not, a locally authored
  citation/summary and retrieval instructions, never an unauthorized copy;
- `availability`: `required`, `supplementary`, or `reference`. Required learning
  must remain usable offline after the initial bundle installation.

Authors must not infer archival permission from public accessibility. Dynamic,
platform, price, regulation, standard, and safety sources carry an owned review
trigger. A changed source opens EN and FR review together. The ordinary offline
build verifies registry records and archived checksums without network access.
The explicit `capture_external.py --allow-network` operation is a maintainer task,
not part of a course build. Nightly CI may probe URLs but never silently replaces
an archived source.

Example entry:

```yaml
- id: SRC-DATASHEET-EXAMPLE
  url: https://manufacturer.example/device.pdf
  title: Device data sheet
  publisher_or_author: Example Manufacturer
  source_kind: datasheet
  edition_or_version: Rev. B
  retrieved_on: 2026-07-13
  review_due: 2027-07-13
  owner: component-library-owner
  affected_artifacts: [ESE111-U04]
  claim_ids: [CLAIM-ESE111-U04-01]
  citation_text: Example Manufacturer, Device data sheet, Rev. B.
  archive_permission: permitted
  permission_evidence: redistribution clause in source license
  license_or_terms: CC-BY-4.0
  license_spdx: CC-BY-4.0
  archive_path: environments/external-archive/SRC-DATASHEET-EXAMPLE.pdf
  media_type: application/pdf
  bytes: 12345
  sha256: <64 lowercase hexadecimal characters>
  availability: required
```
