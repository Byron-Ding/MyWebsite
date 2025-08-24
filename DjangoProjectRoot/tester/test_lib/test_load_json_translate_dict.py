import importlib.util
import pathlib


file_path = pathlib.Path("../../DjangoProjectInnerRoot/lib/load_json_translate_dict.py").resolve()
print(file_path)

# Dynamically import the module
spec = importlib.util.spec_from_file_location("load_json_translate_dict", file_path)
load_json_translate_dict = importlib.util.module_from_spec(spec)
spec.loader.exec_module(load_json_translate_dict)


def test_return_translate_dictionary_by_lang(lang: str = "zh-cn"):
    # Test for English translations
    print(load_json_translate_dict.return_translate_dictionary_by_lang(lang))
    
    
test_return_translate_dictionary_by_lang(lang="en-us")