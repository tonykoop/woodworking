# Gen-Burn woodworking wave: epic packaging for #2 (round2)

## Epic summary

Issue #2 coordinates a codex-spark handoff layer for woodworking content generation:

- #3: prompt/style pack (sonnet)
- #4: per-project hero + step images (agy)
- #5: process video diagrams (agy)
- #6: thumbnails + channel manifest (codex-spark)
- #7: batch runner orchestration (codex-spark)

## Deliverable contract for codex-spark

Codex-spark should treat #2 as pipeline governance, not creative generation.
Its outputs are the reproducible index and run control artifacts:

- per-project manifest row set,
- thumbnail inventory,
- resumable batch cursor,
- run-completion summary.

## Workflow cadence

1. pull dependency status from #4/#5 trackers,
2. generate manifest entries with `ready/blocked/done`,
3. publish package-ready manifest with deterministic path naming,
4. rerun #7 when new projects or blocked items resolve.

## Credit and safety guardrails

The run must respect weekly credit ceilings and avoid duplicate dispatch of a
completed project while preserving a stable manifest history.

## Exit condition for #2

Epic can close once manifest scaffolding exists and every child story can be
attached to a project row for deterministic scheduling.
