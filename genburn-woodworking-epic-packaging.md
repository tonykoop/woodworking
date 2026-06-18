# Gen-Burn woodworking epic packaging (Issue #2)

## Scope

Issue #2 tracks the woodworking content wave for the Gen-Burn sprint across five
sub-stories:

- #3 woodworking project prompt/style pack (sonnet)
- #4 per-project hero + step-illustration image sets (agy)
- #5 process b-roll / motion build diagrams (agy)
- #6 project thumbnails + channel manifest (codex-spark)
- #7 batch runner across the project list (codex-spark)

This document captures the codex-spark packaging plan and handoff format so the
lane can publish/ship the woodworking output stack without duplicating state work.

## Wave-0 kickoff summary

For the next run, the sequence is:

1. Sonnet drafts prompt pack for #3.
2. agy executes image/video variants for #4 and #5.
3. Codex-spark performs final asset packaging + catalog manifesting for #6.
4. Codex-spark runs the #7 batch orchestrator once #4/#5 manifest inputs settle.

## Packaging contract (codex-spark)

For #6 and #7 we need a stable manifest bundle with:

- project list source of truth (projects, asset type, priority, expected duration)
- file naming convention + extension policy
- reusable publish path metadata (YouTube, IG, web channel, local archive)
- per-item status (pending / queued / blocked / delivered)

## Suggested channel manifest schema

Each row in the manifest should capture:

- `project_slug`
- `asset_type` (`hero`, `step`, `broll`, `thumbnail`, `batch-run`)
- `model` (`sonnet`, `agy`, `codex-spark`)
- `source_ref` (issue / shot / file source)
- `status` (`ready`, `queued`, `blocked`)
- `last_seen` (UTC timestamp)
- `notes` (constraints or follow-ups)

## Delivery expectations

This epic should be reusable after weekly resets:

- if `#4/#5` are partially complete, codex-spark can still publish a partial
  manifest and leave blocked rows flagged,
- if #6 completes first, #7 should still be able to batch only completed assets,
- if #2 rolls, every new project can append a row without editing previous entries.

## Exit condition

`genburn-woodworking-epic-packaging.md` plus a matching project manifest is
enough to let #6 and #7 close: the sprint then has a single source of truth for
batch execution, publish ordering, and remaining work.
