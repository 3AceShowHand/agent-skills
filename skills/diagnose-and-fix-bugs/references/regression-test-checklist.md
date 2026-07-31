# Regression Test Checklist

## Test Value

- The test fails before the fix and passes after it when feasible.
- The test checks externally meaningful behavior.
- The test is deterministic or controls timing, randomness, and concurrency.
- The test uses a seam that reproduces the real bug pattern, not a shallower approximation that could pass while the original bug remains.

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

Report why the real bug has no suitable test seam, and include one of:

- Manual reproduction steps.
- Failing command and output.
- Trace or log evidence.
- Follow-up test recommendation.
