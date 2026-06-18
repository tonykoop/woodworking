# Batch runner across woodworking project list (Issue #7)

## Objective

Create a resumable codex-spark batch flow that executes the sonnet→agy→package
pipeline across the woodworking project list and respects weekly credit caps.

## Input list

Run over configured projects:

- segmented woodturning
- beehives
- coffee table family
- picture frames
- recovered woodshop tools

Each project must declare readiness as one of:

- `ready`
- `blocked`
- `done`

Only `ready` items enter the runner in each cycle.

## Resume behavior

- Keep persistent cursor `last_processed_project`.
- Skip entries with `done`.
- Persist per-project checkpoint:
  - prompt pack prepared
  - image sets generated
  - manifest lines written
- If external quota failure occurs, abort safely and persist next retry index.

## Credit policy

- Track `credit_budget` at run start.
- Before each external call, ensure budget remains after estimated spend.
- If low credit, stop with `deferred=true` and emit a partial manifest.

## Output

Runner emits one combined manifest with sections:

- `completed`
- `skipped`
- `deferred`
- `errors`

## Acceptance checks

- full project list supports resumable execution,
- already-finished items are skipped,
- weekly cap prevents overrun,
- combined manifest is emitted even on partial completion.
