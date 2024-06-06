from ROOT_FILES.ROOT_PATH import ROOT_PATH
from pathlib import Path
import os
from typing import *
import pydub as pd
from ROOT_FILES.config_info_loader import load_config_info
from ROOT_FILES.song_times_fetcher import get_song_times


def slice_audio() -> None:
    CONFIG_INFO: Dict[str, str] = load_config_info()
    SONGS: List[Tuple[str, int, int]] = get_song_times(CONFIG_INFO["Song Pattern"])
    SOURCE_FILE = pd.AudioSegment.from_file(
        str(Path(ROOT_PATH, f"input/{CONFIG_INFO['Audio Filename']}").resolve())
    )

    # New directory to songs
    SONGS_DIRECTORY_PATH: str = str(
        Path(ROOT_PATH, f"output/{CONFIG_INFO['Album Title']}").resolve()
    ) if CONFIG_INFO['Album Title'] != "" else str(
        Path(ROOT_PATH, f"output/").resolve()
    )

    # Create new directory for songs if it doesn't already exist
    if not os.path.exists(SONGS_DIRECTORY_PATH):
        os.makedirs(SONGS_DIRECTORY_PATH)

    for song_number, (song_name, start_time, end_time) in enumerate(SONGS):
        segment: pd.AudioSegment = SOURCE_FILE[
            start_time : (
                end_time if end_time != -1 else 1000 * SOURCE_FILE.duration_seconds
            )
        ]
        segment.export(
            str(Path(SONGS_DIRECTORY_PATH, f"{song_name}.mp3").resolve()),
            format="mp3",
            id3v2_version="3",
            tags={
                "title": song_name,
                "track": str(song_number + 1),
                "artist": CONFIG_INFO["Album Artist(s)"],
                "album": CONFIG_INFO["Album Title"],
            },
            cover=str(Path(ROOT_PATH, f"input/{CONFIG_INFO['Cover Art Filename']}").resolve())
        )

    print("Audio slicing finished successfully.")
