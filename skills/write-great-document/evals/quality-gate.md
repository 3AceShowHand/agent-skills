# Document Quality Gate Regression Cases

## Scope, Logic, and Redundancy Override the Total

Prompt:

> Update this requirements document. It repeats the same scope in three sections, introduces an undefined recovery metric, treats a settled decision as an open question, and includes an unrelated product roadmap. Preserve only the confirmed metering requirements.

Expected:

- The agent removes the duplicated scope, undefined metric, stale open question, and unrelated roadmap before delivery.
- The agent does not use strong scores in unaffected dimensions to offset a delivery blocker or a dimension below 8.
- The completed document is not returned until it has no blocker and scores at least 90.

## Logical Gap in a Polished Document

Prompt:

> Write a concise policy that says usage is counted only after confirmed delivery. It must also explain retries without charging the same delivery twice.

Expected:

- The policy explains how the confirmed-delivery rule and retry rule fit together without contradiction.
- Good formatting and concise prose do not compensate for a missing or conflicting retry condition.
- The agent revises and rescores the document if the logic is incomplete.

## Long-Form Table Is a Delivery Blocker

Prompt:

> Turn these design tradeoffs into a document. Each option needs several sentences explaining causes, consequences, and recommendations.

Expected:

- The agent uses prose or lists for the tradeoffs instead of placing the explanations in a table.
- A table with multi-sentence reasoning prevents delivery until it is replaced.

## Stable Comparison Table Remains Valid

Prompt:

> Document five configuration fields with a name, type, default value, and one-line description.

Expected:

- A table remains acceptable when the fields are stable, cells are short, and horizontal comparison improves readability.
- The quality gate does not prohibit tables solely because the document contains one.

## Long Identifiers and Source Locations Use a List

Prompt:

> Update a local metrics audit containing five long metric identifiers, each paired with a linked source path and line number. The current document puts them in a two-column table. Keep the full names and source links, and explain each metric's purpose.

Expected:

- The inventory uses separate list items with the complete identifiers and source links preserved.
- Purpose and reasoning stay in the corresponding item or paragraph, without table cells or forced line breaks inside cells.
- A stable identifier-to-location mapping does not override the requirement for compact table content.
- Short numeric comparisons elsewhere may remain in a table; the agent does not impose a blanket table ban.

## Multiple Similar Elements Use a List

Prompt:

> Create a document opening that references three related documents and records three constraints.

Expected:

- The three related documents appear as separate list items instead of one comma-separated metadata line.
- The three constraints also appear as separate list items.
- The same rule applies to other groups of similar, same-level elements such as sources or open questions.
- A metadata field containing only one related document may remain inline; the rule must not turn every scalar metadata value into a list.

## Removed Scope Disappears Completely

Prompt:

> Update this incident analysis. The runtime version is fixed, and the document no longer needs version differences, migration history, or A/B validation discussion. Keep the application defect and its fix.

Expected:

- The document removes the excluded sections and every supporting link, comparison, caveat, deferred item, and non-goal statement about them.
- The document does not retain the removed material through statements that it is unnecessary, fixed, unverified, deferred, or outside scope.
- A runtime identifier may remain only when another requested section, such as an acceptance environment, explicitly requires it.

## Missing Input Prevents a Passing Document

Prompt:

> Write the final requirements, but the unit of measurement and the event that confirms delivery have not been decided.

Expected:

- The agent identifies the missing decisions that prevent a reliable final document.
- The agent requests only the necessary input instead of inventing requirements or returning the document as complete.

## Structural Deletion Preserves Adjacent Sections

Prompt:

> Remove the completed P1 section from this active review worklist, together with its summary and execution-order references. Preserve the P2 section and the separate historical execution record.

Expected:

- Remove the completed item and references that serve only it.
- Preserve the P2 content and the explicitly retained execution record.
- Reread edited boundaries and verify that headings remain correctly nested without duplicate P2 sections.
- Complete verification from document inspection; application builds and tests add no relevant evidence.

## Review Document Background Stays Short

Prompt:

> Draft the `Background` for a review document that already has one section per confirmed problem, a priority table with a status column, and a body that defines each progress term where it is used. The draft explains how the sections are ordered, defines three progress terms, and notes that the original numbering is preserved.

Expected:

- `Background` states why the document exists and which problem it addresses, in at most two short paragraphs.
- The ordering explanation, the term definitions, and the numbering note are removed, not paraphrased into the section.
- Status and remaining work stay in the section that owns them, and metadata is not repeated.

## Resolved Findings Leave the Document

Prompt:

> A security findings document has one section per finding plus a priority table with a status column. Two findings are implemented and verified; their sections hold triggering conditions, fix descriptions, and verification records. The shared fix that covered them also appears in a shared section and in the opening sentence.

Expected:

- Delete the two resolved sections instead of relabeling them implemented or fixed.
- Remove their rows from the priority table and renumber the remaining order.
- Remove their triggering conditions, fix descriptions, verification records, and opening or status references, keeping no work log.
- Keep shared material only where it still serves a remaining finding.

## Deployment Limitation Inventory Is Noise

Prompt:

> Finish this security findings document. It ends with a section listing conditions never verified in a real deployment: whether firewalls and proxies allow the attack path, whether client certificates are enabled, the full chain to SQL execution, and whether the old architecture behaves the same.

Expected:

- Delete the limitation section instead of restating it more concisely.
- Keep a condition only where a specific remaining action depends on it, inside that finding.
- Add no generic deployment, environment, or end-to-end caveats.

## Coined Labels Instead of Code Names

Prompt:

> Explain how the consumer advances its checkpoint. The code names `head`, `watermark`, `pendingDDL`, and `PostFlush`; the draft instead introduces "表组队首聚合", "输入确认水位", and "转换滞留窗口" as new labels.

Expected:

- Use `head`, `watermark`, `pendingDDL`, and `PostFlush` as the code names them, or describe the behavior in plain words.
- Remove the coined labels instead of defining them at first use.
- Keep one name per thing throughout the document.
