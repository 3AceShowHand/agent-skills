# Correctness Gates

Correctness is binary. Each gate below either passes with evidence or fails; a failed or unverified gate blocks approval, and no quality grade offsets it. State the gate result and its evidence in the report.

## Behavior and boundaries

- The change implements the behavior it claims, and the claimed behavior matches the request or the specification.
- Boundary inputs are handled deliberately: nil or zero value, empty, single element, duplicate, out of range, maximum size, partial input, missing optional configuration.
- Falsified by naming one input that returns a wrong result, panics, or silently does nothing.

## Error paths

- Every returned error is handled, wrapped with the context the caller needs, or explicitly ignored with a stated reason.
- A failed operation leaves no partially applied state, and a retry after failure starts from a defined state.
- Falsified by tracing one failing dependency and showing the state that remains.

## Fallbacks and hidden failures

A fallback is a second behavior for a state the code should not have reached. Answer these before accepting one; a failed answer on the first three blocks approval.

- Can internal code produce the state this branch handles? If it can, fix the producer instead of handling the state here.
- Who observes this branch firing? Without a metric, a log with a stable identifier, or a named owner, it is a silent degradation and does not pass.
- Is the failure a capability limit or a data error? They take different responses, and one flag must not represent both.
- A parameter check at the system boundary is not a fallback. Re-validating an already-typed value inside an internal function is a design defect, not a safety net.

Falsified by naming an internal call path that reaches the branch, or by showing the branch firing with nothing recorded.

## Resource and lifecycle

- Every acquisition (`file`, `conn`, `token`, `lock`, `goroutine`, `channel`) pairs with a release on all paths, including error paths.
- Cancellation, timeout, and shutdown have a defined path that stops work; every goroutine has an exit condition.
- Falsified by pointing at a failure or cancellation path where cleanup is skipped or a goroutine cannot exit.

## Concurrency and ordering

- Shared state has one stated synchronization rule, and the rule holds for every access.
- No correctness depends on timing, scheduling, or message arrival order without an explicit mechanism.
- Lock order is stated when more than one lock is held; visibility requirements (`sync`, atomic, channel) are satisfied.
- Falsified by describing two interleavings that produce different outcomes.

## Contracts and compatibility

- Changes to behavior, API, configuration, wire format, or persisted format state their effect on existing consumers and data, or show that no consumer depends on the old behavior.
- Error semantics stay consistent with the surrounding code: the same failure keeps one representation.
- Falsified by naming one consumer, deployment, or stored record whose behavior changes silently.

## Evidence

- The behavior claim is backed by a test that fails on the unfixed code, or by equivalent evidence such as a reproduction, trace, or measurement.
- Missing evidence marks the gate unverified, which counts as not passed. Do not infer a pass from reading alone when the claim is about runtime behavior.
- Falsified by running the claimed evidence against the pre-change code and seeing it pass.
