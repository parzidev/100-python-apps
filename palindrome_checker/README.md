# Palindrome Checker CLI

Determine whether a given piece of text is a palindrome right from the terminal.

## Features
- Optional case-insensitive comparisons.
- Optionally ignore whitespace characters before evaluating.
- Accepts input either as a command-line argument or via interactive prompt.

## Usage
```bash
python app.py [TEXT] [--ignore-case] [--ignore-spaces]
```
- `TEXT` *(optional)* – the string to inspect. When omitted the program will prompt for input.
- `--ignore-case` – treat uppercase and lowercase letters as identical.
- `--ignore-spaces` – strip all whitespace characters before checking.

## Examples
```bash
python app.py "Never odd or even" --ignore-case --ignore-spaces
python app.py racecar
```
