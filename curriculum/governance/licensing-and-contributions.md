# Licensing, provenance, and contributor terms

**Control ID:** GOV-IP-001
**Owner:** library/IP steward
**Review:** each imported asset and release; annual policy review

This is repository policy, not legal advice. Institutions confirm authority,
employment terms, student choice, sponsor/capstone IP, privacy, moral rights, and
applicable law before publication.

## License matrix

| Artifact | Default SPDX identifier | Boundary |
|---|---|---|
| original prose, templates, slides, figures/media, general curriculum data | `CC-BY-SA-4.0` | only work the rightsholder can license; embedded third-party material remains separately marked |
| scripts, software examples, tests, environment code | `MIT` | dependency notices/source licenses remain |
| HDL as executable logic | `MIT` | hardware-design manifest may additionally declare its hardware license |
| schematics, PCB/layout, fabrication, mechanical and hardware-design source | `CERN-OHL-P-2.0` | product/compliance rights outside copyright are not promised |
| bundled fonts | upstream identifier; prefer `OFL-1.1` | redistribution/embedding follows actual upstream permission |
| third-party asset, standard, datasheet, data, code, model | upstream license or `LicenseRef-Proprietary-*` | do not relicense; store only when redistribution/archival is permitted |
| maximally reusable metadata | `CC0-1.0` only by explicit owner decision | never apply without authority and impact review |

Use SPDX expressions when one file combines separable or alternative grants.
Every source file with supported comment syntax carries an SPDX identifier;
otherwise front matter or the nearest manifest maps its path. Canonical license
texts/notices belong in `LICENSES/` before distribution.

## Third-party and claim record

Record stable ID, title, creator/rightsholder, canonical source, artifact/source
version, retrieval date, exact license/URL, required attribution/notice,
modifications, permitted archival/redistribution, local or external-only
disposition, checksum, affected EN/FR assets, reviewer, and review trigger. A
citation does not create redistribution permission. Prefer a link plus metadata
when an archival copy is not permitted.

## Contributor terms

Contributions use Developer Certificate of Origin 1.1. Each commit includes:

```text
Signed-off-by: Contributor Name <address@example.org>
```

The sign-off certifies origin/right-to-submit under the destination license and
acknowledges retention of the public contribution record. It does not override
employer, institution, sponsor, participant, partner, font, dataset, or
third-party terms. Contributors disclose generated/AI-assisted material and
verify originality, sources, claims, and licenses; tool output supplies no rights.

Student work is not made public as an assessment condition unless an approved,
freely given route and equivalent private alternative exist. Participant and
partner material follows its consent/data agreement. Capstone/sponsored work
requires an IP/data disposition before the brief is accepted.

Unknown, incompatible, or unverified rights block release: replace the material,
obtain permission, link without copying where lawful, or remove it.
