---
name: refactor-safety
description: Use for behavior-preserving refactors, staged rewrites, module moves, symbol renames, dependency inversion, interface simplification, duplicate-code removal, or implementation replacement where external behavior should remain unchanged. Prefer this Skill directly when refactor safety is the dominant review risk; otherwise `engineering-review` may triage first and route here. Guards against scope creep, behavior drift, compatibility breaks, and unreviewable diffs.
---

# Refactor Safety

## Use When

- The user asks for refactoring, restructuring, code movement, module split or merge, interface simplification, staged rewrite, dependency inversion, or duplicate-code removal.
- A change claims to preserve behavior while changing structure.
- A refactor affects multiple call sites, public symbols, tests, or ownership boundaries.

## Do Not Use When

- The task is a small local bug fix with no structural change.
- The user explicitly asks for a behavior change and not a behavior-preserving refactor.
- A broader design review is needed before deciding whether to refactor.
- The right first step is a broad engineering review because the dominant risk area is still unclear.

## Workflow

1. Define the behavior to preserve and the structure to change.
2. State non-goals: no feature changes, no compatibility changes, no error-semantic changes, no performance claims unless explicitly requested.
3. Inspect callers, tests, docs, configs, generated code, and public surfaces affected by the refactor.
4. Add characterization tests when behavior is important and coverage is weak.
5. Split work into small reversible steps that compile and test between meaningful boundaries.
6. Separate mechanical moves or renames from semantic edits.
7. Preserve public APIs unless the user explicitly requests a breaking change.
8. Remove old paths only after callers are migrated and behavior is verified.

## References

- Read `references/refactor-playbook.md` before planning a multi-step refactor.
- Read `references/characterization-tests.md` when tests are weak or behavior must be locked down.
- Read `references/review-checklist.md` before finalizing a refactor.

## Stop Conditions

- The preserved behavior is unclear.
- The refactor requires broad behavior changes to succeed.
- Public API, config, protocol, storage, metrics, or error semantics may change without explicit user approval.
- The diff mixes refactor, feature work, performance optimization, and cleanup in a way that cannot be reviewed safely.

## Output Rules

- Report what behavior was intended to remain unchanged.
- Report mechanical changes separately from semantic changes.
- Report tests or checks that protect behavior.
- State any behavior, compatibility, or performance aspects not verified.
