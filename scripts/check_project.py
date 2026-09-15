#!/usr/bin/env python3
"""Final validation for simple_v2, simple_v1 and legacy YouTube documentary projects."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

SIMPLE_V2_FILES = [
    "00_input.md",
    "01_research.md",
    "02_hook_lab.md",
    "03_story_spine.md",
    "04_draft.md",
    "05_fact_audit.md",
    "06_final_script.md",
    "project_state.json",
]

SIMPLE_V1_FILES = [
    "00_input.md",
    "01_research.md",
    "02_story_spine.md",
    "03_draft.md",
    "04_fact_audit.md",
    "05_final_script.md",
    "project_state.json",
]

LEGACY_FILES = [
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

SOFT_TEMPLATE_PATTERNS = [
    r"\bhere(?:'s| is) the thing\b",
    r"\bthink about that\b",
    r"\bthis is where it gets interesting\b",
    r"\blet that sink in\b",
    r"\bđây là bước ngoặt\b",
    r"\bvà đây là nơi\b",
    r"\bnhưng câu hỏi tiếp theo là\b",
]

EARLY_HOOK_SCAFFOLD_PATTERNS = [
    r"\bcâu trả lời là\b",
    r"\bcâu trả lời bắt đầu\b",
    r"\bcâu trả lời ngắn(?: nhất| gọn)?\b",
    r"\bthe answer is\b",
    r"\bthe answer starts with\b",
    r"\bthe short answer is\b",
    r"\bđể hiểu điều này,? (?:ta|chúng ta) (?:cần|phải)\b",
    r"\bto understand this,? we (?:need|have) to\b",
]


def word_count(text: str) -> int:
    body = re.sub(r"(?m)^#.*$", "", text)
    return len(re.findall(r"\b[\w’'-]+\b", body, flags=re.UNICODE))


def verdict_from(text: str) -> str:
    patterns = [
        r"(?im)^\s*-?\s*Verdict:\s*\**\s*(PASS|FAIL|PENDING)\b",
        r"(?ims)^\s*##\s+Verdict\s*\n+\s*\**\s*(PASS|FAIL|PENDING)\b",
    ]
    for pattern in patterns:
        match = re.search(pattern, text)
        if match:
            return match.group(1).upper()
    return "UNKNOWN"


def hook_lab_selection_from(text: str) -> str:
    match = re.search(r"(?im)^\s*-\s*Status:\s*\**\s*(SELECTED|PENDING)\b", text)
    return match.group(1).upper() if match else "UNKNOWN"


def load_state(path: Path) -> tuple[dict, list[str]]:
    errors: list[str] = []
    if not path.exists():
        return {}, ["Missing required file: project_state.json"]
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(value, dict):
            raise ValueError("state root must be an object")
        return value, errors
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        return {}, [f"Invalid project_state.json: {exc}"]


def detect_layout(project: Path, state: dict) -> tuple[str, list[str], str, str]:
    version = str(state.get("pipeline_version") or "")
    if version == "simple_v2" or (project / "06_final_script.md").exists():
        return "simple_v2", SIMPLE_V2_FILES, "06_final_script.md", "05_fact_audit.md"
    if version == "simple_v1" or (project / "05_final_script.md").exists():
        return "simple_v1", SIMPLE_V1_FILES, "05_final_script.md", "04_fact_audit.md"
    return "legacy", LEGACY_FILES, "07_final_script.md", "05_fact_audit.md"


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

    state, state_errors = load_state(project / "project_state.json")
    errors.extend(state_errors)

    pipeline, required, final_name, fact_name = detect_layout(project, state)

    for name in required:
        if not (project / name).exists():
            errors.append(f"Missing required file: {name}")

    if pipeline == "simple_v2":
        if str(state.get("hook_selection") or "").upper() != "SELECTED":
            errors.append("Hook selection is not SELECTED")
        if not str(state.get("selected_hook") or "").strip():
            errors.append("selected_hook missing or empty")
        if not str(state.get("selected_hook_mechanism") or "").strip():
            errors.append("selected_hook_mechanism missing or empty")

        hook_path = project / "02_hook_lab.md"
        if hook_path.exists():
            hook_status = hook_lab_selection_from(hook_path.read_text(encoding="utf-8"))
            if hook_status != "SELECTED":
                errors.append(f"Hook Lab selection is {hook_status}, expected SELECTED")

    target = int(state.get("target_words") or 0)
    final_path = project / final_name
    final_text = final_path.read_text(encoding="utf-8") if final_path.exists() else ""
    final_words = word_count(final_text) if final_text else 0

    if target and final_words:
        delta = abs(final_words - target) / target
        if delta > 0.07:
            errors.append(f"Final length outside ±7%: {final_words} vs target {target} ({delta:.1%})")
    elif target and not final_words:
        errors.append("Final script is empty")
    elif not target:
        warnings.append("target_words missing or zero; timing gate not checked")

    fact_path = project / fact_name
    if fact_path.exists():
        verdict = verdict_from(fact_path.read_text(encoding="utf-8"))
        if verdict != "PASS":
            errors.append(f"Fact Audit is {verdict}, expected PASS")

    if pipeline == "legacy":
        retention_path = project / "06_retention_audit.md"
        if retention_path.exists():
            verdict = verdict_from(retention_path.read_text(encoding="utf-8"))
            if verdict != "PASS":
                errors.append(f"Legacy Retention Audit is {verdict}, expected PASS")

    if re.search(r"\[(?:VERIFY|TODO|SOURCE|CHECK)[^\]]*\]", final_text, flags=re.I):
        errors.append("Final script still contains editor/verification notes")

    for pattern in SOFT_TEMPLATE_PATTERNS:
        hits = len(re.findall(pattern, final_text, flags=re.I))
        if hits >= 3:
            warnings.append(f"Repeated template-like transition {hits} times: /{pattern}/")

    body = re.sub(r"(?m)^#.*$", "", final_text).lstrip()
    if re.match(r"(?i)^(hãy\b|hãy thử\b|hãy tưởng tượng\b|imagine\b|picture this\b)", body):
        warnings.append("Opening uses an imperative/imagination formula; keep it only if it is genuinely the strongest opening")

    early_words = re.findall(r"\b[\w’'-]+\b|[^\w\s]+", body, flags=re.UNICODE)
    early_text = " ".join(early_words[:500])
    for pattern in EARLY_HOOK_SCAFFOLD_PATTERNS:
        if re.search(pattern, early_text, flags=re.I):
            warnings.append(f"Opening uses answer/scaffolding phrase; confirm it is intentional rather than a repeated hook template: /{pattern}/")

    percentages = re.findall(r"\b\d+(?:[.,]\d+)?\s*%", final_text)
    if percentages:
        warnings.append(f"Final contains {len(percentages)} percentage claim(s); confirm direct research support")

    project_display = project.relative_to(ROOT) if project.is_relative_to(ROOT) else project
    print(f"Project: {project_display}")
    print(f"Pipeline: {pipeline}")
    print(f"Final words: {final_words}" + (f" / target {target}" if target else ""))

    if pipeline == "simple_v2":
        print(f"Hook selection: {state.get('selected_hook', '')} / {state.get('selected_hook_mechanism', '')}")

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
