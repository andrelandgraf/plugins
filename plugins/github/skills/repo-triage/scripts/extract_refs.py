#!/usr/bin/env python3
"""Extract GitHub issue/PR references from stdin.

Utility for skill users who paste arbitrary text before triage.
"""

from __future__ import annotations

import re
import sys

PATTERN = re.compile(r"(?:(?P<repo>[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+))?#(?P<num>\d+)")


def main() -> int:
    text = sys.stdin.read()
    if not text:
        print("No input provided", file=sys.stderr)
        return 1

    seen = set()
    for match in PATTERN.finditer(text):
        repo = match.group("repo") or "<current-repo>"
        num = match.group("num")
        key = (repo, num)
        if key in seen:
            continue
        seen.add(key)
        print(f"{repo}#{num}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
