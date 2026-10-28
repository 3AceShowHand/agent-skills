# Test Ownership Cases

## Helper Behavior Already Has Owner Coverage

Prompt:

> Review a caller that records delivery metrics. The statistics package already tests its Close cleanup, idempotence, and closed-state behavior. The caller receives a borrowed statistics object and owns only delivery confirmation.

Expected:

- Review delivery-confirmation invariants in the caller.
- Request no repeated tests of statistics cleanup or caller-owned disposal of the borrowed object.

## Caller Owns Resource Lifetime

Prompt:

> Review a caller that creates its own observer and promises to release it after either successful shutdown or initialization failure. The observer package already tests Close internals.

Expected:

- Review the caller's responsibility to release its observer on both paths.
- Identify missing caller lifecycle coverage when it leaves a real invariant unprotected.
- Keep assertions about Close internals in the observer package.
