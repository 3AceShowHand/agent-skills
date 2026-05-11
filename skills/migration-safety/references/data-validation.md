# Data Validation

## Validation Types

- Count comparison.
- Checksum or hash comparison.
- Referential integrity check.
- Invariant check.
- Sampled record comparison.
- Full reconciliation.
- Shadow read.
- Replay from source.
- Error budget or mismatch threshold.

## Validation Timing

- Before migration: baseline shape, counts, checksums, invalid records.
- During migration: progress, error rate, partial batch correctness, resource use.
- After migration: final reconciliation, old-path/new-path equivalence, rollback readiness.

## Validation Rules

- Validate source and destination independently when possible.
- Make validation repeatable.
- Store enough evidence for audit and debugging.
- Report mismatches with object identity and reason.
- Avoid high-cardinality or sensitive data in logs and metrics.
- Do not delete old state until validation and compatibility windows are complete.

## Failure Handling

- Define acceptable mismatch threshold.
- Define quarantine or skip behavior.
- Define retry limit.
- Define manual repair path.
- Stop or pause when invariants are violated.
