from django.shortcuts import render
from django.http import HttpRequest, HttpResponse



import importlib.util
from typing import Final, Any
from importlib.machinery import ModuleSpec
from types import ModuleType

# ----------------------------------- Import Lib 导入模块 -----------------------------------
# Dynamically import the get_var module
# 动态导入 get_var 模块
get_menu_bar_dict_path: Final[str] = "./lib/get_menu_bar_dict.py"

get_menu_bar_dict_spec: ModuleSpec | None = importlib.util.spec_from_file_location(
    "get_menu_bar_dict", get_menu_bar_dict_path
)
if get_menu_bar_dict_spec is None:
    raise ImportError(f"Could not load spec for {get_menu_bar_dict_path}")

get_menu_bar_dict_module: ModuleType = importlib.util.module_from_spec(get_menu_bar_dict_spec)
# 如果 spec.loader 存在，则存在Module
if get_menu_bar_dict_spec.loader:
    get_menu_bar_dict_spec.loader.exec_module(get_menu_bar_dict_module)


    

# ----------------------------------- HTML Render 页面渲染 -----------------------------------
# Create your views here.
def home_page(request: HttpRequest) -> HttpResponse:
    # 获取菜单栏选项
    menu_bar_item_dict: dict[str, Any] = get_menu_bar_dict_module.get_menu_bar_dict()
    
    print(menu_bar_item_dict)

    return render(request, './html/home_page/home_page.html', {
        **menu_bar_item_dict
    })
