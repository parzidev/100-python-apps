"""Generate a multiplication table for a given number."""

import argparse
from typing import List


def build_table(number: int, upto: int) -> List[str]:
    return [f"{number} x {i} = {number * i}" for i in range(1, upto + 1)]


def main() -> None:
    parser = argparse.ArgumentParser(description="Create a multiplication table for a number.")
    parser.add_argument("number", type=int, help="Number for which to create the table.")
    parser.add_argument("--upto", type=int, default=10, help="How far the table should go (default: 10).")
    args = parser.parse_args()

    for line in build_table(args.number, args.upto):
        print(line)


if __name__ == "__main__":
    main()
