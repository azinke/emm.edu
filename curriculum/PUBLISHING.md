# Bilingual publication and QA

The authoritative inputs are Markdown/Quarto-family sources under each course's
`en/` and `fr/` trees plus shared technical contracts. Generated files always go
to `curriculum/build/` and are never edited.

## Local and offline build

From the repository root:

```sh
python3 curriculum/scripts/verify_toolchain.py
python3 curriculum/scripts/qa_content.py --offline
python3 curriculum/scripts/build_publications.py --engine auto --offline
python3 curriculum/scripts/run_smoke_hooks.py
python3 curriculum/scripts/check_outputs.py
```

`auto` uses Quarto when it is installed. The locked Pandoc/XeLaTeX route is an
offline recovery path and produces separate EN/FR HTML, PDF, and HTML slide
directories. A release requires the declared Quarto route as well; the fallback
does not excuse a missing release dependency. Builds set `SOURCE_DATE_EPOCH`, do
not fetch remote resources, and embed web assets. Use
`build_publications.py --language en|fr --format html|pdf|slides` to narrow a run.

Prepare the environment once from institution-provided offline media. Verify the
bundle's SHA-256 manifest before installation. Do not run package managers during
class or CI builds. `toolchain.yml` is the machine-readable freeze and includes
the lowest-supported profiles. Each deploying institution must replace
`requires_physical_benchmark` with dated measurements from the actual refurbished
or minimum-spec machines; a desktop CI run is not that evidence.

## Source metadata expected by QA

Each paired teaching source uses YAML front matter containing at least
`artifact_id`, `pair_id`, `lang`, `pair_revision`, and a shared
`technical_contract`. The contract contains outcomes, equations, values, safety
limits, expected ranges, rubric total, and figure IDs as applicable. Figures use
localized captions and a distinct `fig-alt`; complex figures link a localized
long description. External URLs must be registered according to
`external-link-policy.md`.

The validator compares technical contracts structurally rather than comparing
localized prose. It also checks outcome IDs, rubric arithmetic, glossary IDs and
avoided terms, internal links, external-link metadata/checksums, figure captions
and alternative text, stale pair revisions, and public-tree restricted markers.
Seeded fixtures prove that parity, links, accessibility, rubric, and restricted
leakage failures are detected.

## Rendering, print, and device evidence

`check_outputs.py` enforces size budgets, PDF readability/page bounds, embedded
HTML resources, bilingual font markers, MathML/math presence, figure captions,
and schematic/static fallbacks. `visual_regression.py` compares rasterized golden
pages or slides with ImageMagick and fails above the policy thresholds. Golden
images are accepted only after EN and FR review and are stored per viewport.

The configured viewports are phone, lowest-supported student laptop, and
projector. Automated checks complement, but do not replace, a keyboard/screen
reader review, paper print inspection, projector inspection, or the physical
lowest-hardware benchmark. Record OS, CPU, RAM, free storage, cold/warm build
times, output size, failures, and reviewer in `build/reports/benchmark-*.yml`.

## KiCad release gate

`kicad_release.py` runs actual KiCad ERC/DRC with a writable isolated XDG home,
captures JSON and tool versions, rejects undocumented native exclusions, checks
waiver shape/approval/expiry, and verifies the release-file contract. Run its
seeded failing fixture with:

```sh
python3 curriculum/scripts/kicad_release.py \
  curriculum/scripts/tests/fixtures/kicad-seeded-failure --expect fail
```

An expected failure proves the checker; it is never release evidence. A real
project passes only with clean checks or exact, approved, revision-bound,
unexpired waivers and the required fabrication/source artifacts.
