# Offline clone, build, and restore drill — 2026-07-13

- **Task:** M02-E4-T04
- **Status:** pass
- **Timestamp:** 2026-07-13 21:54:24 UTC / 23:54:24 Europe/Berlin
- **Operator:** repository automation
- **Observer/approval:** automated regression; release-manager review required
  before this record is reused as institutional backup evidence
- **Next drill due:** 2026-12-31 or earlier after a backup/access/tool change
- **Scope:** committed M02 public foundation plus a separate synthetic restricted
  Git store; no person, answer, partner, credential, or production-private path
- **Temporary locations:** system-generated `/tmp` paths; destroyed after pass
- **Storage classification:** public bundle and restricted synthetic bundle kept
  separate throughout the drill

## Environment and isolation

- Fedora Linux kernel 6.19.14, x86-64
- Git 2.54.0; Python 3.13.13
- Proxies disabled; global/system Git configuration disabled; prompts disabled;
  Git transport limited to the local `file` protocol
- Duration: 10.705 seconds

## Public recovery set

- Commit: `bef01747883c0982b2b68f5ece1f7d77f5a7e528`
- Tree: `156cacfb48ebf920f149d378dbec36022983a112`
- Reachable refs verified: 6
- Source working tree: clean
- Bundle SHA-256:
  `fd42c4828b6701c9ddf424b4b901c2bbba4942739aa44a2b81722104232b7f3d`
- Bundle verification, clean clone, strict `git fsck`, restored HEAD/tree comparison,
  complete ref-set comparison, and restricted-boundary scan: pass
- Offline command in the restored clone:
  `python3 -m unittest discover -s curriculum/scripts/tests -v`: pass (nine
  tests, including EN/FR HTML/PDF/slides, remote-resource rejection, five smoke
  interfaces, real KiCad seeded failure, rendered HTML/PDF leakage, and visual
  regression)

## Restricted synthetic recovery set

- Commit: `be5eeb5a96c8ae76086de11c668eb60fe4ab4ba7`
- Tree: `c9742175fd94b81e54d1a993859f6358ad3e8781`
- Reachable refs verified: 1
- Source working tree: clean
- Bundle SHA-256:
  `4cb7916a7131afe9f4661f788bde0932b4b32cd303a0252dc121f2533016ee41`
- Recovered synthetic canary SHA-256:
  `ce0b1d22e78e89bcede0fe9107849aa574ca7e47d4183461ea577c96a80e6d21`
- Bundle verification, clean clone, strict `git fsck`, HEAD/tree/ref comparison,
  and canary integrity: pass

## Disposition and limits

No drill defect or missing dependency was observed for this scope. Temporary
bundles and restores were destroyed. This proves the committed public foundation
and synthetic separate-store mechanism on the named Linux host. It does not
attest a production private remote, encryption/key custody, institutional
retention, named-account access, Windows recovery, or the declared 4 GiB learner
profiles; those require their own controlled records.
