"""Count word frequencies in a text source."""

import argparse
import re
from collections import Counter
from pathlib import Path
from typing import Iterable

WORD_RE = re.compile(r"[A-Za-z']+")


def tokenize(text: str) -> Iterable[str]:
    return (match.group(0).lower() for match in WORD_RE.finditer(text))


def count_words(text: str) -> Counter[str]:
    return Counter(tokenize(text))


def read_input(path: str | None) -> str:
    if path:
        return Path(path).read_text(encoding="utf-8")
    return input("Enter text to analyze: ")


def main() -> None:
    parser = argparse.ArgumentParser(description="Count word frequencies in text.")
    parser.add_argument("--file", help="Path to a text file. If omitted, reads from stdin.")
    parser.add_argument("--top", type=int, default=10, help="Number of top words to show.")
    args = parser.parse_args()

    text = read_input(args.file)
    counter = count_words(text)

    for word, freq in counter.most_common(args.top):
        print(f"{word}: {freq}")


if __name__ == "__main__":
    main()
