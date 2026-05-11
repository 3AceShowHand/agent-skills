---
name: debugging-regression
description: Use when fixing bugs, flaky tests, regressions, crashes, data corruption symptoms, production incidents, or unexplained behavior. Guides reproduction, evidence collection, recent-change analysis, root cause isolation, minimal fixes, regression tests, and honest reporting of remaining uncertainty.
---

# Debugging Regression

## Use When

- The user asks to fix or explain a bug, regression, flaky test, crash, incident, data corruption symptom, or unexplained behavior.
- A failure needs reproduction, isolation, or root cause analysis before code changes.
- A bug fix should leave behind a regression test or clear reproduction note.

## Do Not Use When

- The task is a straightforward feature request with no failing behavior.
- The user only asks for a high-level explanation and no diagnosis is needed.

## Workflow

1. Restate the observed failure and expected behavior.
2. Reproduce the issue with the narrowest command, input, or scenario available.
3. Collect evidence: error text, stack trace, logs, metrics, traces, inputs, environment, recent changes, and affected versions.
4. Inspect relevant code and tests before editing.
5. Form a falsifiable hypothesis.
6. Divide and conquer; change one thing at a time.
7. Fix the root cause with the smallest safe change.
8. Add a regression test or clear reproduction note when feasible.
9. Re-run the narrow reproduction, then broaden verification only as needed.

## References

- Read `references/debugging-playbook.md` for diagnosis steps.
- Read `references/regression-test-checklist.md` before adding regression coverage.

## Stop Conditions

- The issue cannot be reproduced and the proposed fix is speculative.
- Evidence points to unrelated failures outside the requested scope.
- A fix would change public behavior, data, compatibility, or security without explicit user approval.

## Output Rules

- Separate observed facts, hypotheses, and assumptions.
- Do not claim root cause unless evidence supports it.
- Report commands run, results, remaining uncertainty, and skipped checks.
