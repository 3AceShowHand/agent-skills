---
name: engineering-review
description: Use for deep code review, design review, or pre-merge review that goes beyond one narrow bug fix. Reviews correctness, simplicity, module boundaries, information hiding, complexity, error handling, tests, performance, compatibility, observability, rollback, and production failure modes with actionable findings.
---

# Engineering Review

## Use When

- The user asks for a code review, design review, architecture review, or pre-merge review.
- A change is non-trivial, cross-module, production-facing, or compatibility-sensitive.
- The review should focus on correctness, simplicity, interfaces, tests, and failure modes rather than style only.

## Do Not Use When

- The user only asks for a quick syntax check or formatting fix.
- A specialized review Skill is more appropriate, such as security, performance, migration, or distributed-system safety.

## Workflow

1. Identify scope, user intent, changed files, and affected subsystems.
2. Read entry points before details.
3. Review correctness and invariants first.
4. Review complexity, module depth, information hiding, ownership, and lifecycle.
5. Review error handling, resource cleanup, concurrency, compatibility, and observability.
6. Review tests for behavior, boundaries, failure paths, and regression coverage.
7. Report actionable findings with severity, evidence, and file/function pointers.
8. Avoid style-only comments unless they affect correctness or maintainability.

## References

- Read `references/review-rubric.md` for severity and finding format.
- Read `references/deep-module-checklist.md` when reviewing design and interfaces.

## Output Rules

- Lead with the highest-risk findings.
- Distinguish blocking issues from suggestions.
- Include why the issue matters and how to fix or investigate it.
- If no major issues are found, say what was reviewed and what remains unverified.
