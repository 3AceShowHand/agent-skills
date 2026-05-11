# Regression Test Checklist

## Test Value

- The test fails before the fix or clearly covers the failing scenario.
- The test checks externally meaningful behavior.
- The test is deterministic or controls timing, randomness, and concurrency.
- The test is focused on the owning module or boundary.

## Case Selection

- Original failing input or scenario.
- Boundary case that triggered the bug.
- Error path or invalid input when relevant.
- Concurrency, retry, timeout, or lifecycle case when relevant.
- Compatibility case when the bug affected public behavior.

## Test Quality

- Clear name that describes behavior.
- Minimal setup.
- Stable assertions.
- No sleeps unless time is explicitly controlled or bounded.
- No dependency on unrelated external services unless the test is intentionally integration-level.

## When A Test Is Not Feasible

Report why, and include one of:

- Manual reproduction steps.
- Failing command and output.
- Trace or log evidence.
- Follow-up test recommendation.
