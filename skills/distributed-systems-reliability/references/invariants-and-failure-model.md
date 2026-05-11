# Invariants And Failure Model

## Safety Invariants

Safety means bad states do not happen, even under concurrency, partial failure, retries, reordering, delay, restart, and recovery.

Common invariants:

- No acknowledged data is lost.
- No non-idempotent side effect is committed twice.
- No two owners hold the same exclusive resource at the same time.
- Epochs, versions, offsets, checkpoints, or watermarks do not move backward unless explicitly designed.
- Uncommitted, unreplicated, or unconfirmed state is not reported as durable success.
- Recovery does not create split-brain, duplicate ownership, or inconsistent metadata.
- Authorization, tenancy, and isolation boundaries remain intact across failover and retry.

## Liveness Requirements

Liveness means desired progress eventually happens under stated assumptions.

Examples:

- Work is eventually scheduled.
- A leader or owner is eventually elected.
- Checkpoints, watermarks, or progress markers eventually advance.
- Backlog eventually drains when input rate falls below capacity.
- Recovery eventually completes after a bounded fault.

## Failure Model

State which failures are in scope:

- Process crash or restart.
- Network delay, loss, duplication, partition, or reordering.
- Slow or unavailable dependency.
- Disk or persistence failure.
- Clock skew or timer delay.
- Duplicate requests or messages.
- Partial write, partial commit, or ambiguous result.
- Mixed-version deployment.
- Operator interruption, rollback, or configuration error.

## Assumption Rules

- Do not assume reliable networks.
- Do not assume exactly-once execution unless enforced by protocol and durable state.
- Do not assume local memory survives restart.
- Do not assume clocks are synchronized unless the protocol requires and enforces it.
- Do not assume retries are harmless unless side effects are idempotent or deduplicated.
- Do not assume progress markers are correct unless update ordering and durability are defined.
