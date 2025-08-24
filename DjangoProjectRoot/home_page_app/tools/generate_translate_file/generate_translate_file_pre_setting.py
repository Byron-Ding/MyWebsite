import json
from typing import Any
import os


# 注意这个脚本单独执行，路径是相对于这个脚本的路径
menu_bar__item_text__json_path: str = "dynamic_resources/settings/menu_items.json"

with open(menu_bar__item_text__json_path, encoding="utf-8") as f:
    data: dict[str, Any] = json.load(f)

# 取所有菜单项
menu_items: dict[str, Any] = data["menu_items"]
menu_items_order: list[str] = data["menu_items_order"]



# 预建表
translation_keys: list[tuple[str, str]] = []

# 取单独菜单项  的翻译键
for item_key in menu_items_order:
    item: dict[str, Any] = menu_items[item_key]
    
    
    page_name: str = item["page_name"]
    if page_name:
        translation_keys.append((page_name, item_key))

# 切换工作目录到当前文件
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# 输出为 .po 格式
# ./cache/generated_translation_keys.po
if not os.path.exists("./cache"):
    os.makedirs("./cache")

with open("./cache/generated_translation_keys.po", "w", encoding="utf-8") as f:
    for key, value in translation_keys:
        # 注释
        f.write(f'# Content for {value}\n')
        f.write(f'msgid "{key}"\nmsgstr ""\n')
        # 空行分隔
        f.write("\n")
