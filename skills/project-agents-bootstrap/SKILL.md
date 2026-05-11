---
name: project-agents-bootstrap
description: Use when creating, updating, auditing, or standardizing a repository-level AGENTS.md. Helps discover project-specific build, test, lint, benchmark, codegen, layout, generated-file, dependency, compatibility, observability, release, migration, and done-criteria instructions without duplicating global rules or inventing commands.
---

# Project AGENTS Bootstrap

## Use When

- The user asks to create, improve, audit, or standardize a repo-level `AGENTS.md`.
- A repo lacks project-specific instructions for build, test, lint, benchmark, code generation, generated files, module boundaries, or done criteria.
- The user wants global `AGENTS.md` rules complemented by repo-specific rules.

## Do Not Use When

- The task only needs a one-off command explanation.
- The user asks for general coding rules rather than repo-specific instructions.
- The repo already has clear instructions and the user is not asking to change them.

## Workflow

1. Inspect existing instructions: root and nested `AGENTS.md`, README files, contributing docs, CI configs, build files, scripts, package manifests, and Makefiles.
2. Identify command facts: build, test, lint, format, benchmark, codegen, local services, and narrow test commands.
3. Identify repo constraints: important modules, generated files, dependency rules, public API boundaries, data or migration rules, observability expectations, and release requirements.
4. Draft only project-specific instructions; do not repeat global behavior rules.
5. Keep instructions short, concrete, and verifiable.
6. Mark uncertain commands, conventions, or ownership as assumptions instead of inventing them.
7. If editing an existing `AGENTS.md`, preserve useful local rules and remove only duplication introduced by the current edit.

## References

- Read `references/discovery-checklist.md` when inspecting a repo.
- Read `references/repo-agents-template.md` when drafting or rewriting a repo-level `AGENTS.md`.

## Output Rules

- Include discovered commands and where they came from.
- Separate verified facts from assumptions.
- Prefer narrow commands for routine verification.
- Do not add broad architecture documentation unless the user asks.
- Do not add project rules that cannot be supported by local evidence.
