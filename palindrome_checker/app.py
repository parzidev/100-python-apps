"""Palindrome checker CLI.

Usage::
    python app.py --text "Never odd or even" --ignore-spaces --ignore-case
"""

import argparse


def normalize_text(text: str, ignore_case: bool, ignore_spaces: bool) -> str:
    if ignore_case:
        text = text.lower()
    if ignore_spaces:
        text = "".join(text.split())
    return text


def is_palindrome(text: str, ignore_case: bool = True, ignore_spaces: bool = True) -> bool:
    cleaned = normalize_text(text, ignore_case, ignore_spaces)
    return cleaned == cleaned[::-1]


def main() -> None:
    parser = argparse.ArgumentParser(description="Check whether a piece of text is a palindrome.")
    parser.add_argument("text", nargs="?", help="Text to check. If omitted, read from stdin.")
    parser.add_argument("--ignore-case", action="store_true", default=False, help="Ignore letter casing.")
    parser.add_argument("--ignore-spaces", action="store_true", default=False, help="Ignore whitespace characters.")
    args = parser.parse_args()

    if args.text:
        text = args.text
    else:
        text = input("Enter text to check: ")

    result = is_palindrome(text, args.ignore_case, args.ignore_spaces)
    if result:
        print(f"'{text}' is a palindrome!")
    else:
        print(f"'{text}' is not a palindrome.")


if __name__ == "__main__":
    main()
