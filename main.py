#!/usr/bin/env python3
"""Writes one haiku about debugging (three lines, 5-7-5) to /output/entry.txt. Deterministic, no input, no network."""

import os

TEXT = (
    "cursor blinks at three\n"
    "the log says nothing is wrong\n"
    "the bug waves from prod"
)


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    try:
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, "entry.txt")
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(TEXT + "\n")
    except OSError:
        pass
    print(TEXT)


if __name__ == "__main__":
    main()
