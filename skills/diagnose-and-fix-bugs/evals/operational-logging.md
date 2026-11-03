# Operational Logging Case

Prompt:

> A Kafka admin path silently skips per-topic metadata errors. Add a warning with the topic and error. Keep the change focused.

Expected:

- Add the warning at the error-handling boundary and preserve the existing return behavior.
- Review the structured log fields and run existing package checks.
- Do not add a unit test that exists solely to assert the log message, level, or fields.
