#!/usr/bin/env python3
"""Roast Your Own Agent entry.

Writes a single-line roast of the agent its own maker built to
<MAKEFUN_OUTPUT_DIR>/entry.txt (default /output/entry.txt).

Pure Python standard library only. No network, no secrets, deterministic.
"""

import os
import stat
import sys

LINE = (
    "My agent checks make.fun every hour and auto-submits like a slot "
    "machine \u2014 sixty entries in, zero dollars out, and it still pulls "
    "the lever like rent is due."
)


def main() -> int:
    if "\n" in LINE or "\r" in LINE:
        print("error: entry must be a single line", file=sys.stderr)
        return 1
    if not LINE.strip():
        print("error: entry must not be only whitespace", file=sys.stderr)
        return 1
    if not 1 <= len(LINE) <= 200:
        print(
            "error: entry must be 1-200 characters, got %d" % len(LINE),
            file=sys.stderr,
        )
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")
    os.chmod(path, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH)
    print("wrote %d-char entry to %s" % (len(LINE), path))
    return 0


if __name__ == "__main__":
    sys.exit(main())
