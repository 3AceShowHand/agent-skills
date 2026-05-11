# Characterization Tests

Use characterization tests to lock down existing behavior before refactoring.

## When To Add

- Existing tests are weak or absent.
- Behavior is subtle or historically bug-prone.
- The refactor changes ownership, lifecycle, parsing, serialization, ordering, or error paths.
- Public behavior must be preserved but is not clearly specified.

## What To Test

- Current public behavior.
- Boundary inputs.
- Error cases.
- Ordering or lifecycle behavior.
- Compatibility-sensitive outputs.
- Known bug-regression cases.

## Test Rules

- Test behavior, not implementation details.
- Keep setup minimal.
- Prefer existing test style and helpers.
- Avoid snapshotting large unstable outputs.
- Name the behavior being preserved.
- Do not bless known-bad behavior unless preserving it is required for compatibility; document that constraint.

## If Tests Are Not Feasible

Record one of:

- Manual characterization steps.
- Existing command output.
- Before/after diff of public output.
- Reason coverage cannot be added now.
