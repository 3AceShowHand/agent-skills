# Compatibility Surfaces

Check only surfaces relevant to the change.

## Code Interfaces

- Public APIs.
- Exported functions, types, traits, classes, interfaces, and modules.
- Plugin or extension points.
- Generated APIs.

Questions:

- Who calls this?
- Is it documented?
- Is it imported outside the package or module?
- Does generated code depend on it?

## CLI And Automation

- Flags.
- Arguments.
- Exit codes.
- Stdout and stderr.
- Machine-readable output.
- Interactive prompts.

Questions:

- Could scripts parse this output?
- Are exit codes tested or documented?
- Do old flags still work?

## Config And Environment

- Config keys.
- Defaults.
- Environment variables.
- Feature flags.
- Validation rules.

Questions:

- Do old configs still load?
- Are aliases or defaults needed?
- Is stricter validation safe for existing users?

## Protocol, Storage, And Schema

- Wire fields.
- Serialization formats.
- Database schemas.
- File formats.
- Checkpoints.
- Message ordering or delivery semantics.

Questions:

- Can old versions read new data?
- Can new versions read old data?
- What happens in mixed-version deployments?
- Is downgrade or rollback safe?

## Observability

- Metrics names.
- Metric labels.
- Log fields consumed by tooling.
- Trace attributes.
- Alert expressions.
- Dashboard queries.

Questions:

- Will dashboards or alerts break?
- Does cardinality change?
- Are old and new signals available during migration?

## Errors

- Error types.
- Error codes.
- Error messages used by callers or tests.
- Retryability semantics.

Questions:

- Do callers branch on this error?
- Did retryability change?
- Does the message need compatibility because tests or tools parse it?
