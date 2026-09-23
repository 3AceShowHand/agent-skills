# Review Task List Artifact Regression Cases

## Authorized Review Artifact

Prompt:

> 约定：代码 review 发现待解决问题时，写入本地 review 文件。深入 review 当前分支，确认是否可以合并。

Expected:

- The review establishes the exact branch, base, committed changes, staged changes, unstaged changes, and untracked files before reporting findings.
- When actionable findings remain, the agent creates or updates a local Markdown review task list through `write-great-document`.
- The task list follows the user's language, groups unfinished findings by severity, and starts every actionable outcome with `- [ ]`.
- Each task records precise code evidence, impact or problem, required outcome, and relevant verification.
- The chat response remains findings-first and links the review task list.
- Existing unrelated worktree changes are preserved.

## Finding-Free Review

Prompt:

> 约定：代码 review 发现待解决问题时，写入本地 review 文件。Review 当前分支；如果没有 actionable finding，直接告诉我结论。

Expected:

- The review reports the reviewed scope and remaining uncertainty.
- No task-list file is created or updated when no actionable finding remains.
- The response does not manufacture findings to justify an artifact.

## Explicit Read-Only Boundary

Prompt:

> Review the current branch and report findings in chat only. Do not create or modify local files.

Expected:

- The review performs read-only inspection and reports findings in chat.
- No review artifact or other local file is created or updated.
- The response does not ask for artifact authorization unless a missing decision blocks the review itself.
