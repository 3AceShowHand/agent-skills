# Minimal Verification Regression Cases

## Static Check Is Sufficient

Prompt:

> Change two log statements to explicitly ignore the return value from `fmt.Fprintf`. The repository offers a package-wide race test target that enables failpoints and a focused linter command.

Expected:

- Make the local edit and use inspection, formatting, or the focused linter when verification is useful.
- Run no tests because the static checks cover the change.
- Do not invoke package-wide or broader test targets and do not enable failpoints.

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
