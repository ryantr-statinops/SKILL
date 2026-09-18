#!/usr/bin/env python3
"""Inspect a project for agent runtimes and existing skill integration points."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import subprocess
import sys

RUNTIME_DIRS = (".agent", ".agents", ".codex", ".claude")
INSTRUCTION_FILES = (
    "AGENTS.md",
    "CLAUDE.md",
    ".agent/AGENTS.md",
    ".agents/AGENTS.md",
    ".codex/AGENTS.md",
    ".claude/CLAUDE.md",
    ".github/copilot-instructions.md",
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project", type=Path)
    parser.add_argument("--format", choices=("markdown", "json"), default="markdown")
    return parser.parse_args()


def relative_paths(project: Path, paths: list[Path]) -> list[str]:
    return sorted(path.relative_to(project).as_posix() for path in paths)


def inspect(project_arg: Path) -> dict[str, object]:
    project = project_arg.expanduser().resolve()
    if not project.is_dir():
        raise ValueError(f"project directory does not exist: {project}")

    runtime_paths = [project / name for name in RUNTIME_DIRS if (project / name).is_dir()]
    skill_roots = [path / "skills" for path in runtime_paths if (path / "skills").is_dir()]
    instruction_paths = [project / name for name in INSTRUCTION_FILES if (project / name).is_file()]
    skill_paths = {
        root: [path.parent.relative_to(root).as_posix() for path in root.rglob("SKILL.md")]
        for root in skill_roots
    }
    occurrences: dict[str, list[str]] = {}
    for root, skills in skill_paths.items():
        for skill in skills:
            occurrences.setdefault(skill, []).append(root.relative_to(project).as_posix())
    conflicts = {
        skill: sorted(roots) for skill, roots in occurrences.items() if len(roots) > 1
    }
    is_git = (project / ".git").exists()
    if skill_roots:
        recommendation = "selected-sync"
        destination = skill_roots[0].relative_to(project).as_posix()
    elif is_git:
        recommendation = "git-subtree-or-selected-sync"
        destination = ".agent/skills"
    else:
        recommendation = "selected-copy"
        destination = ".agent/skills"
    git_state = "not-a-git-project"
    if is_git:
        result = subprocess.run(
            ["git", "-C", str(project), "status", "--short", "--branch"],
            capture_output=True,
            text=True,
            check=False,
        )
        git_state = result.stdout.strip() if result.returncode == 0 else "git-status-unavailable"
    return {
        "project": str(project),
        "git_repository": is_git,
        "git_state": git_state,
        "runtime_directories": relative_paths(project, runtime_paths),
        "instruction_files": relative_paths(project, instruction_paths),
        "skill_roots": relative_paths(project, skill_roots),
        "existing_skills": {
            root.relative_to(project).as_posix(): sorted(skills)
            for root, skills in skill_paths.items()
        },
        "conflicting_skill_paths": conflicts,
        "recommended_method": recommendation,
        "recommended_destination": destination,
        "validation": [
            "inspect the integration diff",
            "preserve unrelated project instructions",
            "validate selected SKILL.md files and relative resources",
            "run one representative and one boundary task",
        ],
    }


def render_markdown(report: dict[str, object]) -> str:
    lines = [
        "# Integration inspection",
        "",
        f"Project: `{report['project']}`",
        f"Git repository: `{report['git_repository']}`",
        f"Recommended method: `{report['recommended_method']}`",
        f"Recommended destination: `{report['recommended_destination']}`",
        "",
        "## Runtime directories",
        "",
    ]
    lines.extend(f"- `{item}`" for item in report["runtime_directories"] or ["none detected"])
    lines.extend(["", "## Instruction files", ""])
    lines.extend(f"- `{item}`" for item in report["instruction_files"] or ["none detected"])
    lines.extend(["", "## Skill roots", ""])
    lines.extend(f"- `{item}`" for item in report["skill_roots"] or ["none detected"])
    lines.extend(["", "## Conflicts", ""])
    if report["conflicting_skill_paths"]:
        lines.extend(
            f"- `{skill}`: {', '.join(roots)}"
            for skill, roots in report["conflicting_skill_paths"].items()
        )
    else:
        lines.append("- none detected")
    lines.extend(["", "## Validation", ""])
    lines.extend(f"- {item}" for item in report["validation"])
    return "\n".join(lines) + "\n"


def main() -> int:
    args = parse_args()
    try:
        report = inspect(args.project)
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    if args.format == "json":
        print(json.dumps(report, indent=2, ensure_ascii=False))
    else:
        print(render_markdown(report), end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
