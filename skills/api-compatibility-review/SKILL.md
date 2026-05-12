---
name: api-compatibility-review
description: Use before changing public APIs, exported functions, CLI behavior, config names, protocol fields, storage formats, schemas, metrics, logs consumed by tooling, or error semantics. Prefer this Skill directly when compatibility is the dominant review risk; otherwise `engineering-review` may triage first and route here. Reviews callers, compatibility impact, migration paths, tests, versioning, defaults, deprecation, mixed-version behavior, and rollback risk.
---

# API Compatibility Review

## Use When

- A change touches public APIs, exported functions, CLI flags or output, config names, protocol fields, storage formats, schemas, metrics, logs consumed by tooling, or error semantics.
- The boundary is unclear and the change might affect external users, persisted data, automation, or mixed-version deployments.
- The user asks whether a change is backward-compatible.

## Do Not Use When

- The change is clearly private to one function and has no external, persisted, generated, documented, or cross-version surface.
- The task is only a local refactor and public behavior is unchanged.
- The right first step is a broad engineering review because the dominant risk area is still unclear.

## Workflow

1. Identify the compatibility surface and the old contract.
2. Inspect callers, tests, docs, generated code, release notes, config examples, schemas, and usage hints.
3. Classify the change as compatible, behavior-changing, breaking, or unclear.
4. Prefer compatibility-preserving designs: additive fields, defaults, aliases, adapters, deprecation windows, feature flags, and fallback behavior.
5. Check mixed-version, downgrade, rollback, invalid input, and old-client behavior when relevant.
6. Require explicit user confirmation before implementing a breaking change.
7. Add or update tests for old behavior, new behavior, compatibility boundaries, and error cases when feasible.

## References

- Read `references/compatibility-surfaces.md` to identify relevant surfaces.
- Read `references/change-classification.md` to classify the change and choose mitigations.

## Stop Conditions

- The change may break persisted data, wire compatibility, config compatibility, CLI automation, or public callers and the user did not ask for a breaking change.
- Existing callers or compatibility impact cannot be inspected.
- Migration, rollback, or mixed-version behavior is unknown for a risky change.

## Report

- Surface changed.
- Classification and evidence.
- Callers or users inspected.
- Compatibility risks.
- Migration or fallback plan.
- Tests added or still needed.
