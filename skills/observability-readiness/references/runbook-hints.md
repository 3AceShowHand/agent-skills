# Runbook Hints

Use runbook hints when a signal requires operator judgment or action.

## Minimum Useful Hint

- What happened?
- Why it matters.
- How to confirm impact.
- What dashboard, query, or log to inspect.
- Safe first action.
- Escalation condition.
- Rollback or containment path when relevant.

## Diagnosis Paths

- Health: check service or component status.
- Scope: identify affected tenant, shard, partition, resource, region, or operation.
- Cause: compare local errors, dependency errors, saturation, and rollout timing.
- Progress: inspect queue length, lag, checkpoint, completion count, or oldest item age.
- Recovery: check retry rate, backoff, circuit state, resumed work, and residual backlog.

## Safety Rules

- Do not suggest destructive actions without preconditions.
- Prefer read-only diagnostics before mutating actions.
- Include rollback only when it is known safe.
- State when human escalation is required.
