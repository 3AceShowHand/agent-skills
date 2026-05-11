# Review Rubric

## Severity

- Critical: likely correctness, data loss, security, availability, or severe compatibility issue.
- High: likely bug, production instability, broken API behavior, unsafe migration, or significant test gap.
- Medium: maintainability, complexity, observability, performance, or edge-case risk that should be addressed.
- Low: cleanup or clarity issue that improves maintainability but is not blocking.

## Finding Format

Use this shape when reporting issues:

- Severity:
- Location:
- Issue:
- Why it matters:
- Suggested fix or investigation:

## Review Areas

- User intent and externally visible behavior.
- Correctness and invariants.
- Data structures and expected scale.
- Ownership, lifecycle, cancellation, and cleanup.
- Error handling and retry behavior.
- Concurrency and ordering.
- Compatibility and migrations.
- Tests and regression coverage.
- Observability and operator diagnosis.
- Performance evidence when performance matters.

## Avoid

- Pure style comments unless style affects maintainability or consistency.
- Broad rewrites as review suggestions unless complexity or risk justifies them.
- Findings without evidence.
- Repeating project rules without applying them to the change.
