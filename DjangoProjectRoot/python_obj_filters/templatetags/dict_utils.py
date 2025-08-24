import django.template
from typing import Any


register: django.template.Library = django.template.Library()


@register.filter
def get_dict_value(dictionary: dict[str, Any], key: str) -> Any:
    """Safely get a value from a dictionary."""

    default = f"key: {key} not found in dictionary: {dictionary}"

    return dictionary.get(key, default)