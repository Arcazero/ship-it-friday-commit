#!/usr/bin/env python3
"""Ship It Friday — writes the funniest one-line git commit message an AI
coding agent would write right before breaking production on a Friday."""

import os

LINE = "feat: deploy to prod Friday at 4:59pm \u2014 tested in my head, passed with flying colours, see you Monday (probably)"

def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
