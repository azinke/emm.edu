# Good and bad examples: requirement-changing context and inquiry/design

These contrasts are review anchors. “Bad” means the artifact would fail content
review; revise it rather than copying it into learner materials.

## Decorative context versus requirement-changing context

### Example 1 — solar study-lamp monitor

**Bad (decorative):** “A student in Cotonou needs a solar lamp. Build the following
3.3 V divider with two 10 kΩ resistors and report the midpoint.” The location and
user can be removed without changing any calculation, architecture, test, cost,
safety, or lifecycle choice. It asserts a need without a context source and turns
the learner into a recipe follower.

**Good (requirement-changing):** “Context brief `CTX-BJ-POWER-004@2026-06` reports
that the approved lamp family has a battery terminal range of 3.0–4.2 V, must not
be opened, and is checked with a 10 MΩ-input DMM. Design a non-invasive measurement
path whose loading changes terminal voltage by less than 0.5%, whose ADC input
never exceeds 3.3 V including stated resistor tolerance, and whose connection can
be serviced with the declared tools. Predict the loaded voltage, measure the safe
external points, compare uncertainty, and select the divider/protection option.”
The sourced voltage range, no-opening boundary, instrument impedance, tolerance,
service route, and acceptance tests change the model and design.

**Review evidence:** context ID/version; source/assumption distinction; loading and
worst-case calculation; safety boundary; raw measurement; uncertainty; requirements
trace; portable alternate profile with the same evidence threshold.

### Example 2 — environmental telemetry

**Bad (decorative):** “Farmers need technology. Program this sensor to upload a
temperature every minute.” It stereotypes a broad group, supplies no observed
need, and fixes the implementation before requirements.

**Good (requirement-changing):** “An approved, locally reviewed context brief for
the named storage site records 8-hour network outages, a 48-hour maximum visit
interval, 40 °C indoor design temperature, dust ingress during loading, a service
phone interface in the users' selected language, and replacement limited to two
documented connector families. Compare local buffering/energy budgets for 1- and
10-minute sampling, choose an enclosure/connector strategy, inject a lost-link
fault, and verify no sample loss across the stated outage plus successful service
handoff.” The context changes energy/storage architecture, enclosure, connector,
fault test, user interface, and acceptance.

**Review evidence:** authorization and bounded site facts; storage/power calculation;
fault log; environmental assumptions; user-tested service route; privacy decision;
honest limits (not a claim about all farms or regions).

## Recipe laboratory versus inquiry/design laboratory

### Example 3 — RC low-pass filter

**Bad (recipe):**

1. Insert a 10 kΩ resistor and 100 nF capacitor exactly as shown.
2. Set the generator to the listed frequencies.
3. Copy oscilloscope amplitudes into the table.
4. Plot the provided formula and state that theory agrees.

The outcome is revealed, the topology and values are fixed, no prediction or
instrument decision is owned, anomalies have no route, and “agreement” has no
tolerance or uncertainty criterion.

**Good (inquiry/design):** “A sampled sensor aliases a measured interference band.
Before building, predict the attenuation and phase at three frequencies and bound
the effect of source/load impedance and component tolerance. Choose safe scope
settings and test points. Measure raw waveforms using the declared apparatus path;
compare model, simulation, and measurement with uncertainty. One station contains
a plausible capacitor-value or probe-loading fault: rank hypotheses and choose a
discriminating test. Then select E-series values that meet passband loss ≤0.5 dB
and interference attenuation ≥15 dB under worst-case tolerances, and verify the
chosen design.”

**What makes it inquiry/design:** prediction precedes reveal; learner owns settings
and diagnosis; evidence can challenge the model; the fault is safe and purposeful;
multiple designs can pass; acceptance is measurable; nonidealities and limitations
matter.

### Example 4 — microcontroller input

**Bad (recipe):** Copy supplied code, connect the named board, press Run, screenshot
“1,” and conclude the input is reliable.

**Good (inquiry/design):** Learners inspect the primary datasheet for input
thresholds and absolute/recommended limits, predict a floating-input trace, choose
pull resistance from leakage/noise/power constraints, capture a bounce/noise event,
diagnose a seeded missing-reference fault, implement and test a debounce strategy,
and defend the choice against latency and energy acceptance tests on an approved
substitute board. A provided-data path may support analysis but cannot certify the
personal wiring and instrumentation outcome.

## Fast reviewer test

Reject or return for revision when:

- deleting the context nouns changes no engineering decision;
- learners know the expected “correct” trace before predicting;
- every action/value is prescribed and there is no defensible choice;
- a screenshot or “worked once” substitutes for raw/configured evidence;
- unexpected data are discarded rather than investigated;
- an advanced instrument makes the task easier but changes the outcome threshold;
- a local or origin claim exceeds the context/contribution evidence;
- enjoyment or spectacle is the only engagement evidence.
