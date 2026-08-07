---
name: evolve-skills
description: Use when a user rejects, corrects, or asks to improve an agent result, process, or behavior; when task outcomes, repeated rework, routing failures, or cross-agent differences suggest that an existing Skill needs improvement; or when the user asks to evolve or review Skill behavior. Analyze evidence, identify the responsible Skills, attribute the cause, generalize a reusable principle, and stop for user confirmation before editing. After confirmation, make the smallest source change, add regression evidence, validate behavior in fresh contexts, and follow the authorized release workflow. Do not use for creating unrelated new Skills, ordinary task failures without evidence of a Skill defect, mechanical maintenance, or one-off project preferences.
---

# Evolve Skills

Improve existing Skills from observed outcomes without turning isolated incidents into permanent rules.

## Evaluate Evidence

Rank evidence by reliability:

1. Explicit user rejection, dissatisfaction, correction, or requested improvement.
2. Objective task, test, or production outcome.
3. Repeated rework, routing failure, or cross-agent difference.
4. Agent self-assessment.

Do not evolve a Skill from self-assessment alone. Reduce retained evidence to the smallest reproducible input, output, and correction; exclude secrets, private data, and unrelated conversation.

Read `references/observations.md` when current feedback may resemble a recorded problem. Compare behavior, impact, and likely cause; do not require identical wording, tasks, or identifiers.

## Attribute the Cause

Identify the Skills that governed the criticized result, process, or behavior. Then classify the failure before proposing a change:

- Routing defect: the correct Skill did not trigger, or an unrelated Skill did.
- Skill defect: a missing, ambiguous, incorrect, or conflicting instruction caused the behavior.
- Execution defect: the Skill already contains a clear instruction that the agent ignored.
- Task-specific exception: the feedback depends on one project, user, or temporary constraint.
- Model variance: independent runs disagree without a stable instruction gap.

Advance routing and Skill defects. Investigate repeated execution defects for ambiguous or overloaded instructions. Do not modify a Skill to encode task-specific exceptions or unexplained model variance.

## Maintain Observations

Use `references/observations.md` for user-confirmed evidence that is not yet sufficient to justify a Skill change. Add or update an observation only after the user confirms that it should be retained.

- Merge similar errors by behavior and likely cause instead of creating one record per phrasing.
- Treat recurrence as stronger evidence, not proof of a Skill defect.
- Reassess attribution whenever an observation is updated.
- Apply the update and clearing rules in the reference on every write.
- Keep observations separate from requirements and regression cases.

## Generalize the Lesson

Express the candidate principle with:

- the behavior it requires or prohibits;
- the Skills and situations it affects;
- its boundary and likely counterexample;
- the existing instruction it replaces, clarifies, or removes.

Reject principles that merely restate the incident, duplicate model defaults, grant default permissions, bind a reusable Skill to one project, or add process without reducing future errors.

## Stop for Confirmation

Report the observed problem, attribution, generalized principle, affected scope, and one representative counterexample. State the proposed next action.

Stop before editing files, adding tests, committing, pushing, or installing. Continue only after the user confirms or corrects the attribution and generalized principle. Treat silence as no confirmation. Return to this checkpoint when later evidence changes the principle or scope materially.

## Modify the Source

After confirmation:

1. Work in the source repository, never an installed copy or agent link. This Skill collection is maintained at `https://github.com/3AceShowHand/agent-skills` and normally checked out at `~/workspace/agent-skills`.
2. Add or update a regression case that reproduces the failure through behavioral invariants instead of an exact preferred answer.
3. Make one minimal change for the confirmed principle. Prefer removing or tightening existing text before adding instructions.
4. Update every affected Skill only when the confirmed scope requires it.
5. Remove superseded rules, examples, and tests.

## Select the Improvement

Validate the candidate against:

- repository structure and metadata checks;
- routing positive and negative cases;
- the original failure and adjacent counterexamples;
- fresh Codex and Pi contexts without leaked expected answers;
- instruction overlap, contradictions, and context growth.

Retain the candidate only when it fixes the observed failure without weakening existing behavior. Return to the confirmation checkpoint when validation requires a different principle or broader scope.

## Release

Follow the repository's authorized release sequence. Report the changed Skills, validation evidence, commit, remote state, installation targets, and remaining uncertainty. Do not commit, push, or install when the user's scope excludes those actions.
