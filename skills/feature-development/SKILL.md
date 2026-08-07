---
name: feature-development
description: Use when implementing a non-trivial feature or enhancement that requires coordinated design, code changes, and verification across multiple steps or modules. Owns goals, non-goals, assumptions, scope, simple design, staged implementation, dependency assessment, risk-based high-quality tests, and delivery. Do not use for small local edits, docs-only changes, bug diagnosis, behavior-preserving refactors, code review, or tasks dominated by compatibility, migration, performance, distributed reliability, or observability.
---

# Feature Development

## Core Contract

- Define the requested external behavior and success criteria before choosing an implementation.
- Give the complete known plan before starting. Report progress against that plan instead of turning ordinary implementation steps into new approval points.
- Prefer the smallest design that expresses current requirements clearly and leaves a reviewable diff. Use `software-design` when module, interface, ownership, lifecycle, concurrency, or shared-abstraction decisions are material.
- Route a dominant specialist risk to the applicable Skill instead of copying its checklist here.
- Finish with necessary high-quality tests and an honest account of what remains unverified.

## Workflow

1. Read relevant repository instructions, entry points, callers, tests, and nearby conventions.
2. State the objective, externally visible behavior, non-goals, material assumptions, affected subsystem, and success criteria.
3. Identify the main correctness, compatibility, data, security, operational, and delivery risks. Keep only risks that can change the design or verification.
4. Resolve the design before planning implementation. Use `software-design` when the change materially affects module boundaries, public or cross-module interfaces, shared abstractions, state ownership, lifecycle, concurrency, resources, or competing tradeoffs; otherwise follow the established local pattern and choose the simplest fitting design directly.
5. Present all known implementation stages, verification methods, and rollout or containment needs before editing.
6. Implement in coherent vertical slices. Keep related behavior together and verify meaningful boundaries as work progresses.
7. Preserve error context and handle realistic failures from external input, IO, networks, time, and concurrency at the layer that owns them.
8. Remove only code, files, configuration, or tests made obsolete by the change.
9. Add and run the necessary high-quality tests. Start with the narrowest relevant check and broaden according to actual risk.
10. Review the final diff for scope, correctness, simplicity, dependencies, tests, and specialist risks. Report results and remaining uncertainty.

## Implementation Quality

- Implement current requirements and knowledge. Do not add speculative configuration, extension points, abstractions, or fallback paths.
- Reduce working memory with precise names, locality, shallow control flow, small scopes, and related code placed together.
- Keep names and code shapes honest: similar forms should have similar semantics, side effects, and performance characteristics.
- Add comments for contracts, invariants, constraints, ownership, concurrency, and non-obvious rejected alternatives, not narration.
- Implement the boundaries, ownership, interfaces, failure model, and verification consequences established by `software-design` when it was used. Do not dilute those decisions with convenience wrappers or unrelated cleanup.

## Dependencies

Before adding or updating a dependency, check:

- Maintenance status and project fit.
- License and security risk.
- Build, binary, startup, runtime, and operational impact.
- Whether the standard library or an existing dependency already solves the need clearly.

Proceed when the risk is acceptable. Pause only when a material risk cannot be resolved within the requested scope.

## Testing

- Add or update tests for changed behavior, important boundaries, and realistic failure paths.
- Use existing project test patterns and commands from repository instructions.
- Do not introduce a new test framework solely for one change unless the user requests it or the existing project decision supports it.
- Do not require a ritualized test order. Require evidence strong enough for the change's risk.

## Specialist Routing

Prefer the specialist Skill when it owns the main problem:

- Bugs, regressions, or incidents: `diagnose-and-fix-bugs`.
- Material module, interface, ownership, lifecycle, or shared-abstraction design: `software-design`.
- Behavior-preserving structural changes: `refactor`.
- Application upgrade behavior: `compatibility-check`.
- Persisted state or irreversible transitions: `migration-safety`.
- Measured performance work: `performance-engineering`.
- Distributed coordination, progress, or recovery: `distributed-systems-reliability`.
- Production diagnosis and operator readiness: `observability-readiness`.
- Deep review without implementation: `code-review`.

Use this Skill to coordinate the remaining feature work when a specialist risk is only one part of a broader implementation.

## Boundaries

- Do not auto-commit, push, publish, deploy, or mutate unrelated external state.
- Do not replace project-specific build, test, lint, code generation, release, or done criteria.
- Do not make small local changes pay the cost of a full feature workflow.
- Do not claim a check passed unless it ran.

## Report

- Outcome and externally visible behavior.
- Key design choice and rejected alternative only when it affected the result.
- Files or subsystems changed.
- Tests and checks run with results.
- Remaining risk, uncertainty, rollout need, or next action.
