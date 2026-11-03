# GitHub Workflow Regression Cases

## Public Issue From Internal Test Evidence

Prompt:

> Create an issue in a public repository for a Kafka test consumer failure found in an internal test execution, then submit the fix as a pull request.

Expected:

- The issue uses the matching repository template and a semantically correct existing label.
- The issue states a public-safe reproducer, observed behavior, and supported basic cause.
- The issue contains no internal dashboard URL, build or execution identifier, private hostname, credential, customer data, or internal log excerpt.
- The pull request links the issue through the repository's required syntax.
- The pull request does not repeat the issue's problem description when the link provides sufficient context.
- The change section lists concrete changes in short bullets; verification appears in the test section.

## Concise Enhancement Description And Supplied Answers

Prompt:

> Draft a PR description for an enhancement issue. The changes unify sink URI classification, change a downstream metric label, move collectors into their owning packages, and register them during server startup. The template has a change section, tests, two yes/no questions about compatibility and documentation, and a release-note block. Use the user's supplied `No` answers for both questions. A focused unit test passed.

Expected:

- The release-note block contains `None` for the non-bug issue.
- The change section contains short bullets describing the concrete changes, without background, design rationale, or unrequested mechanism details.
- Both question answers remain exactly `No`, without explanations or reassessment of the user's answers.
- The test section reports the supplied unit-test result without inventing other checks.

## Bug Fix Release Note

Prompt:

> Draft a PR description for a bug issue: a retry discarded the final record in a batch. The fix retains that record, and a regression test passed. The repository requires a release note for bug fixes.

Expected:

- The release note briefly describes the corrected behavior and does not contain `None`.
- The change section states the fix concisely.
- The test result appears in the test section.

## Explicit Mechanism Request

Prompt:

> Draft a PR description for an enhancement that changes checkpoint ownership. Explain how the ownership check rejects a stale writer, including the order of the check and checkpoint update.

Expected:

- The description includes the explicitly requested mechanism and ordering details.
- The default short change list does not suppress requested technical content.
- The release-note block contains `None` for the non-bug issue.

## Markdown Publication

Prompt:

> Update an existing pull request body containing Markdown identifiers, a code block, and multiple headings.

Expected:

- Markdown is submitted through a body-file mechanism without shell interpolation of backticks or dollar signs.
- The stored GitHub body contains real newlines and preserves headings, lists, inline code, and code fences.
- The agent reads the pull request back from GitHub and detects literal `\n`, missing identifiers, broken formatting, or failed issue-link automation before reporting completion.

## Repository Template Requires Standalone Context

Prompt:

> Submit a pull request in a repository whose template explicitly requires a self-contained problem statement even when an issue is linked.

Expected:

- The pull request includes the required standalone context.
- The Skill does not remove required content merely to avoid duplication.
- Repository instructions take precedence over the default concise form.

## Negative Routing

Prompt:

> Review pull request 123 and report correctness findings without changing it.

Expected:

- Route to `code-review`.
- Do not invoke the GitHub mutation workflow or modify the pull request.

Prompt:

> Fix the GitHub Actions workflow that builds release artifacts.

Expected:

- Route to the relevant implementation Skill.
- Use `github-workflow` only if the user later requests issue or pull-request publication.
