# Batch runner across woodworking project list (Issue #7, round2)

## Scope

Codex-spark orchestrates the sonnet → agy → package path across the woodworking
project portfolio in resumable batches.

## Project inputs

Process list from Epic #2:

- segmented woodturning
- beehives
- coffee tables
- picture frames
- recovered shop tools

Each project reports one of `ready`, `blocked`, or `done`.

## Runner state

- Keep `last_processed_project` cursor.
- Persist per-project checkpoints for:
  - prompt pack prepared,
  - image sets generated,
  - manifest rows emitted.
- Skip `done` entries on re-run.

## Credit/loop control

- Initialize `credit_budget` each run.
- Before each external call, validate remaining budget can cover estimated cost.
- If under threshold, exit with `deferred=true` and a partial manifest.
- Resume from last cursor when credits restore.

## Outputs

Emit combined manifest sections:

- `completed`
- `skipped`
- `deferred`
- `errors`

This manifest drives channel publishing and supports idempotent reruns.

## Exit conditions

Issue #7 is complete when the project list runs as resumable batches with skip +
resume safety and a merged manifest for all states.
