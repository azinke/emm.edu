# Electronics from Elements to Systems

**Document ID:** EMM-CMD-001
**Status:** curriculum architecture
**Version:** 0.4.0
**Last structural review:** 2026-07-14

## 1. Purpose

This document defines the learning architecture for a free, book-first
electronics curriculum. The primary publication is one coherent textbook that
starts with electrical quantities and simple components, develops the major
electronics domains, and ends with complete, verifiable systems.

The textbook is the canonical explanation of a topic. Courses, laboratories,
projects, and lectures select from it by stable chapter ID; they do not maintain
their own copies of the same theory.

The curriculum is designed for self-study, classroom use, and adaptation into a
four-year electronics systems engineering program. It is not an accreditation
claim. A deploying institution remains responsible for local credit, safety,
regulatory, language, staffing, and facility approval.

## 2. Canonical source model

The repository has five content layers:

| Layer | Purpose | Canonical location |
|---|---|---|
| Book | Durable explanations, examples, exercises, and references | `curriculum/book/` |
| Courses | Ordered routes through book chapters | `curriculum/courses/` |
| Labs | Physical evidence and safe measurement | `curriculum/labs/` |
| Projects | Integration from small circuits to fielded systems | `curriculum/projects/` |
| Instructor material | Lecture plans and teaching notes derived from the other layers | `curriculum/instructor/` |

Each concept is explained once. A course record contains outcomes, prerequisites,
chapter IDs, lab IDs, and project IDs. A lecture plan points to sections in the
book. Translation is performed at the book layer before translated course
material is derived.

## 3. Educational direction

The reader follows a vertical slice through electronics:

1. observe voltage, current, energy, and signals safely;
2. model sources, loads, passive components, and networks;
3. understand semiconductor and analog building blocks;
4. construct digital and programmable systems;
5. cross between analog, digital, power, control, and communication domains;
6. realize hardware that can be manufactured, tested, secured, and maintained;
7. integrate and defend complete systems under real constraints.

Every major idea should move through:

**phenomenon → model → calculation → simulation → measurement → design decision**

Simulation is important but does not replace personal measurement where physical
competence is an outcome. Debugging, uncertainty, safety, ethics, repairability,
security, and lifecycle reasoning recur throughout the book.

## 4. Reader profile

The main text assumes secondary-school algebra and elementary physical science.
Programming and prior electronics experience are not required. Mathematical
appendices provide just-in-time support for complex numbers, calculus, linear
algebra, differential equations, probability, statistics, and numerical methods.

The first chapters must be usable with a low-voltage supply or batteries, a
breadboard, passive components, and a multimeter. Higher-energy, mains, RF-power,
high-voltage, and battery-pack work requires separately approved facilities and
supervision.

## 5. Book architecture

Stable IDs are semantic and must not be renumbered when chapters move.

| Part | IDs | Scope |
|---|---|---|
| I. Electrical foundations | F01–F08 | safety, quantities, sources, loads, networks, energy, measurement, transients, AC |
| II. Devices and analog circuits | A01–A08 | semiconductors, transistors, amplifiers, op-amps, instrumentation, noise, integrated circuits, optoelectronics and HMI |
| III. Digital hardware | D01–D06 | representation, logic, state, HDL, architecture, FPGA systems |
| IV. Embedded systems | E01–E06 | C, microcontrollers, timing, protocols, RTOS, embedded Linux |
| V. Signals, control, power, and communication | S01–S10 | signals, conversion, DSP, control, converters, drives, RF, edge inference, off-grid energy, LPWAN connectivity |
| VI. Product realization | R01–R06 | requirements, PCB, EMC, manufacture, test, assurance, lifecycle |
| VII. Complete systems | X01–X05 | instruments, loggers, connected nodes, field systems, capstone handover |
| Appendices | M01–M03, T01–T03 | mathematics, datasheets, tools, reproducible engineering |

The complete chapter registry is
[`curriculum/book/chapters.toml`](../curriculum/book/chapters.toml). The
registry, not the sidebar order, is the machine-readable definition of scope.

## 6. Knowledge threads

The chapter sequence is linear enough for a first reading but preserves several
threads that return at increasing depth:

| Thread | Foundation | Development | System-level destination |
|---|---|---|---|
| Models and mathematics | units, algebra, conservation | differential, frequency, probabilistic models | model selection and validation |
| Analog and mixed signal | passive networks | devices, gain, feedback, noise, conversion | complete signal chains |
| Digital and computing | bits and logic | state, HDL, architecture | FPGA and hardware/software co-design |
| Embedded software | data and C | drivers, timing, protocols, concurrency | updateable edge products |
| Energy and control | power and thermal limits | feedback, converters, motors, storage | safe efficient energy systems |
| Measurement and debug | DMM and uncertainty | instruments, fault isolation, metrology | qualification and production test |
| Realization | breadboard and soldering | schematic, layout, EMC, bring-up | repeatable manufacturing and service |
| Professional practice | notebooks and evidence | requirements, reviews, security, ethics | defensible handover and lifecycle |

## 7. Program outcomes

An institution using the complete program should require graduates to:

1. apply mathematics, science, and computation to electronics problems;
2. analyze and design analog, mixed-signal, digital, power, and feedback circuits;
3. create tested embedded software under timing and resource constraints;
4. implement and verify digital hardware and computer architecture;
5. design manufacturable, testable, and maintainable PCBs and product packages;
6. select sensors, actuators, sources, interfaces, and communication links;
7. plan experiments, measure safely, quantify uncertainty, and justify conclusions;
8. debug hardware and software systematically from evidence;
9. address safety, security, privacy, EMC, reliability, sustainability, and lifecycle;
10. design for user, environmental, economic, and manufacturing constraints;
11. communicate through schematics, code, data, reports, demonstrations, and talks;
12. work inclusively, manage interfaces, and resolve uncertainty in teams;
13. learn from datasheets, standards, research, and experiments;
14. manage configuration and make honest, traceable performance claims.

These outcomes are encoded in [`outcomes.toml`](../curriculum/courses/outcomes.toml)
as a mapping to the chapters that develop them; course coverage and depth are then
derived from the chapter mappings rather than restated per course.

## 8. Reference course architecture

The reference program remains eight semesters and 240 ECTS-equivalent credits,
but its implementation is now data rather than duplicated prose:

- [`catalog.toml`](../curriculum/courses/catalog.toml) defines every course and,
  per chapter, its coverage level (`introduce`, `reinforce`, or `master`);
- [`program.toml`](../curriculum/courses/program.toml) places courses by semester;
- [`outcomes.toml`](../curriculum/courses/outcomes.toml) maps each program outcome
  to the chapters that develop it;
- [`labs/catalog.toml`](../curriculum/labs/catalog.toml) defines practical work;
- [`projects/spine.toml`](../curriculum/projects/spine.toml) defines integration milestones.

`tools/validate.py` checks structural coherence, including that no chapter is
scheduled before a chapter it depends on and that every program outcome is both
introduced and mastered. `tools/report.py` renders the maturity dashboard,
outcome assurance matrix, and prerequisite dependency graph from the same data.

The conceptual progression is:

| Year | Emphasis | Integration result |
|---|---|---|
| 1 | observe, measure, model, and build | measured and calibrated low-voltage device |
| 2 | analyze subsystems and integrate interfaces | custom-PCB data logger |
| 3 | engineer robust connected products | field-tested electronic system |
| 4 | specialize, qualify, and transfer | reproducible capstone release |

Courses are views over the body of knowledge. A self-study reader can follow the
book order; an instructor can create a shorter route by selecting chapter IDs.

## 9. Chapter contract

Every released technical chapter contains:

- a motivating system, observation, or failure;
- explicit outcomes and prerequisite retrieval;
- a physical model and its domain of validity;
- definitions, reference directions, units, and notation;
- derivation and worked examples using estimate → calculate → check → interpret;
- non-ideal behavior and common failure modes;
- at least one measurement or authentic-data encounter;
- comparison of prediction, simulation, and evidence where applicable;
- a design choice with measurable acceptance criteria;
- summary, exercises, references, and downstream links.

The reader-facing chapter should read naturally. Production labels and curriculum
mapping belong in front matter and catalogs, not in repetitive prose boxes.

## 10. Circuit and figure policy

Circuit source is code.

- Use CircuitikZ for instructional schematics.
- Use WaveDrom source for digital timing diagrams.
- Use Mermaid only for architecture, dependency, and process diagrams.
- Use plotting code plus recoverable data for plots.
- Use KiCad source for manufacturing schematics and PCBs.
- Use photography only where physical construction, orientation, or evidence is
  the point.

Do not commit hand-written or generated circuit SVG files. CircuitikZ source lives
under `curriculum/circuits/`. The build may create PDF for print and high-resolution
PNG for HTML inside the ignored build directory; those derivatives are never
authoritative and are never edited.

Every diagram requires a caption, useful alternative text, a text description for
complex relationships, explicit reference designators and values, and a result
that remains understandable without color.

## 11. Laboratory and project policy

Labs answer an engineering question and produce auditable evidence. Each lab
defines prerequisites, hazard level, stop conditions, apparatus, predictions,
test points, measurements, uncertainty, a plausible fault, and an individual
check. Prepared data can teach analysis but cannot certify personal construction,
instrumentation, or debugging.

Projects are integration environments, not decorative demonstrations. They use
requirements, architecture, interfaces, risk control, design review, verification,
configuration control, and handover. The project spine increases in scope from
measurement to a product that another competent person can reproduce and service.

## 12. Instructor-material policy

Slides are not a second textbook. A lecture package should contain only:

- a route through named chapter sections;
- a prediction or retrieval prompt;
- board/diagram cues and one worked example;
- demonstration or data instructions;
- misconceptions and discriminating questions;
- timing, optional cuts, and an exit check.

The chapter remains readable without the slides, and the slides remain brief
enough to support teaching rather than replace it.

## 13. Language and portability

English is the initial authoring language. French is a coequal publication target,
introduced part by part after the English technical content is reviewed. Equations,
values, diagrams, safety limits, datasets, and assessment difficulty form one
shared technical contract. Translation should be natural prose, not duplicated
directory machinery.

Examples may be adapted for climate, supply quality, connectivity, component
availability, maintenance practice, and user need. Context changes engineering
requirements; it never lowers evidence or safety thresholds.

## 14. Definition of done

A chapter is released only when:

- its claims, calculations, code, circuit source, and links have been reviewed;
- examples and exercises cover the stated outcomes;
- circuit and figure sources are reproducible and accessible;
- required physical work has actually been tested;
- safety boundaries and model limitations are explicit;
- the book builds without network access after tools are installed;
- all referenced IDs exist and structural validation passes;
- no restricted assessment, personal data, or partner-confidential content is present.

## 15. Change rule

Prefer improving the shared book over adding a course-specific explanation.
Create a new chapter only when the concept has its own durable question and
dependency boundary. Create a course only when a real audience needs a distinct
route. Create an asset only when prose, equations, tables, or existing code cannot
communicate the relationship clearly.
