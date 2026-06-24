#!/usr/bin/env python3
"""Print star patterns from parameter files."""

from pathlib import Path
import sys


def read_size(file_name: str) -> int:
    text = Path(file_name).read_text(encoding="utf-8").strip()
    if "=" in text:
        text = text.split("=", 1)[1].strip()

    size = int(text)
    if size <= 0:
        raise ValueError("pattern size must be positive")
    return size


def make_pattern(size: int) -> str:
    rows = []
    for row in range(1, size + 1):
        spaces = " " * (size - row)
        stars = "*" * (2 * row - 1)
        rows.append(spaces + stars)
    return "\n".join(rows)


def main() -> int:
    if len(sys.argv) < 2:
        print("Usage: python3 pattern.py <parameter-file> [parameter-file ...]")
        return 1

    for index, file_name in enumerate(sys.argv[1:]):
        size = read_size(file_name)
        if index:
            print()
        print(f"{file_name} -> size {size}")
        print(make_pattern(size))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
