# Measurement Checklist

Use only the parts relevant to the task.

## Target

- Metric: latency, throughput, CPU, memory, allocation, IO, contention, startup time, or tail latency.
- Threshold: target value, regression budget, or acceptable percentage change.
- Scope: function, module, endpoint, command, workload, or system path.

## Baseline

- Record commit, branch, environment, hardware, OS, runtime, flags, config, and dataset.
- Run enough samples to see variance.
- Keep raw output when useful.
- If baseline is unstable, investigate noise before optimizing.

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
