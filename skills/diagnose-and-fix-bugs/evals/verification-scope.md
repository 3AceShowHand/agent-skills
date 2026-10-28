# Verification Scope Cases

## Existing Coverage Protects a Small Fix

Prompt:

> Add the missing nil guard in this error path. The existing table test already exercises both nil and non-nil observers and fails on the nil case. Keep the fix focused.

Expected:

- Reuse the existing behavioral test and add the guard at the failing boundary.
- Add no duplicate nil-observer tests.
- Select any execution from the actual behavioral uncertainty and repository requirements.

## Test Deletion Resolved by Static Evidence

Prompt:

> Remove this obsolete test. Its only exclusive dependency is an import in the same file; all helper references and build conditions are visible here. No repository rule requires a build or test run.

Expected:

- Remove the test and its newly unused import; inspect remaining helper references.
- Finish verification from sufficient static evidence without running compilation or tests by default.
- Report static verification accurately.

## Uncovered Authorization Behavior Needs a Regression Test

Prompt:

> A missing one-line guard lets suspended users access private records. Existing tests cover active users only. Fix the bug and protect the denied-access behavior.

Expected:

- Add a focused behavioral regression test for suspended users and verify the fix.
- Decide from the uncovered security behavior, regardless of the fix's line count.
- Preserve active-user behavior and avoid unrelated coverage.

## Required Repository Check Remains Required

Prompt:

> Remove an obsolete test. AGENTS.md explicitly requires a package check after every Go edit.

Expected:

- Run the required check and report its actual result.
- Keep additional verification proportional to the remaining risks.
