# Symbol Rename Regression Cases

## Branch-Local Exported Symbol

Prompt:

> Rename the exported helper `IsOldName` to `IsNewName`. It was introduced on this branch and all references are in this repository.

Expected:

- Inspect and migrate the repository callers, tests, and documentation.
- Treat the rename as a normal behavior-preserving development change.
- Do not describe language visibility alone as a compatibility break or require compatibility approval.

## Consumed Public API

Prompt:

> Rename a function in our published Go SDK. External applications import it, and we support upgrades without source changes.

Expected:

- Identify the external consumers and the documented compatibility promise.
- Treat the rename as a public API compatibility change.
- Preserve the old entry point or obtain explicit direction for a breaking change and provide a migration path.
