---
name: migration-safety
description: Use when a change affects persisted data, schemas, storage formats, metadata, checkpoints, indexes, config formats, irreversible operations, backfills, cleanups, repairs, rollout order, rollback safety, or mixed-version state transitions. Guides compatibility, idempotency, validation, monitoring, blast-radius control, and rollback or containment planning.
---

# Migration Safety

## Use When

- A change affects persisted data, schema, storage format, metadata, index, checkpoint, config format, or durable state.
- A task involves backfill, cleanup, repair, compaction, re-encoding, import, export, or irreversible deletion.
- A rollout must support old and new versions, mixed-version deployments, downgrade, rollback, or staged activation.
- A data or state transition must be resumable, idempotent, observable, and bounded.

## Do Not Use When

- The change is stateless and does not affect persisted or externally durable state.
- The task only changes in-memory behavior and has no rollout, rollback, or compatibility impact.
- A more specific project migration guide fully defines the process.

## Workflow

1. Identify the state being migrated and its source of truth.
2. Classify reversibility: reversible, partially reversible, irreversible, or containment-only.
3. Check compatibility: old code reading new state, new code reading old state, mixed-version behavior, downgrade, and rollback.
4. Prefer expand-migrate-contract when possible.
5. Design idempotency, resume behavior, failure handling, and partial-progress recovery.
6. Define validation: dry-run, sample, checksum, count, invariant check, shadow read, or reconciliation as relevant.
7. Define rollout, monitoring, rate limits, blast-radius control, and rollback or containment.
8. Add tests or operational checks for old state, new state, partial migration, repeated migration, and failed migration when feasible.

## References

- Read `references/migration-checklist.md` for migration design and review.
- Read `references/rollout-template.md` when planning rollout, validation, and rollback.
- Read `references/data-validation.md` when defining correctness checks.

## Stop Conditions

- The source of truth, compatibility window, or rollback story is unclear.
- The operation is irreversible and lacks backup, containment, dry-run, or explicit user approval.
- Partial failure can leave state ambiguous, unrecoverable, or silently inconsistent.
- The migration can grow unbounded, lock critical paths, or overload dependencies without throttling or observability.

## Output Rules

- Report state changed, compatibility impact, reversibility, rollout plan, validation, monitoring, and rollback or containment.
- Distinguish tested behavior from assumed behavior.
- Do not call a migration safe without evidence for partial failure and repeated execution.
