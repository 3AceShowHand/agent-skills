# Measurement Checklist

Use only the parts relevant to the task.

## Target

- Metric: latency, throughput, CPU, memory, allocation, IO, contention, startup time, or tail latency.
- Threshold: target value, regression budget, or acceptable percentage change.
- Scope: function, module, endpoint, command, workload, or system path.

## Baseline

- Record commit, branch, environment, hardware, OS, runtime, flags, config, and dataset.
- Verify that recorded versions and execution metadata come from the run being analyzed; do not fill provenance gaps from unrelated runs or assumptions.
- Run enough samples to see variance.
- Keep raw output when useful.
- If baseline is unstable, investigate noise before optimizing.

## Regression Attribution

- List the material variables shared by and different between the successful and failing baselines.
- Test the leading hypothesis against the successful baseline before pursuing supporting evidence: verify whether the suspected feature is present, enabled, and implemented differently.
- Separate the resource-retention or hot-path mechanism from the workload, backlog, configuration, or code change that triggered it.
- Do not attribute the outcome difference to a candidate shared by both baselines unless measured interaction evidence explains why its effect differs.
- Distinguish the change that introduced a latent defect from the change that exposed it in the observed regression.
- Treat chronology and correlation as hypotheses until a one-variable comparison, revert, bisection, profiler, trace, or equivalent causal evidence supports them.

## Evidence Source

- Benchmark.
- Profiler.
- Trace.
- Timing logs.
- Metrics.
- Production incident data.
- Reproduction workload.

## Hot Path

- Identify where time, allocation, blocking, or IO is spent.
- Check algorithmic complexity and data size.
- Check locking, queueing, batching, retries, and backpressure.
- Check serialization, copies, allocations, syscalls, and network calls.

## Change Discipline

- Change one variable at a time.
- Keep a simple path or fallback when complexity increases.
- Preserve correctness tests.
- Re-measure under the same conditions.
- Broaden measurement only after narrow evidence is clear.

## Result Quality

- Compare against baseline.
- Report variance and confidence.
- Explain tradeoffs.
- State what remains unmeasured.
