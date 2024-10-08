# audio-slicer

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

A tool for slicing an audio file into individual parts based on specific times, e.g. a music album audio file into individual songs based on specific song start times.

## Requirements

This tool requires an external Python module pydub and FFmpeg. FFmpeg can be installed with the help of [this article](https://www.hostinger.com/tutorials/how-to-install-ffmpeg). The tool was tested with Python **3.11.0**, pydub **0.25.1** and FFmpeg **5.1**.

## How to slice

### 1. Input directory

To slice an audio file, paste it into the `input` directory. If you want the newly created audio parts to have a cover art, also paste this cover art image into the `input` directory.

### 2. Definition of audio parts

Next, open `songs.txt`. Each audio part must occupy exactly one line. The line **can** include the audio part's number and **must** include its name and the time at which it begins in the original large audio file (in the standard MM:SS or HH:MM:SS format).

The audio part definitions in the `songs.txt` file should look like this (with your own custom names and times):

```
1 - Lorem Ipsum 00:00
2 - Dolor Sit 07:32
3 - Amet Consectetur 58:17
4 - Adipiscing 02:03:21
```

or

```
00:00 Lorem Ipsum
07:32 Dolor Sit
58:17 Amet Consectetur
02:03:21 Adipiscing
```

### 3. Config

Now, open `config.txt`, where you will define how the tool will interpret and save the audio parts.

By default, the `config.txt` file looks like this:

```
Audio Filename: "audio.mp3"
Song Pattern: "song_number - song_name start_time"
Album Artist(s): "artist"
Album Title: "title"
Cover Art Filename: "image.png"
```

On each line, replace **only** the text between the quotation marks.

- The *Audio Filename* value tells the tool which audio file it should load. **Do not** include the path to the file, only its name and extension (the file must be located in the `input` directory).

- The *Song Pattern* value tells the tool how the audio parts in the `songs.txt` file are defined. For example, if we were to define an audio part in the `songs.txt` file like this:
  ```
  1 - Lorem Ipsum 00:00
  ```
  then, the *Song Pattern* value would have to look this:
  ```
  song_number - song_name start_time
  ```
  If the audio part definition looked like this:
  ```
  00:00 Lorem Ipsum
  ```
  then, the *Song Pattern* value would have to look this:
  ```
  start_time song_name
  ```
  When defining a custom pattern, use the keyword **song_number** for the audio part's number (optional), **song_name** for its name and **start_time** for its start time (both required).

  **All audio parts in the `songs.txt` file must be defined with the same pattern.**
  
  Note: You can use words and symbols in the audio parts definitions and patterns, e.g. like this:
  Audio part definition:
  ```
  Song #1. Lorem Ipsum, starting at 00:00!
  ```
  Pattern:
  ```
  Song #song_number. song_name, starting at start_time!
  ```

- The *Album Artist(s)* value tells the tool which artists it should write into the audio parts' metadata. This value can be empty.

- The *Album Title* value tells the tool which album the audio parts come from. The album name is written into the audio parts' metadata. This value can be empty.

- The *Cover Art Filename* value tells the tool which image it should use in the audio parts' metadata. **Do not** include the path to the file, only its name and extension (the file must be located in the `input` directory). This value can be empty.

### 4. Run the tool

Run the tool with `python main.py`. Then, wait for the tool to announce a successful finish.

### 5. Output directory

The audio parts created by the tool will be located in the `output` directory (if value for *Album Title* was given, they will be located in a new sub-directory with the same name).

## Footnote

Thank you for using my tool.

If you find a bug, feel free to create a pull request or a bug report. If you'd like help, feel free to contact me.
