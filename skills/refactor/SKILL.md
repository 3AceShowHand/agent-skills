---
name: refactor
description: Use for behavior-preserving refactors, staged rewrites, module moves, symbol renames, dependency inversion, interface simplification, duplicate-code removal, or implementation replacement where external behavior should remain unchanged. Prefer this Skill directly when refactoring is the main task; otherwise `code-review` may triage first and route here. Guards against scope creep, behavior drift, compatibility breaks, and unreviewable diffs.
---

# Refactor

## Use When

- The user asks for refactoring, restructuring, code movement, module split or merge, interface simplification, staged rewrite, dependency inversion, or duplicate-code removal.
- A change claims to preserve behavior while changing structure.
- A refactor affects multiple call sites, public symbols, tests, or ownership boundaries.
- The user asks to simplify correct but hard-to-follow code by reducing understanding cost.

## Do Not Use When

- The task is a small local bug fix with no structural change.
- The user explicitly asks for a behavior change and not a behavior-preserving refactor.
- A broader design review is needed before deciding whether to refactor.
- The right first step is a broad engineering review because the dominant risk area is still unclear.

## Workflow

1. Define the behavior to preserve and the structure to change.
2. State non-goals: no feature changes, no compatibility changes, no error-semantic changes, no performance claims unless explicitly requested.
3. When simplifying for readability, optimize for understanding rather than line count. Remove unnecessary nesting, indirection, state, duplication, abstraction, and comments that restate the code. Preserve behavior and project conventions. Do not compress function bodies or control-flow blocks onto one line; keep idiomatic clause headers such as `if err := f(); err != nil` with a multi-line body. Reject shorter code that obscures semantics.
4. Inspect callers, tests, docs, configs, generated code, and public surfaces affected by the refactor.
5. Add characterization tests when behavior is important and coverage is weak.
6. Split work into small reversible steps and verify at meaningful boundaries. For a local rename or standalone test deletion, inspect bindings, remaining references, imports, and the diff statically. Finish once that evidence resolves the affected behavior; execute compilation or tests only for a specific uncovered failure mode or a mandatory repository check.
7. Separate mechanical moves or renames from semantic edits.
8. Do not infer a public API from language visibility alone. Treat a symbol as a compatibility contract only when actual external, documented, generated, persisted, or cross-version consumers depend on it.
9. Preserve public APIs unless the user explicitly requests a breaking change. A branch-local symbol with no independent consumer may be renamed after its repository callers are migrated.
10. Remove old paths only after callers are migrated and behavior is verified.

## References

- Read `references/refactor-playbook.md` before planning a multi-step refactor, including readability simplification.
- Read `references/characterization-tests.md` when tests are weak or behavior must be locked down.
- Read `references/review-checklist.md` before finalizing a refactor.

## Stop Conditions

- The preserved behavior is unclear.
- The refactor requires broad behavior changes to succeed.
- A verified public API, config, protocol, storage, metrics, or error semantics may change without explicit user approval.
- The diff mixes refactor, feature work, performance optimization, and cleanup in a way that cannot be reviewed safely.

## Output Rules

- Report what behavior was intended to remain unchanged.
- Report mechanical changes separately from semantic changes.
- Report tests or checks that protect behavior.
- State any behavior, compatibility, or performance aspects not verified.
