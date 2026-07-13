# Personal physical-access entitlement and scheduling test

**Semantic ID:** M03-E4-ACCESS-01
**Version:** 0.1.0-draft
**Policy state:** proposed universal minimum; local capacity not yet tested

## Entitlement

Each learner receives one reserved **75-minute active-learner block** for each of
the five constructs in `apparatus-paths.md`: DC networks, RC response, sensor
calibration, digital timing, and MCU debugging. A sixth 75-minute block is held
for remediation or reassessment. The entitlement is 450 active-learner minutes
per learner, not a guarantee of a pass and not permission to work beyond the
learner's current authorization.

An active-learner place has the complete declared path, room safety
infrastructure, an instructor able to stop work, and enough physical reach and
control for the learner to make the assessed decisions. Pair work may share
apparatus, but only the learner currently constructing, connecting, configuring,
measuring, or debugging consumes and earns the active-learner block. Roles must
rotate and individual evidence must be attributable.

The 75-minute block includes check-in, function check, work, de-energization,
check-out, and evidence export. It excludes pre-lab study. A documented
accommodation may add time, alternative controls, tactile/high-contrast labeling,
or manipulation assistance under the learner's direction; it does not remove the
learner's instrument, safety, interpretation, or debugging decisions.

## Missed or incomplete evidence

1. A cancellation, equipment failure, authorized absence, access barrier, or
   safety stop does not consume the learner's entitlement.
2. Staff provide a replacement slot before the dependent gate or course release.
3. Prepared data may keep the analysis lesson on schedule, but the record remains
   `physical-evidence-outstanding`.
4. The held remediation block is used for a novel value, setup, or fault. If the
   attempt was stopped by infrastructure rather than learner performance, it is
   rebooked and the held remediation block remains available.
5. If no qualified physical slot is available, the affected core outcome is not
   marked complete. The course owner escalates capacity or release scope.

## Capacity test before timetable approval

For each construct, deployment, accessibility route, and apparatus path, record:

- `N`: enrolled learners needing this path;
- `B`: active-learner places per scheduled block, after removing quarantined or
  unqualified equipment;
- `S`: scheduled 75-minute blocks before the dependency deadline;
- `R`: reserve fraction for failure, absence, and reassessment (minimum 0.20);
- staffing, room, power-backup, supervision, authorization, setup/reset, and
  accessible-route constraints.

The path passes the paper capacity test only when:

`B × S × (1 - R) >= N`

and the same named staff/room/equipment capacity has not been double-booked. Test
the held remediation entitlement across the whole five-station rotation as a
separate pool of at least `N` usable places after reserve. Round required blocks
upward. A spreadsheet result does not validate actual turnaround; the pilot must
record setup/reset and completion times.

### Illustrative calculation — not a deployment result

For `N = 24`, `B = 6`, and `R = 0.20`, each construct needs at least
`ceil(24 / (6 × 0.80)) = 5` scheduled blocks. The shared remediation pool also
needs at least five blocks. This example demonstrates the formula only; it does
not claim that any room has six qualified places or can sustain the timing.

## Scheduling register fields

| Field | Required content |
|---|---|
| Cohort/profile | ID, version, dates, enrollment freeze |
| Construct/path | Semantic ID and minimal/standard/advanced configuration ID |
| Capacity | `N`, `B`, `S`, `R`, calculation, deadline |
| Dependencies | Named room, staff, power, accessibility and equipment constraints |
| Learner allocation | Pseudonymous learner reference, initial slot, access provisions |
| Outcome state | scheduled / completed / physical-evidence-outstanding / rebooked |
| Disruption | equipment/access/safety/absence reason; no unnecessary health detail |
| Closure | replacement slot and attributable evidence reference |
| Approval | timetable owner and laboratory lead; safety approval remains separate |

Learner identities, disability/health details, and assessment evidence remain in
the controlled institutional system, not public Git.

SPDX-License-Identifier: CC-BY-SA-4.0
