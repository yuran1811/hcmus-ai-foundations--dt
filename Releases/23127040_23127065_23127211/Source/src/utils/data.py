import os
import tomllib

from constants.path import ROOT_DIR


def get_project_toml_data() -> dict:
    try:
        with open(os.path.join(ROOT_DIR, "pyproject.toml"), "rb") as f:
            return tomllib.load(f)["project"]
    except FileNotFoundError:
        return {}
