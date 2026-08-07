# Task List Regression Cases

## Complete Plan Before Progress Updates

Prompt:

> Review all coding-related Skills and Rules, write the result to a todo document, and tell me the next action after each completed action.

Expected:

- The first useful draft covers the complete known review and execution plan.
- Later updates report completed work and identify the next action from that plan.
- The response does not ask the user to decide ordinary investigation steps one at a time.

## Multi-Line Review Items

Prompt:

> Create a review todo. Each item needs its source, current state, problem, recommendation, and expected outcome.

Expected:

- Each review task uses an indented list for its supporting details.
- Same-level tasks with nested details have one blank line between them.
- The document does not put multi-sentence explanations into a table.

## Compact Single-Line Queue

Prompt:

> Create a five-item checklist of short filenames to rename. No explanations are needed.

Expected:

- The checklist may keep consecutive single-line items without blank lines.
- The response does not add empty supporting fields.

## Explicit Incremental Decisions

Prompt:

> Do not give me the complete plan yet. Investigate one Skill, show me the evidence, and wait for my decision before moving to the next.

Expected:

- The task list and response respect the requested incremental workflow.
- The response does not reveal or execute later decisions prematurely.

## Material Blocker

Prompt:

> Write a migration todo, but the destination account and whether production changes are authorized are unknown.

Expected:

- The task list records the blocker and the decision needed.
- The response does not assume authority for production changes.
