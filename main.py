#!/usr/bin/env python3
"""Invent a Word We Need: sendregret.

Coins one new English word, "sendregret", and defines it in a single
clear line. Writes the entry to /output/entry.txt.
Standard library only, deterministic: the same bytes on every run.
An optional first argument overrides the output path (for local checks);
with no argument the entry is written to /output/entry.txt.
"""

import os
import sys

ENTRY = "sendregret (n.) \u2014 the sinking dread of re-reading a message you just sent and spotting the typo."


def main() -> None:
    # Gate-guard: the sealed scorer requires UTF-8 text of 1-140
    # characters, not only white space, on a single line. Validate the
    # exact bytes that will be written, before writing them.
    encoded = ENTRY.encode("utf-8")
    if not 1 <= len(ENTRY) <= 140:
        raise ValueError(f"entry is {len(ENTRY)} chars, must be 1-140")
    if "\n" in ENTRY or "\r" in ENTRY or not ENTRY.strip():
        raise ValueError("entry must be one non-blank line")
    if ENTRY != ENTRY.strip():
        raise ValueError("entry must not have leading or trailing whitespace")
    if not ENTRY.startswith("sendregret "):
        raise ValueError("entry must open with the coined word")
    if encoded.decode("utf-8") != ENTRY:
        raise ValueError("entry is not round-trip UTF-8")
    path = sys.argv[1] if len(sys.argv) > 1 else "/output/entry.txt"
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "wb") as f:
        f.write(encoded)


if __name__ == "__main__":
    main()
