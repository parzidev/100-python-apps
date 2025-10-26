"""Convert temperatures between Celsius and Fahrenheit."""

import argparse
from typing import Callable


def celsius_to_fahrenheit(value: float) -> float:
    return (value * 9 / 5) + 32


def fahrenheit_to_celsius(value: float) -> float:
    return (value - 32) * 5 / 9


CONVERSIONS: dict[str, tuple[str, Callable[[float], float]]] = {
    "c2f": ("Celsius", celsius_to_fahrenheit),
    "f2c": ("Fahrenheit", fahrenheit_to_celsius),
}


def main() -> None:
    parser = argparse.ArgumentParser(description="Convert between Celsius and Fahrenheit.")
    parser.add_argument("mode", choices=CONVERSIONS.keys(), help="Conversion mode: c2f or f2c.")
    parser.add_argument("value", type=float, help="Temperature value to convert.")
    args = parser.parse_args()

    unit, converter = CONVERSIONS[args.mode]
    target_unit = "Fahrenheit" if unit == "Celsius" else "Celsius"
    result = converter(args.value)
    print(f"{args.value:.2f} {unit} is {result:.2f} {target_unit}.")


if __name__ == "__main__":
    main()
