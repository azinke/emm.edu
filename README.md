# Electronics Systems Engineering curriculum source

This repository is the Markdown-first, bilingual, offline-capable production
source for the Electronics Systems Engineering curriculum. The authoritative
program contract is [`blueprint/COURSE_MASTER_DOCUMENT.md`](blueprint/COURSE_MASTER_DOCUMENT.md).
Workbench checkboxes record implementation evidence, not institutional
accreditation, cohort attainment, or unperformed physical approval.

## Start here

- Authors: [`curriculum/README.md`](curriculum/README.md)
- Resource templates: [`curriculum/templates/README.md`](curriculum/templates/README.md)
- Publishing and QA: [`curriculum/PUBLISHING.md`](curriculum/PUBLISHING.md)
- Lifecycle: [`curriculum/workflows/content-lifecycle.md`](curriculum/workflows/content-lifecycle.md)
- Review gate: [`curriculum/governance/review-checklist.md`](curriculum/governance/review-checklist.md)
- Restricted boundary: [`curriculum/governance/restricted-material.md`](curriculum/governance/restricted-material.md)
- Current foundation milestone: [`blueprint/workbench/02-content-operations-and-repository-foundation.md`](blueprint/workbench/02-content-operations-and-repository-foundation.md)

## Offline verification

From the repository root, with the frozen tools already installed:

```sh
python3 curriculum/scripts/generate_canonical_data.py --check
python3 curriculum/scripts/generate_canonical_backlog.py --check
python3 curriculum/scripts/validate_canonical.py --as-of 2026-07-13
python3 -m unittest discover -s curriculum/tests -p 'test_*.py' -v
python3 -m unittest discover -s curriculum/scripts/tests -v
python3 curriculum/scripts/test_governance.py -v
python3 curriculum/scripts/qa_content.py --offline
python3 curriculum/scripts/audit_public_history.py
```

Generated publications belong under `curriculum/build/` and are never edited as
source. Live assessments, current solutions, protected student records, and
partner-confidential data never belong in this public Git history.
