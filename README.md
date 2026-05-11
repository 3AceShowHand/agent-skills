# Agent Skills

Personal source repository for reusable agent Skills.

## Purpose

This repository is the source of truth for my custom Skills. Skills are maintained here, then installed into supported agents with the `skills` CLI.

## Management Rules

- Skills must be installable through the `skills` CLI.
- Skill bodies should be agent-agnostic unless a Skill explicitly targets one agent.
- Use `agents/` metadata only as optional UI integration. Core behavior belongs in `SKILL.md` and `references/`.
- Keep `SKILL.md` concise. Put longer checklists, templates, and examples in `references/`.

## Skills

- `project-agents-bootstrap`: create or update concise repo-level `AGENTS.md` files.
- `api-compatibility-review`: review compatibility impact before API, config, protocol, storage, metrics, or error-semantic changes.
- `distributed-systems-reliability`: review distributed invariants, progress, failure recovery, control loops, and operability under partial failure.
- `performance-engineering`: guide measured performance optimization and regression analysis.
- `migration-safety`: plan safe schema, data, storage-format, and irreversible state changes.
- `debugging-regression`: reproduce, isolate, fix, and regression-test bugs.
- `refactor-safety`: preserve behavior during refactors, staged rewrites, moves, and interface simplification.
- `observability-readiness`: ensure production changes have useful logs, metrics, traces, alerts, dashboards, and runbook signals.
- `engineering-review`: perform deep code and design review focused on correctness, complexity, interfaces, tests, and failure modes.

## Install

- List installable Skills: `skills add https://github.com/3AceShowHand/agent-skills.git --list`
- Install one Skill globally for one agent: `skills add https://github.com/3AceShowHand/agent-skills.git -g -a <agent> --skill performance-engineering`
- Install all Skills globally for one agent: `skills add https://github.com/3AceShowHand/agent-skills.git -g -a <agent> --skill '*'`
- Install all Skills globally for all supported agents: `skills add https://github.com/3AceShowHand/agent-skills.git -g --agent '*' --skill '*'`
- Example for Codex: `skills add https://github.com/3AceShowHand/agent-skills.git -g -a codex --skill '*'`
