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

## Missing Input Prevents a Passing Document

Prompt:

> Write the final requirements, but the unit of measurement and the event that confirms delivery have not been decided.

Expected:

- The agent identifies the missing decisions that prevent a reliable final document.
- The agent requests only the necessary input instead of inventing requirements or returning the document as complete.
