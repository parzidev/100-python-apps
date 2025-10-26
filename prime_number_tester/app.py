"""Check if a number is prime."""

import argparse
import math


def is_prime(number: int) -> bool:
    if number < 2:
        return False
    if number in (2, 3):
        return True
    if number % 2 == 0:
        return False
    limit = int(math.sqrt(number)) + 1
    for candidate in range(3, limit, 2):
        if number % candidate == 0:
            return False
    return True


def main() -> None:
    parser = argparse.ArgumentParser(description="Determine whether a number is prime.")
    parser.add_argument("number", type=int, help="Number to test.")
    args = parser.parse_args()

    result = is_prime(args.number)
    if result:
        print(f"{args.number} is a prime number.")
    else:
        print(f"{args.number} is not a prime number.")


if __name__ == "__main__":
    main()
