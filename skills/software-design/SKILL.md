---
name: software-design
description: Use when designing or materially changing module boundaries, public or cross-module interfaces, shared abstractions, state ownership, lifecycle, concurrency or resource models, or when the user asks for a software design before implementation. Supports feature development, structural refactoring, and design-focused review. Do not use for simple local edits, codebase navigation alone, ordinary bug diagnosis, or reviews without a material design question.
---

# Software Design

## Core Contract

- Design from required external behavior, current constraints, and explicit non-goals.
- Understand the existing system before proposing a new structure. Use `codebase-navigation` when the required call paths, ownership, or impact are not already clear.
- Prefer the smallest coherent design that satisfies current requirements and reduces knowledge required by callers.
- Make ownership, interfaces, invariants, state transitions, failure handling, and verification explicit where they affect the decision.
- Return an implementable design or evidence-backed design findings to the calling workflow; do not take over feature delivery or review reporting.

## When Design Depth Is Material

Use this Skill when at least one decision materially affects:

- Module boundaries or which component owns a behavior.
- A public, cross-module, cross-process, or long-lived interface.
- A shared abstraction that will couple multiple callers.
- State ownership, lifecycle, cancellation, cleanup, or resource bounds.
- Concurrency, ordering, retries, idempotency, or partial failure.
- Data flow, control flow, persistence, or upgrade behavior across a boundary.
- Multiple viable approaches with different correctness, complexity, compatibility, or operational tradeoffs.

For a straightforward implementation that follows an established local pattern, choose the simplest fitting design in the parent workflow without loading this Skill.

## Workflow

1. Define the requested external behavior, success criteria, constraints, non-goals, and assumptions that can change the design.
2. Read repository instructions and establish the current architecture, entry points, authoritative definitions, callers, state owners, tests, and relevant conventions.
3. Model the important concepts, invariants, data and control flow, state transitions, lifecycle, and failure boundaries.
4. Assign each decision and behavior to an owning module. Identify what callers truly need to know and what the owner can hide.
5. Design the smallest useful interfaces. Prefer deep modules whose simple interfaces hide meaningful implementation complexity.
6. Define error semantics, cleanup, cancellation, concurrency, resource bounds, and recovery only to the depth required by realistic failures.
7. Compare alternatives only when their tradeoffs are material. Reject speculative extensibility, configuration, fallback paths, and abstractions.
8. Route compatibility, migration, performance, distributed reliability, observability, or security depth to the applicable specialist Skill when it can change the design.
9. Define behavior-based verification, important boundaries and failure cases, and any rollout or containment needed to validate the design safely.
10. Check the proposed design with `references/design-checklist.md`, then return the decision, rationale, affected boundaries, implementation consequences, and unresolved risks.

## Design Principles

- Keep interfaces small and simple while the owning module absorbs necessary complexity.
- Keep design decisions in the module that owns them. Pull complexity downward when one lower-level implementation can remove that knowledge from every caller.
- Hide a decision only when the interface removes knowledge from callers. Avoid pass-through wrappers and shallow modules.
- Apply DRY to duplicated knowledge: couple code that must change for the same reason, not code that merely looks similar.
- Require abstractions to reduce total cognitive load. Prefer direct code over indirection that adds another place to look without hiding a decision.
- Keep related state and behavior close. Use precise names, honest code shapes, shallow control flow, and explicit ownership to reduce working memory.
- Make similar interfaces behave similarly in semantics, side effects, error handling, and performance characteristics.
- Treat change amplification, excessive cognitive load, hidden coupling, unclear ownership, uncontrolled state growth, and delayed failure as design defects.
- Use test friction as design feedback: excessive setup or assertions against internals often indicate leaked decisions or a shallow interface.
- Implement current requirements and knowledge. Do not design extension points for guessed future uses.

## Parent Workflow Integration

### Feature Development

- Resolve material design decisions before the implementation stages are finalized.
- Return the chosen boundaries, interfaces, ownership, failure model, verification consequences, and rejected alternatives that affected the choice.
- Hand control back to `feature-development` for implementation, testing, progress reporting, and delivery.

### Code Review

- Preserve the review target, base, exclusions, and read-only boundary established by `code-review`.
- Evaluate the implemented or proposed design against the same principles used during implementation.
- Return concrete design findings with evidence, impact, and a correction direction to `code-review`; let it own severity and the final report.

### Refactoring

- Preserve the behavior contract established by `refactor`.
- Use design changes only to clarify ownership, interfaces, and knowledge boundaries required by the requested refactor.
- Hand control back to `refactor` for characterization, staged transformation, and equivalence verification.

## Boundaries

- Do not turn every feature or review into a design exercise.
- Do not implement code, modify the reviewed worktree, or expand the parent task unless the user requested implementation.
- Do not replace repository-specific architecture decisions, compatibility promises, build commands, or done criteria.
- Do not duplicate specialist checklists; consume their conclusions when their risks affect the design.
- Do not claim certainty where the current code, requirements, scale, or failure model remains unknown.

## Report

- Design decision or design findings.
- Required behavior, constraints, and non-goals that shaped the result.
- Module boundaries, interfaces, ownership, state, and failure model affected.
- Material alternative and rejection reason, only when it influenced the decision.
- Implementation and verification consequences.
- Remaining uncertainty or specialist analysis still required.

## Reference

Read `references/design-checklist.md` before finalizing a material design or design finding.
