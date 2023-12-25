# video-reencoder
A simple Python script to re-encode videos in a directory using FFmpeg. This script scans for video files in the current directory and re-encodes them to H.264 (libx264) format with a framerate of 24 fps, while removing the audio. Post re-encoding, the original video file is deleted and the progress is displayed in the terminal.

## Dependencies
FFmpeg
Python 3.x
tqdm

## Installation
Ensure you have FFmpeg installed on your system. You can download it from the official website.

Install the required Python libraries using pip:
pip install tqdm

Clone the repository:
git clone https://github.com/loris-cecks/video-reencoder.git
cd video-reencoder

## Usage
Place the videos you want to re-encode in the same directory as the reencode.py script.
Run the script: python reencode.py

The script will automatically process all video files in the directory (except those already re-encoded), re-encoding them, removing the original files, and displaying the progress in the terminal.
