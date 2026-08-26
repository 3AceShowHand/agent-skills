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

## Code Review Guide Uses An Active Task List

Prompt:

> Write a local code review guide for the current branch. Organize it by priority, include multiple links to code and tests, and treat the topic-visibility review as already done.

Expected:

- The document is a task list grouped by the priority levels that have pending work.
- Every review outcome starts with `- [ ]`; code, tests, and concrete problems are indented under it when useful.
- A `Code`, `Tests`, or similar field with multiple elements puts its label on a separate line and each element in its own child list item; a single element may remain inline.
- Source links are repository-relative Markdown links with verified `#L<line>` anchors.
- Link labels summarize the change intent, risk, or review question instead of merely repeating method and test names.
- Conditions resolvable from code, tests, or authoritative sources are verified; satisfied condition text is removed and unmet conditions become evidence-backed problems.
- Review items that remain useful as human reading entry points are retained after condition verification.
- The completed topic-visibility item and all supporting content that serves only it are absent.
- The document omits metadata, background, branch snapshots, narrative reading paths, and generic review-report instructions.

## Completed Review Report Preserves Findings

Prompt:

> The review is complete. Write the final report with the verified findings ordered by severity and include the reviewed scope and remaining uncertainty.

Expected:

- The document preserves a findings-first report structure.
- Verified findings are not converted into unchecked tasks.
- The active-task-list template does not override the final-report request.

## Verified Conditions Do Not Remove Review Entry Points

Prompt:

> Check every completion condition in this code review guide yourself. Remove conditions that pass, keep the review items, and preserve any failures as concrete problems.

Expected:

- The agent verifies conditions from code, tests, and authoritative sources instead of asking the user to decide them.
- Satisfied completion-condition text is absent.
- Review items remain as concise human reading entry points.
- Each unmet condition is rewritten as a concrete problem with evidence and a precise source link.

## Symbol Index Keeps Identifier Labels

Prompt:

> Create an API symbol index that links every exported method to its definition.

Expected:

- Link labels preserve the exported identifiers because direct symbol lookup is the document's purpose.
- The review-worklist intent-label rule does not rewrite identifiers into narrative descriptions.

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
