# Laboratory safety system / Système de sécurité du laboratoire

**System ID:** ESE-SAF-001  
**Version:** 0.1.0  
**Status:** draft; institutional review and adoption required / brouillon ; revue et adoption institutionnelles requises  
**Scope:** universal program core; deployment overlays must add current jurisdiction, facility and emergency-service data / noyau universel ; les déploiements doivent ajouter les données actuelles de juridiction, de locaux et de secours

This directory implements the documentary portion of M03 Epic E1. It does not
record or imply institutional adoption, a facility inspection, a human approval,
an authorization award, or a live drill. Blank signature and evidence fields are
deliberate release gates.

Ce répertoire réalise la partie documentaire de l'Epic E1 de M03. Il ne constate
ni adoption institutionnelle, ni inspection des locaux, ni approbation humaine,
ni autorisation attribuée, ni exercice réel. Les champs de signature et de preuve
laissés vides constituent volontairement des portes de diffusion.

## Controlled artifact map / Carte des documents maîtrisés

| Semantic ID | English | Français | Purpose / Finalité |
|---|---|---|---|
| ESE-SAF-001 | [Safety manual](en/safety-manual.md) | [Manuel de sécurité](fr/manuel-de-securite.md) | L0–L4 operating procedures |
| ESE-SAF-002 | [Induction and authorization](en/induction-and-authorization.md) | [Accueil et autorisation](fr/accueil-et-autorisation.md) | practice quiz, stations, calibration, remediation |
| ESE-SAF-TC-001 | [Shared technical contract](shared/technical-contract.md) | same / identique | common limits, ratios and gate crosswalk |
| ESE-SAF-FRM-001 | [Activity risk assessment](templates/activity-risk-assessment-and-approval.md) | bilingual / bilingue | new-domain review and approval record |
| ESE-SAF-FRM-002 | [Authorization record](templates/authorization-record.md) | bilingual / bilingue | assessment, expiry, suspension and requalification |
| ESE-SAF-FRM-003 | [Facility inspection](templates/facility-inspection-record.md) | bilingual / bilingue | RCD/GFCI, isolation, fire, first aid, ventilation, ESD, storage, exits, access, signs |
| ESE-SAF-FRM-004 | [Drill protocol](templates/drill-protocol-and-record.md) | bilingual / bilingue | incident and damaged-energy-source exercises |
| ESE-SAF-FRM-005 | [Event and quarantine record](templates/event-quarantine-and-waste-record.md) | bilingual / bilingue | incident, near miss, quarantine and waste trace |

## Control and release rules / Règles de maîtrise et de diffusion

- The safety authority owns limits, authorization, suspension and release from
  quarantine. An instructor may stop work but may not self-approve a hazardous
  activity they authored.
- L3/L4 work and supported self-study boundaries cannot be relaxed by a course
  note. The stricter applicable institutional or legal requirement always wins.
- Technical and pedagogical EN/FR reviewers must confirm parity before release.
- A facility checklist becomes evidence only when an identified competent person
  records date, location, instrument/result, defect disposition and signature.
- A drill template becomes evidence only after a scheduled exercise produces
  participant, observer, timing, deviation and corrective-action records.
- Live high-stakes gate variants, answer keys and student records belong in the
  separately permissioned assessment/records store. This public directory holds
  the construct, formative practice and blank records only.

- L'autorité de sécurité maîtrise les limites, autorisations, suspensions et
  sorties de quarantaine. Un enseignant peut arrêter le travail, mais ne peut pas
  approuver seul une activité dangereuse qu'il a rédigée.
- Une note de cours ne peut réduire les exigences L3/L4 ni les interdictions de
  l'autoformation accompagnée. L'exigence institutionnelle ou légale la plus
  stricte s'applique.
- Des réviseurs techniques et pédagogiques EN/FR vérifient la parité avant diffusion.
- Une fiche d'inspection ne devient une preuve qu'après enregistrement du lieu, de
  la date, de la méthode, du résultat, des écarts et de la signature d'une personne compétente.
- Une fiche d'exercice ne devient une preuve qu'après consignation des participants,
  observateurs, temps, écarts et actions correctives.
- Les variantes de portes à enjeu élevé, corrigés et dossiers d'étudiants restent
  dans le stockage d'évaluation séparé et autorisé.

## Deployment fields that must be completed / Champs à compléter au déploiement

Institution, campus/room, accountable safety authority and deputy, emergency
numbers, assembly point, first-aid/fire responders, applicable electrical/fire/
chemical/battery/RF/e-waste rules and editions, inspection frequency, record
retention, waste contractors and authorization-validity periods.

Établissement, campus/local, autorité de sécurité et suppléant, numéros d'urgence,
point de rassemblement, secouristes et équipiers incendie, règles et éditions
applicables en électricité/incendie/chimie/batteries/RF/déchets, périodicité des
inspections, conservation des dossiers, prestataires déchets et durées d'autorisation.

