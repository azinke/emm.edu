# Backup, restore, and offline-clone runbook

**Control ID:** GOV-BCP-001
**Owners:** release manager (public); restricted-store custodian/data steward
  (restricted)
**Cadence:** lightweight restore each release; complete offline drill each term;
incident-triggered drill after backup, access, or storage changes

## Backup set

The public recovery set contains an all-refs Git bundle, release manifest,
environment locks, external-asset inventory/archival copies where permission
allows, and SHA-256 checksums. The restricted recovery set is created and stored
separately, inherits the highest classification, and never enters the public
build or backup location. Build output is reproducible product, not the only
source backup.

Production backups use at least two independently administered storage copies,
including one offline or immutable copy, with documented encryption, key
custody, region, retention, monitoring, and restoration authority. A successful
backup job is not recovery evidence.

## Automated drill

```sh
python3 curriculum/scripts/backup_restore_drill.py \
  --public-repo . \
  --private-store /approved/path/to/restricted-store \
  --offline-command python3 curriculum/scripts/qa_content.py --offline
```

The drill refuses a private store inside the public checkout; creates separate
Git bundles/checksums; disables global/system Git configuration, prompts,
network protocols and proxy use; verifies the bundle contains every source ref;
clones into clean temporary paths; runs `git fsck`; compares HEAD and tracked
tree; confirms the public restore contains no restricted payload; and runs the
explicit offline QA command when requested. Temporary material is destroyed on
success unless a controlled diagnostic retention path is approved.

Never use production personal/assessment payload to prove the mechanism. Use a
synthetic canary record with no real answer or identity and verify its hash in
the restricted restore without printing its contents.

## Complete drill record

Record date/time/time zone, operators/observers, source commits/refs, tool
versions and supported hardware/OS, backup locations/classes, checksums, network
isolation, restore duration, integrity comparisons, offline build, leak scan,
missing dependencies, defects/owners/dates, approvals, and next drill. A redacted
summary may be public; storage paths, credentials, identities, and restricted
filenames remain controlled.

On failure, preserve logs without payload, label the backup unverified, open an
owned defect, and retain the last known-good set. Do not overwrite the only
backup. Report a restricted failure privately to the data/security owners.
