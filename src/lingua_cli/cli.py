import os
import sys
import deepl
import argparse


def main():
    parser = argparse.ArgumentParser(description=".....")
    parser.add_argument("text", help="text to translate", nargs="+")
    args = parser.parse_args()
    text = " ".join(args.text)

    if any(char in "абвгґдеєжзиіїйклмнопрстуфхцчшщьюя" for char in text.lower()):
        target_lang = "EN-US"
    else:
        target_lang = "UK"

    api_key = os.environ["DEEPL_KEY"]

    if not api_key:
        raise ValueError("DEEPL_KEY environment variable is not set")

    translator = deepl.Translator(api_key)
    try:
        result = translator.translate_text(text, target_lang=target_lang)
    except deepl.DeepLException as e:
        print(f"Translation error: {e}", file=sys.stderr)
        sys.exit(1)

    print(str(result))
