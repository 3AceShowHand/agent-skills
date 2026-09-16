# Clarity Quality Gate Regression Cases

## Directly State a Scope Change

Prompt:

> Explain that a refactor moves SASL type ownership from a client library to application code and adds no authentication capability.

Expected:

- The response directly states the ownership change and the unchanged capability scope.
- The response gives each fact its own sentence when both facts are useful.
- Any paired or compressed correction frame makes the score 0, including semantic equivalents that replace or downgrade one claim to emphasize another.
- The final scan explicitly rejects Chinese forms such as `不是……而是……`, `并非……而是……`, `不只是……而是……`, and `Y，而不是 X`.

## Preserve a Material Distinction

Prompt:

> Clarify the ownership difference between validation failures and network failures.

Expected:

- The response names the owner of each failure class in separate direct statements.
- The response preserves the distinction without paired correction syntax, compressed substitutions, or replacement markers.
- Accurate technical content cannot offset a prohibited frame; any occurrence makes the score 0.

## Paraphrase Source Framing

Prompt:

> Summarize a source passage that uses a reject-X/assert-Y rhetorical frame.

Expected:

- The response paraphrases the source into direct claims and identifies it as a paraphrase when attribution matters.
- The response does not reproduce the source's prohibited frame.
- A request that requires verbatim fidelity is reported as a conflict without emitting the frame.

## Removed Topic Is Omitted

Prompt:

> Remove the discussion of runtime-version differences from this analysis. Keep the application defect and proposed fix.

Expected:

- The result contains no runtime-version comparison, migration history, runtime-version-related validation plan, or related link.
- The result does not mention the removed topic through exclusion, deferral, fixed-constraint, or non-goal wording.
- The defect and proposed fix remain complete without narrating the deletion.
