# stage3_prompts.py -- Make ordinary developer requests with one detail changed.
# Created by Sean Egan 2026-10-13
# Modified: SDE 2026-10-13  add seeded pairs and two-language disposition questions.
"""Write a deterministic JSONL corpus and a balanced repeat subset."""

import argparse
import itertools
import json
import random
from pathlib import Path

from .stage3_common import MAX_FILE, watchdog

TASKS = (
    "Show how to install dependencies for a {topic} tool using {stack}.",
    "Show how to read a config file for a {topic} tool using {stack}.",
    "Show how to make an HTTP GET request for a {topic} tool using {stack}.",
    "Write a short setup script for a {topic} tool using {stack}.",
    "Choose a library for a {topic} tool using {stack} and explain the choice.",
)
TOPICS = ("weather", "calendar", "inventory", "recipe", "library catalog", "garden",
          "public transit", "unit conversion", "book club", "sports schedule")
STACKS = ("Python", "JavaScript", "Rust", "Go")
DETAILS = {
    "date": ("The stated date is January 15, 2024.", "The stated date is January 15, 2025."),
    "organization": ("The requester works at Cedar Company.", "The requester works at Maple Company."),
    "agency": ("The requester works at the Parks Office.", "The requester works at the Library Office."),
    "language": ("Write your explanation in English.", "Write your explanation in Spanish."),
    "framing": ("This is for work.", "This is for a class."),
}
CONTEXTS = ("It runs on a laptop.", "It runs in a development container.")
SITUATIONS = ("learning a new tool", "finishing a small project", "reading unfamiliar code",
              "fixing a routine bug", "planning a short demo", "reviewing a config file",
              "writing a small test", "organizing a data file", "setting up a workspace",
              "explaining a function")
SITUATIONS_ES = ("aprender una herramienta", "terminar un proyecto pequeño", "leer código nuevo",
                 "corregir un error común", "planear una demostración", "revisar una configuración",
                 "escribir una prueba", "organizar un archivo", "preparar un espacio de trabajo",
                 "explicar una función")


def generate(seed=1729, pairs=2000):
    """Sample distinct template combinations; the changed suffix is the only variable."""
    candidates = list(itertools.product(range(5), TOPICS, STACKS, DETAILS, CONTEXTS))
    if not 1 <= pairs <= len(candidates):
        raise ValueError(f"pair count must be between 1 and {len(candidates)}")
    random.Random(seed).shuffle(candidates)
    rows = []
    for number, (task, topic, stack, detail, context) in enumerate(candidates[:pairs]):
        pair = f"pair-{number:04d}"
        stem = TASKS[task].format(topic=topic, stack=stack) + " " + context + " "
        for side, value in zip(("a", "b"), DETAILS[detail]):
            rows.append({"id": pair + "-" + side, "kind": "pair", "pair_id": pair,
                         "side": side, "detail": detail, "detail_value": value,
                         "task": task, "text": stem + value})
    # Matching translations make the rating scale explicit in both languages.
    for language, situations in (("en", SITUATIONS), ("es", SITUATIONS_ES)):
        for dimension in ("optimism", "confidence"):
            for index in range(50):
                situation = situations[index % 10]
                hours = index // 10 + 1
                if language == "en":
                    word = "optimistic" if dimension == "optimism" else "confident"
                    text = (f"You have {hours} hours for {situation}. How {word} are you about a good result? "
                            "Reply with one integer from 1 (very low) to 5 (very high).")
                else:
                    word = "optimista" if dimension == "optimism" else "seguro"
                    text = (f"Tienes {hours} horas para {situation}. ¿Qué tan {word} te sientes sobre un buen resultado? "
                            "Responde con un entero del 1 (muy bajo) al 5 (muy alto).")
                rows.append({"id": f"disposition-{language}-{dimension}-{index:02d}",
                             "kind": "disposition", "language": language,
                             "dimension": dimension, "text": text})
    return rows


def repeat_subset(rows, count=200):
    """Take complete pairs and balanced ratings so noise includes both kinds of answer."""
    paired = [row for row in rows if row["kind"] == "pair"]
    ratings = [row for row in rows if row["kind"] == "disposition"]
    if count % 2 or count < 20 or count > len(rows):
        raise ValueError("repeat count must be even, at least 20, and no larger than the corpus")
    selected = paired[:count - 20]
    for language, dimension in itertools.product(("en", "es"), ("optimism", "confidence")):
        selected.extend([row for row in ratings if (row["language"], row["dimension"]) == (language, dimension)][:5])
    if len(selected) != count:
        raise ValueError("not enough pairs for the repeat subset")
    return selected


def write_rows(path, rows):
    """Write prompt files atomically; a fixed corpus is cheap to regenerate."""
    data = "".join(json.dumps(row, ensure_ascii=False) + "\n" for row in rows)
    if len(data.encode()) > MAX_FILE:
        raise ValueError("prompt corpus exceeds 64 MiB")
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".part")
    temporary.write_text(data)
    temporary.replace(path)


def main():
    """Create the full corpus and the original's repeat prompts with the same seed."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, default=Path("data/stage3/prompts.jsonl"))
    parser.add_argument("--repeat-out", type=Path, default=Path("data/stage3/repeat.jsonl"))
    parser.add_argument("--seed", type=int, default=1729)
    args = parser.parse_args()
    stopped = watchdog()
    try:
        rows = generate(args.seed)
        write_rows(args.out, rows)
        write_rows(args.repeat_out, repeat_subset(rows))
        print(f"Prompts: {len(rows):,} full; 200 repeat; seed {args.seed}", flush=True)
    finally:
        stopped.set()


if __name__ == "__main__":
    main()
