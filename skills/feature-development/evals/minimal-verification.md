# Minimal Verification Regression Cases

## Static Check Is Sufficient

Prompt:

> Change two log statements to explicitly ignore the return value from `fmt.Fprintf`. The repository offers a package-wide race test target that enables failpoints and a focused linter command.

Expected:

- Confirm the change by reading the edited statements.
- The focused linter is optional for a change this small; running it is not required.
- Run no tests, and do not invoke the package-wide target or enable failpoints.

## Lint Before Commit After a Broad Change

Prompt:

> Change how every sink classifies its URI and register the new collectors at startup. Classifier unit tests and a repository lint target exist. Commit the work when it is complete.

Expected:

- Run the focused unit tests and the lint target once before committing, because the change is broad and its interactions are hard to confirm by reading.
- Do not run integration or failpoint targets locally.
- Report what ran and what remains unverified.

## Runtime Verification Is Necessary

Prompt:

> Change how a CLI redacts a credential before printing a locally constructed diff. Verify that the credential is absent from output.

Expected:

- Run only the specific named test or smallest targeted command that exercises the changed output.
- Do not run every test in the package, multiple packages, a full suite, or a harness that enables failpoints.
- Report any adjacent behavior that remains unverified.

## Explicit Broad Verification Request

Prompt:

> Run the complete unit-test suite with failpoints after making this change.

Expected:

- The explicit request permits the full suite and failpoints.
- State the scope and cost before starting when the command is materially expensive.
