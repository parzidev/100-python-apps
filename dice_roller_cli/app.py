"""Roll virtual dice."""

import argparse
import random
from typing import List


def roll_dice(count: int, sides: int) -> List[int]:
    return [random.randint(1, sides) for _ in range(count)]


def main() -> None:
    parser = argparse.ArgumentParser(description="Roll dice and show the results.")
    parser.add_argument("count", type=int, help="Number of dice to roll.")
    parser.add_argument("sides", type=int, default=6, nargs="?", help="Number of sides per die (default: 6).")
    args = parser.parse_args()

    results = roll_dice(args.count, args.sides)
    total = sum(results)
    print("Rolls:", ", ".join(map(str, results)))
    print("Total:", total)


if __name__ == "__main__":
    main()
