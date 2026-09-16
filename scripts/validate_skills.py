#!/usr/bin/env python3
"""Validate the repository's skill layout without external dependencies."""

from pathlib import Path
import re
import sys

from generate_skill_index import (
    ENUMS,
    REQUIRED,
    VERSION_RE,
    collect,
    render_json,
    render_markdown,
)

ROOT = Path(__file__).resolve().parents[1]
CATEGORIES = {"common", "personal", "meta"}
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
PLACEHOLDERS = ("skill-name", "Describe what this skill", "Use this skill when ...")


def error(message: str) -> None:
    print(f"ERROR: {message}")


def validate_skill(path: Path) -> int:
    failures = 0
    skill_file = path / "SKILL.md"
    if not NAME_RE.fullmatch(path.name):
        error(f"invalid skill directory name: {path.relative_to(ROOT)}")
        failures += 1
    if not skill_file.is_file():
        error(f"missing SKILL.md: {path.relative_to(ROOT)}")
        return failures + 1

    text = skill_file.read_text(encoding="utf-8")
    if not text.startswith("---\n") or "\n---\n" not in text[4:]:
        error(f"missing YAML frontmatter: {skill_file.relative_to(ROOT)}")
        failures += 1
    else:
        frontmatter = text[4 : text.index("\n---\n", 4)]
        for field in REQUIRED:
            if not re.search(rf"^\s*{re.escape(field)}\s*.+$", frontmatter, re.MULTILINE):
                error(f"missing {field[:-1]} in {skill_file.relative_to(ROOT)}")
                failures += 1
        values = {}
        for line in frontmatter.splitlines():
            if ":" in line:
                key, value = line.split(":", 1)
                values[key.strip()] = value.strip().strip('"\'')
        if values.get("name") != path.name:
            error(f"name does not match directory in {skill_file.relative_to(ROOT)}")
            failures += 1
        category = path.relative_to(ROOT).parts[0]
        if values.get("category") != category:
            error(f"category does not match path in {skill_file.relative_to(ROOT)}")
            failures += 1
        for field, allowed in ENUMS.items():
            if values.get(field) not in allowed:
                error(f"invalid {field} in {skill_file.relative_to(ROOT)}")
                failures += 1
        if values.get("version") and not VERSION_RE.fullmatch(values["version"]):
            error(f"invalid version in {skill_file.relative_to(ROOT)}")
            failures += 1

    for placeholder in PLACEHOLDERS:
        if placeholder in text:
            error(f"unfinished placeholder in {skill_file.relative_to(ROOT)}: {placeholder}")
            failures += 1

    for directory in path.iterdir():
        if directory.is_dir() and not any(directory.iterdir()):
            error(f"empty resource directory: {directory.relative_to(ROOT)}")
            failures += 1

    if path.parts[0] == "common":
        evaluation = path / "examples/evaluation.md"
        if not evaluation.is_file():
            error(f"missing common skill evaluation: {evaluation.relative_to(ROOT)}")
            failures += 1
        else:
            evaluation_text = evaluation.read_text(encoding="utf-8")
            for section in ("## Representative task", "## Boundary task", "Expected:"):
                if section not in evaluation_text:
                    error(f"missing evaluation section in {evaluation.relative_to(ROOT)}: {section}")
                    failures += 1

    for match in re.finditer(r"\[[^\]]+\]\(([^)]+)\)", text):
        target = match.group(1).split("#", 1)[0]
        if target.startswith(("http://", "https://", "mailto:")):
            continue
        resolved = (skill_file.parent / target).resolve()
        if not resolved.exists():
            error(f"broken link in {skill_file.relative_to(ROOT)}: {target}")
            failures += 1
    return failures


def main() -> int:
    failures = 0
    for category in CATEGORIES:
        category_path = ROOT / category
        if not category_path.is_dir():
            error(f"missing category directory: {category}")
            failures += 1
            continue
        for skill_file in sorted(category_path.rglob("SKILL.md")):
            failures += validate_skill(skill_file.parent)
    try:
        records = collect()
        generated = {
            ROOT / "docs/skill-index.md": render_markdown(records),
            ROOT / "data/skills.json": render_json(records),
        }
        for path, expected in generated.items():
            if not path.is_file() or path.read_text(encoding="utf-8") != expected:
                error(f"stale or missing generated file: {path.relative_to(ROOT)}")
                failures += 1
    except ValueError as exc:
        error(str(exc))
        failures += 1
    if failures:
        print(f"Validation failed with {failures} issue(s).")
        return 1
    print("All skills passed validation.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
