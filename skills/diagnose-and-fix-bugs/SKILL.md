---
name: diagnose-and-fix-bugs
description: Use when diagnosing or fixing bugs, flaky tests, regressions, crashes, data corruption symptoms, production incidents, unexplained behavior, or performance regressions. Builds a tight feedback loop, reproduces and minimizes the failure, tests falsifiable hypotheses, isolates root cause, applies a minimal fix, adds regression coverage, cleans up instrumentation, and reports remaining uncertainty.
---

# Diagnose and Fix Bugs

## Core Contract

- Start with the narrowest reliable pass/fail signal that exercises the reported symptom.
- Scale rigor to difficulty: one strong hypothesis may be enough for an obvious bug; hard bugs need a tighter loop, minimization, and ranked hypotheses.
- Do not make a speculative fix when the failure cannot be reproduced or supported by evidence.
- Fix root cause with the smallest safe change and leave regression coverage or a clear reproduction note.

## Workflow

1. State observed and expected behavior.
2. Build a feedback loop: a test, CLI command, request script, browser check, trace replay, harness, differential run, or human-guided script that can catch this exact failure.
3. Reproduce the issue and minimize the scenario. For flaky bugs, raise and measure the reproduction rate rather than waiting for a perfect repro.
4. Collect evidence and inspect relevant code, tests, environment, versions, and recent changes.
5. Form falsifiable hypotheses. For hard bugs, rank 3–5 and state what observation would confirm or reject each one.
6. Test one variable at a time. Prefer debugger inspection or targeted, uniquely tagged logs; do not log everything.
7. For performance regressions, establish a baseline and use profiling, query plans, traces, or bisection before changing code.
8. Add a failing regression test at the real bug seam before the fix when feasible.
9. Apply the smallest root-cause fix. Avoid unrelated cleanup.
10. Re-run the original feedback loop and regression test, then broaden verification only as risk requires.
11. Remove temporary instrumentation and harnesses. Record the supported root cause, remaining uncertainty, and any architectural gap that prevented good coverage.

## Feedback Loop Standard

For difficult bugs, the loop should be:

- **Specific:** fails on the user's symptom, not a nearby error.
- **Deterministic enough:** repeated runs give a useful verdict; pin time, randomness, network, and filesystem state when possible.
- **Fast:** narrow setup and skip unrelated initialization.
- **Agent-runnable:** automate it; use `scripts/hitl-loop.template.sh` only when human interaction is unavoidable.

If no useful loop can be built, list what was tried and request the missing environment, trace, log, recording, or permission for temporary instrumentation.

## References

- Read `references/debugging-playbook.md` for feedback-loop options, hard-bug branches, instrumentation, and cleanup.
- Read `references/regression-test-checklist.md` before adding regression coverage.
- Use `scripts/hitl-loop.template.sh` only when reproduction requires human actions that cannot be automated.

## Stop Conditions

- The issue cannot be reproduced and the proposed fix is speculative.
- Evidence points to unrelated failures outside the requested scope.
- A fix would change public behavior, data, compatibility, or security without explicit user approval.

## Output Rules

- Separate observed facts, hypotheses, and assumptions.
- Do not claim root cause unless evidence supports it.
- Report the feedback-loop command, results before and after the fix, remaining uncertainty, and skipped checks.
