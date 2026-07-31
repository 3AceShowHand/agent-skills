# Debugging Playbook

## Build a Feedback Loop

Try these seams in roughly this order:

1. A failing unit, integration, or end-to-end test.
2. A CLI, HTTP, or browser script with a focused assertion.
3. A captured trace or request replay.
4. A throwaway harness around the smallest runnable subsystem.
5. A property, fuzz, stress, or repeated-run loop for intermittent failures.
6. An automated bisection or old-versus-new differential check.
7. A human-guided script when interaction cannot be automated.

Tighten the loop before deep investigation: make it faster, more specific, and more deterministic. Capture the exact command, input, config, environment, and failure output.

For flaky bugs, measure a baseline reproduction rate and raise it with repetition, parallelism, stress, or controlled timing. A stable high failure rate is more useful than waiting for certainty.

If reproduction is impossible locally, collect a trace, log, core dump, recording, or enough remote evidence to define a trustworthy pass/fail signal. Do not substitute an unsupported theory.

## Reproduce and Minimize

- Confirm the loop catches the user's exact symptom.
- Remove inputs, callers, config, data, and steps one at a time.
- Keep only elements whose removal makes the failure disappear.
- Preserve the original scenario so the final fix can be checked against it.

## Observe

- Error text.
- Stack trace.
- Logs.
- Metrics.
- Traces.
- Recent changes.
- Inputs and data shape.
- Runtime, OS, dependency versions, config, and feature flags.

## Localize

- Compare expected and actual behavior.
- Identify the first bad state transition.
- Trace ownership and lifecycle of relevant data or resources.
- Check boundary conditions, concurrency, time, retries, IO, and external dependencies.
- Use divide-and-conquer: disable paths, narrow inputs, bisect changes, or isolate modules.

For hard bugs, write 3–5 ranked, falsifiable hypotheses. Each should predict an observation that would confirm or reject it. Test one variable at a time.

Prefer debugger or REPL inspection over added logs. When logs are necessary, make them targeted and tag them with a unique prefix so cleanup is reliable.

For performance regressions, measure a baseline first. Prefer a profiler, query plan, trace, or automated bisection over diagnostic logging.

## Fix

- Fix root cause, not just symptom.
- Make one change at a time.
- Keep fix minimal and reviewable.
- Preserve existing behavior unless the bug is the behavior.
- Avoid opportunistic cleanup.

## Verify

- Run the reproduction after the fix.
- Add or update regression coverage when feasible.
- Run the narrowest relevant test first.
- Broaden only when risk requires it.
- Report any remaining uncertainty.

## Cleanup and Learn

- Remove tagged logs, temporary probes, and throwaway harnesses.
- State the evidence-supported root cause.
- Note what would have prevented the bug.
- If the code has no correct test seam, document that architectural gap after the fix rather than adding a misleading shallow test.
