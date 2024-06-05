from typing import *
import re
from ROOT_FILES.regex_pattern_creator import create_regex_pattern
from ROOT_FILES.song_list_loader import load_song_list


def get_song_times(pattern: str) -> List[Tuple[str, int, int]]:
    song_list: List[str] = load_song_list()

    song_times: List[Tuple[str, int, int]] = []

    regex_pattern: str = create_regex_pattern(pattern)

    for song in song_list:
        song = song.strip("\n ")
        regex_match: re.Match[str] | None = re.search(regex_pattern, song)
        if regex_match is not None:
            song_name: str = regex_match.group(1)
            hours: int = (
                int(regex_match.group(3)) if regex_match.group(3) is not None else 0
            )
            minutes: int = int(regex_match.group(4))
            seconds: int = int(regex_match.group(5))
            song_start_time: int = 1000 * (
                3600 * hours + 60 * minutes + seconds
            )  # Song start time in milliseconds
            song_times.append((song_name, song_start_time, -1))

    for n, song_time in enumerate(song_times):
        song_name: str = song_time[0]
        start_time: int = song_time[1]
        end_time: int = song_time[2]
        if n < len(song_times) - 1:
            end_time = song_times[n + 1][1]
        song_times[n] = (song_name, start_time, end_time)
        
    if len(song_times) == 0:
        raise ValueError("No songs identified in songs.txt, value for Song Pattern in config.txt is probably incorrect!")

    return song_times
