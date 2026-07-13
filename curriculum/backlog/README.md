# Generated child backlog

`canonical-child-backlog.yml` is generated from every resource-applicability
decision in the canonical course and unit manifests. Each resource child owns:

- paired English and French edition children;
- technical, safety, language, accessibility, license, build, apparatus, and
  release-approval facets;
- minimal, standard, and advanced apparatus paths declared by its manifest;
- second-instructor rehearsal, EN/FR learner-usability, and small-cohort pilots;
- defect disposition, evidence links, and named approval roles.

Regenerate with `python3 curriculum/scripts/generate_canonical_backlog.py` and
check drift with the same command plus `--check`. The validator requires exactly
one backlog child for every canonical manifest/resource pair.
