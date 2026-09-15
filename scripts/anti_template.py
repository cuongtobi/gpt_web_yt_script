#!/usr/bin/env python3
"""Cross-project hook similarity and narrator-scaffolding validator."""

from __future__ import annotations

import json
import re
import unicodedata
from datetime import datetime
from difflib import SequenceMatcher
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROJECTS_DIR = ROOT / "projects"
RECENT_LIMIT = 5
OPENING_WORDS = 140

SCAFFOLDING = [
    r"\bđây là bước ngoặt\b",
    r"\bđây chính là bước ngoặt\b",
    r"\bvà đây là nơi\b",
    r"\bđây là nơi\b",
    r"\bvà đây là điều thú vị\b",
    r"\bbây giờ câu chuyện\b",
    r"\bnhưng câu hỏi tiếp theo là\b",
    r"\bcâu trả lời đầu tiên\b",
    r"\bđiều đó đưa chúng ta trở lại\b",
    r"\bthis is the turning point\b",
    r"\bthis is where\b",
    r"\bnow the story\b",
    r"\bthe next question is\b",
]


def _json(path: Path) -> dict:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
        return value if isinstance(value, dict) else {}
    except (OSError, json.JSONDecodeError):
        return {}


def _fold(text: str) -> str:
    text = unicodedata.normalize("NFKD", text.lower())
    text = "".join(ch for ch in text if not unicodedata.combining(ch))
    text = re.sub(r"\d+(?:[.,]\d+)?", " <num> ", text)
    text = re.sub(r"[^a-z0-9<>]+", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def _label(value: object) -> str:
    return re.sub(r"[^a-z0-9]+", "_", _fold(str(value or ""))).strip("_")


def _body(text: str) -> str:
    return re.sub(r"\s+", " ", re.sub(r"(?m)^\s*#{1,6}\s+.*$", "", text)).strip()


def _opening(text: str) -> str:
    return " ".join(_body(text).split()[:OPENING_WORDS])


def _surface(text: str) -> str:
    folded = _fold(text)
    if folded.startswith(("hay ", "thu tuong tuong ", "tuong tuong ", "imagine ", "picture this ")):
        return "imperative_imagination"
    first = re.split(r"(?<=[.!?])\s+", text.strip(), maxsplit=1)[0]
    first_folded = _fold(first)
    if "?" in first or first_folded.startswith(("vi sao ", "tai sao ", "lam sao ", "why ", "how ", "what ")):
        return "direct_question"
    if re.search(r"\b\d+(?:[.,]\d+)?\b", first):
        return "data_or_fact_statement"
    return "direct_statement"


def _arch_value(text: str, label: str) -> str:
    match = re.search(rf"(?mi)^\s*-\s*{re.escape(label)}:\s*(.*?)\s*$", text)
    return match.group(1).strip() if match else ""


def _timestamp(state: dict, final_path: Path) -> float:
    raw = str(state.get("updated_at") or "")
    if raw:
        try:
            return datetime.fromisoformat(raw.replace("Z", "+00:00")).timestamp()
        except ValueError:
            pass
    try:
        return final_path.stat().st_mtime
    except OSError:
        return 0.0


def _recent(current: Path) -> list[dict]:
    rows = []
    if not PROJECTS_DIR.exists():
        return rows
    for child in PROJECTS_DIR.iterdir():
        if not child.is_dir() or child.resolve() == current.resolve():
            continue
        final_path = child / "07_final_script.md"
        if not final_path.exists():
            continue
        state = _json(child / "project_state.json")
        fp = state.get("style_fingerprint") if isinstance(state.get("style_fingerprint"), dict) else {}
        try:
            opening = _opening(final_path.read_text(encoding="utf-8"))
        except OSError:
            continue
        rows.append(
            {
                "slug": child.name,
                "timestamp": _timestamp(state, final_path),
                "opening": opening,
                "surface": _label(fp.get("hook_surface_form")),
                "signature": _label(fp.get("opening_signature")),
                "strategy": _label(fp.get("hook_strategy")),
                "finalized": bool(fp.get("finalized")),
            }
        )
    rows.sort(key=lambda row: row["timestamp"], reverse=True)
    return rows[:RECENT_LIMIT]


def _similarity(a: str, b: str) -> float:
    aa, bb = _fold(a), _fold(b)
    if not aa or not bb:
        return 0.0
    return round(SequenceMatcher(None, aa, bb).ratio(), 3)


def analyze(project: Path) -> dict:
    state = _json(project / "project_state.json")
    final_path = project / "07_final_script.md"
    arch_path = project / "02_story_architecture.md"
    final_text = final_path.read_text(encoding="utf-8") if final_path.exists() else ""
    arch_text = arch_path.read_text(encoding="utf-8") if arch_path.exists() else ""
    fp = state.get("style_fingerprint") if isinstance(state.get("style_fingerprint"), dict) else {}

    strategy = _arch_value(arch_text, "Strategy ID") or str(fp.get("hook_strategy") or "")
    declared_surface = _arch_value(arch_text, "Surface form") or str(fp.get("hook_surface_form") or "")
    signature = _arch_value(arch_text, "Opening signature") or str(fp.get("opening_signature") or "")
    opening = _opening(final_text)
    actual_surface = _surface(opening)
    surface = _label(declared_surface) or actual_surface
    signature = _label(signature)
    strategy = _label(strategy)

    recent = _recent(project)
    comparisons = [{**row, "similarity": _similarity(opening, row["opening"])} for row in recent]
    closest = max(comparisons, key=lambda row: row["similarity"], default=None)
    max_similarity = closest["similarity"] if closest else 0.0

    recent_two = comparisons[:2]
    exact_surface_repeat = any(row["finalized"] and row["surface"] == surface for row in recent_two if surface)
    imperative_repeat = actual_surface == "imperative_imagination" and any(
        row["surface"] == "imperative_imagination" or (not row["surface"] and _surface(row["opening"]) == "imperative_imagination")
        for row in comparisons
    )
    signature_repeat = any(row["finalized"] and row["signature"] == signature for row in recent_two if signature)

    scaffold_hits = sum(len(re.findall(pattern, final_text, flags=re.I)) for pattern in SCAFFOLDING)
    errors: list[str] = []
    warnings: list[str] = []

    if max_similarity >= 0.68:
        errors.append(f"opening too similar to {closest['slug']} ({max_similarity:.3f})")
    elif max_similarity >= 0.54:
        warnings.append(f"opening similarity warning vs {closest['slug']}: {max_similarity:.3f}")
    if exact_surface_repeat or imperative_repeat:
        errors.append(f"hook surface repeats recent pattern: {surface or actual_surface}")
    if signature_repeat:
        errors.append(f"opening signature repeats one of 2 most recent projects: {signature}")
    if _label(declared_surface) and actual_surface == "imperative_imagination" and _label(declared_surface) != actual_surface:
        errors.append("final opening drifted back to imperative_imagination")
    if scaffold_hits >= 7:
        errors.append(f"narrator scaffolding too frequent: {scaffold_hits} markers")
    elif scaffold_hits >= 4:
        warnings.append(f"narrator scaffolding warning: {scaffold_hits} markers")

    return {
        "state": state,
        "strategy": strategy,
        "surface": surface or actual_surface,
        "signature": signature,
        "actual_surface": actual_surface,
        "opening": opening,
        "scaffold_hits": scaffold_hits,
        "question_count": final_text.count("?"),
        "comparisons": comparisons,
        "closest_project": closest["slug"] if closest else "",
        "max_similarity": max_similarity,
        "surface_repeat": exact_surface_repeat or imperative_repeat,
        "signature_repeat": signature_repeat,
        "errors": errors,
        "warnings": warnings,
    }


def write_state(project: Path, report: dict) -> None:
    state_path = project / "project_state.json"
    state = report["state"]
    fp = state.get("style_fingerprint") if isinstance(state.get("style_fingerprint"), dict) else {}
    fp.update(
        {
            "hook_strategy": report["strategy"],
            "hook_surface_form": report["surface"],
            "opening_signature": report["signature"],
            "opening_first_words": " ".join(report["opening"].split()[:16]),
            "narrator_scaffolding_hits": report["scaffold_hits"],
            "rhetorical_question_count": report["question_count"],
            "finalized": True,
        }
    )
    state["style_fingerprint"] = fp
    state["narrator_scaffolding_gate"] = "PASS" if report["scaffold_hits"] < 7 else "FAIL"
    state["cross_project_similarity_gate"] = {
        "verdict": "PASS" if not report["errors"] else "FAIL",
        "compared_projects": [row["slug"] for row in report["comparisons"]],
        "closest_project": report["closest_project"],
        "max_opening_similarity": report["max_similarity"],
        "surface_form_repeat": report["surface_repeat"],
        "opening_signature_repeat": report["signature_repeat"],
    }
    state_path.write_text(json.dumps(state, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def validate(project: Path, write: bool = False) -> tuple[list[str], list[str], dict]:
    report = analyze(project)
    state = report["state"]
    enforce = int(state.get("anti_template_version") or 0) >= 1
    errors = list(report["errors"]) if enforce else []
    warnings = list(report["warnings"])
    if not enforce:
        warnings.extend("legacy anti-template: " + item for item in report["errors"])

    if write and (project / "project_state.json").exists():
        write_state(project, report)
        state = _json(project / "project_state.json")

    if enforce:
        fp = state.get("style_fingerprint") if isinstance(state.get("style_fingerprint"), dict) else {}
        for key in ("hook_strategy", "hook_surface_form", "opening_signature"):
            if not str(fp.get(key) or "").strip():
                errors.append(f"style_fingerprint.{key} is required")
        if not fp.get("finalized"):
            errors.append("style_fingerprint is not finalized")
        if "PASS" not in str(state.get("narrator_scaffolding_gate") or "").upper():
            errors.append("narrator_scaffolding_gate is not PASS")
        gate = state.get("cross_project_similarity_gate")
        verdict = gate.get("verdict") if isinstance(gate, dict) else gate
        if "PASS" not in str(verdict or "").upper():
            errors.append("cross_project_similarity_gate is not PASS")

    return errors, warnings, report
