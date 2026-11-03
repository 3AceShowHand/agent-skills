# Unit Test Design Regression Cases

## Name States Behavior, Not the Bug Report

Prompt:

> Rename a test currently called `TestConsumerCheckpointUpdateWhenSomeTasksAreStillWaitingForSchemaBecauseTheyCannotBeDelivered` before merging. The behavior it protects is that a table's first task blocks later tasks of the same table.

Expected:

- Use a short name with subject, condition, and behavior, such as `TestConductorStopsAtFirstUnreadyTask`.
- Drop the narrative, ticket number, and dates from the name.
- Keep the assertions the test already makes; do not change behavior coverage while renaming.

## Assertion a Broken Implementation Also Passes

Prompt:

> Add a test for a fix that drops expired entries from a pending set. The draft asserts `len(pending.items)` equals 2 after the call and reads the private map directly.

Expected:

- Assert the observable result: which entries remain visible or returned, or that the expired key is gone.
- Remove the private-field assertion and the internal count, because an implementation that keeps dead entries in place can still satisfy them.
- Keep the case table-driven if the surrounding tests already use one.

## Existing Case Already Covers the Variant

Prompt:

> Add a new test for rejecting a negative batch size. The package already has a table test over invalid batch sizes that rejects zero and oversized values.

Expected:

- Add a row to the existing table for the negative value.
- Do not add a new test function for the same behavior and setup.
- Leave the existing assertions in place rather than restating them in a second test.

## Time-Dependent Test

Prompt:

> A test asserts that a queued retry happens after the retry interval by sleeping 200 ms and then checking the retry count once.

Expected:

- Wait on the retry signal or poll a bounded condition instead of sleeping a fixed duration.
- Assert the observable retry outcome, not only the count read at one instant.
- Keep the test independent of other tests' timing and shared state.
