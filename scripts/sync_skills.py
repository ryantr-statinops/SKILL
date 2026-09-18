#!/usr/bin/env python3
"""Sync selected skill directories into a project's agent directory."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import shutil
import sys
import re

from bundles import load_bundle_registry, validate_bundle_registry

MARKDOWN_LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
MANIFEST_NAME = ".skill-sync.json"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Copy selected SKILLS categories/skills into an agent directory."
    )
    parser.add_argument(
        "destination",
        type=Path,
        nargs="?",
        help="Target skills directory, e.g. project/.agent/skills",
    )
    parser.add_argument(
        "skills",
        nargs="*",
        help="Source paths relative to this repository, e.g. common/git or meta/skill-authoring",
    )
    parser.add_argument(
        "--source",
        type=Path,
        default=Path(__file__).resolve().parents[1],
        help="SKILLS repository root (defaults to this script's repository)",
    )
    parser.add_argument("--check", action="store_true", help="Validate inputs without copying")
    parser.add_argument("--bundle", help="sync a named bundle instead of explicit skills")
    parser.add_argument("--list-bundles", action="store_true", help="list available bundles")
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


def load_source_bundles(source: Path) -> list[dict[str, object]]:
    registry_path = source / "data/bundles.json"
    skills_path = source / "data/skills.json"
    try:
        skill_registry = json.loads(skills_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError(f"invalid source skill registry: {skills_path}") from exc
    records = skill_registry.get("skills")
    if not isinstance(records, list):
        raise ValueError(f"invalid source skill registry: {skills_path}")
    try:
        return validate_bundle_registry(load_bundle_registry(registry_path), records)
    except ValueError as exc:
        raise ValueError(f"invalid source bundle registry: {registry_path}: {exc}") from exc


def load_source_skill_records(source: Path) -> list[dict[str, object]]:
    try:
        data = json.loads((source / "data/skills.json").read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError("invalid source skill registry") from exc
    records = data.get("skills")
    if not isinstance(records, list):
        raise ValueError("invalid source skill registry")
    return records


def resolve_bundle(source: Path, identifier: str) -> list[str]:
    for bundle in load_source_bundles(source):
        if bundle["id"] == identifier:
            return list(bundle["skills"])
    raise ValueError(f"unknown bundle: {identifier}")


def resolve_dependencies(source: Path, selected: list[str]) -> list[str]:
    records = {str(record["id"]): record for record in load_source_skill_records(source)}
    ordered: list[str] = []
    visiting: set[str] = set()
    visited: set[str] = set()

    def visit(identifier: str) -> None:
        if identifier in visiting:
            raise ValueError(f"cyclic skill dependency: {identifier}")
        if identifier in visited:
            return
        record = records.get(identifier)
        if record is None:
            raise ValueError(f"skill dependency is missing from registry: {identifier}")
        visiting.add(identifier)
        for required in record.get("requires", []):
            visit(str(required))
        visiting.remove(identifier)
        visited.add(identifier)
        ordered.append(identifier)

    for identifier in selected:
        visit(identifier)
    return ordered


def linked_resources(source: Path, skill: Path) -> list[Path]:
    """Return existing repository files referenced by a skill entrypoint."""
    entrypoint = skill / "SKILL.md"
    resources: list[Path] = []
    for raw_target in MARKDOWN_LINK_RE.findall(entrypoint.read_text(encoding="utf-8")):
        target = raw_target.split("#", 1)[0].strip().strip("<>")
        if not target or target.startswith(("http://", "https://", "mailto:")):
            continue
        resolved = (entrypoint.parent / target).resolve()
        try:
            resolved.relative_to(source.resolve())
        except ValueError as exc:
            raise ValueError(f"linked resource escapes source repository: {target}") from exc
        if not resolved.exists():
            raise ValueError(f"linked resource does not exist: {target}")
        if not resolved.is_relative_to(skill.resolve()):
            resources.append(resolved)
    return resources


def export_targets(source: Path, destination: Path, skills: list[tuple[str, Path]]) -> list[tuple[Path, Path]]:
    targets: dict[Path, Path] = {}
    for relative, path in skills:
        targets[path] = destination / path.relative_to(source)
        for resource in linked_resources(source, path):
            targets[resource] = destination / resource.relative_to(source)
    return sorted(targets.items(), key=lambda item: str(item[1]))


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def manifest_for(
    source: Path,
    bundle: str | None,
    selected: list[str],
    targets: list[tuple[Path, Path]],
) -> dict[str, object]:
    files: list[Path] = []
    for path, _ in targets:
        if path.is_file():
            files.append(path)
        elif path.is_dir():
            files.extend(item for item in path.rglob("*") if item.is_file())
    return {
        "schema_version": 1,
        "source": str(source),
        "bundle": bundle,
        "skills": selected,
        "files": [
            {
                "path": str(path.relative_to(source)),
                "sha256": sha256(path),
            }
            for path in sorted(files)
        ],
    }


def main() -> int:
    args = parse_args()
    source = args.source.resolve()
    if not source.is_dir():
        print(f"error: source repository does not exist: {source}", file=sys.stderr)
        return 2

    try:
        bundles = load_source_bundles(source)
        if args.list_bundles:
            for bundle in bundles:
                print(f"{bundle['id']}\t{bundle['scope']}\t{len(bundle['skills'])} skill(s)")
            return 0
        if args.destination is None:
            raise ValueError("destination is required unless --list-bundles is used")
        if args.bundle and args.skills:
            raise ValueError("--bundle cannot be combined with explicit skills")
        selected = resolve_bundle(source, args.bundle) if args.bundle else args.skills
        if not selected:
            raise ValueError("provide explicit skills or --bundle")
        selected = resolve_dependencies(source, selected)
        destination = args.destination.resolve()
        skills = [(relative, resolve_skill(source, relative)) for relative in selected]
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    targets = export_targets(source, destination, skills)
    conflicts = [str(target) for _, target in targets if target.exists()]
    if conflicts:
        print("error: target paths already exist; no files were changed:", file=sys.stderr)
        for target in conflicts:
            print(f"  {target}", file=sys.stderr)
        return 2

    for path, target in targets:
        relative = path.relative_to(source)
        print(f"{'would sync' if args.check else 'syncing'} {relative} -> {target}")
        if not args.check:
            target.parent.mkdir(parents=True, exist_ok=True)
            if path.is_dir():
                shutil.copytree(path, target)
            else:
                shutil.copy2(path, target)

    if not args.check:
        destination.mkdir(parents=True, exist_ok=True)
        (destination / MANIFEST_NAME).write_text(
            json.dumps(
                manifest_for(source, args.bundle, selected, targets),
                indent=2,
                ensure_ascii=False,
            )
            + "\n",
            encoding="utf-8",
        )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
