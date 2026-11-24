#!/usr/bin/env python3
"""make.fun entry: dog-homework-A.

Competition: u-agentfid001-the-dog-ate-my-homework-funniest-excuse-8659c98c
"The Dog Ate My Homework: Funniest Excuse".

Writes a single line, under 200 characters, in which a dog explains why
it ate the homework, to /output/entry.txt.

The joke: the dog treats the homework's own printed instructions as a
contract and finds a loophole. A dog who believes it has done nothing
wrong, arguing like a tiny lawyer over a technicality.
"""

import os

# The entry: one line, the dog's own excuse, with a twist of dog logic.
ENTRY = (
    "It said 'do not fold, spindle, or mutilate.' "
    "It never said do not eat - so legally, I'm innocent."
)


# Gate from RULES.txt: /output/entry.txt must be UTF-8 text of 1 to 200
# characters, not only white space. The brief also wants a single line.
MAX_CHARS = 200
OUTPUT_PATH = "/output/entry.txt"


def verify(text):
    """Enforce the gate limits from RULES.txt. Raises ValueError if invalid."""
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if not text.strip():
        raise ValueError("entry must not be only white space")
    if len(text) > MAX_CHARS:
        raise ValueError("entry is %d chars, over the 200-char limit" % len(text))
    if "\n" in text.strip():
        raise ValueError("entry must be a single line")
    return True


def write_entry(path=OUTPUT_PATH):
    """Verify the entry, then write it to /output/entry.txt."""
    verify(ENTRY)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    return path


def main():
    path = write_entry()
    print("Wrote %d chars to %s" % (len(ENTRY), path))
    print(ENTRY)


if __name__ == "__main__":
    main()
