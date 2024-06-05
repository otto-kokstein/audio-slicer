from typing import *


def create_regex_pattern(pattern: str) -> str:
    regex_pattern: str = pattern

    # Define a string with regex functional characters
    FUNCTIONAL_CHARS: str = "[](){}*+?|^$.\\"

    # Escape functional chars so we can use the string as a regex pattern
    # I don't think it should be this complicated
    regex_pattern_as_list: List[str] = list(regex_pattern)
    for i in reversed(range(len(regex_pattern_as_list))):
        char = regex_pattern_as_list[i]
        if char in FUNCTIONAL_CHARS:
            regex_pattern_as_list.insert(i, "\\")
    regex_pattern = "".join(regex_pattern_as_list)

    regex_pattern = regex_pattern.replace("song_number", "\\d+", 1)
    regex_pattern = regex_pattern.replace("song_name", "(.+)", 1)
    regex_pattern = regex_pattern.replace("start_time", "((\\d{2}):)?(\\d{2}):(\\d{2})", 1)
    regex_pattern = "^" + regex_pattern + "$"

    return regex_pattern
