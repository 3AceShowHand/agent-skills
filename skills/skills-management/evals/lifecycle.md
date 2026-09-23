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

> Install this committed Skill globally for Codex and Pi.

Expected:

- Use only the `skills` CLI for installation.
- Verify the successful installation summary and universal Skill path.
- Do not infer that Codex is missing solely because a global-list `agents` field names only Pi.
- Do not create a duplicate copy under `~/.codex/skills`.
