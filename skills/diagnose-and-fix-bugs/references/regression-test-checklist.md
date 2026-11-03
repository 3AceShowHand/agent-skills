# Regression Test Checklist

## Test Value

- Identify the uncovered behavior and the invariant's owner. Reuse existing coverage when it already protects the changed behavior.
- The test fails before the fix and passes after it when feasible.
- The test checks externally meaningful behavior.
- The test is deterministic or controls timing, randomness, and concurrency.
- The test uses a seam that reproduces the real bug pattern, not a shallower approximation that could pass while the original bug remains.
- A change limited to operational logging does not need a new unit test for log messages, levels, or fields. Review the log call and use existing checks.

## Case Selection

- Original failing input or scenario.
- Boundary case that triggered the bug.
- Error path or invalid input when relevant.
- Concurrency, retry, timeout, or lifecycle case when relevant.
- Compatibility case when the bug affected public behavior.

## Test Quality

Naming, structure, assertions, reuse, and determinism are owned by `feature-development` in `references/unit-test-design.md`. Apply those rules when writing the case.

## When A Test Is Not Feasible

Report why the real bug has no suitable test seam, and include one of:

- Manual reproduction steps.
- Failing command and output.
- Trace or log evidence.
- Follow-up test recommendation.
