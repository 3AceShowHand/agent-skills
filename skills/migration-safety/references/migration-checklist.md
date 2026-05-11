# Migration Checklist

Use only relevant checks.

## State And Source Of Truth

- What state changes?
- Where is the source of truth?
- Who reads and writes it?
- Is it durable, cached, derived, replicated, or externally visible?
- What invariants must hold before, during, and after migration?

## Compatibility

- Can old code read new state?
- Can new code read old state?
- Can old and new versions run together?
- Can rollback or downgrade happen after new state is written?
- Are aliases, defaults, feature flags, version fields, or compatibility readers needed?

## Migration Shape

- Expand: add new fields, tables, files, indexes, formats, or readers without breaking old behavior.
- Migrate: copy, backfill, re-encode, rebuild, verify, or dual-read/dual-write as needed.
- Contract: remove old fields, old paths, old formats, or compatibility code only after the compatibility window closes.

## Failure And Recovery

- What happens if the process crashes mid-step?
- What happens if the result is ambiguous?
- Can the migration resume safely?
- Is the operation idempotent?
- Are partial writes detectable?
- Is cleanup safe to repeat?

## Blast Radius

- Can the migration run by tenant, shard, partition, range, table, file, or batch?
- Is there throttling or rate limiting?
- Can it pause and resume?
- Can it skip, quarantine, or report bad records?
- Can operators stop it safely?

## Tests

- Old state with new code.
- New state with new code.
- Mixed old and new state.
- Partial migration and resume.
- Repeated migration.
- Invalid or corrupted input.
- Rollback or containment path.
