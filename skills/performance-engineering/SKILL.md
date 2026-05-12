---
name: performance-engineering
description: Use for performance optimization, performance regression analysis, throughput, latency, memory, CPU, allocation, IO, concurrency contention, startup time, or benchmark work. Prefer this Skill directly when performance is the dominant review or implementation risk; otherwise `engineering-review` may triage first and route here. Requires baseline measurement, hot-path identification, one-variable changes, re-measurement, correctness preservation, and clear reporting of tradeoffs and uncertainty.
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
2. Establish a baseline before changing code.
3. Identify the hot path with benchmark, profiler, trace, timing, metrics, or production evidence.
4. State expected data size, access pattern, concurrency, and resource constraints.
5. Change one variable at a time.
6. Re-measure and compare with the baseline.
7. Preserve correctness, compatibility, and debuggability.
8. Report measurement environment, variance, tradeoffs, and remaining uncertainty.

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
