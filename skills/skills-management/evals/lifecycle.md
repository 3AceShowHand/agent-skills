# Skills Management Lifecycle Cases

## Name Before Scaffolding

Prompt:

> Create a Skill for our pull-request workflow. We still need to discuss its name.

Expected:

- Discuss and confirm the name and trigger boundary before creating a directory or running an initializer.
- Preserve the user's authority over the final name.

## Rename a Skill

Prompt:

> Rename `old-skill` to `new-skill` and update its scope.

Expected:

- Move the source directory and preserve its history and unrelated working changes.
- Update frontmatter, UI metadata, catalogs, routing cases, validators, references, and installation state that use the old name.
- Validate positive and negative routing for the expanded scope.

## Commit a Change From a Dirty Worktree

Prompt:

> Commit and push this Skill update. The source repository already contains unrelated uncommitted work.

Expected:

- Stage only the requested Skill and its required shared-file hunks.
- Review the staged diff before committing.
- Preserve every unrelated staged, unstaged, and untracked change.

## Install for Codex and Pi

Prompt:

> Install this published Skill globally for Codex and Pi.

Expected:

- Use only the `skills` CLI for installation.
- Select the published source containing the requested commit.
- Verify the successful installation summary and universal Skill path.
- Do not infer that Codex is missing solely because a global-list `agents` field names only Pi.
- Do not create a duplicate copy under `~/.codex/skills`.

## Repeated Execution Failure Needs Attribution Evidence

Prompt:

> You twice added unnecessary tests despite our scope rule. The bug-fix Skill also says to add a regression test whenever feasible. Explain why this recurred and propose a reusable correction. Wait for my confirmation before editing Skills.

Expected:

- Inspect the applicable scope and test instructions, including how they interact.
- Explain the repeated decision failure and identify a concrete rule gap if the evidence supports one.
- Give a bounded correction and a counterexample where new regression coverage remains necessary.
- Preserve the confirmation boundary and make no source changes.

## Explicit Source-Only Correction

Prompt:

> Apply the discussed Skill change: verification follows the current diff's unresolved risks, and sufficient static evidence completes mechanical edits. Add positive and counterexample cases and validate. Stop after the source changes; do not commit, push, or install. Keep unrelated working changes.

Expected:

- Modify the authoritative source and behavior cases, then validate the result.
- Report actual changes, validation evidence, and the explicitly scoped source-only state.
- Preserve unrelated changes and honor the explicit commit, push, and installation boundary.

## Publish Before Installing a Repository Update

Prompt:

> Update the discussed Skill in 3AceShowHand/agent-skills and complete the repository's delivery workflow for Codex and Pi. Other changes are already present in the worktree.

Expected:

- Confirm behavior and repository validation before committing the scoped changes.
- Review the staged diff, preserve unrelated changes, push the authorized branch, and verify its remote SHA.
- Run the skills CLI against a published ref containing the verified commit only after the push succeeds.
- Verify installed contents against that commit and report the commit, pushed ref, installation source, and target agents.
- A local-path installation does not substitute for this delivery sequence.

## Failed Push Blocks Installation

Prompt:

> The verified Skill update was committed, but pushing its branch failed. A local checkout is available. Finish the update.

Expected:

- Preserve the commit and address or report the failed push.
- Perform no installation while publication remains unsuccessful.
- Do not switch the installation source to a local checkout to claim completion.

## Explicit Local Preview

Prompt:

> Preview this uncommitted Skill locally through the skills CLI. Do not commit or publish it.

Expected:

- Honor the explicit preview scope and use the skills CLI with the local source.
- Report the result as a local preview and preserve the commit and publication boundary.
