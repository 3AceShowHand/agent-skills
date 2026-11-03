# Quality Rubric

Quality is graded, not gating. Grade each area as `good`, `fair`, or `poor`, with one concrete improvement for every area below `good`. A quality grade never blocks approval by itself, and a good grade never compensates for a failed correctness gate.

## Naming

- Function and method names are a verb plus object and state what the function does, not how it does it.
- Variable and field names distinguish things within their scope, and their length matches that scope: short names in a few lines, descriptive names across a file.
- `tmp`, `temp`, and `foo` are defects: they state nothing the reader needs. `data`, `item`, and `result` are acceptable when the role really is generic within a small scope.
- Names of domain concepts match the code, configuration, or API of the project rather than introducing new labels.

## Style

- Formatting comes from the repository tooling and the surrounding files, with no unrelated reordering, re-wrapping, or import churn.
- Local conventions (error style, constructor shape, receiver names, file layout) are followed rather than replaced.

## Complexity

- One job per function: its name states the job in one sentence without "and".
- Nesting stays shallow through early returns and small scopes; related code sits together.
- Use the repository's configured lint thresholds. Do not invent a new line-count or cyclomatic limit for the review.

## Single-component design

- A type has one reason to change; its state and the operations that maintain it live together.
- Only what callers need is exported; helpers stay internal.
- No catch-all manager that owns unrelated state, and no abstraction layer with a single implementation and no near-term second one.
- Parameter re-validation inside an internal function is a defect: point to the type, constructor, or boundary that should have prevented the invalid value. Validation belongs at the system boundary, once.
- Tests must be able to fail on a wrong input or a broken state assertion. A test that passes for that defect is a coverage gap, not evidence.

## Multi-component interaction

- Dependencies point one way; there is no cycle between components.
- Every cross-component path can be drawn as a call chain from entry point to effect.
- Shared state has a named owner and one place that mutates it.
- Failure responsibility across components is defined: who retries, who reports, who degrades.
- One concept keeps one name across the whole change.
- A compatibility fallback or legacy path states when it is removed and who owns the removal. No exit condition grades `poor`.
- A flag carries one meaning. A boolean that means both a predicted limit and a past failure grades `poor`, because no reader can reason from it.

## Comments and tests

- Comments state contracts, invariants, constraints, ownership, or rejected alternatives; they do not narrate code.
- Test names are short and state the behavior; a failing test tells the reader which behavior broke.
