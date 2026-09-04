---
name: skills-management
description: Use when creating, naming, updating, renaming, validating, publishing, installing, removing, or reviewing Skills; or when user feedback, repeated rework, routing failures, or cross-agent differences suggest that Skill behavior should improve. Owns the Skill lifecycle from source changes and regression evidence through authorized release and installation with the skills CLI. Do not use when a Skill merely applies to an ordinary task and no durable Skill change is requested or supported.
---

# Skills Management

Manage the complete Skill lifecycle while keeping source, release, and installed state explicit.

## Select the Operation

- Create: confirm the purpose, trigger boundary, and final name before generating files.
- Update: identify the source instruction and the smallest behavior change.
- Rename: move the source directory and update frontmatter, UI metadata, catalogs, routing cases, references, validators, and installation state.
- Evolve from feedback: evaluate evidence and attribute the failure before changing durable guidance.
- Release or install: validate, commit, push, and install only the steps the user authorized.

Do not create a tentative Skill directory while its name is still under discussion. A user-specified final name and scope are direct confirmation for that requested change.

## Work From the Source

- Work in the source repository, never an installed copy or agent link. This Skill collection is maintained at `https://github.com/3AceShowHand/agent-skills` and normally checked out at `~/workspace/agent-skills`.
- Read repository instructions and inspect the branch, remotes, staged changes, unstaged changes, and untracked files before editing.
- Preserve existing work. Limit edits and staging to the requested Skill change, including partial staging when a shared catalog or routing file already contains unrelated modifications.
- Use `skill-creator` for Skill structure and metadata rules. Reuse existing references and tests when they already own the behavior.

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

This checkpoint applies to inferred improvements from feedback. Proceed when the user directly requests a specific creation, rename, update, removal, release, or installation and its scope is clear.

## Modify the Source

After confirmation:

1. Add or update a regression case that reproduces the required behavior through invariants instead of an exact preferred answer.
2. Make the smallest source change that covers the confirmed scope. Prefer removing or tightening existing text before adding instructions.
3. Update the Skill directory, frontmatter, UI metadata, references, catalogs, routing cases, validators, and cross-Skill references affected by a creation or rename.
4. Remove superseded names, rules, examples, and tests.
5. Keep substantial conditional guidance in routed references and keep the entrypoint concise.

## Select the Improvement

Validate the candidate against:

- repository structure and metadata checks;
- routing positive and negative cases;
- the original failure and adjacent counterexamples;
- fresh Codex and Pi contexts without leaked expected answers;
- instruction overlap, contradictions, and context growth.

Retain the candidate only when it fixes the observed failure without weakening existing behavior. Return to the confirmation checkpoint when validation requires a different principle or broader scope.

For this Skill repository, run the repository validator after focused structure checks. Use a temporary Python environment when `PyYAML` is unavailable instead of changing the repository or global Python environment:

```bash
uv run --with pyyaml python scripts/validate_skills.py
```

## Release

Follow the repository's authorized release sequence. Commit, push, install, remove, or update installed Skills only when the user explicitly requests those operations.

- Review the staged diff before committing, especially when shared files have unrelated worktree changes.
- Install and remove Skills only through the `skills` command. Do not use installer Python scripts or manually copy files into agent directories.
- Install from the validated source with a command such as:

```bash
skills add <source> -g -a codex pi --skill <skill-name> -y
```

- Treat the successful `skills add` summary and the universal installation path as the installation result. In this environment, `~/.agents/skills/<skill-name>` is available to Codex; an `agents` field that lists only Pi does not prove that Codex is missing the Skill.
- Re-read the installed Skill through the next-turn Skill catalog when availability matters. Do not create a second copy under `~/.codex/skills` to compensate for the CLI's agent display.

Report the changed Skills, validation evidence, commit and remote state when requested, installation command and target, preserved unrelated changes, and remaining uncertainty.
