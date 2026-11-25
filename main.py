"""Worst Fix Ever: Funniest Commit Message.

Writes one commit message line to /output/entry.txt. The line is a
single self-contained commit subject, 62 characters, no trailing
newline, so the gate sees exactly the text and nothing else.
"""

import os

LINE = "fix memory leak by deleting the database, nothing left to leak"


def main():
    out = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    parent = os.path.dirname(out)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
