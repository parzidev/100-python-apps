"""Simple command-line stopwatch."""

import time


def main() -> None:
    input("Press Enter to start the stopwatch...")
    start = time.perf_counter()
    input("Press Enter to stop the stopwatch...")
    end = time.perf_counter()
    elapsed = end - start
    print(f"Elapsed time: {elapsed:.3f} seconds")


if __name__ == "__main__":
    main()
