"""Calculate Body Mass Index (BMI)."""

import argparse


CATEGORIES = [
    (18.5, "Underweight"),
    (25, "Normal weight"),
    (30, "Overweight"),
    (float("inf"), "Obesity"),
]


def calculate_bmi(weight_kg: float, height_cm: float) -> float:
    height_m = height_cm / 100
    return weight_kg / (height_m ** 2)


def categorize_bmi(bmi: float) -> str:
    for threshold, category in CATEGORIES:
        if bmi < threshold:
            return category
    return "Unknown"


def main() -> None:
    parser = argparse.ArgumentParser(description="Calculate BMI from weight and height.")
    parser.add_argument("weight", type=float, help="Weight in kilograms.")
    parser.add_argument("height", type=float, help="Height in centimeters.")
    args = parser.parse_args()

    bmi = calculate_bmi(args.weight, args.height)
    category = categorize_bmi(bmi)
    print(f"BMI: {bmi:.2f} ({category})")


if __name__ == "__main__":
    main()
