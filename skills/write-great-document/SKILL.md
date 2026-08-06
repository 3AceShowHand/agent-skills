---
name: write-great-document
description: Create, organize, or update local Markdown documents such as requirements, designs, and task lists from discussions, existing materials, and code. Use only when the user intends to create or modify a local Markdown file. Do not use for chat-only prose or requests to create or update documents on platforms handled by dedicated skills.
---

# Write Great Documents

## Quality Standards

Check every item before presenting the first draft. Deliver the draft only when it meets all of these standards:

- Write naturally in the target language, following its idioms, common usage, and professional writing conventions. Do not mechanically copy another language's syntax or word order.
- Make the purpose immediately clear. Use clear topic sentences, lead with conclusions, and make the document's purpose apparent at a glance.
- Organize the document logically. Order sections for the reader and keep each paragraph focused on one topic.
- Choose precise language. Use accurate, consistent terminology and avoid vague, inflated, or cluttered wording.
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
6. Check the draft against the quality standards before delivering it.

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
- Explain the relevant current state, the causes or conditions that produced it, and its impact on requirements or goals.
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

- Keep it concise. Use the filename and level-one heading to convey purpose; omit metadata, `Background`, and the last-updated date.
- List only tasks after the level-one heading. Start each task with `- [ ]`.
- When clarification is necessary, use a regular indented list to describe the issue and recommendation briefly. Do not preserve fixed fields that have no meaningful content.
- Assume tasks run sequentially. Determine the order from actual dependencies rather than inferring dependencies from list position. Without violating dependencies, order tasks from lower risk to higher risk.
- Within the same risk level, use vertical slices: complete one end-to-end unit across the full stack before expanding to other units.
- When the user reports a task complete, remove it from the document. Delete the task-list file after the final task is complete.
