# Discovery Checklist

Inspect only what is relevant for the repository.

## Instruction Files

- `AGENTS.md`
- nested `*/AGENTS.md`
- `README*`
- `CONTRIBUTING*`
- `docs/`
- `.github/`

## Command Sources

- `Makefile`
- `justfile`
- `Taskfile.yml`
- `package.json`
- `pnpm-workspace.yaml`
- `yarn.lock`
- `Cargo.toml`
- `go.mod`
- `pyproject.toml`
- `requirements*.txt`
- `tox.ini`
- `noxfile.py`
- `CMakeLists.txt`
- `BUILD`, `BUILD.bazel`, `WORKSPACE`
- CI workflow files
- `scripts/`

## Facts To Extract

- Build commands.
- Unit, integration, e2e, and narrow test commands.
- Lint, format, typecheck, benchmark, and codegen commands.
- Required local services or environment variables.
- Important modules and ownership boundaries.
- Generated files and files that should not be edited manually.
- Public API, config, protocol, storage, schema, metrics, and log compatibility constraints.
- Migration, release, rollback, and observability expectations.
- Project-specific done criteria.

## Evidence Rules

- Prefer commands documented in repo files over guesses.
- If a command is inferred, label it as inferred.
- If several commands exist, record the narrowest routine command and the broader pre-merge command.
- Do not run expensive commands unless the user asks or the task requires it.
