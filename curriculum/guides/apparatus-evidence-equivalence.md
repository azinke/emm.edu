# Equivalent evidence across minimal, standard, and advanced apparatus paths

Equipment paths may change access and resolution, but not the outcome, cognitive
level, personal agency, safety, or evidence threshold. Equivalence is a reasoned
claim supported by physical pilots, not a label attached to three shopping lists.

## Equivalence test

For each outcome, specify the invariant evidence:

- phenomenon/capability the learner must personally produce or observe;
- decision, model, instrument/configuration choice, and independence required;
- measurand, usable range/resolution/bandwidth/timing and uncertainty needed;
- safe operating envelope, stop conditions, and function/calibration checks;
- raw evidence and provenance retained;
- anomaly/debug and acceptance decision;
- rubric rows, mastery cut, time burden, accessibility, and novel transfer.

A path is equivalent only if pilots show that these invariants remain achievable.
Greater instrument precision does not justify a higher grade, and lower-cost
apparatus does not justify a lower uncertainty/safety/reasoning standard.

## Example A — RC cutoff and loading

| Path | Apparatus/action | Evidence produced | Equivalence limit |
|---|---|---|---|
| Minimal | Low-cost MCU-based stimulus/acquisition whose rate/input impedance are independently characterized; DMM for static checks. Learner selects sample rate, measures loaded response, and exports raw data. | Predicted and measured gain at sufficient points around cutoff; source/load correction; timing/amplitude uncertainty; seeded probe/input-loading diagnosis; design acceptance. | Not equivalent if sample rate/bandwidth cannot resolve the required response or if prepared data replaces personal connection/instrument choice. Redesign values/frequency while preserving the same model and uncertainty reasoning. |
| Standard | Bench generator and oscilloscope with probe/function checks. Learner chooses amplitude/frequency/trigger/coupling and records recoverable measurements. | Same gain/model/loading/debug/decision evidence with scope configuration. | Screenshot alone is insufficient; raw/settings and uncertainty are required. |
| Advanced | FRA/network analyzer or automated scope sweep, after learner predicts range and validates fixture/reference plane. | Same evidence plus dense sweep/repeatability; optional enrichment on parasitics. | Automation cannot remove learner model, setup validation, anomaly diagnosis, or acceptance decision. Extra bandwidth is enrichment, not a higher core cut. |

## Example B — digital timing and fault localization

| Path | Apparatus/action | Evidence produced | Equivalence limit |
|---|---|---|---|
| Minimal | MCU timestamp/capture plus characterized low-cost logic analyzer. Learner configures acquisition, finds an intermittent protocol/timing fault, and cross-checks one interval. | Timing prediction, trace with configuration, hypothesis table, discriminating test, root cause/correction, acceptance over repeated transactions. | Cannot certify analog signal-integrity or voltage-threshold behavior the apparatus cannot observe; that construct needs another safe path. |
| Standard | Bench oscilloscope/logic analyzer. Learner chooses probes, thresholds, timebase and trigger. | Same timing/debug/repetition evidence; can include threshold/rise-time only if bandwidth/probe uncertainty suffices. | Default “Auto” screenshots without settings or hypothesis work fail. |
| Advanced | Mixed-signal/high-bandwidth instrument with protocol decode. Learner independently validates decoder against raw timing/electrical evidence. | Same core evidence plus optional jitter/eye analysis. | Tool decoding is not the learner's diagnosis; opaque automated pass/fail is insufficient. |

## Example C — inaccessible phenomenon versus practical competence

Prepared, richly documented RF/power/high-energy data can let all paths model,
analyze uncertainty, find an anomaly, and make a design decision safely. This is
equivalent for a stated **data-analysis** outcome. It is not equivalent evidence for
personally connecting a probe, constructing a circuit, making a safe energy-state
decision, or debugging physical hardware. The manifest and rubric must name which
construct is and is not certified and provide supervised physical evidence later
where the program outcome requires it.

## Approval record

| Outcome/construct | Path configuration and profile ID | Physical pilot/version | Expected/observed range and uncertainty | Timing/access findings | Reviewer decision/expiry trigger |
|---|---|---|---|---|---|
| [ID] | [details] | [evidence] | [evidence] | [evidence] | [equivalent/not; trigger] |

Re-pilot after apparatus/substitute/firmware/software/procedure/environment changes,
out-of-range observations, incidents, access barriers, or supported-profile changes.
