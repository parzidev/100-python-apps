"""Simple countdown timer."""

import argparse
import time


def countdown(seconds: int) -> None:
    for remaining in range(seconds, -1, -1):
        print(f"Time left: {remaining} seconds", end="\r", flush=True)
        time.sleep(1)
    print("\nTime's up!")


def main() -> None:
    parser = argparse.ArgumentParser(description="Start a countdown timer.")
    parser.add_argument("seconds", type=int, help="Number of seconds to count down.")
    args = parser.parse_args()

    countdown(args.seconds)


if __name__ == "__main__":
    main()
