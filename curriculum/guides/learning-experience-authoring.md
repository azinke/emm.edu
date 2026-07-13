# Authoring hands-on, contextual, misconception, fault, and evidence-led learning

Use this guide when drafting chapters, sessions, explorations, laboratories,
projects, problem sets, demonstrations, or practical assessments. The goal is
engineering agency: learners predict, reason, act, confront evidence, change a
decision, and qualify the resulting claim.

## Start with the seven-field safeguard

Write specific content before exposition. Review rejects blanks, “TBD,” generic
boilerplate, or a context that does not affect engineering work.

| Field | Authoring question | Acceptable evidence |
|---|---|---|
| `real_life_question` | What credible user/system question creates a reason to learn this concept? | Approved context brief or bounded professional scenario; changed requirement is named. |
| `prediction` | What direction, magnitude, behavior, or best next action can learners commit to before the reveal? | Individual response plus reason/assumptions; confidence when useful. |
| `student_action` | What does each learner personally calculate, construct, instrument, program, configure, diagnose, decide, or defend? | Observable action; manipulation assistance can preserve learner direction when dexterity is not the construct. |
| `physical_or_data_evidence` | What raw and interpreted evidence can another person audit? | Setup/configuration, raw data, units, uncertainty, plots/logs, individual defense. |
| `fault_or_anomaly` | What credible mismatch prevents recipe-following? | Seeded or natural fault with safe insertion, evidence trail, discriminating tests, recovery. |
| `design_decision` | Which choice changes because of evidence? | Trade study against requirements; before/after rationale and residual limitation. |
| `acceptance_test` | What measured condition determines pass, fail, or qualified result? | Procedure, configuration, range/tolerance/uncertainty, decision rule, and evidence rung. |

## Author the complete learning cycle

### Discover

Present a device, waveform, failure, observation, or user need. Ask for a prediction
before teaching the formula. Capture reasoning through an inclusive route (private
note, card, accessible poll, pair explanation, sketch). Do not grade the predicted
value as prior knowledge; use it to expose the starting model.

### Understand

Connect phenomenon, physical/architectural representation, words, mathematics,
and limits. Derive rather than merely announce; show units, assumptions, limiting
cases, tolerances, loading, bandwidth, noise, temperature, parasitics, uncertainty,
and failure modes where relevant. Work estimate → calculation → sanity check →
interpretation, then fade support.

### Experiment

Learners safely operate on physical hardware or authentic data, record raw evidence,
and preserve configuration/provenance. Define minimal/standard/advanced capability
paths and argue outcome equivalence. Prepared data can support inaccessible
analysis; it cannot certify personal physical measurement, construction, or debug.

### Analyze

Compare prediction, calculation, simulation, and measurement. Ask what evidence
would distinguish competing explanations. Quantify residuals and uncertainty;
retain negative results and investigate anomalies. A mismatch is instructional
evidence, not a result to erase.

### Design

Require a choice under conflicting constraints, a requirements trace, an acceptance
test, and a qualified claim. Learners own architecture/interface decisions and
state what remains unverified. An extension that only changes a component value by
instruction is practice, not design.

## Turn a context brief into engineering requirements

1. Cite an approved context ID/version and distinguish observed fact, stakeholder
   statement, assumption, and author-created scenario.
2. Extract measurable constraints: supply range/outages, temperature/humidity/dust,
   connectivity, language/access, maintenance interval/tools/skills, sourcing and
   landed cost, privacy/safety, service life, disposal, and acceptance conditions.
3. Trace each relevant constraint to at least one calculation, architecture,
   component/interface choice, verification condition, cost, safety control, or
   service/lifecycle decision.
4. Provide a portable alternative or mark the unit deployment-specific. The
   context may change access and apparatus, never lower outcome, reasoning, safety,
   or evidence thresholds.
5. Avoid extraction and stereotype: name provenance/consent/authority, uncertainty,
   within-context diversity, benefit/harms, and who accepts the requirement.

Reject a context when deleting the place/person names leaves every engineering
quantity and decision unchanged. See the paired examples in
[`context-and-inquiry-examples.md`](context-and-inquiry-examples.md).

## Design misconceptions deliberately

Create a misconception record with:

```text
tag -> prerequisite/model -> eliciting prompt -> predicted observable response
    -> discriminating evidence/question -> feedback activity -> transfer recheck
```

- Select high-leverage misconceptions from prior learner evidence, literature,
  instructor experience, or prerequisite logic; label conjecture as conjecture.
- Elicit before telling. A plausible distractor, waveform sketch, explanation,
  diagnosis choice, or conflicting example is more informative than “Do you
  understand?”
- Distinguish concept error from arithmetic, language ambiguity, apparatus fault,
  prior-knowledge gap, and unsafe process.
- Give feedback that makes the learner reconcile model and evidence. Then recheck
  with a new representation or parameter; repeating the same item tests recall.
- Record whether the misconception changed during pilots. If EN/FR patterns differ,
  investigate wording and access before inferring competence differences.

## Seed faults for diagnosis, not surprise

Choose faults that are plausible, bounded, recoverable, and aligned to the outcome:
wrong value, open reference, reversed low-energy polarity, probe loading, aliasing,
saturation, swapped pins, bad constraint, brownout, race, packet corruption, or
connector intermittency. Never seed a fault that bypasses a safety control or can
damage non-sacrificial equipment.

For each fault define:

- fault ID, outcome/misconception, exact insertion/configuration and custodian;
- starting symptoms and evidence deliberately available/withheld;
- at least two plausible hypotheses and a best discriminating test;
- instrumentation/accessibility paths and expected observation ranges;
- safe-stop, reset, verification, contamination prevention, and maximum time;
- scoring for observe → hypothesize → test → update, even before repair;
- root-cause/corrective/preventive evidence and a transfer variant;
- controlled answer security for live assessments.

Do not grade rapid part swapping as expert debugging. Reward efficient evidence
selection, hypothesis updates, honest uncertainty, and verified prevention.

## Specify an evidence ladder per claim

Use the common ladder:

```text
opinion → estimate → calculation → simulation → bench measurement
        → repeated/uncertainty-aware test → independent reproduction
        → field evidence → qualified claim with stated limits
```

The ladder is not always linear: a primary-source safety limit can constrain a test,
and field anecdotes cannot replace a controlled calculation. For every major claim
name the minimum rung, why it fits the consequence, exact conditions/population,
and what higher claim remains forbidden. Require triangulation for consequential
claims: model/source plus empirical evidence and independent review as applicable.

## Author review questions

- Will every learner—not merely the team—make, interpret, and defend a relevant
  decision or practical action?
- Does evidence change a decision, or is the activity decorative motion?
- Are physical and simulation/data roles honest and outcome-aligned?
- Does the context change a requirement and remain evidence-based/non-stereotyped?
- Does the fault test diagnosis without introducing uncontrolled hazard?
- Are EN/FR technical contract, cognitive demand, and accessible/offline routes
  equivalent?
- Does each claim stop at the evidence rung actually reached?
