# Caesar Cipher Tool

Encode or decode text using a classic Caesar cipher implementation.

## Features
- Supports custom positive or negative shift values.
- Preserves the case of alphabetic characters and leaves punctuation intact.
- Works for both encoding and decoding messages.

## Usage
```bash
python app.py TEXT [--shift N]
```
- `TEXT` – the message to transform.
- `--shift` – integer shift to apply (default: 3). Use a negative value to decode.

## Examples
```bash
python app.py "attack at dawn" --shift 5
python app.py Fyyfhp fy ifbs --shift -5
```
