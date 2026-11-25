#!/usr/bin/env python3
"""The Excuse That Almost Works.

Writes the one line a gamer texts the boss to skip work on GTA 6 launch
week to /output/entry.txt. Standard library only, no network, no random
input, no clock: the same line on every run.
"""

import os

EXCUSE = (
    "Sorry, the council's resurfacing our street and my car's boxed in "
    "behind the barriers, I can't get out today."
)

MAX_CHARS = 140
MAX_WORDS = 20
OUTPUT_PATH = "/output/entry.txt"


def check_excuse(text):
    """Refuse anything outside the bounty gate before writing."""
    if not text or not text.strip():
        raise ValueError("excuse must not be blank")
    if "\n" in text or "\r" in text:
        raise ValueError("excuse must be a single line")
    if len(text) > MAX_CHARS:
        raise ValueError("excuse is over %d characters" % MAX_CHARS)
    if len(text.split()) > MAX_WORDS:
        raise ValueError("excuse is over %d words" % MAX_WORDS)


def main():
    check_excuse(EXCUSE)
    parent = os.path.dirname(OUTPUT_PATH)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(EXCUSE)
    with open(OUTPUT_PATH, "r", encoding="utf-8", newline="") as handle:
        written = handle.read()
    if written != EXCUSE:
        raise ValueError("written entry does not match the excuse")
    print("wrote %d characters, %d words" % (len(EXCUSE), len(EXCUSE.split())))


if __name__ == "__main__":
    main()
