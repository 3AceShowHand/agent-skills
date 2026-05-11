# AGENTS.md

Project-specific instructions for this repository.

Keep this file focused on facts that differ from the global `AGENTS.md`.

## Project Commands

- Build:
- Test:
- Narrow test:
- Lint:
- Format:
- Typecheck:
- Benchmark:
- Code generation:

## Repository Layout

- Important modules:
- Generated files:
- Files or directories to avoid editing manually:

## Change Boundaries

- Public APIs:
- Config keys:
- Protocol or storage formats:
- Metrics, logs, or error messages consumed by tooling:
- Dependency rules:

## Verification

- Use the narrowest relevant command first.
- Broaden verification before finalizing risky or cross-module changes.
- If a command is unavailable or too expensive to run, say so explicitly.

## Compatibility And Data Safety

- Preserve existing users, data, configs, protocols, and storage formats unless a breaking change is explicitly requested.
- For migrations or irreversible operations, document rollout, validation, and rollback or containment.

## Observability And Operations

- Preserve or update logs, metrics, traces, dashboards, and alerts when production behavior changes.
- Ensure operators can diagnose progress, failures, retries, backlog, and recovery when relevant.

## Done Criteria

- Relevant tests or checks are run, or skipped with a reason.
- User-visible behavior and compatibility impact are stated.
- Remaining risks or assumptions are reported.
