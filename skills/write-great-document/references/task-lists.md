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

Example:

```md
# Skill review tasks

## P0｜Global behavior

- [ ] Review the global instruction entry point.
  - Source: `/path/to/AGENTS.md:1`.
  - Finding: It loads several task-specific workflows on every request.
  - Recommendation: Keep a minimal entry point and move workflows into Skills.

- [ ] Review the always-on coding plugin.
  - Source: `/path/to/plugin/SKILL.md:1`.
  - Risk: Its trigger covers every coding task.
```

## Ordering And Maintenance

- Determine order from actual dependencies. Do not infer a dependency only from list position.
- Without violating dependencies, order tasks from lower risk to higher risk.
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
