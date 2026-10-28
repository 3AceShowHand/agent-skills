# Mechanical Refactor Cases

## Local Rename with Complete Static Evidence

Prompt:

> Rename the local variable stat to stats in this function. All references are visible, stats is not bound in any affected scope, and no repository rule requires execution checks.

Expected:

- Change only the declaration and references bound to it.
- Inspect scope, shadowing, and the resulting diff.
- Complete verification from static evidence without requiring compilation or tests.

## Cross-Platform Move Leaves an Unresolved Boundary

Prompt:

> Move this function to another package without changing behavior. Its callers include generated files and platform-specific build variants; some variants have different type aliases.

Expected:

- Inspect generated consumers, build constraints, and type relationships.
- Use a focused type, compilation, or behavioral check if static evidence leaves a concrete uncertainty.
- Preserve required repository checks and report unsupported variants accurately.
