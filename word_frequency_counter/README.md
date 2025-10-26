# Word Frequency Counter

Analyze text input or files and display the most common words.

## Features
- Accepts text through an interactive prompt or a file path.
- Displays the top *N* most frequent words with counts.
- Treats words case-insensitively and ignores punctuation.

## Usage
```bash
python app.py [--file PATH] [--top N]
```
- `--file` – path to a UTF-8 encoded text file to analyze.
- `--top` – number of top results to display (default: 10).

## Examples
```bash
python app.py --file sample.txt --top 5
python app.py
```
