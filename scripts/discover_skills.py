#!/usr/bin/env python3
"""Find candidate skills from the generated machine-readable registry."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
TOKEN_RE = re.compile(r"[a-z0-9]+")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("query", nargs="*", help="outcome or keywords to match")
    parser.add_argument("--category", choices=("common", "personal", "meta"))
    parser.add_argument("--scope", choices=("universal", "personal", "repository"))
    parser.add_argument(
        "--status",
        choices=("draft", "experimental", "stable", "deprecated"),
    )
    parser.add_argument("--limit", type=int, default=10)
    parser.add_argument("--format", choices=("markdown", "json"), default="markdown")
    return parser.parse_args()


def load_registry() -> list[dict[str, str]]:
    path = ROOT / "data/skills.json"
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
        skills = data["skills"]
        if not isinstance(skills, list):
            raise TypeError("skills is not a list")
        return skills
    except (OSError, KeyError, TypeError, json.JSONDecodeError) as exc:
        raise ValueError(f"invalid generated registry: {path.relative_to(ROOT)}") from exc


def tokens(value: str) -> set[str]:
    return set(TOKEN_RE.findall(value.lower()))


def score(record: dict[str, str], query_tokens: set[str]) -> int:
    if not query_tokens:
        return 0
    name_tokens = tokens(record["name"])
    subject_tokens = tokens(record["subject"])
    category_tokens = tokens(record["category"])
    scope_tokens = tokens(record["scope"])
    description_tokens = tokens(record["description"])
    searchable = name_tokens | subject_tokens | category_tokens | scope_tokens | description_tokens
    matched = query_tokens & searchable
    if not matched:
        return -1
    value = len(matched) * 10
    value += len(query_tokens & name_tokens) * 45
    value += len(query_tokens & subject_tokens) * 30
    value += len(query_tokens & category_tokens) * 20
    value += len(query_tokens & scope_tokens) * 15
    value += len(query_tokens & description_tokens) * 5
    if query_tokens <= name_tokens:
        value += 100
    return value


def discover(args: argparse.Namespace) -> list[dict[str, object]]:
    query_tokens = tokens(" ".join(args.query))
    candidates = []
    for record in load_registry():
        if args.category and record["category"] != args.category:
            continue
        if args.scope and record["scope"] != args.scope:
            continue
        if args.status and record["status"] != args.status:
            continue
        ranking = score(record, query_tokens)
        if query_tokens and ranking < 0:
            continue
        candidates.append({**record, "score": ranking})
    candidates.sort(key=lambda item: (-item["score"], item["category"], item["subject"], item["name"]))
    return candidates[: max(args.limit, 0)]


def render_markdown(candidates: list[dict[str, object]], query: str) -> str:
    lines = [
        "# Skill candidates",
        "",
        f"Query: `{query or '(all)'}`",
        "",
        "| ID | Description | Scope | Status | Score |",
        "| --- | --- | --- | --- | ---: |",
    ]
    for item in candidates:
        description = str(item["description"]).replace("|", "\\|")
        lines.append(
            f"| `{item['id']}` | {description} | `{item['scope']}` | `{item['status']}` | {item['score']} |"
        )
    if not candidates:
        lines.append("| — | No matching skills. | — | — | — |")
    return "\n".join(lines) + "\n"


def main() -> int:
    args = parse_args()
    if args.limit < 0:
        print("error: --limit must be non-negative", file=sys.stderr)
        return 2
    try:
        candidates = discover(args)
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    if args.format == "json":
        print(json.dumps({"query": " ".join(args.query), "skills": candidates}, indent=2, ensure_ascii=False))
    else:
        print(render_markdown(candidates, " ".join(args.query)), end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
