# Signal Checklist

## Logs

- Log important lifecycle events and state transitions.
- Log abnormal conditions with reason, impact, object identity, and next action.
- Avoid per-item logs on hot paths unless sampled or rate-limited.
- Avoid secrets, credentials, raw payloads, and large objects.
- Keep message text stable enough for humans and tooling if consumed.

## Metrics

- Success and failure count.
- Latency and duration distribution.
- Retry, timeout, throttle, drop, and circuit-breaker counts.
- Queue length, lag, backlog age, and in-flight work.
- Progress, completion, skipped, failed, and quarantined work.
- Dependency health and error categories.
- Resource use: CPU, memory, disk, network, file descriptors, connections.

## Traces

- Cross-component request path.
- External dependency calls.
- Long-running operations.
- Retries and fallback branches.
- Critical state transitions.

## Dashboards

- Health summary.
- Error and latency trends.
- Backlog, lag, and progress.
- Dependency health.
- Saturation and resource pressure.
- Rollout or migration progress.

## Blind Spots

- Can operators detect degraded mode?
- Can operators identify stuck progress?
- Can operators distinguish dependency failure from local failure?
- Can operators find affected objects or users?
- Can operators see recovery state?
