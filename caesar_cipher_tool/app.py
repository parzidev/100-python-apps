"""Caesar cipher encoder and decoder."""

import argparse
import string

ALPHABET = string.ascii_lowercase


def shift_char(char: str, shift: int) -> str:
    if char.lower() not in ALPHABET:
        return char
    base = ALPHABET.index(char.lower())
    shifted = ALPHABET[(base + shift) % len(ALPHABET)]
    return shifted.upper() if char.isupper() else shifted


def transform_text(text: str, shift: int) -> str:
    return "".join(shift_char(ch, shift) for ch in text)


def main() -> None:
    parser = argparse.ArgumentParser(description="Encode or decode messages using the Caesar cipher.")
    parser.add_argument("text", help="Text to transform.")
    parser.add_argument("--shift", type=int, default=3, help="Shift amount (positive to encode, negative to decode).")
    args = parser.parse_args()

    print(transform_text(args.text, args.shift))


if __name__ == "__main__":
    main()
