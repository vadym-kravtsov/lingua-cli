# lingua-cli

A tiny DeepL-powered CLI translator for quick Ukrainian/English swaps.

## Install

```bash
python -m pip install -e .
```

Set your DeepL key:

```bash
export DEEPL_KEY="your-api-key"
```

## Usage

```bash
t "привіт, світ"
t "hello world"
```

The tool auto-detects whether the input is mostly Ukrainian or English and translates into the other language.
