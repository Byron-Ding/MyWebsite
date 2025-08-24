import importlib.util
import json
from typing import Final, Any
from importlib.machinery import ModuleSpec
from types import ModuleType

# ----------------------------------- Import Lib 导入模块 -----------------------------------
# # Dynamically import the get_var module
# # 动态导入 get_var 模块
# get_var_lib_path: Final[str] = "./home_page_app/get_vars.py"

# get_var_module_spec: ModuleSpec | None = importlib.util.spec_from_file_location(
#     "get_var", get_var_lib_path
# )
# if get_var_module_spec is None:
#     raise ImportError(f"Could not load spec for {get_var_lib_path}")

# get_var_module: ModuleType = importlib.util.module_from_spec(get_var_module_spec)
# # 如果 spec.loader 存在，则存在Module
# if get_var_module_spec.loader:
#     get_var_module_spec.loader.exec_module(get_var_module)


# ----------------------------------- Constants 常量 -----------------------------------
menu_items_json_path: Final[str] = r"./dynamic_resources/settings/menu_items.json"
translate_form_json_file_path: Final[str] = r"./dynamic_resources/settings/translate_form.json"

# ----------------------------------- Core 核心函数 -----------------------------------
# ----------------------------------- Get  Variables 获取变量 -----------------------------------
def get_menubar_items_var_dict() -> dict[str, Any]:

    with open(menu_items_json_path, "r", encoding="utf-8") as menu_items_json_file:
        # 获取用于a标签的动态数量的menubar item
        menu_bar_item_json: dict[str, Any] = json.load(
            menu_items_json_file
        )

        
        # 获取菜单栏标签顺序
        menu_bar_item_url_order_list: list[str] = menu_bar_item_json["menu_items_order"]
        
        menu_bar_item_url_dict: dict[str, dict[str, str]] = menu_bar_item_json["menu_items"]
        
    # 最后集体传给HTML Templates

    return {
        "menu_items_order": menu_bar_item_url_order_list,
        "menu_items": menu_bar_item_url_dict
    }


def get_translate_form_var_dict() -> dict[str, Any]:
    with open(translate_form_json_file_path, "r", encoding="utf-8") as translate_form_json_file:
        translate_form_json: dict[str, Any] = json.load(translate_form_json_file)

    # 获取“language”的翻译
    translate_form_translate_form_titles: dict[str, str] = translate_form_json["translate_form_titles"]

    # 获取翻译表单选项
    translate_form_language_options: list[dict[str, str]] = translate_form_json["language_options"]
    
    # 语言顺序
    translate_form_language_options_order: list[str] = translate_form_json["language_options_order"]
    
    

    return {
        "translate_form_titles": translate_form_translate_form_titles,
        "language_options": translate_form_language_options,
        "language_options_order": translate_form_language_options_order
    }
    

def get_menu_bar_dict() -> dict[str, Any]:
    # 获取菜单栏选项
    # Subitems
    # menu_bar_item_url_order_list: list[str]
    # menu_bar_item_url_dict: dict[str, dict[str, str]]
    menu_bar_item_dict: dict[str, Any] = get_menubar_items_var_dict()

    # 获取翻译表单选项
    translate_form_dict: dict[str, Any] = get_translate_form_var_dict()



    return {
        'default_menubar': {
            'menu_items': menu_bar_item_dict,
            # Translate form
            'translate_form': translate_form_dict
        }
    }