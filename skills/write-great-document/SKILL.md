---
name: write-great-document
description: Create, organize, or update local Markdown documents such as requirements, designs, and task lists from discussions, existing materials, and code. Use only when the user intends to create or modify a local Markdown file. Do not use for chat-only prose, repository-level AGENTS.md work handled by project-agents-bootstrap, or documents on platforms handled by dedicated skills.
---

# Write Great Documents

## Structure Standards

Apply these standards before presenting the first draft:

- Make the document's purpose apparent from its title and opening.
- Organize the document logically. Order sections for the reader and keep each paragraph focused on one topic.
- Use prose for settled claims and causal chains. Present unresolved items as a short list regardless of their count; keep the items at the same logical level and in parallel grammatical form.
- Make headings identify the section's actual subject and distinguish it from neighboring sections. Avoid generic workflow labels such as `Current Stage` when the section contains more specific material such as requirement inputs and open questions.
- Keep each fact, decision, assumption, unknown, and recommendation in one canonical location.
- When the user removes a topic from scope, delete its sections, links, comparisons, caveats, deferred-work notes, and exclusion statements. Do not preserve the removed topic by explaining that it is unnecessary, unverified, fixed, deferred, or outside the current scope. Retain only facts that still serve another explicitly requested part of the document.
- Follow Markdown conventions. Use correct syntax for headings, lists, code blocks, and links.
- Present multiple similar, same-level elements as a list instead of joining them inline with commas, slashes, or conjunctions. This includes metadata fields: keep a single value inline, but when fields such as `Related documents`, `Related links`, `Sources`, or `Constraints` contain multiple values, put the label on its own line and list each value as a separate bullet.
- Across every document type, use a table only when fields are stable, cells are short, and horizontal comparison is materially faster. Align table columns in the Markdown source. Use prose or lists when cells would contain causal explanations, multiple sentences, recommendations, tradeoffs, or steps.
- Meet the professional standards of the document type: current-state analysis, requirements, design, or task list.
- Use `clarity` for sentence-level expression, narrative flow, concision, and tone.

## Writing Process

Complete this process internally before presenting the first draft. Do not include the process itself in the document:

1. Identify the document's purpose, audience, and deliverable format.
2. Separate facts, decisions, assumptions, unknowns, and recommendations.
3. Select only material that supports the document's purpose.
4. Decide the reading order and where each piece of information belongs.
5. Keep one topic per paragraph and one canonical location for each piece of information.
6. Read the headings alone and verify that they form an accurate, non-redundant outline of the document.
7. Check the document structure against this Skill and its prose against `clarity`.
8. Apply the pre-delivery quality gate and deliver only after the document passes.

## Pre-Delivery Quality Gate

Score every new or updated document before delivery. Keep the score and deductions internal unless the user asks for them.

Score each dimension from 0 to 10, using whole points, for a total of 100:

1. **Purpose and scope:** The purpose is clear, and every section stays within the requested scope.
2. **Source fidelity:** Facts, decisions, requirements, and recommendations are traceable and correctly classified.
3. **Logical integrity:** Premises support conclusions; rules and sections contain no material contradiction, circular reasoning, missing condition, or conflicting boundary.
4. **Coverage:** The document includes every in-scope input that can materially affect understanding, decisions, or execution.
5. **Structure:** The reading order is logical, headings describe their contents, and each claim has one canonical location.
6. **Clarity:** Sentences are direct, paragraphs stay focused, and the reader can understand the document without reconstructing its meaning.
7. **Concision:** The document contains no repeated conclusion, duplicated background, empty transition, or detail that does not serve its purpose.
8. **Terminology:** New or specialized terms are explained when first used and retain one meaning throughout the document.
9. **Format:** Markdown, headings, lists, links, spacing, and tables follow the user's requirements and repository conventions. Tables contain only short, stable fields suited to horizontal comparison.
10. **Document-type fitness:** The document works as the requested analysis, requirements, design, or task list and includes the corresponding decisions, acceptance criteria, verification, or completion conditions when applicable.

Assign scores from observed defects, not intended quality:

- `10`: no known defect in the dimension.
- `8-9`: one or a few isolated defects that do not impair understanding or use.
- `6-7`: an obvious defect requires revision.
- `0-5`: a material defect makes the document unreliable or unsuitable for its purpose.

Record each deduction internally with the affected location and defect. Do not award `10` to a dimension with a known defect.

A total score cannot override a delivery blocker. Fix every blocker before delivery:

- content outside the requested scope;
- a user-removed topic retained as an exclusion, non-goal, caveat, comparison, deferred item, or related link;
- an unsupported fact, decision, or requirement presented as established;
- an unresolved item presented as settled, or a settled item retained as unresolved work;
- a material logical gap, contradiction, or inconsistent rule;
- an undefined or inconsistently used core term;
- material or repeated redundancy;
- a table containing long-form prose, causal analysis, tradeoffs, recommendations, or procedural steps;
- a required-format violation, broken required reference, or document type that does not match its content.

Deliver only when no blocker remains, every dimension scores at least 8, and the total score is at least 90. Otherwise, revise and rescore. If missing information makes the gate unattainable, report the specific blocker and request only the necessary input instead of returning the document as complete. Evaluate an explicitly requested draft against its declared scope and maturity; draft status does not waive the gate.

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
Related documents:

- (Document A title and path or URL)
- (Document B title and path or URL)

## Background

(Explain why this document exists and what problem it addresses.)

(Document body)
```

- Place metadata between the title and `Background`. Always include `Last updated`; add `Status`, `Scope`, `Audience`, `Related documents`, and similar fields only when useful. Do not leave empty fields.
- Keep one-value metadata fields inline. For multi-value metadata, keep the field label above a bullet list as shown in the template.
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

- Treat a review guide, checklist, plan, or queue that drives unfinished review work as a task list. For code review worklists, follow the priority-based template in the reference. Preserve a completed review report as an evidence-backed findings report.
- Keep the document focused on unfinished work. Use the filename and level-one heading to convey purpose; omit metadata, `Background`, and the last-updated date.
- Give the complete known plan in the first useful draft. Sequential execution controls order, not how much of the plan the user can see.
- Use headings when they make priorities, sources, or topics easier to scan. Start each actionable task with `- [ ]` and put supporting detail in an indented list.
- Put one blank line between same-level items when an item contains nested content or spans multiple lines. A compact list of single-line items may remain tight.
- Remove completed tasks instead of keeping a work log. Delete the task-list file after the final task is complete.
