# M01 — Local Context, Needs, and Regulatory Mapping

**Goal:** instantiate a dated deployment profile—initially Benin—that grounds the universal curriculum in actual learners, professions, communities, infrastructure, supply chains, manufacturing capability, and applicable rules without treating any country as a proxy for Africa.

**Indicative duration:** 6–10 weeks  
**Primary owners:** curriculum research lead, local faculty, regulatory/accreditation lead, community/industry liaison  
**Depends on:** M00  
**Authoring entry:** M00 approves research authority, ethics/data boundaries, and responsible owners\
**Release gate:** M00 charter is approved and every local-profile claim has a source, owner, and review date\
**Exit unlocks:** final M02 data model, M03 procurement/safety, M05 bridge, M13 fieldwork

## Epic E0 — Authorize ethical context research

- [x] **M01-E0-T01 [REV]** Complete a preliminary named-jurisdiction legal and ethics screen covering human-participant status, personal data, minors/vulnerable participants, site access, recording, compensation, partner confidentiality, and required institutional approvals; unresolved authorization blocks the affected research method.
- [x] **M01-E0-T02 [SPEC]** Approve research purpose, sampling, informed consent, privacy/data minimization, retention, accessibility, safeguarding, compensation/benefit, interpreter, partner-confidentiality, and withdrawal routes before collecting learner/partner data.
- [x] **M01-E0-T03 [SPEC]** Approve site-risk, travel, photography/recording, incident, and stop-work procedures for every observation type.
- [x] **M01-E0-T04 [DEC]** Name data controller/custodian, ethical reviewer, partner acceptance authority, and escalation route; distinguish curriculum research from the operational M05 diagnostic.
- [x] **M01-E0-T05 [TEST]** Pilot consent and data-collection instruments for language, accessibility, burden, and unintended coercion.

### E0 authorization package and current disposition

The [Benin ethical context-research authorization dossier](../mappings/benin/m01-e0-ethical-context-research-authorization.md) provides the preliminary legal/ethics screen, bounded method decision, risk analysis, research purpose and sampling controls, consent/privacy/retention rules, site and stop-work procedure, authority model, M01/M05 separation, pilot acceptance thresholds, source register, and approval record for T01–T05.

Reusable controlled instruments are maintained under [`curriculum/templates/context-research/`](../../curriculum/templates/context-research/README.md):

- [protocol and method register](../../curriculum/templates/context-research/protocol-and-method-register.md);
- [interview and observation instrument](../../curriculum/templates/context-research/interview-and-observation-instrument.md);
- paired [English participant information/consent](../../curriculum/templates/context-research/participant-information-and-consent-en.md) and [French participant information/consent](../../curriculum/templates/context-research/participant-information-and-consent-fr.md);
- [site-visit risk and authorization record](../../curriculum/templates/context-research/site-visit-risk-and-authorization.md);
- [instrument pilot and acceptance record](../../curriculum/templates/context-research/instrument-pilot-record.md).

**Current decision:** documentation is complete enough for institutional and qualified local review, but it is not authorization to recruit or collect. The baseline permits consideration only of minimal-risk, staff-led research with independently consenting adults; it excludes minors and sensitive-data collection, defaults to no recording, and holds health/health-systems inquiry for a specific CNERS applicability decision. M00-E2 has not yet named the deploying institution/controller, custodian, independent ethical reviewer, local legal/data reviewer, field-safety authority, or partner acceptance authorities. The APDP route, site permissions, protocol instances, compensation, and two-round pilot also remain unevidenced. Consequently all five E0 tasks stay open and every participant-facing method stays blocked until the dossier's §2.2 release gate is signed.

## Epic E1 — Learner and educator research

- [ ] **M01-E1-T01 [TEST]** Sample incoming algebra, graph, unit, physical-science, digital, English/French technical-reading, and practical-tool readiness.
- [ ] **M01-E1-T02 [TEST]** Interview representative students about device access, internet/power reliability, language choice, travel/time constraints, disability/access, prior schooling, and cost barriers.
- [ ] **M01-E1-T03 [TEST]** Observe existing laboratories and teaching sessions; record equipment utilization, bottlenecks, safety behavior, and common misconceptions.
- [ ] **M01-E1-T04 [SPEC]** Build evidence-based learner and instructor personas; state sample limits and avoid treating personas as fixed cultural traits.
- [ ] **M01-E1-T05 [DEC]** Validate bridge assumptions, language support, loan/access schemes, and lab opening hours with students.
- [ ] **M01-E1-T06 [SPEC]** Record relevant community/user languages, literacy and non-text communication needs, and interpreter capacity for projects; do not infer these from nationality or replace EN/FR academic parity.

## Epic E2 — Professional and community problem discovery

- [ ] **M01-E2-T01 [TEST]** Interview electronics manufacturers, repair technicians, energy/water/agriculture/telecom/health organizations, startups, public services, and research groups.
- [ ] **M01-E2-T02 [SPEC]** Inventory recurring real problems, failure modes, instruments, standards, workflows, and graduate skill gaps.
- [ ] **M01-E2-T03 [TEST]** Conduct safe site observations for candidate M1–M8 contexts; capture environmental, power, connectivity, maintenance, user, and acceptance constraints.
- [ ] **M01-E2-T04 [SPEC]** Convert findings into reusable context briefs with evidence, stakeholders, ethical boundaries, measurable constraints, and possible learning links.
- [ ] **M01-E2-T05 [DEC]** Form an advisory group and agree how partners propose, review, host, maintain, or decline student projects.

## Epic E3 — Regulatory and accreditation mapping

- [ ] **M01-E3-T01 [SPEC]** Map the active jurisdiction and institution—Benin, CAMES/LMD, and the deploying institution for the initial profile—plus any targeted accreditation requirements to courses, credits, outcomes, evidence, and owners.
- [ ] **M01-E3-T02 [SPEC]** Identify applicable electrical, occupational, fire, chemical, battery, radio, e-waste, accessibility, data-protection, human-participant, product, and import rules.
- [ ] **M01-E3-T03 [SPEC]** Document current grid, plug, frequency, environmental design, radio authorization, product-origin/local-content, and waste-handling facts with jurisdiction, authoritative source, effective/retrieval date, reviewer, uncertainty, and next review.
- [ ] **M01-E3-T04 [DEC]** Identify activities needing institutional review, licensed supervision, external laboratory access, partner consent, or prohibition.
- [ ] **M01-E3-T05 [REV]** Have qualified local legal/safety/regulatory contacts review high-stakes mappings; record that educational planning is not legal certification.

## Epic E4 — Supply, repair, and infrastructure baseline

- [ ] **M01-E4-T01 [SPEC]** Survey local/regional suppliers, authorized distributors, customs/duty, lead times, counterfeit risk, and payment constraints.
- [ ] **M01-E4-T02 [SPEC]** Record dated deployment-currency and source-currency landed costs—XOF for the Benin profile—with exchange-rate source/date, tax/duty/freight, candidate kits, boards, computers, instruments, consumables, fabrication, calibration, repair, and spares.
- [ ] **M01-E4-T03 [TEST]** Visit repair/fabrication ecosystems to identify common packages, tools, connectors, substitute practices, and service documentation needs.
- [ ] **M01-E4-T04 [SPEC]** Baseline classroom power, ventilation, network, local server, storage, ESD, fire, accessibility, and security conditions.
- [ ] **M01-E4-T05 [DEC]** Identify minimal, standard, and advanced equipment paths; separately define institutional, partner, or shared-regional access models and minimum per-student physical access.
- [ ] **M01-E4-T06 [SPEC]** Map the product value chain: need/design organizations, prototype and PCB services, enclosure/harness/mechanical fabrication, assembly/rework, incoming inspection, fixtures and test/calibration, standards/certification, logistics, service/repair, and e-waste.
- [ ] **M01-E4-T07 [TEST]** Assess each local process for capability, quality limits, volume, skills, equipment, lead time, traceability, cost, and safe student/partner access; record which V-level evidence the capability can support and what upgrade gap remains, without assigning a product-authority level to a supplier or process itself.
- [ ] **M01-E4-T08 [SPEC]** Jointly instantiate the canonical M02 deployment-profile schema with the collected locale facts before either milestone releases; use a controlled provisional field register during concurrent drafting so a later jurisdiction can replace Benin data without editing universal technical content.

## Hands-on and real-life safeguard

At least twelve context briefs must contain an observable problem and engineering acceptance measures. Example: not “irrigation,” but “detect pump dry-running within 5 s, survive 10–16 V supply excursions, buffer 30 days without network, permit connector replacement with local tools, and explain false-alarm cost.” At least four briefs must represent scientific, industrial, artistic, assistive, or consumer contexts in addition to public-development needs.

## Required deliverables

- Learner/readiness research report and personas
- Context/problem library with partner evidence
- Regulation/accreditation/outcome mapping
- Dated infrastructure, supplier, landed-cost, and repair baseline
- Versioned deployment profile and manufacturing/service capability map with V0–V4 targets
- Partner engagement, ethics, data, and project-acceptance principles

## Exit criteria

- [ ] M03 can make safe platform and procurement decisions with current evidence.
- [ ] M05 has measured bridge requirements rather than assumptions.
- [ ] M1–M8 have multiple credible context candidates.
- [ ] Local regulatory gaps are owned and none are silently assumed resolved.
- [ ] The initial Benin profile is approved, sourced, dated, reviewable, and separable from the universal curriculum core.
- [ ] Local manufacture/service ambitions have measured capability evidence, gaps, partners, and truthful contribution/origin constraints.
