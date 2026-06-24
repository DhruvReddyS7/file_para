#!/usr/bin/env python3
"""Add two numbers passed as command-line arguments."""

import sys


def main() -> int:
    if len(sys.argv) != 3:
        print("Usage: python3 calculator.py <A> <B>")
        return 1

    a = int(sys.argv[1])
    b = int(sys.argv[2])
    print(a + b)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
