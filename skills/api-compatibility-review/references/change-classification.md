# Change Classification

## Compatible

A change is usually compatible when old callers, old data, old configs, and old automation continue to work without modification.

Examples:

- Add optional API parameters with safe defaults.
- Add optional response fields that old clients ignore.
- Add config keys with defaults.
- Add metrics without removing or renaming old metrics.
- Broaden accepted input while preserving old behavior.

Checks:

- Old callers compile or run unchanged.
- Old configs still load.
- Old stored data still reads.
- Old automation still parses expected output.

## Behavior-Changing

A change is behavior-changing when existing callers still work mechanically but observe different semantics.

Examples:

- Different default timeout, retry, ordering, batching, or error behavior.
- Changed log text used by humans but not documented as tooling input.
- Different validation strictness.
- Different performance characteristics that can affect operators.

Checks:

- Document visible behavior changes.
- Add tests for old and new semantics when feasible.
- Consider feature flags, opt-in behavior, or staged rollout.

## Breaking

A change is breaking when existing users, data, configs, protocols, or automation require changes.

Examples:

- Rename or remove public symbols.
- Rename CLI flags or change machine-readable output.
- Remove config keys without aliases.
- Change wire protocol or storage format without compatibility layer.
- Rename metrics or labels consumed by dashboards or alerts.
- Change error types or messages consumed by callers or tests.

Required mitigations:

- Explicit user approval.
- Migration or compatibility layer.
- Deprecation plan when possible.
- Rollback or containment plan.
- Tests for old, new, and mixed behavior when relevant.

## Unclear

Classify as unclear when the boundary or consumers cannot be verified.

Rules:

- Inspect more context before implementing.
- State the uncertainty.
- Prefer additive, reversible changes.
- Ask before proceeding if risk is meaningful.
