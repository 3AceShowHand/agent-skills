# Agent Skills

Personal source repository for reusable agent Skills.

## Purpose

This repository is the source of truth for my custom Skills. Skills are maintained here, then installed into supported agents with the `skills` CLI.

## Management Rules

- Skills must be installable through the `skills` CLI.
- Skill bodies should be agent-agnostic unless a Skill explicitly targets one agent.
- Skill definitions, triggers, and workflows must use reusable engineering concepts. Project-specific details may appear only as examples or test fixtures; they must not define the Skill's scope or required behavior.
- Write only instructions the agent would not reliably infer: required actions and prohibitions. Omit statements that merely grant a default capability or explain what remains allowed after a prohibition.
- Use `agents/` metadata only as optional UI integration. Core behavior belongs in `SKILL.md` and `references/`.
- Keep `SKILL.md` concise. Put longer checklists, templates, and examples in `references/`.

## Skills

- `feature-development`: plan and implement non-trivial features and enhancements with simple design and risk-based verification.
- `codebase-navigation`: trace code structure, ownership, call paths, and change impact with CodeGraph or native search.
- `software-design`: design module boundaries, interfaces, ownership, state, failure models, and deep modules for material structural decisions.
- `code-review`: review local worktrees, remote changes, and designs with correct scope and evidence-backed findings.
- `diagnose-and-fix-bugs`: build a tight feedback loop, isolate root cause, fix, and regression-test bugs.
- `refactor`: preserve behavior during refactors, staged rewrites, moves, and interface simplification.
- `compatibility-check`: ensure applications and critical workflows keep working during and after upgrades.
- `migration-safety`: plan safe schema, data, storage-format, and irreversible state changes.
- `project-agents-bootstrap`: create or update concise repo-level `AGENTS.md` files.
- `distributed-systems-reliability`: review distributed invariants, progress, failure recovery, control loops, and operability under partial failure.
- `performance-engineering`: guide measured performance optimization and regression analysis.
- `observability-readiness`: ensure production changes have useful logs, metrics, traces, alerts, dashboards, and runbook signals.
- `clarity`: keep all original user-facing narrative content direct, precise, concise, and useful.
- `evolve-skills`: turn feedback on agent results, processes, and behavior into minimal, regression-tested Skill improvements.
- `write-great-document`: organize and maintain local Markdown documents, including complete and readable active task lists.

## Install

- List installable Skills: `skills add https://github.com/3AceShowHand/agent-skills.git --list`
- Install one Skill globally for one agent: `skills add https://github.com/3AceShowHand/agent-skills.git -g -a <agent> --skill performance-engineering`
- Install all Skills globally for one agent: `skills add https://github.com/3AceShowHand/agent-skills.git -g -a <agent> --skill '*'`
- Install all Skills globally for Codex and Pi: `skills add https://github.com/3AceShowHand/agent-skills.git -g -a codex pi --skill '*' -y`

## Validate

Run the repository checks and routing-contract cases:

```sh
uv run --with pyyaml python scripts/validate_skills.py
```
