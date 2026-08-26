# Task List Rules

Use these rules for todo documents, review queues, migration plans, and implementation task lists.

## First Draft

- Inspect the available conversation, documents, and code before drafting.
- Cover the complete known scope in the first useful draft. Include later phases, dependencies, verification, publication, rollback, and completion conditions when they are already known.
- Do not turn ordinary investigation steps or decisions supported by available evidence into separate user approval points.
- If the user asks for the next action after each completed action, provide the full plan first. During execution, report the result and identify the next action from that plan.
- Use incremental decision-making only when the user explicitly requests it or when missing information would materially change scope, authority, external side effects, or an irreversible result.

## Structure

- Keep only content that supports unfinished tasks, blockers, open questions, or pending verification.
- Use headings to group tasks by priority, source, or topic when grouping improves navigation. State a priority once in the group heading instead of repeating it on every task.
- Start every actionable task with `- [ ]`. Describe one outcome per task, not a sequence of tiny operations.
- Add indented subitems when they help the reader decide or execute. Useful subitems include source, current state, problem, recommendation, dependencies, expected outcome, verification, and rollback. Omit fields that add no information.
- Use prose for a settled conclusion or causal explanation that belongs to the whole section. Keep task-specific evidence and instructions under the task they support.

## Lists And Tables

- Use an indented list when an item needs several sentences, evidence, rationale, recommendations, or execution details.
- Put one blank line between same-level items when an item contains nested content or spans multiple lines.
- Keep single-line sibling items together when a compact list is easier to scan.
- Use a table only when all fields are stable, cells are short, and readers need repeated horizontal comparison.
- Convert a table to a list when cells contain causal explanations, multiple sentences, recommendations, or step-by-step instructions.

## Code Review Worklists

Use this shape for a code review guide, checklist, plan, or queue that tracks unfinished review work:

- Group tasks by actual priority. Put correctness and resource safety before tests, scope, and maintainability. Omit empty priority groups.
- Make every review outcome a top-level `- [ ]` task. Keep code, tests, risks, verification, and completion conditions as indented supporting details.
- When a supporting field such as `Code` or `Tests` contains multiple elements, put the field label on its own line and list each element as a child item. A field with one element may remain inline.
- Use repository-relative Markdown links with `#L<line>` anchors when the document renderer supports source jumps. Resolve links from the document's location and verify every target and line.
- Keep only pending work. Remove a completed review item and all supporting content that serves only that item.
- Omit metadata, background, branch snapshots, narrative reading paths, and generic review-report instructions unless one is necessary to execute a pending task.
- Put validation commands under the task whose completion they verify, or in one final validation task when they cover the whole worklist.

Template:

```md
# Change review tasks

## P0｜Correctness and resource safety

- [ ] Review task-list document behavior.
  - Code:
    - [Task List routing](../SKILL.md#L164)
    - [Task List structure](./task-lists.md#L1)
  - Tests:
    - [Task-list evals](../evals/task-lists.md#L1)
    - [Quality-gate evals](../evals/quality-gate.md#L1)
  - Completion conditions:
    - Pending work is ordered by priority.
    - Completed work is absent.

## P1｜Validation

- [ ] Run focused validation.
  - Verification: `uv run --with pyyaml python scripts/validate_skills.py`.
```

A completed code review report is a different artifact. Preserve its evidence-backed findings and severity order instead of converting resolved findings into unchecked tasks.

## Ordering And Maintenance

- Determine order from actual dependencies. Do not infer a dependency only from list position.
- Without violating dependencies, order tasks from higher priority and risk to lower priority and risk.
- Within the same risk level, prefer vertical slices that complete one end-to-end outcome before expanding.
- Remove completed tasks immediately. Put completed work in the final response, commit, pull request, or changelog instead of the active task list.
- Delete the task-list file after the final task is complete unless the user needs it retained as a durable record.
- Update the document when scope, priority, risk, blockers, or pending verification changes.

## Locations And Verification

- For code-related tasks, include at least one concrete `path:line` pointing to the highest-signal affected location.
- If a target does not exist yet, name the planned path without inventing a line number. Add the real line after creating it.
- For non-code review tasks, cite a concrete file, URL, command result, or conversation decision when it helps the reader verify the task.
- Update stale line references when touching an item.
- State an actionable completion condition and relevant verification for each task. Do not claim a check passed until it ran.
