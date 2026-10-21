#!/usr/bin/env python3
"""Build a concise flash-card JSON deck from a completed combined Q&A file."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from html_utils import fence_start, fence_end


MARK_GROUPS = {
    1: "Quick recall",
    2: "Explain and compare",
    3: "Apply and calculate",
    4: "Multi-step application",
}

HEADING_RE = re.compile(r"^##\s+(\d+)\s+marks?\s*$", re.IGNORECASE)
QUESTION_RE = re.compile(r"^\*\*(\d+)\.\*\*\s*(.*)$")
ANSWER_RE = re.compile(r"^\*\*Answer:\*\*\s*(.*)$")
IMAGE_RE = re.compile(r"!\[[^\]]*\]\([^)]*\)")


def clean_line(line: str) -> str:
    line = IMAGE_RE.sub("", line).strip()
    if line.startswith("- "):
        line = line[2:].strip()
    return line


def clean_answer(lines: list[str]) -> list[str]:
    """Keep each code block as one point, with indentation and empty lines."""
    points = []
    block = None
    marker = None
    for line in lines:
        if block is not None:
            block.append(line)
            if fence_end(line, marker):
                points.append('\n'.join(block))
                block, marker = None, None
        elif (fence := fence_start(line)):
            block, marker = [line], fence[1]
        elif (value := clean_line(line)):
            points.append(value)
    if block is not None:
        points.append('\n'.join(block))
    return points


def parse_cards(text: str) -> list[dict[str, object]]:
    cards: list[dict[str, object]] = []
    marks: int | None = None
    question: list[str] | None = None
    answer: list[str] = []
    reading_answer = False
    active_fence = None

    def save() -> None:
        nonlocal question, answer, reading_answer
        if marks not in MARK_GROUPS or question is None:
            question, answer, reading_answer = None, [], False
            return
        front = ("\n".join(question).strip() if any(fence_start(line) for line in question)
                 else " ".join(part for part in map(clean_line, question) if part))
        back = clean_answer(answer)
        if front and back and "diagram" not in front.lower() and "figure" not in front.lower():
            cards.append({"category": MARK_GROUPS[marks], "front": front, "back": back})
        question, answer, reading_answer = None, [], False

    for raw in text.splitlines():
        if active_fence is not None:
            (answer if reading_answer else question).append(raw)
            if fence_end(raw, active_fence):
                active_fence = None
            continue
        if question is not None and (fence := fence_start(raw)):
            (answer if reading_answer else question).append(raw)
            active_fence = fence[1]
            continue
        heading = HEADING_RE.match(raw)
        if heading:
            save()
            marks = int(heading.group(1))
            continue

        new_question = QUESTION_RE.match(raw)
        if new_question:
            save()
            question = [new_question.group(2)]
            continue

        if question is None:
            continue

        answer_start = ANSWER_RE.match(raw)
        if answer_start:
            reading_answer = True
            if answer_start.group(1).strip():
                answer.append(answer_start.group(1))
            continue

        if raw.startswith("## "):
            save()
            marks = None
            continue

        if reading_answer:
            answer.append(raw)
        elif raw.strip():
            question.append(raw)

    save()
    return cards



def build_cards(source: Path) -> list[dict[str, object]]:
    """Combine Q&A cards with reviewed revision-note additions and refinements.

    Keep this supplement outside Flash Cards so the site builds one deck.
    Updating Q&A later must not silently discard independently authored cards.
    """
    cards = parse_cards(source.read_text(encoding="utf-8"))
    supplement = source.parent.parent / "revision-flashcards.json"
    if supplement.exists():
        data = json.loads(supplement.read_text(encoding="utf-8"))
        # Some subjects have independently curated decks, rather than Q&A extracts.
        # Preserve that full base instead of replacing it with a smaller parsed bank.
        if "base_cards" in data:
            cards = data["base_cards"]
        by_front = {card["front"]: card for card in cards}
        for update in data.get("updates", []):
            front = update["front"]
            if front not in by_front:
                raise ValueError(f"Unknown flashcard update in {supplement}: {front}")
            by_front[front]["back"] = update["back"]
        cards.extend(data.get("additions", []))
    fronts = []
    for card in cards:
        if not isinstance(card.get("front"), str) or not card["front"].strip():
            raise ValueError(f"Missing flashcard prompt in {source}")
        back = card.get("back")
        if not isinstance(back, list) or not back or any(not isinstance(p, str) or not p.strip() for p in back):
            raise ValueError(f"Missing flashcard answer in {source}: {card['front']}")
        if not isinstance(card.get("category"), str) or not card["category"].strip():
            raise ValueError(f"Missing flashcard category in {source}: {card['front']}")
        fronts.append(card["front"].strip().casefold())
    if len(fronts) != len(set(fronts)):
        raise ValueError(f"Duplicate flashcard prompts in {source}")
    return cards


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path)
    parser.add_argument("destination", type=Path)
    parser.add_argument("title")
    args = parser.parse_args()

    cards = build_cards(args.source)
    if not cards:
        raise SystemExit(f"No suitable 1–4 mark cards found in {args.source}")
    fronts = [card["front"] for card in cards]
    if len(fronts) != len(set(fronts)):
        raise SystemExit(f"Duplicate flash-card prompts found in {args.source}")

    args.destination.parent.mkdir(parents=True, exist_ok=True)
    args.destination.write_text(
        json.dumps({"title": args.title, "cards": cards}, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(f"Wrote {len(cards)} cards to {args.destination}")


if __name__ == "__main__":
    main()
