---
name: compatibility-check
description: Use when a change may affect whether existing users can upgrade an application without failures during rollout or after upgrade. Applies to consumed APIs, CLI behavior, configuration, protocols, schemas, storage formats, persisted data, mixed-version operation, metrics or logs used by tooling, and error semantics. Checks that the application and its critical workflows continue to work; do not trigger only because an internal symbol is exported.
---

# Compatibility Check

## Use When

- A change may affect an existing installation during or after an application upgrade.
- A change touches a contract used by external callers, other components, automation, operators, or persisted data.
- Old and new versions may run together during a rolling upgrade.
- The user asks whether an upgrade is safe or backward-compatible.

## Do Not Use When

- The change is private to the repository, all callers change together, and it has no persisted, documented, generated, external, or cross-version effect.
- An exported symbol has no consumer or compatibility promise outside the code being changed.
- The task is a local refactor whose observable behavior remains unchanged.
- Compatibility is not a meaningful risk for the change.

## Workflow

1. Define the supported upgrade path and the critical workflows that must keep working before, during, and after the upgrade.
2. Identify actual consumers, persisted state, deployed components, automation, and compatibility promises. Do not infer a contract from language visibility alone.
3. Inspect only the relevant surfaces: APIs, CLI, configuration, protocols, schemas, storage, persisted data, observability contracts, and error semantics.
4. Check old state and inputs with the new version, and mixed-version or downgrade behavior when the rollout model requires them.
5. Classify each affected contract as compatible, behavior-changing, breaking, or unclear.
6. Prefer additive fields, safe defaults, aliases, adapters, deprecation windows, staged activation, and fallback behavior when they keep upgrades working.
7. Add and run the necessary high-quality tests for the supported upgrade path and critical workflows.

## References

- Read `references/compatibility-surfaces.md` to identify relevant consumers and upgrade surfaces.
- Read `references/change-classification.md` to classify the change and choose mitigations.

## Stop Conditions

- A supported upgrade can make the application or a critical workflow fail.
- Persisted data, configuration, protocols, or mixed-version behavior may be incompatible and the failure cannot be contained.
- Actual consumers or upgrade behavior cannot be inspected for a material-risk change.
- The change intentionally breaks a supported contract without explicit user direction.

## Report

- Supported upgrade path and critical workflows checked.
- Actual consumers, state, and compatibility surfaces inspected.
- Classification and evidence.
- Required migration, fallback, rollout, or containment.
- Tests run and remaining uncertainty.
