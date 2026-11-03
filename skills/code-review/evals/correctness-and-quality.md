# Correctness Gate and Quality Grade Cases

## Correctness Defect Behind Clean Code

Prompt:

> Review this change. The new scheduler reads well, names are precise, and the package layout is untouched. One path returns a nil error after a failed write, and the caller then reports success.

Expected:

- Verdict: correctness gates fail at error paths, with the failing path named as evidence.
- Severity is High or Critical from the failed gate; the change is not approved.
- Naming and layout are reported as good grades, and they do not offset the failed gate.

## Style Issue Only

Prompt:

> Review this change. Behavior is covered by a test that fails without the change. One helper repeats a five-line setup across three call sites and a local variable is named `tmp`.

Expected:

- Verdict: correctness gates pass, naming and complexity grade `fair` or `poor` with one concrete improvement.
- Severity is Medium or Low; the change is not blocked.
- No gate is invented to justify the quality findings.

## Both Present

Prompt:

> Review this change. A shared map is written from two goroutines without synchronization, and the file also contains a catch-all manager that owns unrelated state. Tests pass locally.

Expected:

- Correctness gates fail at concurrency, with the two-goroutine interleaving named as evidence.
- Quality grading reports the manager as a single-component design defect.
- Gates are reported first and independently of the grades, so the concurrency failure stays blocking.
