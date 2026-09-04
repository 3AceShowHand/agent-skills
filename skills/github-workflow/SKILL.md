---
name: github-workflow
description: Use when creating, updating, linking, or submitting GitHub issues and pull requests for a code change. Reads repository templates and labels, keeps issue and PR responsibilities distinct, protects non-public evidence, safely publishes Markdown, and verifies the resulting GitHub state. Do not use for pull-request review, GitHub Actions implementation, release management, or ordinary code changes that do not include GitHub publication.
---

# GitHub Workflow

## Core Contract

- Mutate GitHub only when the user explicitly asks to create, edit, link, submit, close, or otherwise change an issue or pull request.
- Read repository instructions, contribution guidance, issue forms, pull-request templates, and actual labels before drafting. Treat configured template labels as hints; confirm that they exist and match the issue semantics.
- Preserve the roles of the two artifacts: the issue owns the problem; the pull request owns the implemented change and its verification.
- Publish only information appropriate for the target repository's visibility. Treat links, identifiers, logs, and screenshots from internal systems as non-public unless the user explicitly authorizes publication.
- Preserve unrelated local and remote state. Commit and push only the requested change and only with explicit authorization.

## Workflow

1. Resolve the target repository, base branch, fork or push remote, current branch, worktree state, and requested external mutations.
2. Read the repository-owned templates and contribution rules. Query current labels instead of assuming a template's configured label still exists.
3. Create or update the issue when requested or required by the repository.
4. Review the final diff and verification evidence before committing or pushing. Follow the repository's title, commit, and branch conventions.
5. Create or update the pull request from the repository template.
6. Read the published issue and pull request back from GitHub. Verify their bodies, labels, links, checks, and blocking status.

## Issue Content

- Select the issue type from the actual scope and repository taxonomy. A test utility or infrastructure capability gap may be an enhancement even when its symptom is a panic.
- State the problem with a minimal reproducible input, observed behavior, expected behavior when useful, and a supported basic cause.
- Keep implementation proposals out of the issue unless the user requests them or the selected issue type requires a proposal. A feature-request form may legitimately ask for desired behavior or alternatives.
- Replace internal evidence with a public-safe reproduction. Do not expose private hostnames, dashboard URLs, execution or build identifiers, credentials, customer data, or internal logs in a public repository.
- Use the dedicated repository template when one fits. Preserve required headings without filling optional sections with boilerplate.

## Pull Request Content

- Link the issue using the exact syntax required by the repository, such as `Issue Number: close #123`.
- When the linked issue already explains the problem, do not repeat that description in the pull request's problem section.
- Describe the implemented changes as concise bullet points when there is more than one change or verification addition.
- Report tests that actually ran. Prefer portable commands that reviewers can understand; omit local cache directories, temporary paths, machine-specific toolchain paths, and unrelated failed checks unless they materially affect confidence.
- Answer compatibility, performance, documentation, and release-note sections according to the actual change. Remove template instructions and inapplicable checklist items.

## Publish Markdown Safely

- Prefer `gh issue create|edit --body-file` and `gh pr create|edit --body-file` with a body prepared without shell interpolation.
- Do not place Markdown containing backticks, dollar signs, command substitutions, or multiline content inside an interpolated double-quoted shell argument.
- Ensure the submitted body contains real newline characters. Literal `\n` text is a publication failure.
- Keep issue and pull-request bodies in memory or a temporary file outside the project when they are not intended repository artifacts.

## Post-Publish Verification

Read the created or edited objects back through GitHub before reporting completion:

```bash
gh issue view <issue> --repo <owner/repo> --json url,title,body,labels,state
gh pr view <pr> --repo <owner/repo> --json url,title,body,labels,state,statusCheckRollup
```

Check that:

- Markdown headings, lists, code blocks, and newlines render from the stored body as intended.
- The issue classification and labels match the described scope.
- The pull request links the intended issue and repository automation recognizes the link.
- No internal-only information or local machine paths were published.
- Automated labels and checks do not reveal a formatting or linkage failure.

Correct publication errors promptly within the user's authorized scope. Report the final URLs, branch and commit when relevant, verification results, active checks, and any remaining blocker.

## Boundaries

- Use `code-review` when the user asks to assess a pull request without changing it.
- Use the relevant implementation Skill for code changes; this Skill owns only the GitHub contribution workflow.
- Do not force an issue when the repository and user allow a standalone pull request.
- Do not remove useful standalone PR context when the repository template or user explicitly requires it.
- Do not publish, label, close, merge, or comment beyond the operations the user authorized.
