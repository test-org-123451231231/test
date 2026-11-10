#!/usr/bin/env python3
"""Enumerate Fibonacci numbers.

Usage:
    python3 fibonacci.py [n] [--start K] [--json]

Prints the first n Fibonacci numbers, one per line. With --start,
enumeration begins at index K (F(0)=0, F(1)=1, ...). With --json,
the numbers are printed as a JSON array.

Defaults to n=10 when no argument is given.
"""

import argparse
import json


def fibonacci(n: int, start: int = 0):
    """Yield n Fibonacci numbers, beginning at index `start` (F(0)=0)."""
    a, b = 0, 1
    for _ in range(start):
        a, b = b, a + b
    for _ in range(n):
        yield a
        a, b = b, a + b


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Enumerate the first n Fibonacci numbers."
    )
    parser.add_argument(
        "n", nargs="?", type=int, default=10,
        help="how many numbers to print (default: 10)",
    )
    parser.add_argument(
        "--start", type=int, default=0, metavar="K",
        help="index of the first number to enumerate (default: 0)",
    )
    parser.add_argument(
        "--json", action="store_true",
        help="print the numbers as a JSON array",
    )
    args = parser.parse_args()

    if args.n < 0:
        parser.error("n must be non-negative")
    if args.start < 0:
        parser.error("--start must be non-negative")

    numbers = list(fibonacci(args.n, args.start))
    if args.json:
        print(json.dumps(numbers))
    else:
        for value in numbers:
            print(value)


if __name__ == "__main__":
    main()
