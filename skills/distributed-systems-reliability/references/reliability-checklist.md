# Reliability Checklist

Use only relevant questions.

## State And Ownership

- Who owns each piece of state or work?
- Can ownership overlap during failover, retry, rebalance, or mixed-version deployment?
- Is ownership fenced by epoch, lease, version, token, or durable compare-and-swap?
- Is cleanup performed by the layer that owns the resource?

## Ordering And Progress

- What order must be preserved?
- What can be reordered safely?
- What marker represents durable progress?
- Can progress move backward?
- What happens after restart from the last durable marker?

## Idempotency And Replay

- Which operations may be retried?
- Which operations have external side effects?
- Are duplicate inputs, duplicate requests, and duplicate completions safe?
- Is deduplication durable and bounded?
- Is replay from checkpoint, log, snapshot, or persisted state safe?

## Consistency And Durability

- What consistency model is promised?
- When is data considered committed, visible, or durable?
- Can readers observe partial updates?
- Can old and new versions coexist safely?
- Is rollback or downgrade safe after new state is written?

## Recovery And Rollout

- What happens on crash at each state transition?
- What happens if the operation result is ambiguous?
- Can recovery be repeated safely?
- Is rollout staged, reversible, and observable?
- Is there a containment plan for bad state?

## Operability

- Can operators see health, progress, lag, backlog, ownership, retries, errors, and recovery state?
- Are alerts actionable and not noisy?
- Are state transitions logged or measured at the right level?
- Is there enough context to diagnose delayed failure?
