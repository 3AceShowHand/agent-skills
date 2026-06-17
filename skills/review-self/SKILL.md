---
name: review-self
description: Review the current local branch or worktree against the latest upstream base branch, including committed and dirty changes. Use when the user asks to review my current branch, review my local changes, self-review before merge, compare this branch with upstream/master or upstream/main, or do a design-guided review of the current branch. Builds a correct diff scope, guided reading path, and actionable review findings; pair with engineering-review and specialized review skills when risk areas require deeper coverage.
---

# Review Self

## Overview

Use this skill to review what is currently checked out, not a colleague's remote branch. The skill owns review-scope correctness: refresh the base, include committed and dirty changes, build a reading path, then perform a deep review without modifying code.

For remote branch or PR review, use a branch-review skill instead. For current-branch review, use this skill first and then apply `engineering-review` and any specialized review skills that match the dominant risk area.

## Invocation

Common prompts:

- `$review-self`
- `$review-self --base upstream/main`
- `$review-self --doc /absolute/path/design.md`
- `$review-self --paths pkg/scheduler,server`

Supported options:

- `--base <ref>`: override the base ref. Accepts `upstream/master`, `upstream/main`, `origin/main`, `master`, or `main`.
- `--doc <path>`: read a design document fully before review.
- `--paths <p1,p2>`: prioritize these paths in the reading path and review.
- `--no-fetch`: skip network fetch when offline or when the user explicitly wants local refs only.

## Rules

- Review only. Do not edit code, run formatters, commit, branch, merge, reset, or checkout.
- Refresh the base ref unless `--no-fetch` is requested.
- Include staged and unstaged changes in scope, not only committed changes.
- Do not guess from names. Open unclear definitions and follow call chains until the behavior and invariants are understood.
- If the repository has its own agent instructions, read the relevant files before judging tests, errors, logs, generated code, compatibility, or validation.
- Begin the final review report with exactly: `[skill: review-self] activated`

## Workflow

1. Run repository preflight:
   - `git rev-parse --show-toplevel`
   - `git status --porcelain`
   - `git branch --show-current`
   - `git remote -v`
   - `git log -1 --oneline`
2. Collect review context with `scripts/collect_review_context.sh` when available. It is read-only except for optional `git fetch` of remote-tracking refs.
3. Select the base:
   - Prefer `upstream/master`.
   - Fall back to `upstream/main`.
   - Use `--base` if the user supplied one.
   - If no suitable base can be resolved, ask the user and stop.
4. Compute the committed change set:
   - `git diff --stat BASE...HEAD`
   - `git diff BASE...HEAD`
   - `git log --oneline --decorate BASE..HEAD`
5. Include dirty changes:
   - `git diff --cached --stat`
   - `git diff --cached`
   - `git diff --stat`
   - `git diff`
6. If `--doc` is provided, read it fully and extract goals, non-goals, architecture, data flow, invariants, performance expectations, and test expectations.
7. Build a guided reading path before judging:
   - Identify entry points, exported APIs, controllers, orchestrators, state machines, and hot paths.
   - Follow definitions, callers, and callees for all unclear symbols.
   - For stateful or concurrent code, enumerate states, transitions, ownership, retries, cancellation, cleanup, and partial-failure behavior.
8. Review using these categories:
   - Correctness: edge cases, errors, idempotency, races, ordering, cleanup, state transitions.
   - Simplicity: unnecessary layers, speculative abstraction, avoidable indirection.
   - Boundaries: ownership, package responsibilities, leaked internals, coupling.
   - Comments and readability: public docs, invariant comments, confusing names.
   - Tests: missing regression paths, boundary cases, failure paths, flaky or bloated tests.
   - Performance: hot-path allocations, copies, conversions, blocking, lock contention, repeated IO.
9. Route deeper when needed:
   - API/config/protocol/storage/error semantics: `api-compatibility-review`.
   - Data migrations or durable state: `migration-safety`.
   - Distributed coordination, retries, ownership, recovery: `distributed-systems-reliability`.
   - Production signals and operator diagnosis: `observability-readiness`.
   - Measured latency, throughput, memory, CPU, IO: `performance-engineering`.
   - Behavior-preserving rewrites: `refactor-safety`.

## Output

Produce Markdown with:

1. `[skill: review-self] activated`
2. Base and diff info:
   - base ref and base SHA
   - head SHA
   - commit range
   - whether dirty changes were included
3. What changed: high-level summary.
4. Guided reading path:
   - start locations with files/functions
   - why each location matters
   - the top three places to read if time is short
5. Design alignment, only when `--doc` was provided:
   - matches
   - mismatches
   - missing implementation or tests
   - design-doc issues
6. Review findings grouped by category:
   - `**[Severity: Blocker|High|Med|Low|Nit]** file:line or symbol`
   - issue
   - why it matters
   - concrete fix direction
7. Questions for the author, only when still unresolved after deep reading.
8. Risk assessment and suggested next steps.

If no actionable findings are found, say that clearly and state what remains unverified.

## Script

Use `scripts/collect_review_context.sh` to standardize preflight and diff-scope collection:

```bash
scripts/collect_review_context.sh
scripts/collect_review_context.sh --base upstream/main
scripts/collect_review_context.sh --paths pkg/scheduler,server
scripts/collect_review_context.sh --no-fetch --base HEAD
```
