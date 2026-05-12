---
name: distributed-systems-reliability
description: Use when a change affects distributed coordination, replication, partitioning, ownership transfer, ordering, idempotency, progress, failure recovery, retries, timeouts, backpressure, consistency guarantees, or operability under partial failure. Prefer this Skill directly when distributed-system reliability is the dominant review risk; otherwise `engineering-review` may triage first and route here. Trigger on distributed-system properties, not on project names or product categories.
---

# Distributed Systems Reliability

## Use When

- Multiple independent processes, nodes, workers, replicas, shards, partitions, or regions coordinate state or work.
- A change affects ownership, membership, leader election, leases, epochs, versions, quorum, replication, placement, scheduling, or rebalancing.
- A change affects ordering, deduplication, idempotency, replay, checkpoint, offset, watermark, commit point, or monotonic progress.
- A change affects retries, timeouts, backoff, backpressure, rate limits, circuit breakers, degradation, recovery, or failover.
- A change may affect consistency, availability, durability, data loss, duplicate side effects, split-brain, stalled progress, or operator diagnosis.

## Do Not Use When

- The task only touches local single-process logic with no distributed state, coordination, recovery, or progress semantics.
- A project belongs to a distributed domain but the specific change does not touch distributed-system properties.
- A more specific Skill fully covers the task, such as API compatibility, performance, migration, security, or observability.
- The right first step is a broad engineering review because the dominant risk area is still unclear.

## Workflow

1. State the distributed invariant: what must never be violated.
2. State the progress requirement: what must eventually happen.
3. Identify the failure model: process crash, network delay, partition, retry, duplicate, reordering, slow dependency, disk failure, clock behavior, restart, and mixed-version deployment as relevant.
4. Identify ownership and lifecycle boundaries for state, work, resources, and side effects.
5. Check consistency, ordering, idempotency, replay, and recovery semantics.
6. Check control loops: retry, timeout, backoff, backpressure, rate limit, circuit breaker, queue growth, and feedback delay.
7. Check observability for health, progress, lag, backlog, ownership, retries, errors, recovery, and degraded behavior.
8. Require validation and rollback or containment for risky production behavior changes.

## References

- Read `references/invariants-and-failure-model.md` when defining correctness and failure assumptions.
- Read `references/reliability-checklist.md` when reviewing a design or implementation.
- Read `references/control-loop-stability.md` when retries, backpressure, queues, scheduling, or feedback loops are involved.

## Stop Conditions

- The safety invariant or progress requirement is unclear.
- The change can violate data correctness, ownership exclusivity, durability, or consistency under partial failure.
- Recovery, retry, rollback, or mixed-version behavior is unknown for a risky change.
- The implementation adds unbounded growth, unbounded retries, hidden state transitions, or unobservable failure modes.

## Output Rules

- Distinguish safety, liveness, availability, and operability concerns.
- Report the invariant, failure model, evidence inspected, validation plan, and remaining uncertainty.
- Do not claim reliability improvement without tests, model reasoning, fault-injection evidence, metrics, or operational evidence.
