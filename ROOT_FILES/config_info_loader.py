from ROOT_FILES.ROOT_PATH import ROOT_PATH
from pathlib import Path
from typing import *


def load_config_info() -> Dict[str, str]:
    config_info_dict: Dict[str, str] = {}

    config_info_list: List[str] = open(
        str(Path(ROOT_PATH, "config.txt").resolve())
    ).readlines()

    for line in config_info_list:
        dict_key: str = line[: line.find(":")]
        dict_value: str = line[line.find('"') + 1 : line.rfind('"')]

        if len(dict_value) == 0:
            raise ValueError(f"No value for key \"{dict_key}\" in config.txt!")

        config_info_dict[dict_key] = dict_value

    return config_info_dict
