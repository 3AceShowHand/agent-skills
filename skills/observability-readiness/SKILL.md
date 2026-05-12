---
name: observability-readiness
description: Use when a change affects production behavior, failure modes, recovery, performance, operator workflows, external dependencies, background work, retries, queues, migrations, or user-visible reliability. Prefer this Skill directly when diagnosability and operator readiness are the dominant review risks; otherwise `engineering-review` may triage first and route here. Checks logs, metrics, traces, alerts, dashboards, runbook signals, cardinality, privacy, and diagnostic coverage.
---

# Observability Readiness

## Use When

- A change affects production behavior, user-visible reliability, recovery, performance, or operator workflows.
- A task introduces new failure modes, degraded modes, retries, queues, background work, migrations, external dependency calls, or long-running operations.
- Operators need to diagnose health, progress, latency, errors, backlog, resource use, ownership, or recovery.

## Do Not Use When

- The change is documentation-only, cosmetic, or purely local with no operational impact.
- Existing project observability rules already define the needed signals and the task only follows them mechanically.
- The right first step is a broad engineering review because the dominant risk area is still unclear.

## Workflow

1. Identify the states operators must distinguish: healthy, degraded, failed, retrying, throttled, paused, backlogged, recovering, or complete.
2. Identify key objects and correlation IDs: request, job, tenant, shard, resource, operation, task, owner, or dependency.
3. Define metrics for rate, errors, latency, duration, retries, drops, throttling, queue length, lag, progress, and resource use as relevant.
4. Define logs for state transitions, abnormal conditions, recovery actions, and high-value summaries.
5. Define traces or spans for cross-component paths and slow dependency calls when relevant.
6. Check alerts and dashboards for actionable signals, thresholds, noise, and missing degraded states.
7. Check cardinality, cost, privacy, sampling, and retention.
8. Add runbook hints when operators need a diagnosis or recovery path.

## References

- Read `references/signal-checklist.md` when choosing logs, metrics, traces, dashboards, and alerts.
- Read `references/alert-quality.md` when creating or reviewing alerts.
- Read `references/runbook-hints.md` when operator action is required.

## Stop Conditions

- A production-impacting change cannot be diagnosed after deployment.
- A failure mode is hidden or only visible through user reports.
- A new alert is noisy, unactionable, or based on high-cardinality labels.
- Logs or metrics may expose secrets, credentials, private data, or large payloads.

## Output Rules

- Report what operators can see before and after the change.
- Distinguish logs, metrics, traces, alerts, dashboards, and runbook changes.
- State remaining blind spots and why they are acceptable or need follow-up.
