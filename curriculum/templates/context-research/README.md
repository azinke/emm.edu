# Context-research controlled templates

These templates instantiate the ethical-context-research controls defined by [M01-E0](../../../blueprint/mappings/benin/m01-e0-ethical-context-research-authorization.md). They are blank public templates, not approvals and not collection instruments until completed, reviewed, piloted, versioned, and signed.

## Template set

| Template | Use |
|---|---|
| [Protocol and method register](protocol-and-method-register.md) | freeze purpose, sample, methods, fields, processing, outputs, approvals, and amendments |
| [Interview and observation instrument](interview-and-observation-instrument.md) | control paired prompts, allowed fields, non-identifying observations, live stops, closeout, and claim handoff |
| [Participant information and consent — EN](participant-information-and-consent-en.md) | paired English participant route |
| [Information et consentement — FR](participant-information-and-consent-fr.md) | paired French participant route |
| [Site-visit risk and authorization](site-visit-risk-and-authorization.md) | approve access, hazards, travel, observation, recording, stop/restart, and handover |
| [Instrument pilot record](instrument-pilot-record.md) | test comprehension, language parity, access, burden, coercion, data flow, and incident response |

## Control rules

1. Copy the needed template into the deploying institution's controlled research workspace; never complete participant or restricted site records in the public repository.
2. Assign a stable artifact ID and semantic version. Record the parent M01-E0 dossier version.
3. Replace every bracketed field. An unresolved field is a blocker, not permission to improvise.
4. Preserve paired EN/FR consent meaning and choices. A change to purpose, risk, privacy, compensation, rights, or recording is made in both versions and re-reviewed.
5. Obtain the required legal, ethics, controller/data, accessibility/language, site, partner, safety, and release dispositions before recruitment.
6. Pilot the exact released versions. Material changes after pilot require proportionate retest.
7. Store completed consent, contact, partner-confidential, site-security, incident, payment, access, and withdrawal records only in the approved restricted store represented by `curriculum-private/protected-student-partner-data/`.
8. Publish only release-reviewed aggregate or properly de-identified artifacts. Public Git history must never contain participant data.

## Minimum release naming

Suggested IDs:

- protocol: `ESE-M01-BJ-PRO-001`;
- method/instrument: `ESE-M01-BJ-INT-###`, `OBS-###`, or `PIL-###`;
- site authorization: `ESE-M01-BJ-SITE-###`;
- consent pair: `ESE-M01-BJ-PIS-001-EN` and `ESE-M01-BJ-PIS-001-FR`.

The release manifest records ID, version, language, checksum where used offline, owner, reviewers, approval references, valid-from/expiry, superseded version, and destruction/withdrawal implications of a change.
