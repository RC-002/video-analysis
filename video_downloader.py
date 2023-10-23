# video_downloader.py

# imports
import re
import os
import configparser
from pytube import YouTube

# config file
config_filename="config.ini"

def download_video(video_id):
    # Initialize the configuration parser
    config = configparser.ConfigParser()

    # Load and read the configuration file
    config.read(config_filename)

    # Extract parameters from the configuration
    output_dir = config.get("Download", "download_path", fallback="videos")

    # YouTube video URL
    video_url = 'https://www.youtube.com/watch?v=' + video_id

    # Extract the video ID from the URL
    video_id = re.search(r'[?&]v=([^&]+)', video_url).group(1)

    # Construct the file name
    output_filename = f"{video_id}.mp4"

    # Construct the output_path
    output_path = os.path.join(output_dir, output_filename)

    # Create youtube stream object
    yt = YouTube(video_url)

    print(f"Video-namme: '{yt.title}'")
    # check if video exists already, else download it
    if not os.path.exists(output_path):
        stream = yt.streams.get_highest_resolution()
        stream.download(output_path=output_dir, filename=output_filename)

    print(f"Download Status: Successful!")
    return True

if __name__ == "__main__":
    download_video()
    
