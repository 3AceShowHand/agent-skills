# Debugging Playbook

## Reproduce

- Prefer the narrowest deterministic reproduction.
- Capture exact command, input, config, environment, and failure output.
- If reproduction is flaky, estimate frequency and collect multiple samples.
- If reproduction is impossible locally, collect enough evidence to define a remote or theoretical reproduction path.

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
