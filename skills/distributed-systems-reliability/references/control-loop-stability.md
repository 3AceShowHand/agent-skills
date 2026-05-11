# Control Loop Stability

Distributed systems often fail through unstable feedback loops. Review control behavior when changing retries, timeouts, scheduling, queues, backpressure, rate limits, or autoscaling.

## Control Loop Elements

- Target variable: latency, throughput, error rate, backlog, progress, resource use, or operator toil.
- Sensor: metric, log, trace, counter, health check, queue length, lag, or heartbeat.
- Control action: retry, shed load, pause, resume, rebalance, scale, compact, throttle, or fail over.
- Delay: metric delay, network delay, retry delay, scheduling delay, recovery delay, or operator response delay.
- Saturation: queue limit, worker limit, memory limit, connection limit, disk limit, or dependency quota.

## Stability Risks

- Retry storm.
- Thundering herd.
- Queue or memory growth without bound.
- Oscillation between owners, leaders, routes, or capacity levels.
- Positive feedback where failures create more load.
- Slow feedback that triggers late and overcorrects.
- Noisy alerts that hide real failures.
- Local optimization that worsens global progress.

## Design Rules

- Bound retries and total retry time.
- Use deadlines and cancellation.
- Add backpressure before queues become unbounded.
- Make side effects idempotent or fenced before retrying.
- Prefer jittered exponential backoff for shared dependencies.
- Use circuit breakers or load shedding when dependencies are unhealthy.
- Ensure queue length, lag, retry count, and dropped work are observable.
- Prefer monotonic progress and explicit state transitions.
- Avoid adding a new feedback loop without understanding delay and saturation.

## Validation

- Test duplicate, reorder, timeout, restart, and partial failure cases when feasible.
- Stress test queue growth and retry behavior when scale matters.
- Verify metrics and logs show degraded and recovering states.
- Check rollback behavior when new state may already be written.
