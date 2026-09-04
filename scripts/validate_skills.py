#!/usr/bin/env python3

import json
import re
import stat
import sys
from collections import Counter
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
CASES_FILE = ROOT / "tests" / "skill-routing-cases.json"
REMOVED_NAMES = {
    "api-compatibility-review",
    "engineering-review",
    "evolve-skills",
    "refactor-safety",
    "review-self",
}
PROJECT_BOUND_TERMS = {"TiCDC", "ticdc", "changefeed"}
REDUNDANT_PERMISSION_PATTERNS = {
    r"\b(?:you|the agent|codex)\s+(?:can|may)\b": "default capability grant",
    r"\b(?:is|are)\s+(?:allowed|permitted)\b": "permission statement",
    r"\bfeel free to\b": "permission statement",
}
REQUIRED_CASE_IDS = {
    "feature-cross-module-workflow",
    "bug-crash-regression",
    "refactor-module-split",
    "review-local-worktree",
    "review-remote-pr",
    "document-task-list",
    "compat-application-upgrade",
    "design-module-boundary",
    "evolve-user-correction",
    "skills-install-cli",
    "no-skill-known-file-typo",
}


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def load_frontmatter(path: Path, errors: list[str]) -> tuple[dict, str]:
    text = path.read_text(encoding="utf-8")
    match = re.match(r"\A---\n(.*?)\n---\n", text, re.DOTALL)
    if not match:
        fail(errors, f"{path.relative_to(ROOT)}: missing YAML frontmatter")
        return {}, text
    try:
        metadata = yaml.safe_load(match.group(1))
    except yaml.YAMLError as exc:
        fail(errors, f"{path.relative_to(ROOT)}: invalid YAML: {exc}")
        return {}, text
    if not isinstance(metadata, dict):
        fail(errors, f"{path.relative_to(ROOT)}: frontmatter must be a mapping")
        return {}, text
    return metadata, text


def validate_markdown_links(path: Path, errors: list[str]) -> None:
    text = path.read_text(encoding="utf-8")
    for target in re.findall(r"\[[^\]]+\]\(([^)]+)\)", text):
        target = target.strip().split("#", 1)[0]
        if not target or target.startswith(("http://", "https://", "mailto:")):
            continue
        resolved = (path.parent / target).resolve()
        if not resolved.exists():
            fail(
                errors,
                f"{path.relative_to(ROOT)}: broken relative link {target!r}",
            )


def validate_skill(skill_dir: Path, errors: list[str]) -> str:
    skill_name = skill_dir.name
    skill_file = skill_dir / "SKILL.md"
    if not skill_file.is_file():
        fail(errors, f"{skill_dir.relative_to(ROOT)}: missing SKILL.md")
        return skill_name

    metadata, text = load_frontmatter(skill_file, errors)
    if set(metadata) != {"name", "description"}:
        fail(
            errors,
            f"{skill_file.relative_to(ROOT)}: frontmatter must contain only name and description",
        )
    if metadata.get("name") != skill_name:
        fail(
            errors,
            f"{skill_file.relative_to(ROOT)}: name does not match directory {skill_name!r}",
        )
    description = metadata.get("description")
    if not isinstance(description, str) or len(description.strip()) < 40:
        fail(errors, f"{skill_file.relative_to(ROOT)}: description is too short")
    elif any(term in description for term in PROJECT_BOUND_TERMS):
        fail(errors, f"{skill_file.relative_to(ROOT)}: project-bound trigger description")
    if len(text.splitlines()) >= 500:
        fail(errors, f"{skill_file.relative_to(ROOT)}: SKILL.md must stay under 500 lines")
    if "[TODO" in text:
        fail(errors, f"{skill_file.relative_to(ROOT)}: unresolved TODO placeholder")

    agent_file = skill_dir / "agents" / "openai.yaml"
    if not agent_file.is_file():
        fail(errors, f"{skill_dir.relative_to(ROOT)}: missing agents/openai.yaml")
    else:
        agent_text = agent_file.read_text(encoding="utf-8")
        try:
            agent_data = yaml.safe_load(agent_text)
        except yaml.YAMLError as exc:
            fail(errors, f"{agent_file.relative_to(ROOT)}: invalid YAML: {exc}")
            agent_data = {}
        interface = agent_data.get("interface", {}) if isinstance(agent_data, dict) else {}
        for key in ("display_name", "short_description", "default_prompt"):
            if not re.search(rf'^  {key}: ".*"$', agent_text, re.MULTILINE):
                fail(errors, f"{agent_file.relative_to(ROOT)}: {key} must be quoted")
        short_description = interface.get("short_description", "")
        default_prompt = interface.get("default_prompt", "")
        if not 25 <= len(short_description) <= 64:
            fail(
                errors,
                f"{agent_file.relative_to(ROOT)}: short_description must be 25-64 characters",
            )
        if f"${skill_name}" not in default_prompt:
            fail(
                errors,
                f"{agent_file.relative_to(ROOT)}: default_prompt must mention ${skill_name}",
            )

    for markdown_file in skill_dir.rglob("*.md"):
        validate_markdown_links(markdown_file, errors)
        markdown = markdown_file.read_text(encoding="utf-8")
        for pattern, label in REDUNDANT_PERMISSION_PATTERNS.items():
            if re.search(pattern, markdown, re.IGNORECASE):
                fail(
                    errors,
                    f"{markdown_file.relative_to(ROOT)}: {label}; state the required action or prohibition instead",
                )
        for removed_name in REMOVED_NAMES:
            if removed_name in markdown:
                fail(
                    errors,
                    f"{markdown_file.relative_to(ROOT)}: stale Skill name {removed_name!r}",
                )

    for script in (skill_dir / "scripts").glob("*") if (skill_dir / "scripts").is_dir() else []:
        if script.is_file() and ".template." not in script.name:
            if not script.stat().st_mode & stat.S_IXUSR:
                fail(errors, f"{script.relative_to(ROOT)}: script is not executable")

    for forbidden_name in ("README.md", "CHANGELOG.md", "INSTALLATION_GUIDE.md"):
        forbidden = skill_dir / forbidden_name
        if forbidden.exists():
            fail(errors, f"{forbidden.relative_to(ROOT)}: extraneous Skill documentation")

    return skill_name


def validate_readme(skill_names: set[str], errors: list[str]) -> None:
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    match = re.search(r"^## Skills\n(.*?)(?=^## )", readme, re.MULTILINE | re.DOTALL)
    if not match:
        fail(errors, "README.md: missing Skills section")
        return
    listed = set(re.findall(r"^- `([^`]+)`: ", match.group(1), re.MULTILINE))
    if listed != skill_names:
        missing = sorted(skill_names - listed)
        extra = sorted(listed - skill_names)
        fail(errors, f"README.md: Skill inventory mismatch; missing={missing}, extra={extra}")


def validate_routing_cases(skill_names: set[str], errors: list[str]) -> None:
    try:
        cases = json.loads(CASES_FILE.read_text(encoding="utf-8"))["cases"]
    except (OSError, json.JSONDecodeError, KeyError, TypeError) as exc:
        fail(errors, f"{CASES_FILE.relative_to(ROOT)}: invalid routing cases: {exc}")
        return

    positive = Counter()
    negative = Counter()
    seen_ids: set[str] = set()

    for index, case in enumerate(cases, start=1):
        location = f"{CASES_FILE.relative_to(ROOT)} case {index}"
        if not isinstance(case, dict):
            fail(errors, f"{location}: case must be an object")
            continue
        case_id = case.get("id")
        prompt = case.get("prompt")
        expected_behavior = case.get("expected_behavior")
        primary = case.get("expected_primary")
        supporting = case.get("expected_supporting", [])
        excluded = case.get("must_not_trigger", [])

        if not isinstance(case_id, str) or not case_id:
            fail(errors, f"{location}: missing id")
        elif case_id in seen_ids:
            fail(errors, f"{location}: duplicate id {case_id!r}")
        else:
            seen_ids.add(case_id)
        if not isinstance(prompt, str) or not prompt.strip():
            fail(errors, f"{location}: missing prompt")
        if isinstance(case_id, str) and case_id.startswith(("quality-", "evolve-")):
            if not isinstance(expected_behavior, str) or not expected_behavior.strip():
                fail(errors, f"{location}: behavior case requires expected_behavior")
        if primary is not None and primary not in skill_names:
            fail(errors, f"{location}: unknown primary Skill {primary!r}")
        if not isinstance(supporting, list) or not isinstance(excluded, list):
            fail(errors, f"{location}: supporting and excluded values must be lists")
            continue
        named = ([primary] if primary else []) + supporting + excluded
        unknown = sorted({name for name in named if name not in skill_names})
        if unknown:
            fail(errors, f"{location}: unknown Skills {unknown}")
        triggered = ({primary} if primary else set()) | set(supporting)
        overlap = triggered & set(excluded)
        if overlap:
            fail(errors, f"{location}: triggered and excluded overlap {sorted(overlap)}")
        if len(supporting) != len(set(supporting)) or len(excluded) != len(set(excluded)):
            fail(errors, f"{location}: duplicate Skill in a routing list")

        positive.update(triggered)
        negative.update(excluded)

    for skill_name in sorted(skill_names):
        if positive[skill_name] < 3:
            fail(
                errors,
                f"{CASES_FILE.relative_to(ROOT)}: {skill_name} has only {positive[skill_name]} positive cases",
            )
        if negative[skill_name] < 3:
            fail(
                errors,
                f"{CASES_FILE.relative_to(ROOT)}: {skill_name} has only {negative[skill_name]} negative cases",
            )

    missing_required_cases = sorted(REQUIRED_CASE_IDS - seen_ids)
    if missing_required_cases:
        fail(
            errors,
            f"{CASES_FILE.relative_to(ROOT)}: missing required scenarios {missing_required_cases}",
        )

    print(f"routing cases: {len(cases)}")
    for skill_name in sorted(skill_names):
        print(
            f"  {skill_name}: positive={positive[skill_name]}, negative={negative[skill_name]}"
        )


def main() -> int:
    errors: list[str] = []
    skill_dirs = sorted(path for path in SKILLS_DIR.iterdir() if path.is_dir())
    skill_names = {validate_skill(path, errors) for path in skill_dirs}
    validate_readme(skill_names, errors)
    validate_routing_cases(skill_names, errors)

    if errors:
        print("validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(f"validated {len(skill_names)} Skills")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
