from ROOT_FILES.ROOT_PATH import ROOT_PATH
from pathlib import Path
from typing import *


def load_song_list() -> List[str]:
    song_list: List[str] = [line.rstrip("\n\t ") for line in open(str(Path(ROOT_PATH, "songs.txt").resolve())).readlines()]
    song_list = list(filter(None, song_list))

    if len(song_list) == 0:
        raise ValueError("No songs in songs.txt!")

    return song_list
