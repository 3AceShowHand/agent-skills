# Change Classification

## Compatible

A change is compatible when supported upgrades complete without making the application or its critical workflows fail. Existing consumers, data, configuration, and automation continue to work without modification.

Examples:

- Add optional parameters or fields with safe defaults.
- Add configuration keys with defaults while old configurations still load.
- Add signals without removing names or fields consumed by tooling.
- Broaden accepted input while preserving previous behavior.

Checks:

- Critical workflows work before, during, and after the supported upgrade.
- Old callers, clients, configuration, automation, and stored data still work.
- Old and new components can coexist when the rollout model requires it.

## Behavior-Changing

A change is behavior-changing when the upgrade still works but existing users or operators observe different semantics.

Examples:

- Different default timeout, retry, ordering, batching, or error behavior.
- Different validation strictness.
- Different performance or resource behavior that affects operation.
- Changed human-facing output that is not a documented automation contract.

Checks:

- Verify that critical workflows still succeed.
- Document the visible behavior change.
- Consider opt-in behavior, staged activation, or a feature flag.

## Breaking

A change is breaking when a supported upgrade can fail or requires existing consumers, data, configuration, or automation to change before the application works again.

Examples:

- Remove or change a consumed interface without migrating its consumers.
- Rename CLI flags or machine-readable output used by automation.
- Remove configuration keys without aliases or migration.
- Change a protocol, schema, or storage format without compatible readers and writers.
- Rename metrics or labels consumed by dashboards and alerts.
- Change error types, codes, or retryability used by callers.

An internal exported symbol is not a breaking change by itself. Treat it as a compatibility surface only when an actual external, generated, documented, persisted, or cross-version consumer depends on it.

Required mitigations:

- Explicit user direction for an intentional break.
- A migration or compatibility layer.
- A deprecation window when applicable.
- A rollout, rollback, or containment plan.
- Tests for the supported upgrade path and critical workflows.

## Unclear

Classify a change as unclear when actual consumers, persisted state, or supported upgrade behavior cannot be verified.

Rules:

- Inspect more context before implementing.
- State the uncertainty.
- Prefer additive, reversible changes.
- Stop for user direction when the unresolved risk can break a supported upgrade.
