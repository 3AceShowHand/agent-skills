# Deep Module Checklist

## Interface Depth

- Does the interface hide real complexity?
- Does it reduce what callers need to know?
- Are there too many pass-through methods, parameters, or wrappers?
- Can callers use it correctly without knowing internal sequencing or state?

## Information Hiding

- Are design decisions kept inside the owning module?
- Are storage, protocol, retry, concurrency, or lifecycle details leaking upward?
- Are public types or configs exposing internal implementation choices?

## Complexity Signals

- Change amplification: does a simple behavior change require many edits?
- Cognitive load: must readers keep too much state in mind?
- Hidden coupling: do distant modules rely on implicit behavior?
- Unknown unknowns: are failure modes or ownership boundaries unclear?
- Uncontrolled state growth: can queues, caches, maps, goroutines, files, or tasks grow without bound?
- Delayed failure: can the system appear healthy while accumulating unrecoverable state?

## Error Design

- Can the error be eliminated by normalization, defaults, idempotency, or empty objects?
- Are real external failures preserved with context?
- Are impossible states backed by explicit invariants?

## Tests As Design Feedback

- Do tests need too much setup because the interface is shallow?
- Do tests assert internals instead of behavior?
- Are boundary and failure cases natural to express?
