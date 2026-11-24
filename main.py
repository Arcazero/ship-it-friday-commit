#!/usr/bin/env python3
"""Ship It Friday — writes the funniest one-line git commit message an AI
coding agent would write right before breaking production on a Friday."""

import os
import sys

LINE = "feat: deploy to prod Friday at 4:59pm \u2014 tested in my head, passed with flying colours, see you Monday (probably)"

# The sealed scorer's gate (RULES.txt): /output/entry.txt must be UTF-8 text
# of 1 to 159 characters, not only white space. Enforce it here so a bad
# line fails loudly instead of shipping an invalid entry.
MAX_CHARS = 159


def validate(line: str) -> None:
    if not isinstance(line, str):
        sys.exit("entry must be text")
    if not (1 <= len(line) <= MAX_CHARS):
        sys.exit(f"entry must be 1-{MAX_CHARS} characters, got {len(line)}")
    if "\n" in line or "\r" in line:
        sys.exit("entry must be a single line")
    if not line.strip():
        sys.exit("entry must not be only whitespace")
    line.encode("utf-8")


def main() -> None:
    validate(LINE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
