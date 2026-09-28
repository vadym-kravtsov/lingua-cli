import deepl
import os
def main():
    api_key = os.environ["DEEPL_KEY"]

    translator = deepl.Translator(api_key)

    result = translator.translate_text("Hello World", target_lang="UK")
    print(str(result))