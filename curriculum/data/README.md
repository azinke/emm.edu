# Canonical curriculum data

These records instantiate Epic E1 from `blueprint/COURSE_MASTER_DOCUMENT.md`.
Files ending in `.yml` use JSON syntax, a valid YAML 1.2 subset, so the required
validation path works offline with the Python standard library.
The sole authoritative controlled termbase is `curriculum/i18n/termbase.yml`,
matching the repository architecture in master §14.1; it is generated and
drift-checked with the data records.

Authority is intentionally separated:

- `outcomes.yml`, `prerequisite-graph.yml`, the course/unit manifests, platform
  capability contracts, safety levels, and V0–V4 definitions are universal
  program records;
- `deployment-profiles/*.yml` contains dated national/institutional overlays;
- `context-briefs.yml` contains project/user contexts and must reference a dated
  deployment profile and provenance evidence;
- `claims.yml` and `local-value-ladder.yml` hold review dates and contribution /
  provenance evidence. A location or origin claim is not inferred from a
  deployment name.

The initial Benin profile is deliberately `mapping-in-progress` and not release
eligible. Empty authoritative-source, supplier, quote, facility, and capability
fields are owned evidence gaps—not claims that the local mapping is complete.

Regenerate and validate from the repository root:

```sh
python3 curriculum/scripts/generate_canonical_data.py --check
python3 curriculum/scripts/generate_canonical_backlog.py --check
python3 curriculum/scripts/validate_canonical.py --as-of 2026-07-13
python3 -m unittest discover -s curriculum/tests -p 'test_*.py' -v
```

Run the data generator without `--check` only after changing its source model or
the master document. Generated files must never be edited independently.
