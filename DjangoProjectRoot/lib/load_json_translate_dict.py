import json
from typing import Final

translate_dictionary_path: Final[str] = r"dynamic_resources/settings/translate.json"

from typing import Any

def return_translate_dictionary_by_lang(lang: str) -> dict[str, Any]:
    # Load the JSON file
    with open(translate_dictionary_path, "r", encoding="utf-8") as file:
        translate_dict: dict[str, Any] = json.load(file)

        # Return the translation dictionary for the specified language
    return translate_dict.get(lang, {})