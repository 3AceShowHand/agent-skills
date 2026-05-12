---
name: engineering-review
description: Use as the default entry point for deep code review, design review, or pre-merge review that goes beyond one narrow bug fix. Reviews correctness, simplicity, module boundaries, information hiding, complexity, error handling, tests, compatibility, observability, rollback, and production failure modes with actionable findings. Identify the dominant risk area and route to specialized review Skills when needed. Assess performance hygiene only when the review includes business-code modifications that may affect runtime behavior.
---

# Engineering Review

## Use When

- The user asks for a code review, design review, architecture review, or pre-merge review.
- A change is non-trivial, cross-module, production-facing, or compatibility-sensitive.
- The review should focus on correctness, simplicity, interfaces, tests, and failure modes rather than style only.
- The right first step is a broad engineering pass to identify the dominant risk before deciding whether specialized review depth is needed.

For this Skill, "business code" means application or service logic that can change runtime behavior, data flow, resource usage, or externally visible behavior in production. It excludes documentation-only edits, comments, pure formatting changes, snapshot refreshes with no logic change, and test-only changes unless those tests reveal a runtime performance risk in the changed production path.

## Do Not Use When

- The user only asks for a quick syntax check or formatting fix.
- A specialized review Skill is more appropriate, such as security, performance, migration, or distributed-system safety.
- The task is already clearly scoped to one dominant specialized review area and does not need a broader engineering pass.

## Routing Guide

Use this Skill as the default review entry point, then add or prefer a specialized review Skill when one risk area clearly dominates:

| Dominant risk area | Route to |
| --- | --- |
| Public API behavior, exported interfaces, config names, protocol fields, storage formats, schemas, metrics, or error semantics | `api-compatibility-review` |
| Behavior-preserving refactors, module moves, symbol renames, or implementation replacement with no intended behavior change | `refactor-safety` |
| Persisted data, migrations, backfills, cleanup jobs, schema evolution, irreversible state transitions, or mixed-version state | `migration-safety` |
| Distributed coordination, retries, ownership transfer, replication, ordering, idempotency, recovery, or partial-failure handling | `distributed-systems-reliability` |
| Production signals, dashboards, alerts, operator workflows, logging, metrics, tracing, or diagnosability gaps | `observability-readiness` |
| Measured performance goals, regressions, bottlenecks, CPU, memory, IO, startup time, or benchmark-driven optimization | `performance-engineering` |
| Security-sensitive code paths, auth, authorization, validation, secrets handling, or secure-by-default concerns | `security-best-practices` |

## Trigger Heuristics

Use `engineering-review` first when the prompt sounds like:

- "Review this PR/change/design"
- "What are the main risks here?"
- "Is this safe to merge?"
- "Do a deep review, not style-only feedback"
- "Tell me what needs more specialized review"

Prefer a specialized review Skill first when the prompt already says:

- "Check API compatibility"
- "Review this migration/backfill/schema change"
- "Review this refactor for behavior drift"
- "Review distributed reliability/retries/recovery"
- "Review observability/readiness for production"
- "Analyze performance/regression/benchmark results"
- "Do a security review"

## Workflow

1. Identify scope, user intent, changed files, and affected subsystems.
2. Identify the dominant risk area and decide whether to route or add a specialized review Skill, such as security, API compatibility, migration safety, distributed-systems reliability, observability readiness, refactor safety, or performance engineering.
3. Read entry points before details.
4. Review correctness and invariants first.
5. Review complexity, module depth, information hiding, ownership, and lifecycle.
6. If business code is modified, assess performance hygiene for the changed paths: algorithmic complexity, scale sensitivity, repeated IO or queries, unnecessary allocations or copies, and obvious contention or blocking risks.
7. Review error handling, resource cleanup, concurrency, compatibility, and observability.
8. Review tests for behavior, boundaries, failure paths, and regression coverage.
9. Report actionable findings with severity, evidence, and file/function pointers.
10. Avoid style-only comments unless they affect correctness or maintainability.

## References

- Read `references/review-rubric.md` for severity and finding format.
- Read `references/deep-module-checklist.md` when reviewing design and interfaces.

## Output Rules

- Lead with the highest-risk findings.
- Distinguish blocking issues from suggestions.
- Include why the issue matters and how to fix or investigate it.
- State when a specialized review Skill should be added or preferred for deeper coverage.
- If no major issues are found, say what was reviewed and what remains unverified.
