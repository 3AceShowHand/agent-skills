# Software Design Checklist

## Required Behavior

- Is the externally visible behavior and success criterion explicit?
- Are non-goals and material constraints clear?
- Does the design solve a current requirement rather than a guessed future use?

## Interface Depth

- Does each interface hide a meaningful decision or implementation complexity?
- Does it reduce what callers need to know?
- Can callers use it correctly without knowing internal sequencing or state?
- Are pass-through methods, parameters, wrappers, or one-use abstractions adding indirection without hiding knowledge?

## Ownership And Information Hiding

- Does every important behavior, state transition, and lifecycle have an owner?
- Are design decisions kept inside the owning module?
- Can storage, protocol, retry, concurrency, or lifecycle details move downward instead of leaking to callers?
- Are public types or configuration exposing internal implementation choices unnecessarily?

## Complexity And Knowledge

- Would a simple behavior change require edits in many places?
- Must readers keep too much distant state or sequencing in mind?
- Do distant modules rely on implicit behavior or hidden coupling?
- Was similar-looking code merged even though it represents different knowledge and changes for different reasons?
- Are related state and behavior close enough to understand without excessive navigation?
- Do similar names and code shapes have similar semantics, side effects, errors, and performance characteristics?

## State, Resources, And Failure

- Are state transitions and invariants explicit?
- Are ownership, lifetime, cancellation, cleanup, and resource bounds clear?
- Can queues, caches, maps, tasks, goroutines, files, or other resources grow without control?
- Can normalization, defaults, idempotency, or empty objects eliminate an avoidable error?
- Are realistic external failures preserved with enough context?
- Can the system appear healthy while accumulating delayed or unrecoverable failure?

## Verification

- Are important behavior, boundaries, and failure paths natural to test through the interface?
- Does testing require excessive setup because implementation decisions leak outward?
- Are tests protecting behavior instead of coupling to internals?
- Are rollout, containment, compatibility, or specialist checks defined where the risk requires them?
