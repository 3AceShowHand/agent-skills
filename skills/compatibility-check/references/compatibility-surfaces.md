# Compatibility Surfaces

Start with the supported upgrade and its critical workflows. Inspect only surfaces that can affect that outcome.

## Application Outcome

- Application availability and startup.
- Critical user and operator workflows.
- Existing resources, jobs, or long-running work.
- Data correctness and progress.
- Rolling-upgrade and mixed-version operation when supported.

Questions:

- What worked before the upgrade and must still work afterward?
- Can the old and new versions coexist for the required rollout window?
- Can a partial upgrade leave the application unavailable, stuck, or inconsistent?
- What evidence proves the upgrade path works?

## Actual Consumers

- External callers and clients.
- Other deployed components or versions.
- Plugins, generated code, scripts, and automation.
- Persisted state read by current or older versions.
- Documented or explicitly promised behavior.

Questions:

- Who or what depends on this contract?
- Does the consumer deploy independently?
- Is the contract documented, generated, persisted, or used across versions?
- Can all consumers change atomically with this repository?

Language visibility alone does not establish a compatibility contract. An exported symbol with no independent consumer or promise may be changed as internal code.

## Code Interfaces

- Consumed APIs, functions, types, interfaces, modules, and extension points.
- Generated APIs.

Questions:

- Do existing callers compile or run unchanged?
- Are aliases, adapters, or a deprecation window needed?

## CLI And Automation

- Flags, arguments, exit codes, stdout, stderr, machine-readable output, and prompts.

Questions:

- Do existing commands and scripts still work?
- Are exit codes or output fields consumed by automation?

## Configuration And Environment

- Configuration keys, defaults, environment variables, feature flags, and validation rules.

Questions:

- Do old configurations still load?
- Are aliases, defaults, or staged activation needed?
- Can stricter validation reject an existing deployment?

## Protocol, Storage, And Schema

- Wire fields, serialization formats, database schemas, files, checkpoints, ordering, and delivery semantics.

Questions:

- Can the new version read existing state?
- Can mixed versions read what each other writes?
- Can partial rollout, downgrade, or rollback corrupt or strand state?

## Observability Contracts

- Metrics, labels, log fields consumed by tooling, trace attributes, alerts, and dashboard queries.

Questions:

- Will existing dashboards, alerts, or automation keep working?
- Are old and new signals available during the upgrade window?

## Errors

- Error types, codes, messages consumed by tooling, and retryability semantics.

Questions:

- Do callers branch or retry based on this error?
- Can changed error behavior make a critical workflow fail or stall?
