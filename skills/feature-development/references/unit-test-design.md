# Unit Test Design

Use these rules when adding, extending, or renaming unit tests. Test-running scope stays in the `feature-development` entrypoint; whether a regression case is warranted stays in `diagnose-and-fix-bugs`.

## Define the Unit First

- Name the unit under test and the invariant it must hold before writing the test. One test protects one behavior.
- Choose the narrowest real seam that reaches that behavior through the production call path. A shallower approximation can pass while the real path stays broken.
- Test the module that owns the invariant. A caller tests only the contract it owns.
- State the smallest correctness condition the unit must always satisfy, then test that condition rather than the current implementation around it.

## Protect Against Real Failures

- Confirm the test fails for the defect it claims to protect, then passes after the change. A test that also passes on the unfixed code protects nothing.
- Assert observable results: returned values, errors, persisted state, emitted output, or boundary behavior.
- Avoid private fields, internal counts, call order, and other implementation shape. Those assertions fail on refactors instead of on defects.
- Cover the boundary the defect actually changes, such as nil, empty or single element, duplicate, out-of-range, retry exhaustion, cancellation, concurrent access, or partial failure, when the unit owns that boundary.
- Keep the test meaningful: each assertion must be one a broken implementation would violate.

## Reuse Before Adding

- Search existing tests, table cases, helpers, and fixtures for the same behavior. Extend them instead of adding a parallel test.
- Add one table case for a new variant. Add a new test function only for a distinct behavior or a distinct setup.
- Do not repeat assertions a lower-level package already owns. Test the value this unit adds.
- Follow the project's existing test patterns, naming style, and commands; do not introduce a harness for one test.

## Determinism

- Control time, randomness, concurrency, and retries explicitly. Bound or avoid sleeps and wait on a condition instead.
- Prefer real implementations for cheap, local dependencies. Use a stand-in only for slow, external, or unavailable ones, and keep it faithful to the contract it replaces.
- Keep tests independent: no shared mutable state, no dependence on execution order, no reliance on a previous test's side effects.

## Naming and Structure

- Name the test with subject, condition, and expected behavior, such as `TestConductorStopsAtFirstUnreadyTask`.
- Keep names short. Drop bug-report narratives, ticket numbers, dates, and long sentences; the test body and the commit carry that context.
- Keep setup minimal and local. Extract a helper when three or more tests share the same setup and the helper hides no assertion.
- Split a test when its name would need "and", or when one failure cannot tell which behavior broke.
- Make failures diagnosable: report the observed value, the expected value, and the input that produced them.

## Keep the Suite Healthy

- Update or delete a test whose contract no longer exists. Keep no duplicate coverage.
- Add a test for changed behavior or uncovered risk. A small change settled by inspection and existing coverage does not need a new test.
- When no feasible seam exists, report the reproduction and the missing seam instead of shipping a test that cannot fail.
