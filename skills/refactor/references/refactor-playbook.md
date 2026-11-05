# Refactor Playbook

## Plan

- State the current structure and target structure.
- State behavior that must remain unchanged.
- Identify public surfaces and compatibility constraints.
- Identify generated files and code ownership boundaries.
- Decide whether the change can be split into mechanical and semantic commits or steps.

## Readability Simplification

- Optimize for lower understanding cost, not fewer lines.
- Remove unnecessary nesting, indirection, state, duplication, abstraction, and comments that restate the code.
- Preserve behavior and repository conventions.
- Do not compress a function body or a control-flow block onto one line. Keep idiomatic clause headers such as `if err := f(); err != nil` with a multi-line body.
- Reject a shorter version when it hides control flow, ownership, or intermediate meaning.
- Verify behavior is unchanged and compare the resulting structure, not line count alone.

## Safe Step Patterns

- Add new helper or interface without switching callers.
- Migrate one caller or package at a time.
- Keep old path as adapter while migrating.
- Remove old path only after all callers move.
- Verify each meaningful step with the smallest sufficient static or executable evidence.
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
- If compatibility changes are needed, use `compatibility-check`.
