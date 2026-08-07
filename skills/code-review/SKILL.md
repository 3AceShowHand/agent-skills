---
name: code-review
description: Use for deep code review, self-review of the current local branch or worktree, review of a remote pull request or branch, design review, or pre-merge assessment. Builds the correct review scope, including committed changes plus staged, unstaged, and untracked work for local reviews; creates a guided reading path; reviews correctness, simplicity, boundaries, tests, and failure modes; routes dominant specialist risks; and reports evidence-backed findings without modifying the reviewed code.
---

# Code Review

## Core Contract

- Review only. Do not edit code, run formatters, commit, merge, reset, checkout, or rewrite the user's worktree.
- Establish the exact review target and comparison base before judging the change.
- Read repository instructions before assessing project commands, generated files, tests, compatibility, or done criteria.
- Lead with evidence-backed findings ordered by severity. Do not manufacture low-value comments when no actionable issue exists.
- Route a dominant specialist risk to the applicable Skill instead of duplicating its checklist.

## Review Modes

### Local Branch Or Worktree

Review all work that may enter the next change:

- Commits unique to the current branch relative to the selected upstream merge base.
- Staged changes in the Git index.
- Unstaged tracked changes in the worktree.
- Untracked files, opened and reviewed directly because they do not appear in normal Git diffs.

Use `scripts/collect_review_context.sh` to collect the base, SHAs, status, commit range, changed-file summaries, and dirty scopes. Refresh the remote base unless the user requests `--no-fetch`. If refresh fails, do not silently review against a stale remote-tracking ref.

Supported script options:

- `--base <ref>`: select the comparison base.
- `--paths <p1,p2>`: prioritize paths without excluding other in-scope changes.
- `--no-fetch`: use existing local refs when the user accepts that limitation.

### Remote Pull Request Or Branch

- Resolve the requested head and its intended base without checking it out over the user's worktree.
- Read pull request or branch metadata when available, then compute the merge-base diff and commit range.
- Include the files, commits, tests, and design material in the requested remote scope.
- State when authentication, missing refs, or stale local data prevents a complete review.

### Design Review

- Extract goals, non-goals, external behavior, data flow, interfaces, state, ownership, invariants, failure model, compatibility, verification, rollout, and containment.
- Review claims against available code and project constraints when the task includes an implementation context.
- Report design findings by section or concept when no meaningful `file:line` exists.

## Workflow

1. Identify the review mode, user intent, target, base, paths, design documents, and explicit exclusions.
2. Collect the exact review scope. For local work, include committed, staged, unstaged, and untracked content.
3. Summarize what changed and build a guided reading path from entry points, authoritative definitions, state owners, public boundaries, and tests. Use `codebase-navigation` when structural tracing is substantial.
4. Review correctness and invariants before maintainability. Follow unclear definitions and call paths instead of guessing from names.
5. Review scope, simplicity, and dependency changes. Use `software-design` when module boundaries, interfaces, information hiding, ownership, lifecycle, concurrency, resources, or competing design tradeoffs are material.
6. Review tests for changed behavior, boundaries, failure paths, regression coverage, and signal quality. Flag excessive tests when they increase maintenance without protecting behavior.
7. Check performance hygiene for changed runtime paths: algorithmic complexity, expected scale, repeated IO, avoidable allocation or copying, blocking, and contention. Require measurement only when making a performance claim.
8. Route specialist risks when deeper analysis is needed.
9. Verify each candidate finding against the actual code or design, remove speculative or style-only comments, and order the remaining findings by severity.
10. Report findings first, followed by scope, evidence, unresolved questions, and unverified areas.

## Code Quality Review

- Reject behavior or cleanup outside the requested scope.
- Reject speculative configuration, extension points, fallback paths, and abstractions that do not serve a current requirement.
- Reject a new dependency when the standard library or an existing dependency already solves the need clearly, or when its maintenance, license, security, build, or runtime cost is not justified.
- Prefer precise names, locality, shallow control flow, small scopes, and related code placed together.
- Check that similar names and code shapes have similar semantics, side effects, error behavior, and performance characteristics.
- Require comments to explain contracts, invariants, constraints, ownership, concurrency, or non-obvious rejected alternatives rather than narrating code.
- Require tests to protect changed behavior, important boundaries, and realistic failures; flag tests that only mirror implementation details or add maintenance cost without useful signal.

## Specialist Routing

- Application upgrades and consumed contracts: `compatibility-check`.
- Material module, interface, ownership, lifecycle, concurrency, resource, or shared-abstraction design: `software-design`.
- Persisted data, schemas, backfills, or irreversible state: `migration-safety`.
- Measured latency, throughput, CPU, memory, IO, or contention: `performance-engineering`.
- Coordination, ordering, retries, progress, and recovery: `distributed-systems-reliability`.
- Production signals and operator diagnosis: `observability-readiness`.
- Behavior-preserving structural changes: `refactor`.

Use `code-review` to preserve the common scope and final findings. Load specialist depth only when the risk warrants it.

## References

- Read `references/review-rubric.md` for severity and finding structure.
- Use `software-design` when reviewing interfaces, module design, or complex ownership boundaries; return its design findings through this Skill's severity and reporting structure.

## Report

1. Actionable findings ordered by severity. For each finding, include location or design area, evidence, impact, and a concrete fix or investigation direction.
2. Review scope: base and head, commit range, dirty scopes, paths, design documents, and exclusions.
3. Guided reading path when it helps the user continue the review.
4. Questions only when evidence cannot resolve a material issue.
5. Unverified areas and the reason they remain unverified.

If there are no actionable findings, say so directly and still state the reviewed scope and remaining uncertainty.

## Script

```bash
scripts/collect_review_context.sh
scripts/collect_review_context.sh --base upstream/main
scripts/collect_review_context.sh --paths pkg/scheduler,server
scripts/collect_review_context.sh --no-fetch --base HEAD
```
