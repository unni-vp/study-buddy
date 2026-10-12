#!/usr/bin/env python3
"""Record a generated flash-card deck in a topic README and coverage JSON."""

from __future__ import annotations

import argparse
import json
from datetime import date
from pathlib import Path
from urllib.parse import quote


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("topic", type=Path)
    parser.add_argument("deck", type=Path)
    parser.add_argument("resource_filename")
    parser.add_argument("summary")
    args = parser.parse_args()

    deck_path = args.topic / args.deck
    deck = json.loads(deck_path.read_text(encoding="utf-8"))
    count = len(deck["cards"])
    categories = list(dict.fromkeys(card["category"] for card in deck["cards"]))

    coverage_path = args.topic / "resource-coverage.json"
    coverage = json.loads(coverage_path.read_text(encoding="utf-8"))
    coverage["flashcards"] = {
        "reviewed": date.today().isoformat(),
        "source": str(next((args.topic / "Questions and Answers").glob("*.md")).relative_to(args.topic)).replace("\\", "/"),
        "deck": str(args.deck).replace("\\", "/"),
        "count": count,
        "categories": categories,
    }
    coverage_path.write_text(json.dumps(coverage, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    readme_path = args.topic / "README.md"
    readme = readme_path.read_text(encoding="utf-8")
    flash_line = "- Flash Cards: short question-and-answer prompts for active recall.\n"
    if flash_line not in readme:
        readme = readme.replace(
            "- Mind Maps: links between ideas in large or complex topics.\n",
            "- Mind Maps: links between ideas in large or complex topics.\n" + flash_line,
        )
    has_mindmaps = coverage.get("mindmaps") != []
    resource_summary = (
        "Revision notes, visual mind maps and combined exam questions with answers"
        if has_mindmaps
        else "Revision notes, combined exam questions with answers and flash cards"
    )
    available = (
        "## Available resources\n\n"
        f"- {resource_summary} are available from the topic page.\n"
        f"- [Interactive flash cards](../../library/resources/{args.resource_filename}): {count} cards {args.summary}.\n"
        f"- [Editable flash-card deck]({quote(str(args.deck).replace(chr(92), '/'))})\n"
    )
    placeholder = "Resources have not yet been authored. Follow the project AGENTS.md and RESOURCE_GUIDELINES.md."
    if placeholder in readme:
        readme = readme.replace(placeholder, available.rstrip())
    elif "## Available resources" not in readme:
        readme = readme.rstrip() + "\n\n" + available
    readme_path.write_text(readme, encoding="utf-8")
    print(f"Recorded {count} flash cards in {args.topic}")


if __name__ == "__main__":
    main()
