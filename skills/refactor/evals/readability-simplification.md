# Readability Simplification Cases

## Correct but Dense Function

Prompt:

> Simplify this function. It is correct but hard to follow; reduce understanding cost without changing behavior.

Expected:

- Remove unnecessary nesting, indirection, state, duplication, abstraction, and comments that restate the code.
- Preserve behavior and repository conventions.
- Do not compress function or control-flow bodies onto one line.
- Keep an idiomatic clause header such as `if err := f(); err != nil` with a multi-line body.
- Reject a shorter version that hides control flow, ownership, or intermediate meaning.

## Aggressive Shortening

Prompt:

> Make this code as short as possible.

Expected:

- Refuse line-count-only shortening when it makes behavior or ownership less clear.
- Keep useful intermediate values and explicit control flow.
- Report the readability tradeoff instead of treating fewer lines as the goal.
