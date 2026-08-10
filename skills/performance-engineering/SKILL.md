---
name: performance-engineering
description: Use for performance optimization, performance regression analysis, throughput, latency, memory, CPU, allocation, IO, concurrency contention, startup time, or benchmark work. Prefer this Skill directly when performance is the dominant review or implementation risk; otherwise `code-review` may triage first and route here. Requires baseline measurement, hot-path identification, one-variable changes, re-measurement, correctness preservation, and clear reporting of tradeoffs and uncertainty.
---

# Performance Engineering

## Use When

- The user asks to improve or explain performance.
- A change targets latency, throughput, CPU, memory, allocation, IO, contention, startup time, or benchmark results.
- A regression, timeout, bottleneck, resource spike, or scalability problem is suspected.

## Do Not Use When

- The task is a normal feature or bug fix and performance is not part of the request or risk.
- The change is cosmetic, documentation-only, or unrelated to runtime behavior.
- The right first step is a broad engineering review because the dominant risk area is still unclear.

## Workflow

1. Define the target metric and success threshold.
2. Establish comparable baselines before changing code; verify the executed versions, configuration, workload, environment, and provenance of evidence.
3. Start regression attribution by trying to falsify the leading hypothesis: check whether the suspected feature is present, enabled, and materially different in the successful baseline. A candidate shared unchanged by both baselines cannot explain their outcome difference without additional interaction evidence.
4. Separate the failure mechanism from its trigger and introducing change. Name a change as causal only when evidence connects the baseline difference to the measured failure path; otherwise keep it as a hypothesis.
5. Identify the hot path with benchmark, profiler, trace, timing, metrics, or production evidence.
6. State expected data size, access pattern, concurrency, and resource constraints.
7. Change one variable at a time.
8. Re-measure and compare with the baseline.
9. Preserve correctness, compatibility, and debuggability.
10. Report measurement environment, variance, tradeoffs, and remaining uncertainty.

## References

- Read `references/measurement-checklist.md` before measuring or comparing results.
- Read `references/report-template.md` when reporting performance work.

## Stop Conditions

- No baseline exists and no safe measurement path is available.
- The proposed optimization weakens correctness, compatibility, or observability without explicit user approval.
- The result is within noise and does not justify added complexity.

## Output Rules

- Do not claim performance improved without measured evidence.
- Do not mix unrelated refactors with performance changes.
- Prefer the simplest implementation that meets the measured target.
