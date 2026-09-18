#!/usr/bin/env python3
"""Load and validate the explicitly promoted skill set."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
PROMOTION_SCHEMA_VERSION = 1


def load_promotion_registry(path: Path | None = None) -> dict[str, Any]:
    registry_path = path or ROOT / "data/promoted.json"
    try:
        data = json.loads(registry_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError(f"invalid promotion registry: {registry_path}") from exc
    if not isinstance(data, dict):
        raise ValueError("promotion registry must be an object")
    return data


def validate_promotion_registry(
    data: dict[str, Any],
    skill_records: list[dict[str, str]],
    bundles: list[dict[str, Any]],
    root: Path | None = None,
) -> list[str]:
    if data.get("schema_version") != PROMOTION_SCHEMA_VERSION:
        raise ValueError(
            f"unsupported promotion schema version: {data.get('schema_version')}"
        )
    promoted = data.get("skills")
    if not isinstance(promoted, list):
        raise ValueError("promotion registry skills must be a list")
    if any(not isinstance(identifier, str) for identifier in promoted):
        raise ValueError("promoted skill IDs must be strings")
    if len(set(promoted)) != len(promoted):
        raise ValueError("duplicate promoted skill")

    records = {record["id"]: record for record in skill_records}
    bundled = {member for bundle in bundles for member in bundle["skills"]}
    source_root = root or ROOT
    for identifier in promoted:
        record = records.get(identifier)
        if record is None:
            raise ValueError(f"promoted skill does not exist: {identifier}")
        if record.get("status") != "stable":
            raise ValueError(f"promoted skill is not stable: {identifier}")
        if not str(record.get("description", "")).strip():
            raise ValueError(f"promoted skill is undocumented: {identifier}")
        if identifier not in bundled:
            raise ValueError(f"promoted skill is not in a supported bundle: {identifier}")
        skill_path = source_root / identifier
        if not (skill_path / "SKILL.md").is_file():
            raise ValueError(f"promoted skill is missing SKILL.md: {identifier}")
        if not (skill_path / "examples/evaluation.md").is_file():
            raise ValueError(f"promoted skill is missing evaluation: {identifier}")
        if record.get("invocation") not in {"user", "model", "both"}:
            raise ValueError(f"promoted skill has invalid invocation: {identifier}")
    return list(promoted)


def load_and_validate_promotions(
    skill_records: list[dict[str, str]],
    bundles: list[dict[str, Any]],
    path: Path | None = None,
    root: Path | None = None,
) -> list[str]:
    return validate_promotion_registry(
        load_promotion_registry(path), skill_records, bundles, root=root
    )
