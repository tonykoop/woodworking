# Project thumbnails + channel manifest (Issue #6)

## Goal

Define a deterministic packaging format that codex-spark can use to create
at-least-two thumbnails per woodworking project and emit a channel-ready
manifest.

## Thumbnail contract

For each project in the Gen-Burn runbook, the packaging step should produce:

- `thumb_primary` (16:9, hook-first framing)
- `thumb_alt` (square or near-square, process-detail framing)

Both thumbnails should preserve a minimum 80% readable headline region and keep
the project family style in one lane.

## Manifest contract

Emit `woodworking-manifest.json` with stable schema fields:

- `project_slug`
- `version`
- `generated_at_utc`
- `thumbnail_pack`
- `publish_channel`
- `credit_responsibility`
- `status`
- `depends_on`

`credit_responsibility` must include `anthropic_camp` for review/spot-review
traceability.

## Output shape example

```json
{
  "project_slug": "woodturning-bottle-gourd",
  "version": "1",
  "generated_at_utc": "2026-06-18T00:00:00Z",
  "thumbnail_pack": {
    "primary": "images/woodturning-bottle-gourd-thumb-a.jpg",
    "alt": "images/woodturning-bottle-gourd-thumb-b.jpg"
  },
  "publish_channel": ["web", "youtube", "ig"],
  "credit_responsibility": "anthropic_camp",
  "status": "ready",
  "depends_on": ["#4"]
}
```

## Release step

The manifest should be append-only per run so prior thumbnails remain auditable even
if a later pass re-renders a project.
