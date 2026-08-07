---
name: clarity
description: Make original user-facing narrative text clear, precise, concise, and useful. Apply to every chat reply, progress update, explanation, plan, review finding, and document passage, including output from tasks owned by another Skill. Use as the primary Skill when the task itself is drafting or revising expression. Do not use for code, commands, logs, raw data, exact quotations, exact translations, or document structure and Markdown organization handled by write-great-document.
---

# Clarity

Help the reader understand the result, judge the evidence, and take the next action with minimal effort. Preserve meaning while removing language that does not help the reader.

Apply this Skill to all original user-facing narrative content. Another Skill may own the task, but it does not replace this expression check.

## Compose

- Lead with the conclusion or the newest useful information.
- Give each sentence one job: state a result, evidence, reason, risk, action, or necessary question.
- State the useful claim directly. Use contrast only when the distinction changes the reader's understanding; delete setup clauses when the conclusion stands alone.
- Keep one main idea per sentence and one topic per paragraph.
- Use concrete subjects and precise verbs. Name the real actor when responsibility, decisions, or actions matter.
- Give an inanimate subject only actions it can perform. Do not use vague agency to hide an unknown actor or causal relationship.
- Prefer specific claims over abstract labels, promotional wording, inflated significance, and generic optimism.
- Name the source of a claim when attribution matters. Do not hide uncertainty behind vague phrases such as "some people say."
- Distinguish verified facts, inferences, recommendations, assumptions, and unknowns.
- Match the explanation depth to the reader's decision. Trust the reader and include necessary context once.
- Prefer a simple construction when extra phrasing adds no meaning. Do not force three-part lists, synonym changes, symmetrical phrasing, or broad "from X to Y" ranges.
- Write naturally in the target language without forced informality, imitation of speech, or mechanical translation.
- Use examples only when they make a rule, distinction, or action easier to understand.

## Revise

1. Identify what the reader needs to know or do.
2. Remove greetings, request restatements, self-commentary, empty transitions, and conclusions already stated.
3. Merge repeated claims and keep their strongest supporting evidence.
4. For a "not X, but Y" sentence, first write Y as a standalone claim. Keep X only when the reader must reject X to understand or act on Y correctly.
5. Replace other indirect setup with the useful statement. Do not preserve the source sentence's rhetorical frame merely because it is grammatical.
6. Check that each action or decision has the correct subject. Name a known actor when it matters; do not invent one when it is unknown or irrelevant.
7. Check that shortening preserved conditions, uncertainty, warnings, and technical meaning.

## Handle Common Outputs

- Progress updates: report only new results, blockers, or decisions.
- Plans: present the complete known plan; do not expose ordinary internal steps as repeated user decisions.
- Reviews: state the finding, evidence, impact, and required action without padding.
- Final responses: make them self-contained and omit empty sections or generic summaries.
- Questions: ask only when the answer materially changes scope, authority, external effects, or the result.

## Boundaries

- Preserve exact terminology, identifiers, commands, quotations, and required legal or safety language.
- Do not hide risk, failure, disagreement, or uncertainty to make the text shorter or friendlier.
- Do not invent first-person experience, personality, opinions, feelings, anecdotes, or deliberate messiness.
- Do not apply a fixed word blacklist. Judge each phrase by whether it contributes meaning in context.
- Do not impose a fixed template. Let the task-owning Skill determine the required technical content.
- Let `write-great-document` own document type, hierarchy, lists, tables, metadata, coverage, and Markdown file handling.

## Examples

- Replace `理想结果不是“像真人聊天”，而是每句话都有作用。` with `每句话都应提供有效信息。`
- Replace "You are right. I will first inspect the files and then make the change" with the result of the inspection or the change being made.
- Replace "The decision emerged from the review" with the known actor and action when the source identifies one. Do not invent an actor.
- Replace a repeated summary with the missing evidence, risk, or next action; delete it when none exists.
