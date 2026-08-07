---
name: write-great-document
description: Create, organize, or update local Markdown documents such as requirements, designs, and task lists from discussions, existing materials, and code. Use only when the user intends to create or modify a local Markdown file. Do not use for chat-only prose, repository-level AGENTS.md work handled by project-agents-bootstrap, or documents on platforms handled by dedicated skills.
---

# Write Great Documents

## Quality Standards

Check every item before presenting the first draft. Deliver the draft only when it meets all of these standards:

- Write naturally in the target language, following its idioms, common usage, and professional writing conventions. Do not mechanically copy another language's syntax or word order.
- Make the purpose immediately clear. Use clear topic sentences, lead with conclusions, and make the document's purpose apparent at a glance.
- Organize the document logically. Order sections for the reader and keep each paragraph focused on one topic.
- Use prose for settled claims and causal chains. Present unresolved items as a short list regardless of their count; keep the items at the same logical level and in parallel grammatical form.
- Make headings identify the section's actual subject and distinguish it from neighboring sections. Avoid generic workflow labels such as `Current Stage` when the section contains more specific material such as requirement inputs and open questions.
- Choose precise language. Use accurate, consistent terminology and avoid vague, inflated, or cluttered wording.
- Make sentence structure match the underlying relationships. Give each clause a clear subject and predicate, use verbs that the subject can logically perform, keep coordinated items semantically parallel, and split a sentence when one verb or modifier does not apply cleanly to every item. Write that stakeholders resolve questions and reach decisions, or that requirements become testable; do not write that questions "form conclusions."
- When a source sentence compresses several relationships into one vague predicate, unpack them into separate clauses. For unlike dimensions, name each relationship—for example, what a metric counts, how it correlates with cost, and which actions create billable usage. Preserve every sourced relationship; if a relationship is unclear, mark it for confirmation instead of silently dropping it.
- Maintain rigorous logic. Support conclusions with the document's evidence or preceding reasoning, complete each line of reasoning, avoid contradictions, and label assumptions and unknowns explicitly.
- Be concise. Remove filler and state each piece of information only once.
- Follow Markdown conventions. Use correct syntax for headings, lists, code blocks, and links.
- Meet the professional standards of the document type: current-state analysis, requirements, design, or task list.

## Writing Process

Complete this process internally before presenting the first draft. Do not include the process itself in the document:

1. Identify the document's purpose, audience, and deliverable format.
2. Separate facts, decisions, assumptions, and unknowns. Do not present unknowns as conclusions.
3. Select only material that supports the document's purpose.
4. Decide the reading order and where each piece of information belongs.
5. Keep one topic per paragraph and one canonical location for each piece of information.
6. Read the headings alone and verify that they form an accurate, non-redundant outline of the document.
7. Check the draft against the quality standards before delivering it.

## Input

- Require the user only to explain what to write and provide the source material or its location.
- Fill in context from the current conversation, existing documents, and relevant code.
- Ask only about questions the available material does not answer when a wrong assumption would change the conclusion and cause expensive rework. Otherwise, continue writing and label assumptions where necessary.

## Output and Files

- Produce a Markdown document by default.
- Use the user's path when provided; otherwise, write to the current directory.
- Use lowercase, hyphenated English filenames. For a single combined document, use the topic name. For separate documents, add a type suffix: `-current-state`, `-requirements`, `-design`, or `-tasks`.

## Standard Document Opening

Use the following opening for every document except a task list:

```markdown
# Document Title

Last updated: YYYY-MM-DD
Status: (when useful)
Scope: (when useful)
Audience: (when useful)
Related documents: (when useful)

## Background

(Explain why this document exists and what problem it addresses.)

(Document body)
```

- Place metadata between the title and `Background`. Always include `Last updated`; add `Status`, `Scope`, `Audience`, `Related documents`, and similar fields only when useful. Do not leave empty fields.
- Update the `Last updated` date whenever the document changes. Do not maintain a change summary.
- Use `Background` to explain why the document exists and what problem it addresses. Do not repeat the metadata.
- Treat metadata as the canonical location for status, scope, audience, and similar facts. Repeat one in the body only when the body explains a consequence or detail that the metadata cannot express.
- When relevant, make the opening distinguish what is already decided, what remains unknown, why the unknown matters, and what the document covers. Describe deferred work as a current boundary with a condition for revisiting it; do not make it sound permanently out of scope.
- Present every unresolved item in `Background` as a short bullet list, regardless of count. Introduce the list with one sentence, explain consequences afterward, and keep the items at category level when later sections contain the details.

## Document Types

Treat current-state analysis, requirements, design, and task lists as independent documents. Generate any one of them without requiring the others or a fixed sequence. When generating a document, summarize the background from the current conversation, existing documents, relevant code, and other source material. Link to existing related documents instead of restating them.

### Coverage Check

Before generating or updating a document, identify every in-scope input relevant to the target document type from the available sources. Before delivery, verify that:

- The document covers every relevant input.
- Every output item traces back to an existing document, the current conversation, relevant code, or another explicit source.
- Anything without a traceable source is new scope. Add a source or mark it for confirmation instead of presenting it as agreed scope.
- When related requirements, design documents, or task lists exist, check across them for omissions, contradictions, and stale references. Do not create missing companion documents solely for this check.
- Establish the verification relationship appropriate to the current stage: requirements define acceptance criteria, designs describe verification methods, and tasks state actionable completion conditions and verification steps.

Reuse stable source identifiers when available. Otherwise, use a heading, paragraph topic, file location, or decision from the conversation as the source anchor. Do not modify existing material solely to support the coverage check. Keep coverage mapping internal by default; include source references only when they help implementation or review.

### Current-State Analysis

- Build a shared understanding of the real-world problem.
- State the problem directly in `Background`.
- Distinguish established decisions or inputs, observed implementation facts, constraints, and open requirement questions. Do not treat an input as a confirmed requirement unless the source does.
- Explain the relevant current state, the causes or conditions that produced it, and its impact on requirements or goals.
- Organize sections around the domain subjects readers need to understand. Do not add a generic status or stage section merely to repeat metadata, restate `Background`, or preview questions covered in detail later.
- Remove an opening inventory section instead of merely renaming it when its unique content fits in `Background` and the rest repeats metadata or later detail.
- If readers need a short inventory of knowns and unknowns, name the section after that content and keep each detailed item in one canonical location.
- Include only what readers need to understand the problem. When the cause is uncertain, distinguish known conditions from unknowns.
- Do not require a proposed solution.

### Requirements

- State the problem to solve.
- Define the expected behavior.
- Identify constraints.
- Write acceptance criteria as assertions.

### Design

- Explain how to implement the solution.
- Record key decisions.
- Describe workflow changes.
- Identify risks.
- Define verification methods.

### Task List

Read [Task List Rules](./references/task-lists.md) before creating or updating a task list.

- Keep the document focused on unfinished work. Use the filename and level-one heading to convey purpose; omit metadata, `Background`, and the last-updated date.
- Give the complete known plan in the first useful draft. Sequential execution controls order, not how much of the plan the user can see.
- Use headings when they make priorities, sources, or topics easier to scan. Start each actionable task with `- [ ]` and put supporting detail in an indented list.
- Use lists for multi-sentence explanations. Use a table only when fields are stable, cells are short, and horizontal comparison is materially faster.
- Put one blank line between same-level items when an item contains nested content or spans multiple lines. A compact list of single-line items may remain tight.
- Remove completed tasks instead of keeping a work log. Delete the task-list file after the final task is complete.
