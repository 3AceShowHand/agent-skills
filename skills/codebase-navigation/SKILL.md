---
name: codebase-navigation
description: Use when understanding an unfamiliar codebase, tracing architecture, data flow, or control flow, locating definitions, callers, or callees, identifying ownership boundaries, building a reading path, or analyzing change impact. Use CodeGraph only when its tools are available and the repository already has an index; otherwise use file listing, rg, and exact reads. Do not use for a simple known-file edit, an exact literal lookup alone, or external library documentation.
---

# Codebase Navigation

## Core Contract

- Answer structural questions from the smallest trustworthy set of repository evidence.
- Explain code behavior from the authoritative implementation in the exact revision or artifact in scope, tracing from its entry point to the relevant state or data change and effective configuration.
- Prefer an existing structural index when it is available and appropriate; otherwise continue with native search and exact reading without blocking.
- Build a guided reading path that explains why each location matters.
- Stop when the requested structure or impact is clear. Do not repeat the same query through a second tool merely for reassurance.

## Choose The Route

- Use CodeGraph for definitions, signatures, callers, callees, impact, architecture, feature flow, and bug context only when the tools are available and the repository is already indexed.
- Use `rg --files` and `rg -n` for file discovery, exact text, configuration keys, error strings, known symbols, and narrowing candidate locations.
- Use exact file reads after search identifies a relevant location or when the user already named the file.
- Use the applicable documentation Skill or official source for external libraries, frameworks, SDKs, APIs, CLIs, and cloud services.

If CodeGraph is missing, reports that the repository is not initialized, or lacks the required result, fall back immediately to native search and reads. Do not retry it repeatedly, ask the user to create an index, or initialize one without an explicit request.

## Workflow

1. Read repository instructions and identify the question: entry point, ownership, call path, state flow, behavior, or change impact.
2. Start with the narrowest route that can answer it.
3. Locate entry points and authoritative definitions before reading implementation details.
4. Follow callers, callees, data transformations, state transitions, configuration, and tests only as far as the question requires.
5. For stateful or concurrent behavior, identify ownership, lifecycle, cancellation, retries, cleanup, and partial-failure boundaries.
6. For change impact, identify direct consumers first, then persisted, generated, documented, external, and cross-version contracts when relevant.
7. For cross-version behavior, trace the equivalent path and effective configuration in every exact revision being compared, including renamed, moved, inline, or replaced implementations. A missing commit, file, or symbol does not prove that the behavior is absent.
8. Cross-check claims only when evidence conflicts, a result is ambiguous, or risk requires an independent source.
9. Return the reading path, relationships, affected scope, evidence, and unresolved facts.

## Boundaries

- Do not infer architecture from filenames alone.
- Do not use commit messages, history, or symbol presence as a substitute for reading the implementation that produced the behavior.
- Do not read the whole repository when targeted structural queries or searches are sufficient.
- Do not initialize, rebuild, or mutate a code index without explicit direction.
- Do not use CodeGraph for a simple literal search or exact known-file edit.
- Do not use external documentation tools for repository-owned business logic.
- Do not turn navigation into implementation or review unless the user requested that broader task.

## Report

- Best entry points and why they matter.
- Key definitions, callers, callees, and data or state flow.
- Ownership and module boundaries.
- Files and behaviors likely affected by a change.
- Evidence used and any unresolved uncertainty.
