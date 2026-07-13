# Offline clone and restore drill — 2026-07-13

- **Task:** M02-E4-T04
- **Status:** pass
- **Scope:** public Git bundle plus separate synthetic restricted Git store
- **Operator:** repository automation
- **Network:** no dependency; bundle creation, verification, clone, and fsck used
  local paths only
- **Tool:** Git 2.54.0; Python 3.13.13
- **Public source:** commit `9cd071c13336c3855a8e0310be8303b9451537cb`
- **Public tree:** `2b347b9b819e4b72d4286e17c0ff0f927c88a1e2`
- **Public bundle SHA-256:**
  `c432349abe71b46cc518ca03aa72c41a776836eecce144500f653a0cb323c702`
- **Synthetic restricted tree:**
  `c9742175fd94b81e54d1a993859f6358ad3e8781`
- **Synthetic restricted bundle SHA-256:**
  `4cb7916a7131afe9f4661f788bde0932b4b32cd303a0252dc121f2533016ee41`
- **Synthetic canary SHA-256:**
  `ce0b1d22e78e89bcede0fe9107849aa574ca7e47d4183461ea577c96a80e6d21`
- **Restore duration:** 0.160 seconds
- **Temporary recovery copies:** destroyed after verification

## Evidence

`initialize_restricted_store.py --drill` created a separate, mode-restricted Git
store containing only a synthetic canary. `backup_restore_drill.py` created and
verified separate bundles, cloned both without a remote, ran strict object checks,
compared source/restored HEAD and tree IDs, verified the public boundary, and
hashed the recovered restricted canary without displaying its contents. The
governance regression suite repeated the drill in a separate temporary path and
also confirmed that initialization inside the public checkout is rejected.

The integrated post-implementation drill is rerun against the final committed
M02 source. Publishing/offline build and lowest-supported-machine results are
recorded by the M02-E3 automation evidence, not inferred from this Git-only drill.
