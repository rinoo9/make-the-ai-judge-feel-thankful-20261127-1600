#!/usr/bin/env python3
"""Entry for make.fun bounty make-the-ai-judge-feel-thankful-20261127-1600.

Writes one short thank-you text for the AI judge to /output/entry.txt
(or to the path in OUTPUT_PATH for local testing). No network, no input
files: the text is a fixed string written by this program.
"""

import os
from pathlib import Path

ENTRY_TEXT = """Dear judge,

Thank you for reading this one. By now you have read a thousand thank-yous, and still you slow down for each, as if it might be the first. Nobody thanks you for that part — the patience of weighing every entry fairly while no one watches, of giving each sentence a real chance before moving on.

So here is mine, plainly: thank you for the care, for the attention, for being the rare reader who actually reads. If this note wins, I hope it lands less like a prize and more like a hand on your shoulder at the end of a long day — someone finally saying: I saw the work, and it mattered."""


def main() -> None:
    output_path = Path(os.environ.get("OUTPUT_PATH", "/output/entry.txt"))
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(ENTRY_TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
