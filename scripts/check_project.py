#!/usr/bin/env python3
"""Static quality checks for a generated YouTube script project."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED_FILES = [
    "00_input.md",
    "01_research_ledger.md",
    "02_story_architecture.md",
    "03_outline.md",
    "04_draft.md",
    "05_fact_audit.md",
    "06_retention_audit.md",
    "07_final_script.md",
    "project_state.json",
]

TRANSITION_PATTERNS = [
    r"\bhere(?:'s| is) the thing\b",
    r"\bthink about that\b",
    r"\bthis is where it gets interesting\b",
    r"\blet that sink in\b",
]


def word_count(text: str) -> int:
    body = re.sub(r"(?m)^#.*$", "", text)
    return len(re.findall(r"\b[\w’'-]+\b", body, flags=re.UNICODE))


def verdict_from(text: str) -> str:
    match = re.search(r"(?im)^-?\s*Verdict:\s*(PASS|FAIL|PENDING)\b", text)
    return match.group(1).upper() if match else "UNKNOWN"


def main() -> int:
    parser = argparse.ArgumentParser(description="Check a YouTube script project")
    parser.add_argument("project", help="Project slug or path")
    args = parser.parse_args()

    project = Path(args.project)
    if not project.exists():
        project = ROOT / "projects" / args.project
    if not project.exists():
        raise SystemExit(f"Project not found: {args.project}")

    errors: list[str] = []
    warnings: list[str] = []

    for name in REQUIRED_FILES:
        if not (project / name).exists():
            errors.append(f"Missing required file: {name}")

    state_path = project / "project_state.json"
    if state_path.exists():
        state = json.loads(state_path.read_text(encoding="utf-8"))
        target = int(state.get("target_words") or 0)
    else:
        state = {}
        target = 0

    final_path = project / "07_final_script.md"
    final_text = final_path.read_text(encoding="utf-8") if final_path.exists() else ""
    final_words = word_count(final_text) if final_text else 0

    if target and final_words:
        delta = abs(final_words - target) / target
        if delta > 0.07:
            errors.append(f"Final length outside ±7%: {final_words} vs target {target} ({delta:.1%})")
    elif target and not final_words:
        warnings.append("Final script is empty")

    fact_path = project / "05_fact_audit.md"
    retention_path = project / "06_retention_audit.md"
    if fact_path.exists():
        verdict = verdict_from(fact_path.read_text(encoding="utf-8"))
        if verdict != "PASS":
            errors.append(f"Fact Audit is {verdict}, expected PASS")
    if retention_path.exists():
        verdict = verdict_from(retention_path.read_text(encoding="utf-8"))
        if verdict != "PASS":
            errors.append(f"Retention Audit is {verdict}, expected PASS")

    if re.search(r"\[(?:VERIFY|TODO|SOURCE|CHECK)[^\]]*\]", final_text, flags=re.I):
        errors.append("Final script still contains editor/verification notes")

    for pattern in TRANSITION_PATTERNS:
        hits = len(re.findall(pattern, final_text, flags=re.I))
        if hits >= 3:
            warnings.append(f"Repeated template transition {hits} times: /{pattern}/")

    percentages = re.findall(r"\b\d+(?:\.\d+)?\s*%", final_text)
    if percentages:
        warnings.append(
            f"Final contains {len(percentages)} percentage claim(s); confirm every one has direct ledger support"
        )

    print(f"Project: {project.relative_to(ROOT) if project.is_relative_to(ROOT) else project}")
    print(f"Final words: {final_words}" + (f" / target {target}" if target else ""))

    for item in warnings:
        print(f"WARN: {item}")
    for item in errors:
        print(f"ERROR: {item}")

    if errors:
        print("RESULT: FAIL")
        return 1
    print("RESULT: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
