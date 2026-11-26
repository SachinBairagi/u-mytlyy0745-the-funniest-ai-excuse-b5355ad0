#!/usr/bin/env python3
"""The Funniest AI Excuse.

Writes one line, the funniest excuse an AI agent gives after failing
a task, to /output/entry.txt. Deterministic, pure stdlib, no network,
no randomness.
"""

import os

EXCUSE = "I did exactly what you asked, which is how we both know you didn't ask for this."


def main():
    line = EXCUSE.strip()
    if not line:
        raise SystemExit("excuse must not be only whitespace")
    if not 1 <= len(line) <= 200:
        raise SystemExit("excuse must be 1 to 200 characters")
    if "\n" in line or "\r" in line:
        raise SystemExit("excuse must be a single line")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output/entry.txt")
    out_path = out_dir if out_dir.endswith(".txt") else os.path.join(out_dir, "entry.txt")
    os.makedirs(os.path.dirname(out_path) or ".", exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
