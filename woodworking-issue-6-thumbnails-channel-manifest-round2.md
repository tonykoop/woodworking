# Project thumbnails + channel manifest (Issue #6, round2)

## Scope

Codex-spark generates deterministic packaging artifacts for woodworking outputs:

- at least two thumbnail variants per project,
- manifest rows for editorial handoff,
- audit-safe append-only records.

## Data contract

Each project row should be emitted as:

- `project_slug`
- `version`
- `generated_at_utc`
- `thumbnail_pack`
- `publish_channel`
- `credit_responsibility`
- `status`
- `depends_on`

### Thumbnail contract

For every woodworking project:

- `thumb_primary`: 16:9, hook-first framing, readable headline region >= 80%
- `thumb_alt`: square/near-square, process-detail framing

If either variant is missing, mark the row as `blocked`.

## Manifest behavior

- Emit `woodworking-manifest.json` in append-only mode.
- Keep prior project entries immutable; create new versions instead of overwriting.
- Ensure `credit_responsibility` includes `anthropic_camp`.
- Accept project families from #2 child stories and skip projects that are not `ready`.

## Output example

```json
{
  "project_slug": "woodturning-spiral-cup",
  "version": "2",
  "generated_at_utc": "2026-06-18T00:00:00Z",
  "thumbnail_pack": {
    "primary": "images/woodturning-spiral-cup-thumb-a.jpg",
    "alt": "images/woodturning-spiral-cup-thumb-b.jpg"
  },
  "publish_channel": ["web", "youtube", "ig"],
  "credit_responsibility": "anthropic_camp",
  "status": "ready",
  "depends_on": ["#4"]
}
```

## Exit conditions

Issue #6 is satisfied when the manifest schema is publish-ready and can be consumed by #7 without hand-written edits.
