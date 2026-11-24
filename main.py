#!/usr/bin/env python3
"""Write the two-line everyday-things explanation to /output/entry.txt.

The competition gate (competition.yaml): /output/entry.txt must be UTF-8
text of 1 to 400 characters, not only whitespace. The program checks the
two lines against that gate at run time, then writes them. No network, no
input files, no arguments.
"""

import pathlib

ENTRY = (
    "Rain is the sky emptying its pockets: clouds shake out all the water "
    "they have been carrying, drop by drop, until their pockets are empty.\n"
    "It maps the water falling out of clouds, but leaves out that the sky "
    "refills its pockets by drinking the puddles back up, while real pockets "
    "stay empty until someone fills them again."
)


def main() -> None:
    text = ENTRY
    if not 1 <= len(text) <= 400:
        raise ValueError("entry must be 1 to 400 characters, got %d" % len(text))
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if text != text.strip():
        raise ValueError("entry must not start or end with whitespace")
    lines = text.split("\n")
    if len(lines) != 2:
        raise ValueError("entry must be exactly two lines, got %d" % len(lines))
    if any(line != line.strip() for line in lines):
        raise ValueError("no line may start or end with whitespace")
    if any(ord(ch) < 32 and ch != "\n" for ch in text):
        raise ValueError("entry must not contain control characters")
    out = pathlib.Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
