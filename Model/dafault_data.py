import ast
import os
from pathlib import Path
from typing import Union

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR.joinpath("assets", "data")


def get_data(path_to_json_file: str) -> Union[dict, list, None]:
    """Sets a dictionary/list of values from a `*.json` file."""

    if os.path.exists(path_to_json_file):
        with open(path_to_json_file, encoding="utf-8") as json_file:
            return ast.literal_eval(json_file.read())
