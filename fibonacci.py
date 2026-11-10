#!/usr/bin/env python3
"""Enumerate the first n Fibonacci numbers.

Usage:
    python3 fibonacci.py [n]

Prints the first n Fibonacci numbers (starting from 0), one per line.
Defaults to n=10 when no argument is given.
"""

import sys


def fibonacci(n: int):
    """Yield the first n Fibonacci numbers, starting from 0."""
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def main() -> None:
    try:
        n = int(sys.argv[1]) if len(sys.argv) > 1 else 10
    except ValueError:
        sys.exit(f"error: {sys.argv[1]!r} is not an integer")

    if n < 0:
        sys.exit("error: n must be non-negative")

    for value in fibonacci(n):
        print(value)


if __name__ == "__main__":
    main()
