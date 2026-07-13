#!/usr/bin/env python3
"""Generate the canonical E1 curriculum records from the Course Master Document.

The generated ``.yml`` files contain JSON, which is valid YAML 1.2.  This keeps
the ordinary validation path dependency-free and deterministic while allowing
YAML-aware editors and downstream tooling to consume the records.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "curriculum" / "data"
SCHEMAS = ROOT / "curriculum" / "schemas"
I18N = ROOT / "curriculum" / "i18n"
MASTER = ROOT / "blueprint" / "COURSE_MASTER_DOCUMENT.md"
GENERATED_ON = "2026-07-13"
VERSION = "1.0.0"


PEOS = [
    ("PEO-1", "Practice", "contribute effectively to the design, verification, deployment, or maintenance of electronic and embedded products", "contribuer efficacement à la conception, la vérification, au déploiement ou à la maintenance de produits électroniques et embarqués", ["PLO-02", "PLO-03", "PLO-05", "PLO-07", "PLO-08"]),
    ("PEO-2", "Grow", "learn unfamiliar devices, standards, and tools from primary documentation and continue into employment, entrepreneurship, or advanced study", "apprendre à partir de sources primaires de nouveaux composants, normes et outils, puis poursuivre vers l'emploi, l'entrepreneuriat ou les études avancées", ["PLO-01", "PLO-11", "PLO-13", "PLO-14"]),
    ("PEO-3", "Lead responsibly", "communicate and collaborate across disciplines and languages while considering safety, ethics, sustainability, security, and community impact", "communiquer et collaborer entre disciplines et langues en intégrant sécurité, éthique, durabilité, cybersécurité et impact communautaire", ["PLO-09", "PLO-11", "PLO-12", "PLO-14"]),
    ("PEO-4", "Create value", "adapt globally sound engineering to local constraints and increase local design, production, test, service, and improvement capability", "adapter une ingénierie solide aux contraintes locales et accroître les capacités locales de conception, production, essai, service et amélioration", ["PLO-05", "PLO-06", "PLO-10", "PLO-12", "PLO-14"]),
    ("PEO-5", "Improve systems", "use measurements, field evidence, and stakeholder feedback to improve products and engineering processes", "utiliser les mesures, les preuves de terrain et les retours des parties prenantes pour améliorer les produits et processus d'ingénierie", ["PLO-07", "PLO-08", "PLO-10", "PLO-13", "PLO-14"]),
]


PLOS = [
    ("PLO-01", "Apply mathematics, science, and computation to formulate and solve complex electronics problems.", "Appliquer les mathématiques, les sciences et le calcul pour formuler et résoudre des problèmes électroniques complexes.", "Defensible model, computation, assumptions, and validation", 3),
    ("PLO-02", "Analyze and design analog, mixed-signal, digital, power, and feedback circuits.", "Analyser et concevoir des circuits analogiques, mixtes, numériques, de puissance et asservis.", "Design review plus measured performance", 3),
    ("PLO-03", "Design embedded software with peripherals, concurrency, real-time behavior, and resource constraints.", "Concevoir des logiciels embarqués avec périphériques, concurrence, comportement temps réel et contraintes de ressources.", "Tested firmware, timing and resource evidence", 3),
    ("PLO-04", "Describe and implement digital logic and computer architecture, including an FPGA-based system.", "Décrire et mettre en œuvre la logique numérique et l'architecture des ordinateurs, y compris un système sur FPGA.", "HDL verification and FPGA demonstration", 3),
    ("PLO-05", "Capture schematics and design manufacturable, testable, reliable PCBs and product realization packages.", "Saisir des schémas et concevoir des circuits imprimés et dossiers produit fabricables, testables et fiables.", "DRC-clean release, bring-up, assembly/test instructions, and production evidence", 3),
    ("PLO-06", "Select sensors, actuators, power sources, interfaces, and communication links from requirements and datasheets.", "Sélectionner capteurs, actionneurs, sources d'énergie, interfaces et liaisons à partir des exigences et fiches techniques.", "Trade study and requirements traceability", 3),
    ("PLO-07", "Plan experiments; measure safely; quantify uncertainty; analyze data; and draw justified conclusions.", "Planifier des expériences, mesurer en sécurité, quantifier l'incertitude, analyser les données et tirer des conclusions justifiées.", "Reproducible data package and uncertainty budget", 4),
    ("PLO-08", "Debug hardware and software systematically using hypotheses, instruments, isolation, and evidence.", "Déboguer systématiquement matériel et logiciel à l'aide d'hypothèses, d'instruments, d'isolement et de preuves.", "Timed fault-localization practical", 4),
    ("PLO-09", "Engineer systems for safety, security, privacy, EMC, reliability, sustainability, and lifecycle.", "Concevoir des systèmes intégrant sûreté, cybersécurité, vie privée, CEM, fiabilité, durabilité et cycle de vie.", "Hazard/threat analyses and verification cases", 3),
    ("PLO-10", "Create solutions responsive to user, cultural, environmental, economic, and manufacturing constraints, with a credible local realization and service plan.", "Créer des solutions adaptées aux contraintes humaines, culturelles, environnementales, économiques et de fabrication, avec un plan crédible de réalisation et de service locaux.", "Stakeholder-validated requirements, make/buy and local-value plan, and impact review", 3),
    ("PLO-11", "Communicate technical reasoning through schematics, code, data, reports, talks, and demonstrations to varied audiences.", "Communiquer le raisonnement technique par schémas, code, données, rapports, présentations et démonstrations à des publics variés.", "Professional design dossier and defense, bilingual abstract and cross-language briefing", 4),
    ("PLO-12", "Work effectively and inclusively in teams, plan work, manage interfaces, and resolve uncertainty.", "Travailler efficacement et de façon inclusive en équipe, planifier, gérer les interfaces et résoudre l'incertitude.", "Peer evidence, interface contracts, retrospectives", 3),
    ("PLO-13", "Learn independently from datasheets, standards, research, and experiments; evaluate source quality.", "Apprendre de manière autonome à partir de fiches techniques, normes, recherches et expériences; évaluer la qualité des sources.", "Datasheet-based implementation and literature trail", 3),
    ("PLO-14", "Practice ethically, manage configuration and evidence, and make honest claims about system performance.", "Exercer avec éthique, gérer la configuration et les preuves, et formuler des affirmations honnêtes sur les performances.", "Auditable repository, limitations, attribution, and AI-use log", 3),
]


# id, semester, credits, English title, French title, practical result, PLOs
COURSES = [
    ("ESE101", 1, 5, "Engineering Practice, Safety and Prototyping", "Pratique, sécurité et prototypage", "safe tool qualification and continuity tester", ["PLO-07", "PLO-08", "PLO-09", "PLO-14"]),
    ("MAT101", 1, 6, "Engineering Mathematics I", "Mathématiques I", "model and plot measured linear and nonlinear relations", ["PLO-01", "PLO-07"]),
    ("PHY101", 1, 5, "Physics I: Mechanics, Energy and Thermal Science", "Physique I", "energy and thermal experiment", ["PLO-01", "PLO-07"]),
    ("CSC101", 1, 5, "Programming and Computational Thinking", "Programmation", "tested Python data-acquisition and analysis script", ["PLO-01", "PLO-13", "PLO-14"]),
    ("ESE111", 1, 6, "DC Circuits and Measurement", "Circuits continus et mesure", "characterize and debug a sensor interface", ["PLO-01", "PLO-02", "PLO-07", "PLO-08"]),
    ("COM101", 1, 3, "Bilingual Technical Communication I", "Communication technique bilingue I", "English/French abstract, notebook, and technical explanation", ["PLO-11", "PLO-12", "PLO-14"]),
    ("MAT102", 2, 6, "Engineering Mathematics II", "Mathématiques II", "apply complex numbers, calculus, and linear algebra in circuits", ["PLO-01"]),
    ("PHY102", 2, 5, "Physics II: Fields, Waves and Materials", "Physique II", "field, wave, and material characterization", ["PLO-01", "PLO-07"]),
    ("ESE121", 2, 6, "AC Circuits, Transients and Signals", "Circuits alternatifs, transitoires et signaux", "filter and transient verification", ["PLO-01", "PLO-02", "PLO-07"]),
    ("ESE122", 2, 6, "Electronic Devices I", "Composants électroniques I", "diode/transistor switch and amplifier", ["PLO-02", "PLO-06", "PLO-07", "PLO-08"]),
    ("CSC102", 2, 4, "C Programming and Data Structures", "Langage C et structures de données", "tested C and scaffolded low-voltage MCU interface", ["PLO-03", "PLO-08", "PLO-14"]),
    ("DES102", 2, 3, "Human-Centered and Sustainable Design", "Conception centrée usager et durable", "repairability and lifecycle teardown", ["PLO-09", "PLO-10", "PLO-12"]),
    ("MAT201", 3, 6, "Differential Equations, Probability and Numerical Methods", "Équations différentielles, probabilités et calcul numérique", "fit, simulate, and validate a dynamic stochastic model", ["PLO-01", "PLO-07"]),
    ("ESE211", 3, 6, "Analog Electronics", "Électronique analogique", "low-noise multistage sensor front end", ["PLO-01", "PLO-02", "PLO-06", "PLO-07"]),
    ("ESE212", 3, 6, "Digital Logic and HDL", "Logique numérique et HDL", "verified finite-state controller on programmable logic", ["PLO-02", "PLO-04", "PLO-08"]),
    ("ESE213", 3, 5, "Signals and Systems", "Signaux et systèmes", "time/frequency analysis of a measured signal", ["PLO-01", "PLO-02", "PLO-07"]),
    ("ESE214", 3, 4, "Instrumentation and Metrology", "Instrumentation et métrologie", "calibrated instrument with uncertainty statement", ["PLO-06", "PLO-07", "PLO-13"]),
    ("PRJ201", 3, 3, "Integrated Design Studio I", "Atelier de conception intégrée I", "M3 design reviews and verification", ["PLO-08", "PLO-10", "PLO-11", "PLO-12", "PLO-14"]),
    ("ESE221", 4, 6, "Embedded Systems I", "Systèmes embarqués I", "bare-metal drivers, interrupts, timers, and low power", ["PLO-03", "PLO-06", "PLO-08"]),
    ("ESE222", 4, 5, "Feedback and Control", "Automatique", "identified and stabilized physical plant", ["PLO-01", "PLO-02", "PLO-07"]),
    ("ESE223", 4, 5, "Communications and Data Networks", "Communications et réseaux", "robust wired/wireless telemetry link", ["PLO-06", "PLO-07", "PLO-09"]),
    ("ESE224", 4, 5, "Power Electronics and Energy Systems", "Électronique de puissance et énergie", "protected DC conversion and power budget", ["PLO-02", "PLO-06", "PLO-09"]),
    ("ESE225", 4, 6, "PCB Design, EMC and Manufacturing", "Conception de PCB, CEM et fabrication", "fabrication-ready two-layer PCB and bring-up plan", ["PLO-05", "PLO-08", "PLO-09", "PLO-14"]),
    ("PRJ202", 4, 3, "Integrated Design Studio II", "Atelier de conception intégrée II", "M4 production release", ["PLO-05", "PLO-10", "PLO-11", "PLO-12", "PLO-14"]),
    ("ESE311", 5, 6, "Embedded Systems II: RTOS, Concurrency and Security", "RTOS, concurrence et sécurité", "RTOS product with tests, update, and threat model", ["PLO-03", "PLO-08", "PLO-09"]),
    ("ESE312", 5, 6, "Computer Architecture and FPGA Systems", "Architecture et systèmes FPGA", "verified RISC-V subset or accelerator on FPGA", ["PLO-03", "PLO-04", "PLO-08"]),
    ("ESE313", 5, 5, "Mixed-Signal Systems and Data Conversion", "Systèmes mixtes et conversion de données", "converter chain with noise/error budget", ["PLO-01", "PLO-02", "PLO-07"]),
    ("ESE314", 5, 5, "RF, Wireless and Antennas", "RF, radio et antennes", "legal low-power link and link-budget validation", ["PLO-01", "PLO-06", "PLO-09"]),
    ("ESE315", 5, 4, "Engineering Statistics, Reliability and Test", "Statistiques, fiabilité et test", "DOE, accelerated test, and production-test concept", ["PLO-01", "PLO-07", "PLO-09"]),
    ("PRJ301", 5, 4, "Product Engineering Sprint", "Sprint d'ingénierie produit", "M5 alpha prototype and design history file", ["PLO-05", "PLO-10", "PLO-12", "PLO-14"]),
    ("ESE321", 6, 5, "Digital Signal Processing", "Traitement numérique du signal", "real-time filter/classifier with fixed-point analysis", ["PLO-01", "PLO-03", "PLO-07"]),
    ("ESE322", 6, 5, "Drives, Renewable Energy and Advanced Control", "Entraînements, énergies renouvelables et commande avancée", "motor or energy-conversion controller", ["PLO-02", "PLO-06", "PLO-09"]),
    ("ESE323", 6, 5, "Embedded Linux and Edge Networking", "Linux embarqué et réseaux périphériques", "reproducible Linux service, device interface, and telemetry", ["PLO-03", "PLO-09", "PLO-14"]),
    ("ESE324", 6, 5, "Semiconductor and Integrated-Circuit Fundamentals", "Semi-conducteurs et circuits intégrés", "CMOS block analysis and layout-aware simulation", ["PLO-01", "PLO-02", "PLO-04"]),
    ("ESE325", 6, 4, "Systems Safety, Cybersecurity and Compliance", "Sûreté, cybersécurité et conformité", "hazard, threat, EMC, and compliance plan", ["PLO-09", "PLO-13", "PLO-14"]),
    ("PRJ302", 6, 6, "Community Field Engineering", "Ingénierie de terrain communautaire", "M6 pilot deployment and field evidence", ["PLO-07", "PLO-09", "PLO-10", "PLO-11", "PLO-12", "PLO-14"]),
    ("RES401", 7, 4, "Research Methods, Standards, Ethics and IP", "Recherche, normes, éthique et PI", "review, experiment plan, and ethics/IP analysis", ["PLO-07", "PLO-13", "PLO-14"]),
    ("ESE401", 7, 5, "Secure Hardware–Software Co-design", "Co-conception matériel–logiciel sécurisée", "root-of-trust, secure update, or fault-injection study", ["PLO-03", "PLO-04", "PLO-09"]),
    ("ELE4A", 7, 5, "Technical Elective A", "Option technique A", "cluster-specific evidence at integrated level", ["PLO-01", "PLO-13"]),
    ("ELE4B", 7, 5, "Technical Elective B", "Option technique B", "cluster-specific evidence at integrated level", ["PLO-01", "PLO-13"]),
    ("CAP401", 7, 8, "Capstone I: Discovery through Engineering Validation", "Projet de fin d'études I", "requirements, architecture, risks, prototypes, and CDR", ["PLO-05", "PLO-07", "PLO-10", "PLO-11", "PLO-12", "PLO-14"]),
    ("ENT401", 7, 3, "Enterprise, Manufacturing and Product Lifecycle", "Entrepreneuriat, fabrication et cycle de vie", "costed production and service plan", ["PLO-05", "PLO-09", "PLO-10", "PLO-14"]),
    ("CAP402", 8, 15, "Capstone II: Verification, Field Trial and Handover", "Projet de fin d'études II", "verified product, dossier, defense, and handover", ["PLO-05", "PLO-07", "PLO-08", "PLO-10", "PLO-11", "PLO-12", "PLO-14"]),
    ("IND402", 8, 6, "Internship or Applied Engineering Clinic", "Stage ou clinique d'ingénierie", "supervisor evidence and reflective technical report", ["PLO-11", "PLO-12", "PLO-13", "PLO-14"]),
    ("ELE4C", 8, 6, "Technical Elective C", "Option technique C", "cluster-specific advanced work", ["PLO-01", "PLO-13"]),
    ("SEM402", 8, 3, "Emerging Technology and Professional Seminar", "Technologies émergentes et séminaire professionnel", "technical horizon scan and bilingual briefing", ["PLO-11", "PLO-13", "PLO-14"]),
]


PROJECTS = [
    ("M1", 1, "Solar study-lamp monitor", "measurement, calibration, energy, technical explanation", "V0", ["G1", "G2"]),
    ("M2", 2, "Calibrated environmental monitor", "transistor interface, filtering, scaffolded MCU C, calibration", "V1", ["G1", "G2", "G3", "G4"]),
    ("M3", 3, "Precision instrument", "op-amps, noise, ADC, metrology", "V2", ["G1", "G2", "G4", "G5"]),
    ("M4", 4, "Custom-PCB resilient data logger", "MCU, power, PCB, EMC, DFM, firmware", "V2", ["G1", "G2", "G3", "G4", "G5", "G6"]),
    ("M5", 5, "Secure connected node", "concurrency, threat model, FPGA integration, reliability", "V3", ["G1", "G2", "G3", "G4", "G5", "G6", "G7"]),
    ("M6", 6, "Context-responsive field system", "stakeholders, Linux/edge, field reliability, service", "V3", ["G1", "G2", "G3", "G4", "G5", "G6", "G7", "G8"]),
    ("M7", 7, "Capstone engineering prototype", "research, standards, economics, complex interfaces", "V3", ["G1", "G2", "G3", "G4", "G5", "G6", "G7", "G8"]),
    ("M8", 8, "Qualified capstone release", "verification coverage, manufacture, maintenance, defense", "V4", ["G1", "G2", "G3", "G4", "G5", "G6", "G7", "G8", "G9"]),
]


RESOURCE_TYPES = [
    "syllabus", "prerequisite-diagnostic", "chapter", "lecture-studio-plan", "slides",
    "demonstration", "exploration", "problem-set", "solution", "laboratory", "mcq-item",
    "practical-design-assessment", "professor-notes", "project", "figure-metadata",
    "reference-artifact-metadata", "remediation-enrichment-map", "claim-register",
    "contribution-dossier", "qa-record",
]


def write_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def source_metadata() -> dict:
    raw = MASTER.read_bytes()
    return {
        "document_id": "ESE-CMD-001",
        "version": "0.2.0",
        "review_date": "2026-07-13",
        "path": "blueprint/COURSE_MASTER_DOCUMENT.md",
        "sha256": hashlib.sha256(raw).hexdigest(),
    }


def outcomes() -> dict:
    levels = [
        (0, "Encountered", "Sensibilisé", "recognize language and purpose with guidance", "concept check"),
        (1, "Assisted", "Accompagné", "execute a documented method safely", "guided lab"),
        (2, "Independent", "Autonome", "select and apply a method to a bounded problem", "practical exam or design task"),
        (3, "Integrated", "Intégré", "combine domains under incomplete and conflicting constraints", "milestone project"),
        (4, "Defensible", "Défendable", "justify trade-offs, verify claims, handle anomalies, and transfer learning", "capstone review and individual defense"),
    ]
    course_outcomes = []
    for cid, semester, _, title_en, title_fr, result, plos in COURSES:
        level = min(4, 1 + ((semester - 1) // 2))
        coid = f"{cid}-CO01"
        course_outcomes.append({
            "id": coid,
            "course_id": cid,
            "semester": semester,
            "definition": {
                "en": f"Produce and defend the course's core practical result: {result}.",
                "fr": f"Produire et défendre le résultat pratique central du cours « {title_fr} » avec des preuves traçables.",
            },
            "progression_level": level,
            "maps_to": plos,
            "evidence": [{"type": "direct-practical", "artifact": result, "individual_attribution_required": True}],
            "assessment_points": [f"{cid}-COURSE-END"],
            "status": "approved-baseline",
        })
    return {
        "schema_version": "1.0.0", "version": VERSION, "status": "approved-baseline",
        "source": source_metadata(),
        "progression_levels": [
            {"level": n, "name": {"en": en, "fr": fr}, "definition": {"en": definition, "fr": definition}, "typical_evidence": evidence}
            for n, en, fr, definition, evidence in levels
        ],
        "peos": [
            {"id": pid, "name": name, "definition": {"en": en, "fr": fr}, "time_horizon_years": "3-5", "maps_to": maps, "evidence_sources": ["graduate-survey", "employer-or-client-feedback", "portfolio-follow-up"], "status": "approved-baseline"}
            for pid, name, en, fr, maps in PEOS
        ],
        "plos": [
            {"id": pid, "definition": {"en": en, "fr": fr}, "graduation_evidence": evidence, "minimum_level": minimum, "graduation_confirmation": "G9", "mapped_peos": [p[0] for p in PEOS if pid in p[4]], "status": "approved-baseline"}
            for pid, en, fr, evidence, minimum in PLOS
        ],
        "course_outcomes": course_outcomes,
        "graduation_rule": {"all_plos_minimum": 3, "level_4_required": ["PLO-07", "PLO-08", "PLO-11"], "level_4_technical_elective_count": 2},
    }


def prerequisite_graph() -> dict:
    nodes = []
    for cid, semester, _, title_en, title_fr, _, _ in COURSES:
        nodes.append({"id": cid, "kind": "course", "semester": semester, "title": {"en": title_en, "fr": title_fr}, "remediation": "diagnostic, mapped bridge evidence, and reassessment before dependent work"})
    for pid, semester, title, _, _, _ in PROJECTS:
        nodes.append({"id": pid, "kind": "project", "semester": semester, "title": {"en": title, "fr": title}, "remediation": "owned project recovery plan with retained individual evidence"})
    nodes.append({"id": "PRJ302-G8-MODULE", "kind": "unit", "semester": 6, "title": {"en": "Early field-readiness module", "fr": "Module préalable de préparation au terrain"}, "remediation": "repeat consent, field-safety, privacy, communications, incident, and rollback cases"})
    gate_defs = [
        ("G1", "Safe bench user", "S1 week 4", ["ESE101"], ["ESE121", "ESE122"], "repeat supervised safety demonstration and stop-condition oral check"),
        ("G2", "Fundamental measurement and uncertainty", "end S1", ["ESE111", "M1"], ["M2", "ESE121"], "repeat individual measurement practical with uncertainty feedback"),
        ("G3", "Soldering and rework", "end S2", ["ESE101", "ESE122"], ["M3", "ESE225"], "supervised rework clinic followed by inspected individual sample"),
        ("G4", "C programming and source control", "before ESE221", ["CSC102"], ["ESE221", "M2"], "C/version-control bridge and individually defended test commit"),
        ("G5", "Analog/digital fault localization", "end S3", ["ESE211", "ESE212", "ESE214", "M3"], ["M4", "ESE225"], "targeted fault dojo and timed individual reassessment"),
        ("G6", "PCB release and safe bring-up", "end S4", ["ESE225", "PRJ202", "M4"], ["M5", "ESE311"], "correct release defects, rerun ERC/DRC, and repeat safe bring-up review"),
        ("G7", "Embedded timing/concurrency debug", "end S5", ["ESE311", "M5"], ["M6", "PRJ302"], "timing/concurrency remediation practical with trace evidence"),
        ("G8", "Field readiness and deployment ethics", "before stakeholder research or M6 field activity", ["PRJ302-G8-MODULE", "ESE325", "G1", "G7"], ["M6", "CAP401"], "repeat consent, ethics, field-safety, privacy, incident, and rollback scenarios; institutional approval remains separate"),
        ("G9", "Independent system defense", "capstone", ["CAP402", "M8"], [], "owned evidence-gap plan and a new individual defense; team evidence cannot substitute"),
    ]
    for gid, title, timing, requires, unlocks, remediation in gate_defs:
        nodes.append({"id": gid, "kind": "gate", "title": {"en": title, "fr": title}, "timing": timing, "requires": requires, "unlocks": unlocks, "remediation": remediation, "individual_evidence_required": True})

    requires = {
        "MAT102": ["MAT101"], "PHY102": ["PHY101", "MAT101"], "ESE121": ["ESE111", "G1"], "ESE122": ["ESE111", "G1"], "CSC102": ["CSC101"],
        "MAT201": ["MAT102"], "ESE211": ["ESE121", "ESE122", "MAT102"], "ESE212": ["CSC102"], "ESE213": ["ESE121", "MAT102"], "ESE214": ["ESE111", "MAT102"], "PRJ201": ["M2", "G4"],
        "ESE221": ["CSC102", "ESE122", "G4"], "ESE222": ["ESE121", "MAT201"], "ESE223": ["ESE121", "CSC102"], "ESE224": ["ESE122", "ESE121"], "ESE225": ["ESE211", "ESE212", "G3"], "PRJ202": ["PRJ201", "M3", "G5"],
        "ESE311": ["ESE221", "G6"], "ESE312": ["ESE212", "CSC102"], "ESE313": ["ESE211", "ESE213", "ESE214"], "ESE314": ["ESE213", "ESE223"], "ESE315": ["MAT201", "ESE214"], "PRJ301": ["M4", "G6"],
        "ESE321": ["ESE213", "ESE221", "MAT201"], "ESE322": ["ESE222", "ESE224"], "ESE323": ["ESE221", "ESE223"], "ESE324": ["ESE212", "ESE211"], "ESE325": ["ESE225", "ESE311"], "PRJ302": ["M4", "M5", "G7"],
        "PRJ302-G8-MODULE": ["PRJ302", "ESE325"], "RES401": ["M6", "G8"], "ESE401": ["ESE311", "ESE312", "ESE325"], "ELE4A": ["M6"], "ELE4B": ["M6"], "CAP401": ["M6", "G8"], "ENT401": ["M6"],
        "CAP402": ["CAP401", "M7"], "IND402": ["M6", "G8"], "ELE4C": ["ELE4A"], "SEM402": ["RES401"],
        "M1": ["ESE101", "ESE111"], "M2": ["M1", "ESE121", "ESE122", "CSC102", "DES102"], "M3": ["M2", "ESE211", "ESE212", "ESE214", "PRJ201"], "M4": ["M3", "ESE221", "ESE225", "PRJ202"], "M5": ["M4", "ESE311", "ESE312", "ESE313", "PRJ301"], "M6": ["M5", "ESE321", "ESE322", "ESE323", "ESE324", "ESE325", "PRJ302", "G8"], "M7": ["M6", "CAP401"], "M8": ["M7", "CAP402", "IND402"],
    }
    for gid, _, _, reqs, _, _ in gate_defs:
        requires[gid] = reqs
    co_requires = [
        {"from": "ESE101", "to": "ESE111", "constraint": "co-requisite; both gate later physical laboratories"},
        {"from": "ESE225", "to": "ESE221", "constraint": "sequenced co-requisite; interface/bring-up units precede MCU PCB work"},
        {"from": "ESE211", "to": "ESE214", "constraint": "may be co-taught with coordinated metrology evidence"},
    ]
    req_edges = [{"from": source, "to": target, "relation": "requires"} for target, sources in requires.items() for source in sources]
    unlocks = [{"from": edge["from"], "to": edge["to"], "relation": "unlocks"} for edge in req_edges]
    return {
        "schema_version": "1.0.0", "version": VERSION, "status": "approved-baseline", "source": source_metadata(),
        "nodes": nodes, "requires": req_edges, "co_requires": co_requires, "unlocks": unlocks,
        "root_policy": {"allowed_roots": ["ESE101", "MAT101", "PHY101", "CSC101", "ESE111", "COM101", "DES102"], "terminal_nodes": ["G9"], "orphan_definition": "a non-exempt node with neither an incoming nor outgoing requires edge"},
        "validation_policy": {"cycles_forbidden_in": "requires", "co_requisite_cycles_allowed": True, "unknown_ids_forbidden": True, "gate_bypass_forbidden": True},
    }


def parse_termbase() -> dict:
    text = MASTER.read_text(encoding="utf-8")
    block = text.split("### 11.6 Controlled terminology glossary", 1)[1].split("\n---\n", 1)[0]
    domain = None
    records = []
    seen = set()
    domain_ids = {
        "Foundations, measurement, and analog": "foundations-measurement-analog",
        "Digital, embedded, PCB, and FPGA": "digital-embedded-pcb-fpga",
        "Systems, assurance, manufacture, and lifecycle": "systems-assurance-manufacture-lifecycle",
    }
    for raw in block.splitlines():
        if raw.startswith("#### "):
            domain = domain_ids.get(raw[5:].strip())
            continue
        if not domain or not raw.startswith("|") or "---" in raw or "English" in raw:
            continue
        cells = [re.sub(r"\*", "", cell.strip()) for cell in raw.strip().strip("|").split("|")]
        if len(cells) != 3:
            continue
        en, fr, note = cells
        slug = re.sub(r"[^a-z0-9]+", ".", en.lower()).strip(".")
        concept_id = f"ee.{slug}"
        if concept_id in seen:
            continue
        seen.add(concept_id)
        fr_terms = [part.strip() for part in re.split(r"\s*/\s*", fr) if part.strip()]
        approved_fr = fr_terms[0]
        alternatives_fr = fr_terms[1:]
        acronyms = sorted(set(re.findall(r"\b[A-Z][A-Z0-9-]{1,}\b", en + " " + fr + " " + note)))
        avoided = []
        for pattern in (r"avoid(?: formal)? ([^;,]+)", r"never (?:literal )?([^;,]+)", r"not ([^;,]+)"):
            avoided.extend(m.group(1).strip(" *.") for m in re.finditer(pattern, note, re.I))
        scope_en = note if note else f"Use the precise {domain.replace('-', ' ')} meaning and define the operating context when ambiguity is possible."
        domain_fr = {
            "foundations-measurement-analog": "fondements, mesure et électronique analogique",
            "digital-embedded-pcb-fpga": "numérique, embarqué, circuits imprimés et FPGA",
            "systems-assurance-manufacture-lifecycle": "systèmes, assurance, fabrication et cycle de vie",
        }[domain]
        records.append({
            "id": concept_id,
            "concept_id": concept_id,
            "domain": domain,
            "definition": {
                "en": f"The controlled {domain.replace('-', ' ')} concept denoted by “{en}”; {scope_en.rstrip('.') }.",
                "fr": f"Concept contrôlé du domaine « {domain_fr} » désigné par « {approved_fr} »; préciser le contexte technique et les distinctions indiquées dans la note d'usage.",
            },
            "terms": {"en": {"preferred": en, "alternatives": []}, "fr": {"preferred": approved_fr, "alternatives": alternatives_fr}},
            "avoided_terms": [{"fr": phrase} for phrase in sorted(set(avoided))],
            "acronym_policy": {"acronyms": acronyms, "expand_on_first_use": bool(acronyms), "retain_in_tools_or_datasheets": bool(acronyms)},
            "example": {"en": f"Use “{en}” consistently in a requirement, calculation, schematic, or test statement.", "fr": f"Employer « {approved_fr} » de façon cohérente dans une exigence, un calcul, un schéma ou un essai."},
            "usage_note": note or "No additional trap recorded in the master glossary.",
            "reviewer": "bilingual-technical-editor",
            "status": "approved-baseline",
            "source_section": "11.6",
        })
    return {"schema_version": "1.0.0", "version": VERSION, "status": "approved-baseline", "source": source_metadata(), "terms": records}


def platform_matrix() -> dict:
    return {"schema_version": "1.0.0", "version": VERSION, "status": "draft", "platforms": [
        {"id": "PLAT-MCU-FOUNDATION", "category": "mcu-foundation", "capability_contract": "low-voltage MCU with ADC, PWM, digital I/O, documented offline toolchain, and debug route", "reference": "Raspberry Pi Pico 2 / RP2350-class", "alternatives": ["institution-approved capability-equivalent MCU"], "binding": "platform-bound", "review_due": "2027-07-13", "context_ids": [], "claim_ids": ["CLM-PLAT-001"], "status": "review"},
        {"id": "PLAT-MCU-PRO", "category": "mcu-professional", "capability_contract": "professional MCU with hardware debug, production peripherals, security, and long-lived documentation", "reference": "deployment-selected", "alternatives": [], "binding": "platform-bound", "review_due": "2027-07-13", "context_ids": [], "claim_ids": ["CLM-PLAT-001"], "status": "review"},
        {"id": "PLAT-FPGA", "category": "fpga", "capability_contract": "open-flow-capable FPGA path with HDL simulation, synthesis, timing, and hardware demonstration", "reference": "deployment-selected", "alternatives": ["simulation-first path before board access"], "binding": "platform-bound", "review_due": "2027-07-13", "context_ids": [], "claim_ids": ["CLM-PLAT-001"], "status": "review"},
        {"id": "PLAT-PCB", "category": "pcb-cad", "capability_contract": "offline schematic/PCB capture, ERC/DRC, fabrication outputs, and editable project source", "reference": "KiCad-family workflow", "alternatives": [], "binding": "platform-bound", "review_due": "2027-07-13", "context_ids": [], "claim_ids": ["CLM-PLAT-001"], "status": "review"},
    ]}


def component_inventory() -> dict:
    return {"schema_version": "1.0.0", "version": VERSION, "status": "draft", "components": [
        {"id": "COMP-DMM", "name": {"en": "digital multimeter", "fr": "multimètre numérique"}, "category": "instrument", "quantity_basis": "one per student", "minimum_specification": "CAT/rating and protection appropriate to approved low-voltage work; continuity, voltage, current, resistance", "approved_substitutes": [], "safety_level": "L1", "storage": "dry secured instrument storage", "maintenance": "pre-use inspection and scheduled function check", "calibration": "institutional metrology plan", "supplier_ids": [], "cost_ids": [], "status": "qualification-pending"},
        {"id": "COMP-BREADBOARD", "name": {"en": "solderless breadboard", "fr": "plaque d'essai sans soudure"}, "category": "construction", "quantity_basis": "one per student", "minimum_specification": "documented contact map and current limits", "approved_substitutes": [], "safety_level": "L1", "storage": "clean dry kit", "maintenance": "inspect damaged contacts", "calibration": "not-applicable", "supplier_ids": [], "cost_ids": [], "status": "qualification-pending"},
        {"id": "COMP-PSU-LV", "name": {"en": "current-limited low-voltage supply", "fr": "alimentation basse tension limitée en courant"}, "category": "instrument", "quantity_basis": "one per pair", "minimum_specification": "adjustable current limit and visible output indication", "approved_substitutes": ["approved battery pack with fuse/current limit"], "safety_level": "L1", "storage": "secured bench", "maintenance": "lead inspection and function check", "calibration": "scheduled voltage/current verification", "supplier_ids": [], "cost_ids": [], "status": "qualification-pending"},
    ]}


def project_dependencies() -> dict:
    projects = []
    for pid, semester, title, burden, target, gates in PROJECTS:
        projects.append({"id": pid, "semester": semester, "title": {"en": title, "fr": title}, "integration_burden": burden, "target_contribution_level": target, "required_gates": gates, "individual_evidence_required": True, "status": "approved-baseline"})
    return {"schema_version": "1.0.0", "version": VERSION, "status": "approved-baseline", "projects": projects, "dependencies": [{"from": f"M{n}", "to": f"M{n+1}", "relation": "requires"} for n in range(1, 8)]}


def local_value_ladder() -> dict:
    levels = [
        ("V0", "Diagnose and maintain", "identify functions, authenticate or characterize parts, localize faults, repair safely, and document limits", ["teardown/service map", "measurements", "fault/repair record", "component passport"]),
        ("V1", "Adapt and integrate", "select modules/components and design interfaces, harness/enclosure, firmware, calibration, and user/service adaptation", ["interface contract", "make/buy record", "locally executable build and calibration instructions"]),
        ("V2", "Design and verify", "own measurable requirements, architecture, editable design, test points, verification, and controlled release", ["editable source", "design reviews", "bring-up", "raw verification data", "independent reproduction"]),
        ("V3", "Pilot-production readiness", "execute controlled repeat assembly/test with incoming inspection, serialization, fixtures, nonconformance, cost, and service", ["repeat batch", "traveler", "checked production test", "sample-specific defect/rework/cost report", "technician handoff"]),
        ("V4", "Exercise product authority", "control configuration and lifecycle decisions, compliance, supplier quality, scale, warranty/service, improvement, IP/data, and end of life", ["accepted product dossier", "supplier/capability plan", "field/quality evidence", "training", "truthful contribution/origin statement"]),
    ]
    return {"schema_version": "1.0.0", "version": VERSION, "status": "approved-baseline", "levels": [{"id": lid, "name": name, "capability": capability, "required_evidence": evidence, "claim_limit": "claim only the highest level independently reproducible from released evidence"} for lid, name, capability, evidence in levels], "contribution_records": [
        {"id": "CONTRIB-ESE111-001", "project_id": "M1", "target_level": "V0", "achieved_level": None, "context_ids": [], "contributions": [{"domain": "measurement-and-diagnosis", "organization": "deploying institution", "location": "deployment-defined", "control": "learner-owned evidence", "evidence_ids": ["EVIDENCE-M1-V0-PENDING"]}], "imported_dependencies": [], "make_buy_rationale": "not applicable until a deployment selects apparatus", "cost_ids": [], "capability_gaps": ["deployment supplier, facility, and service evidence pending"], "next_local_step": "qualify the local apparatus and service route", "permitted_claim": "No geographic product-origin claim is permitted from this baseline record.", "legal_review": {"status": "required-before-origin-wording", "jurisdiction_ids": []}, "reviewer": "product-realization-lead", "status": "draft"}
    ]}


def supporting_records() -> dict[str, dict]:
    return {
        "claims.yml": {"schema_version": "1.0.0", "version": VERSION, "status": "draft", "claims": [
            {"id": "CLM-PLAT-001", "wording": "Named teaching platforms remain suitable only while they satisfy the capability scorecard and frozen cohort toolchain.", "claim_class": "platform-bound", "verification_method": "annual capability, supply, lifecycle, offline-tool, and substitute review", "source": {"type": "primary-program-source", "id": "ESE-CMD-001", "version": "0.2.0", "retrieved": "2026-07-13", "path": "blueprint/COURSE_MASTER_DOCUMENT.md"}, "assumptions_and_domain": "curriculum platform selection; not a product certification claim", "affected_assets": ["curriculum/data/platform-matrix.yml"], "reviewer": "platform-lead", "last_reviewed": "2026-07-13", "review_due": "2027-07-13", "trigger": "supply, lifecycle, security, toolchain, or local cost change", "context_ids": [], "status": "review"},
            {"id": "CLM-CTX-001", "wording": "The deployment profile is a dated overlay and does not lower universal outcome, safety, reasoning, or individual-evidence thresholds.", "claim_class": "concept-stable", "verification_method": "schema and parity review", "source": {"type": "primary-program-source", "id": "ESE-CMD-001", "version": "0.2.0", "retrieved": "2026-07-13", "path": "blueprint/COURSE_MASTER_DOCUMENT.md"}, "assumptions_and_domain": "all deployments", "affected_assets": ["curriculum/data/deployment-profiles/benin-2026-07.yml"], "reviewer": "learning-content-architect", "last_reviewed": "2026-07-13", "review_due": None, "trigger": "program-major-revision", "context_ids": [], "status": "approved"},
        ]},
        "context-briefs.yml": {"schema_version": "1.0.0", "version": VERSION, "status": "draft", "contexts": [
            {"id": "CTX-BJ-ENERGY-001", "profile_id": "DP-BJ-2026-07", "title": {"en": "Low-voltage study-lamp measurement context", "fr": "Contexte de mesure d'une lampe d'étude basse tension"}, "layer": "project-context", "need_statement": "Characterize an approved low-voltage lamp system without modifying hazardous circuitry.", "evidence_ids": ["CLM-CTX-001"], "stakeholder_authority": "staff-approved brief until G8 and any separate institutional approval", "portable_alternative": "any approved low-voltage source-load-light measurement system", "privacy_class": "no-personal-data", "review_date": "2026-07-13", "review_due": "2027-07-13", "status": "review"}
        ]},
        "manufacturing-capabilities.yml": {"schema_version": "1.0.0", "version": VERSION, "status": "draft", "capabilities": [
            {"id": "CAP-BJ-PENDING-001", "profile_id": "DP-BJ-2026-07", "capability": "electronics repair, assembly, test, calibration, fabrication, service, and end-of-life ecosystem mapping", "level_supported": None, "organizations": [], "locations": [], "evidence_ids": [], "limitations": ["No capability or geographic-origin assertion is approved until field evidence and named organizations are reviewed."], "review_date": "2026-07-13", "review_due": "2026-10-13", "status": "qualification-pending"}
        ]},
        "suppliers.yml": {"schema_version": "1.0.0", "version": VERSION, "status": "draft", "suppliers": [
            {"id": "SUP-BJ-PENDING-001", "profile_id": "DP-BJ-2026-07", "name": "deployment procurement qualification queue", "locations": [], "categories": ["components", "instruments", "fabrication", "logistics"], "lead_time_days": None, "qualification_evidence": [], "last_checked": "2026-07-13", "review_due": "2026-10-13", "status": "qualification-pending"}
        ]},
        "costs.yml": {"schema_version": "1.0.0", "version": VERSION, "status": "draft", "costs": [
            {"id": "COST-BJ-PENDING-001", "profile_id": "DP-BJ-2026-07", "item_id": "COMP-DMM", "supplier_id": "SUP-BJ-PENDING-001", "quantity": 1, "source_amount": None, "source_currency": None, "landed_amount": None, "deployment_currency": "XOF", "exchange_rate": None, "quoted_on": None, "valid_until": None, "included_costs": [], "status": "quote-required"}
        ]},
        "facilities.yml": {"schema_version": "1.0.0", "version": VERSION, "status": "draft", "facilities": [
            {"id": "FAC-BJ-PENDING-001", "profile_id": "DP-BJ-2026-07", "name": "deployment laboratory qualification record", "location": "to be named by deploying institution", "capabilities": [], "capacity_learners": None, "safety_authorizations": [], "equipment_ids": [], "accessibility_routes": [], "partner_routes": [], "evidence_ids": [], "review_date": "2026-07-13", "review_due": "2026-10-13", "status": "qualification-pending"}
        ]},
        "safety.yml": {"schema_version": "1.0.0", "version": VERSION, "status": "draft", "levels": [
            {"id": "L0", "scope": "observation, simulation, and de-energized inspection", "authorization_gate": None, "supervision": "as defined by activity", "stop_conditions": ["unknown energy source", "damaged apparatus"]},
            {"id": "L1", "scope": "approved low-voltage current-limited bench work", "authorization_gate": "G1", "supervision": "trained staff available under local laboratory plan", "stop_conditions": ["unexpected heat, smell, smoke, damaged insulation, unstable supply, or measurement outside expected bounds"]},
            {"id": "L2", "scope": "institution-controlled elevated energy or specialized apparatus", "authorization_gate": "deployment-specific", "supervision": "direct qualified supervision", "stop_conditions": ["any permit, enclosure, interlock, PPE, or supervision failure"]},
        ], "prohibited_self_study": ["mains", "high-energy battery", "RF power", "high voltage"], "incident_owner": "institutional-safety-lead"},
        "assessments.yml": {"schema_version": "1.0.0", "version": VERSION, "status": "draft", "assessments": [
            {"id": "ESE111-COURSE-END", "course_id": "ESE111", "type": "individual-practical", "outcome_ids": ["ESE111-CO01", "PLO-01", "PLO-07", "PLO-08"], "language_routes": ["en", "fr"], "difficulty_contract": "same construct, thresholds, data, and safety limits", "evidence": ["schematic", "raw measurements", "uncertainty statement", "fault-localization defense"], "rubric_total": 100, "status": "draft"}
        ]},
    }


def course_manifests() -> tuple[dict, dict]:
    graph_prerequisites: dict[str, list[str]] = {}
    for edge in prerequisite_graph()["requires"]:
        graph_prerequisites.setdefault(edge["to"], []).append(edge["from"])
    manifests = []
    for cid, semester, credits, title_en, title_fr, _, plos in COURSES:
        unit_ids = ["ESE111-CH04"] if cid == "ESE111" else []
        manifests.append({
            "id": cid, "semantic_id": cid, "title": {"en": title_en, "fr": title_fr}, "semester": semester,
            "credits_ects": credits, "editions": ["en", "fr"], "status": "brief", "owners": {"technical": "course-owner", "language": "bilingual-editor"},
            "outcomes": [f"{cid}-CO01", *plos], "prerequisites": sorted(graph_prerequisites.get(cid, [])), "unit_ids": unit_ids,
            "resource_applicability": {rtype: {"decision": "required", "reason": "complete package baseline; course owner may submit a reviewed not-applicable decision"} for rtype in RESOURCE_TYPES},
            "apparatus_paths": ["minimal", "standard", "advanced"], "offline_required": True, "localization_layer": "universal-core", "context_ids": [],
            "claim_register_ids": ["CLM-CTX-001"], "contribution_record_ids": [], "last_parity_review": "2026-07-13", "license": "CC-BY-SA-4.0",
        })
    units = {"schema_version": "1.0.0", "version": VERSION, "status": "draft", "units": [{
        "semantic_id": "ESE111-CH04", "course_id": "ESE111", "title": {"en": "Kirchhoff Models", "fr": "Modèles de Kirchhoff"}, "editions": ["en", "fr"], "status": "brief",
        "owners": {"technical": "ESE111-technical-owner", "language": "bilingual-technical-editor"}, "outcomes": ["ESE111-CO01", "PLO-01", "PLO-07", "PLO-08"], "prerequisites": [],
        "resource_applicability": {rtype: {"decision": "required", "reason": "paired vertical exemplar contract"} for rtype in RESOURCE_TYPES},
        "hands_on_contract": {"real_life_question": "How can measured node voltages and branch currents reveal whether an unfamiliar low-voltage network matches its schematic?", "prediction": "predict signs and approximate magnitudes before calculation or measurement", "student_action": "construct or inspect an approved network and make individual instrument decisions", "physical_or_data_evidence": "schematic, raw voltage/current table, uncertainty, and KCL/KVL residuals", "fault_or_anomaly": "one documented wiring or measurement fault with hypothesis-led localization", "design_decision": "select test points and a measurement sequence that controls risk and loading", "acceptance_test": "independently reconcile the physical network, schematic, equations, and measurements within stated uncertainty"},
        "apparatus_paths": {"minimal": "DMM, current-limited low-voltage source, passive network", "standard": "minimal plus bench supply and oscilloscope", "advanced": "standard plus automated acquisition; same individual evidence threshold"},
        "platform_binding": "concept-stable", "localization_layer": "universal-core", "context_ids": [], "claim_register_ids": ["CLM-CTX-001"], "claim_review_due": None,
        "contribution_record_ids": [], "last_parity_review": "2026-07-13", "license": "CC-BY-SA-4.0",
    }]}
    return {"schema_version": "1.0.0", "version": VERSION, "status": "draft", "courses": manifests}, units


def deployment_profile() -> dict:
    return {
        "schema_version": "1.0.0", "version": VERSION, "id": "DP-BJ-2026-07", "country_code": "BJ", "name": "Benin reference deployment evidence queue", "effective_date": "2026-07-13", "review_due": "2026-10-13", "status": "mapping-in-progress", "release_eligible": False,
        "universal_contract": {"outcome_set": "outcomes.yml@1.0.0", "prerequisite_graph": "prerequisite-graph.yml@1.0.0", "threshold_changes_permitted": False},
        "jurisdictions": [{"id": "JUR-BJ-PENDING", "name": "Benin national and applicable regional/institutional mappings", "authoritative_sources": [], "areas": ["higher-education", "credits-and-award", "electrical", "occupational", "fire", "chemical", "battery", "RF-telecommunications", "e-waste", "environment", "data-protection", "human-participant", "product", "import", "product-origin"], "verification_status": "pending-authoritative-local-review", "reviewer": "deploying-institution-authority", "review_due": "2026-10-13"}],
        "languages": ["fr", "en"], "currency": "XOF", "context_ids": ["CTX-BJ-ENERGY-001"], "facility_ids": ["FAC-BJ-PENDING-001"], "supplier_ids": ["SUP-BJ-PENDING-001"], "manufacturing_capability_ids": ["CAP-BJ-PENDING-001"],
        "required_evidence_gaps": ["regulator and institutional mappings", "grid and climate primary data", "supplier quotes and landed costs", "facility and computing baseline", "manufacturing/service ecosystem", "product-origin rules"],
        "claim_ids": ["CLM-CTX-001"], "approvers": {"institutional": None, "regulatory": None, "program": "program-board-pending"},
    }


def schema(name: str, required: list[str], properties: dict, *, title: str) -> dict:
    base_properties = {
        "schema_version": {"type": "string", "pattern": r"^\d+\.\d+\.\d+$"},
        "version": {"type": "string", "pattern": r"^\d+\.\d+\.\d+$"},
        "status": {"type": "string"},
    }
    return {
        "$schema": "https://json-schema.org/draft/2020-12/schema", "$id": f"https://emm.edu/schemas/{name}.schema.json", "title": title, "type": "object",
        "required": required, "properties": {**base_properties, **properties}, "additionalProperties": False,
        "$defs": {
            "id": {"type": "string", "pattern": r"^[A-Z][A-Z0-9]*(?:-[A-Z0-9]+)+$"},
            "date": {"type": "string", "format": "date"},
            "localized": {"type": "object", "required": ["en", "fr"], "properties": {"en": {"type": "string", "minLength": 1}, "fr": {"type": "string", "minLength": 1}}, "additionalProperties": False},
            "status": {"enum": ["brief", "draft", "review", "technical-review", "language-review", "pilot", "pilot-ready", "stable", "released", "retired", "approved", "approved-baseline", "mapping-in-progress", "qualification-pending", "quote-required", "not-started", "pending"]},
        },
    }


def schemas() -> dict[str, dict]:
    def field_contract(field: str) -> dict:
        if field in {"title", "name", "definition"}:
            return {"type": ["object", "string"]}
        if field in {"status"}:
            return {"$ref": "#/$defs/status"}
        if field in {"id", "semantic_id", "course_id", "profile_id", "supplier_id", "item_id", "project_id", "manifest_id"} or field.endswith("_id"):
            return {"type": "string", "minLength": 1}
        if field.endswith("_ids") or field in {
            "levels", "projects", "dependencies", "platforms", "components", "contexts", "capabilities", "suppliers", "costs", "facilities", "claims", "assessments", "courses", "units", "items", "peos", "plos", "course_outcomes", "nodes", "requires", "co_requires", "unlocks", "contribution_records", "jurisdictions",
            "editions", "outcomes", "prerequisites", "languages", "required_evidence_gaps", "areas", "authoritative_sources", "locations", "categories", "qualification_evidence", "included_costs", "safety_authorizations", "accessibility_routes", "partner_routes", "required_gates", "evidence", "evidence_sources", "maps_to", "mapped_peos", "assessment_points", "progression_levels", "affected_assets", "stop_conditions", "prohibited_self_study", "imported_dependencies", "capability_gaps", "required_evidence", "contributions", "edition_children", "approval_facets", "pilots", "evidence_links",
        }:
            return {"type": "array"}
        if field in {"effective_date", "review_due", "review_date", "last_reviewed", "last_parity_review", "last_checked", "quoted_on", "valid_until", "retrieved"}:
            return {"type": ["string", "null"], "format": "date"}
        if field in {"semester", "credits_ects", "quantity", "capacity_learners", "rubric_total", "progression_level", "minimum_level", "source_amount", "landed_amount", "exchange_rate", "lead_time_days", "level"}:
            return {"type": ["number", "null"], "minimum": 0}
        if field in {"release_eligible", "offline_required", "individual_evidence_required"}:
            return {"type": "boolean"}
        if field in {"source", "owners", "universal_contract", "approvers", "legal_review", "resource_applicability", "hands_on_contract", "acronym_policy", "terms", "avoided_terms", "example", "apparatus_paths", "defect_disposition"}:
            return {"type": ["object", "array"]}
        return {"type": ["string", "object", "array", "number", "boolean", "null"]}

    def arr(required: list[str]) -> dict:
        return {
            "type": "array",
            "items": {
                "type": "object",
                "required": required,
                "properties": {field: field_contract(field) for field in required},
            },
        }
    return {
        "platform": schema("platform", ["schema_version", "version", "status", "platforms"], {"platforms": arr(["id", "category", "capability_contract", "binding", "review_due", "status"])}, title="Platform matrix"),
        "component": schema("component", ["schema_version", "version", "status", "components"], {"components": arr(["id", "name", "category", "quantity_basis", "minimum_specification", "safety_level", "maintenance", "calibration", "status"])}, title="Component inventory"),
        "project": schema("project", ["schema_version", "version", "status", "projects", "dependencies"], {"projects": arr(["id", "semester", "title", "target_contribution_level", "required_gates", "status"]), "dependencies": arr(["from", "to", "relation"])}, title="Project dependency records"),
        "context": schema("context", ["schema_version", "version", "status", "contexts"], {"contexts": arr(["id", "profile_id", "title", "layer", "need_statement", "evidence_ids", "portable_alternative", "review_date", "review_due", "status"])}, title="Context briefs"),
        "deployment-profile": schema("deployment-profile", ["schema_version", "version", "id", "country_code", "effective_date", "review_due", "status", "release_eligible", "universal_contract", "jurisdictions", "required_evidence_gaps"], {"id": {"$ref": "#/$defs/id"}, "country_code": {"type": "string", "pattern": "^[A-Z]{2}$"}, "name": {"type": "string"}, "effective_date": {"$ref": "#/$defs/date"}, "review_due": {"$ref": "#/$defs/date"}, "release_eligible": {"type": "boolean"}, "universal_contract": {"type": "object", "required": ["outcome_set", "prerequisite_graph", "threshold_changes_permitted"]}, "jurisdictions": {"type": "array", "items": {"$ref": "jurisdiction.schema.json"}}, "languages": {"type": "array"}, "currency": {"type": "string"}, "context_ids": {"type": "array"}, "facility_ids": {"type": "array"}, "supplier_ids": {"type": "array"}, "manufacturing_capability_ids": {"type": "array"}, "required_evidence_gaps": {"type": "array"}, "claim_ids": {"type": "array"}, "approvers": {"type": "object"}}, title="Dated deployment profile"),
        "jurisdiction": {"$schema": "https://json-schema.org/draft/2020-12/schema", "$id": "https://emm.edu/schemas/jurisdiction.schema.json", "title": "Jurisdiction mapping", "type": "object", "required": ["id", "name", "authoritative_sources", "areas", "verification_status", "reviewer", "review_due"], "properties": {"id": {"type": "string"}, "name": {"type": "string"}, "authoritative_sources": {"type": "array"}, "areas": {"type": "array", "minItems": 1}, "verification_status": {"enum": ["pending-authoritative-local-review", "review", "approved", "expired"]}, "reviewer": {"type": "string"}, "review_due": {"type": "string", "format": "date"}}, "additionalProperties": False},
        "manufacturing-capability": schema("manufacturing-capability", ["schema_version", "version", "status", "capabilities"], {"capabilities": arr(["id", "profile_id", "capability", "organizations", "locations", "evidence_ids", "limitations", "review_date", "review_due", "status"])}, title="Local manufacturing and service capability"),
        "supplier": schema("supplier", ["schema_version", "version", "status", "suppliers"], {"suppliers": arr(["id", "profile_id", "name", "locations", "categories", "qualification_evidence", "last_checked", "review_due", "status"])}, title="Supplier qualification"),
        "cost": schema("cost", ["schema_version", "version", "status", "costs"], {"costs": arr(["id", "profile_id", "item_id", "supplier_id", "quantity", "source_amount", "source_currency", "landed_amount", "deployment_currency", "quoted_on", "valid_until", "included_costs", "status"])}, title="Dated landed-cost records"),
        "facility": schema("facility", ["schema_version", "version", "status", "facilities"], {"facilities": arr(["id", "profile_id", "name", "location", "capabilities", "capacity_learners", "safety_authorizations", "equipment_ids", "accessibility_routes", "partner_routes", "evidence_ids", "review_date", "review_due", "status"])}, title="Facility capability records"),
        "contribution": schema("contribution", ["schema_version", "version", "status", "levels", "contribution_records"], {"levels": arr(["id", "name", "capability", "required_evidence", "claim_limit"]), "contribution_records": arr(["id", "project_id", "target_level", "contributions", "imported_dependencies", "make_buy_rationale", "capability_gaps", "next_local_step", "permitted_claim", "legal_review", "reviewer", "status"])}, title="V0-V4 and contribution/provenance dossier"),
        "claim-source": schema("claim-source", ["schema_version", "version", "status", "claims"], {"claims": arr(["id", "wording", "claim_class", "verification_method", "source", "assumptions_and_domain", "affected_assets", "reviewer", "last_reviewed", "trigger", "context_ids", "status"])}, title="Technical claim and source register"),
        "safety": schema("safety", ["schema_version", "version", "status", "levels", "prohibited_self_study", "incident_owner"], {"levels": arr(["id", "scope", "authorization_gate", "supervision", "stop_conditions"]), "prohibited_self_study": {"type": "array"}, "incident_owner": {"type": "string"}}, title="Safety levels and authorization"),
        "assessment": schema("assessment", ["schema_version", "version", "status", "assessments"], {"assessments": arr(["id", "course_id", "type", "outcome_ids", "language_routes", "difficulty_contract", "evidence", "rubric_total", "status"])}, title="Assessment contract"),
        "course-manifest": schema("course-manifest", ["schema_version", "version", "status", "courses"], {"courses": arr(["id", "semantic_id", "title", "semester", "credits_ects", "editions", "status", "owners", "outcomes", "prerequisites", "unit_ids", "resource_applicability", "apparatus_paths", "offline_required", "localization_layer", "context_ids", "claim_register_ids", "contribution_record_ids", "last_parity_review", "license"])}, title="Canonical course manifests"),
        "unit-manifest": schema("unit-manifest", ["schema_version", "version", "status", "units"], {"units": arr(["semantic_id", "course_id", "title", "editions", "status", "owners", "outcomes", "prerequisites", "resource_applicability", "hands_on_contract", "apparatus_paths", "platform_binding", "localization_layer", "context_ids", "claim_register_ids", "contribution_record_ids", "last_parity_review", "license"])}, title="Canonical vertical-unit manifests"),
        "backlog": schema("backlog", ["schema_version", "version", "generated_from", "items"], {"generated_from": {"type": "array"}, "generated_at": {"type": "string"}, "generation_rule": {"type": "string", "minLength": 1}, "items": arr(["id", "manifest_id", "manifest_kind", "resource", "applicability", "edition_children", "approval_facets", "apparatus_paths", "pilots", "defect_disposition", "evidence_links", "approver", "status"])}, title="Generated canonical child backlog"),
        "outcome": schema("outcome", ["schema_version", "version", "status", "progression_levels", "peos", "plos", "course_outcomes", "graduation_rule"], {"progression_levels": arr(["level", "name", "definition", "typical_evidence"]), "peos": arr(["id", "name", "definition", "time_horizon_years", "maps_to", "evidence_sources", "status"]), "plos": arr(["id", "definition", "graduation_evidence", "minimum_level", "graduation_confirmation", "mapped_peos", "status"]), "course_outcomes": arr(["id", "course_id", "semester", "definition", "progression_level", "maps_to", "evidence", "assessment_points", "status"]), "graduation_rule": {"type": "object"}, "source": {"type": "object"}}, title="Program and course outcomes"),
        "prerequisite-graph": schema("prerequisite-graph", ["schema_version", "version", "status", "nodes", "requires", "co_requires", "unlocks", "root_policy", "validation_policy"], {"nodes": arr(["id", "kind", "title", "remediation"]), "requires": arr(["from", "to", "relation"]), "co_requires": arr(["from", "to", "constraint"]), "unlocks": arr(["from", "to", "relation"]), "root_policy": {"type": "object"}, "validation_policy": {"type": "object"}, "source": {"type": "object"}}, title="Course, project, unit, and competence dependency graph"),
        "termbase": schema("termbase", ["schema_version", "version", "status", "terms"], {"terms": arr(["id", "concept_id", "domain", "definition", "terms", "avoided_terms", "acronym_policy", "example", "usage_note", "reviewer", "status", "source_section"]), "source": {"type": "object"}}, title="Controlled bilingual terminology"),
    }


def canonical_assets() -> dict[Path, object]:
    assets: dict[Path, object] = {
        DATA / "outcomes.yml": outcomes(),
        DATA / "prerequisite-graph.yml": prerequisite_graph(),
        I18N / "termbase.yml": parse_termbase(),
        DATA / "platform-matrix.yml": platform_matrix(),
        DATA / "component-inventory.yml": component_inventory(),
        DATA / "project-dependencies.yml": project_dependencies(),
        DATA / "local-value-ladder.yml": local_value_ladder(),
    }
    for name, value in supporting_records().items():
        assets[DATA / name] = value
    courses, units = course_manifests()
    assets[DATA / "course-manifests.yml"] = courses
    assets[DATA / "unit-manifests.yml"] = units
    assets[DATA / "deployment-profiles" / "benin-2026-07.yml"] = deployment_profile()
    for name, value in schemas().items():
        assets[SCHEMAS / f"{name}.schema.json"] = value
    return assets


def generate() -> None:
    for path, value in canonical_assets().items():
        write_json(path, value)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="fail if regenerated canonical files differ")
    args = parser.parse_args()
    if not args.check:
        generate()
        return 0
    assets = canonical_assets()
    changed = []
    for path, value in assets.items():
        expected = json.dumps(value, ensure_ascii=False, indent=2) + "\n"
        if not path.exists() or path.read_text(encoding="utf-8") != expected:
            changed.append(str(path.relative_to(ROOT)))
    if changed:
        print("canonical generation drift:\n" + "\n".join(f"- {path}" for path in changed))
        return 1
    print(f"canonical generation check passed ({len(assets)} files)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
