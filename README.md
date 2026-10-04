## lingua-cli

A tiny DeepL-powered CLI translator for quick Ukrainian/English swaps.

### Install

Install it directly from GitHub without cloning the repo:

```bash
python -m pip install "git+https://github.com/vadym-kravtsov/lingua-cli.git"
```

Set your DeepL key:

```bash
export DEEPL_KEY="your-api-key"
```

### Usage

```bash
t "привіт, світ"
t "hello world"
```

### Remove

If you installed it with pip, remove it like this:
```bash
python -m pip uninstall lingua-cli
```
The tool auto-detects whether the input is mostly Ukrainian or English and translates into the other language.
