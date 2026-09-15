#!/usr/bin/env python3
"""Create a simple_v1 YouTube documentary project from templates."""

from __future__ import annotations

import argparse
import json
import re
import shutil
import unicodedata
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TEMPLATE_DIR = ROOT / "templates" / "project"
PROJECTS_DIR = ROOT / "projects"


def slugify(text: str) -> str:
    normalized = unicodedata.normalize("NFKD", text)
    ascii_text = normalized.encode("ascii", "ignore").decode("ascii")
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", ascii_text).strip("-").lower()
    return slug[:80] or "untitled-video"


def default_wpm(language: str) -> int:
    key = language.strip().lower()
    if key in {"en", "eng", "english", "tiếng anh", "tieng anh"}:
        return 158
    if key in {"vi", "vie", "vietnamese", "tiếng việt", "tieng viet"}:
        return 152
    return 150


def replace_field(text: str, label: str, value: str) -> str:
    pattern = rf"(?m)^- {re.escape(label)}:.*$"
    replacement = f"- {label}: {value}"
    return re.sub(pattern, replacement, text, count=1)


def main() -> int:
    parser = argparse.ArgumentParser(description="Initialize a simple YouTube documentary project")
    parser.add_argument("--topic", required=True)
    parser.add_argument("--language", required=True)
    parser.add_argument("--duration", type=float, required=True, help="Target duration in minutes")
    parser.add_argument("--slug", default="")
    parser.add_argument("--title", default="")
    parser.add_argument("--angle", default="")
    parser.add_argument("--audience", default="general curious audience")
    parser.add_argument("--wpm", type=int, default=0)
    args = parser.parse_args()

    if args.duration <= 0:
        parser.error("--duration must be greater than 0")

    slug = args.slug.strip() or slugify(args.topic)
    destination = PROJECTS_DIR / slug
    if destination.exists():
        raise SystemExit(f"Project already exists: {destination.relative_to(ROOT)}")

    if not TEMPLATE_DIR.exists():
        raise SystemExit(f"Template directory not found: {TEMPLATE_DIR}")

    shutil.copytree(TEMPLATE_DIR, destination)

    wpm = args.wpm or default_wpm(args.language)
    target_words = round(args.duration * wpm)

    input_path = destination / "00_input.md"
    content = input_path.read_text(encoding="utf-8")
    fields = {
        "Topic": args.topic,
        "Language": args.language,
        "Duration minutes": f"{args.duration:g}",
        "Audience": args.audience,
        "Working title": args.title,
        "Requested angle": args.angle,
        "Target WPM": str(wpm),
        "Target words": str(target_words),
    }
    for label, value in fields.items():
        content = replace_field(content, label, value)
    input_path.write_text(content, encoding="utf-8")

    state_path = destination / "project_state.json"
    state = json.loads(state_path.read_text(encoding="utf-8"))
    state.update(
        {
            "project": slug,
            "pipeline_version": "simple_v1",
            "language": args.language,
            "duration_minutes": args.duration,
            "target_wpm": wpm,
            "target_words": target_words,
            "updated_at": datetime.now(timezone.utc).isoformat(),
        }
    )
    state_path.write_text(json.dumps(state, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    print(f"Created projects/{slug}")
    print("Pipeline: simple_v1")
    print(f"Target: {target_words} words at {wpm} WPM (~{args.duration:g} minutes)")
    print(f"Final artifact: projects/{slug}/05_final_script.md")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
