#!/usr/bin/env python3
"""Sync selected skill directories into a project's agent directory."""

from __future__ import annotations

import argparse
from pathlib import Path
import shutil
import sys


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Copy selected SKILLS categories/skills into an agent directory."
    )
    parser.add_argument("destination", type=Path, help="Target skills directory, e.g. project/.agent/skills")
    parser.add_argument(
        "skills",
        nargs="+",
        help="Source paths relative to this repository, e.g. common/git or meta/skill-authoring",
    )
    parser.add_argument(
        "--source",
        type=Path,
        default=Path(__file__).resolve().parents[1],
        help="SKILLS repository root (defaults to this script's repository)",
    )
    parser.add_argument("--check", action="store_true", help="Validate inputs without copying")
    return parser.parse_args()


def resolve_skill(source: Path, relative: str) -> Path:
    path = (source / relative).resolve()
    try:
        path.relative_to(source.resolve())
    except ValueError as exc:
        raise ValueError(f"skill path escapes source repository: {relative}") from exc
    if not path.is_dir():
        raise ValueError(f"skill directory does not exist: {relative}")
    if not (path / "SKILL.md").is_file():
        raise ValueError(f"skill directory has no SKILL.md: {relative}")
    return path


def main() -> int:
    args = parse_args()
    source = args.source.resolve()
    destination = args.destination.resolve()
    if not source.is_dir():
        print(f"error: source repository does not exist: {source}", file=sys.stderr)
        return 2

    try:
        skills = [(relative, resolve_skill(source, relative)) for relative in args.skills]
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    for relative, path in skills:
        target = destination / path.relative_to(source)
        print(f"{'would sync' if args.check else 'syncing'} {relative} -> {target}")
        if not args.check:
            target.parent.mkdir(parents=True, exist_ok=True)
            if target.exists():
                shutil.rmtree(target)
            shutil.copytree(path, target)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
