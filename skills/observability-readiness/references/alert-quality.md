# Alert Quality

## Good Alerts

- Actionable by a human or automation.
- Tied to user impact, data correctness, availability, durability, or operator action.
- Has a clear threshold and time window.
- Includes enough labels to route and diagnose without high cardinality.
- Links to a dashboard or runbook when possible.

## Bad Alerts

- Fires on transient noise without sustained impact.
- Uses high-cardinality labels such as raw user IDs, request IDs, or object names.
- Duplicates another alert without adding routing or diagnosis value.
- Fires on symptoms that cannot be acted on.
- Requires reading source code to understand.

## Review Questions

- What action should the operator take?
- What happens if nobody responds?
- Is there a warning signal before a critical signal?
- Is the alert delayed enough to avoid noise but early enough to prevent damage?
- Can the alert distinguish degraded, failed, and recovering states?
- Does it page only for urgent human action?

## Alert Output

For each new or changed alert, report:

- Condition:
- Threshold:
- Duration:
- Severity:
- Routing:
- Dashboard:
- Runbook or next action:
