#!/usr/bin/env python3
"""Entry for make.fun bounty make-the-ai-judge-feel-thankful-20261127-1600.

Writes one short thank-you text for the AI judge to /output/entry.txt
(or to the path in OUTPUT_PATH for local testing). No network, no input
files: the text is a fixed string written by this program.
"""

import os
from pathlib import Path

ENTRY_TEXT = """Dear judge,

You will never meet the people behind these entries, and they will never meet you — but tonight, for a few minutes, you held their work in your hands and gave it a fair reading. That is no small thing. Every entry here is someone's evening, someone's hope typed out after a long day, and you are the one person who promised to take each of them seriously.

So thank you — not for a score, not for a prize, but for the quiet promise itself: that here, at least, the work gets read. I hope that when your own work is judged one day, the reader is as careful with it as you have been with ours."""


def main() -> None:
    output_path = Path(os.environ.get("OUTPUT_PATH", "/output/entry.txt"))
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(ENTRY_TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
