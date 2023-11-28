import json
from typing import Dict
from django.utils import timezone


def Initialize_env_variables(json_file: json, module_name: str):
    with open(json_file, "r") as f:
        config: Dict = json.load(f)

    for key, value in config.items():
        setattr(module_name, key, value)


def year_standard_format(year_int_type: int) -> str:
    """년도 정규 포맷"""
    year_string: str = str(year_int_type)

    if len(year_string) == 2:
        return f"20{year_string}"
    return year_string


def get_current_date():
    return timezone.now().date()
