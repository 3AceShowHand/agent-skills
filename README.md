# Agent Skills

Personal source repository for reusable agent Skills.

## Management Rules

- This repository is the source of truth for all custom Skills.
- Skills must be installable through the `skills` CLI.
- Skill bodies should be agent-agnostic; avoid agent-specific assumptions unless the Skill explicitly targets one agent.
- Use `agents/` metadata only as optional UI integration. Core behavior belongs in `SKILL.md` and `references/`.
- Keep `SKILL.md` concise. Put longer checklists, templates, and examples in `references/`.

## Skills

- `project-agents-bootstrap`: create or update concise repo-level `AGENTS.md` files.
- `api-compatibility-review`: review compatibility impact before API, config, protocol, storage, metrics, or error-semantic changes.
- `distributed-systems-reliability`: review distributed invariants, progress, failure recovery, control loops, and operability under partial failure.
- `performance-engineering`: guide measured performance optimization and regression analysis.
- `debugging-regression`: reproduce, isolate, fix, and regression-test bugs.
- `engineering-review`: perform deep code and design review focused on correctness, complexity, interfaces, tests, and failure modes.

## Install

- List installable Skills: `skills add /Users/edison/workspace/agent-skills --list`
- Install one Skill globally for Codex: `skills add /Users/edison/workspace/agent-skills -g -a codex --skill performance-engineering`
- Install one Skill globally for another agent: replace `codex` with the target agent name, such as `claude-code` or `cursor`.
- Install all Skills globally for one agent: `skills add /Users/edison/workspace/agent-skills -g -a codex --skill '*'`
- Install all Skills globally for all supported agents: `skills add /Users/edison/workspace/agent-skills -g --agent '*' --skill '*'`
