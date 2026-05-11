# Refactor Playbook

## Plan

- State the current structure and target structure.
- State behavior that must remain unchanged.
- Identify public surfaces and compatibility constraints.
- Identify generated files and code ownership boundaries.
- Decide whether the change can be split into mechanical and semantic commits or steps.

## Safe Step Patterns

- Add new helper or interface without switching callers.
- Migrate one caller or package at a time.
- Keep old path as adapter while migrating.
- Remove old path only after all callers move.
- Keep tests passing at each meaningful step.
- Revert or pause if a step reveals hidden behavior change.

## Keep Separate

- File moves.
- Symbol renames.
- Formatting.
- Feature changes.
- Error behavior changes.
- Logging changes.
- Performance optimizations.
- Dependency updates.

## Compatibility

- Preserve public API unless explicitly changing it.
- Preserve config names, CLI behavior, serialization, metrics, logs consumed by tooling, and error semantics.
- If compatibility changes are needed, use an API compatibility review.
