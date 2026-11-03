# Review Rubric

## Severity

Severity follows the standard that owns the issue, and the two standards do not trade against each other:

- Critical: a failed gate from `correctness-gates.md` with data loss, security, availability, or severe compatibility impact.
- High: any other failed or unverified gate from `correctness-gates.md`. Blocking.
- Medium: a quality grade below `good` from `quality-rubric.md` that costs maintainability, on a change whose gates pass.
- Low: isolated clarity or cleanup issue. Never blocking on its own.

## Verdict

State the outcome as two separate results:

- Correctness gates: passed, failed, or unverified, naming each gate and its evidence.
- Quality grades: `good`, `fair`, or `poor` per area with one improvement for anything below `good`.

Do not compute a total score, and do not let a good quality grade compensate for a failed gate or an unverified behavior claim.

## Finding Format

Use this shape when reporting issues:

- Gate or area:
- Severity:
- Location:
- Issue:
- Why it matters:
- Evidence:
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
- Reporting a quality grade as a blocker, or a failed gate as a style note.
- Broad rewrites as review suggestions unless complexity or risk justifies them.
- Findings without evidence.
- Repeating project rules without applying them to the change.
- Filling the report with low-value suggestions when no actionable issue exists.
