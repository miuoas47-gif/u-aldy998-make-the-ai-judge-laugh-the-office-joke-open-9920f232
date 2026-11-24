#!/usr/bin/env python3
"""Make the AI Judge Laugh: the Office Joke Open.

Writes one single-line joke about office life to <output>/entry.txt,
where <output> is the grader's /output directory when it exists, or the
directory named by MAKEFUN_OUTPUT_DIR, or ./output for local runs.

The joke is fixed text, so every run writes byte-identical output.
"""

import os
import sys

JOKE = (
    "I asked IT for a second monitor, so they gave me a mirror "
    "\u2014 now I can watch myself pretend to work twice as fast."
)

MAX_CHARS = 200


def output_dir() -> str:
    """Pick the output directory: explicit env override, else /output."""
    override = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if override:
        return override
    if os.path.isdir("/output"):
        return "/output"
    return os.path.join(os.getcwd(), "output")


def main() -> int:
    joke = JOKE.strip()
    if not joke or len(joke) > MAX_CHARS or "\n" in joke:
        print("joke is not a single line of 1-200 characters", file=sys.stderr)
        return 1
    out_dir = output_dir()
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(joke + "\n")
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != joke + "\n":
        print("entry.txt did not round-trip", file=sys.stderr)
        return 1
    print(f"wrote {len(joke)} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
