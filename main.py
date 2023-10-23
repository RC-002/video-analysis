# imports
import configparser
import os

# file imports
from video_downloader import *
from frames_extracter import *
from frame_detector import *

def main():
    print("Enter the id of the youtube video: ")
    # videoId = "Ln38av8gLng"
    videoId = input().strip()

    # Initialize the configuration parser
    config = configparser.ConfigParser()

    # Load and read the configuration file
    config_filename = "./config.ini"
    config.read(config_filename)

    # Extract detection path from the configuration
    detection_path = config.get("Extract", "detection_path", fallback="extraction")
    detectionFile = os.path.join(detection_path, "{}.txt".format(videoId))

     # check if frames exists already, else download it
    if not os.path.exists(detectionFile):
        downloadStatus = download_video(videoId)

        if not downloadStatus:
            print("There is some error")
            exit()

        extractStatus = extract_frames(videoId)

        if not extractStatus[0]:
            print("There is some error")
            exit()

        get_frame_attributes(videoId, extractStatus[1])
    
    with open(detectionFile, "r") as file:
        print(file.read())

    print("Video Downloaded and extracted successfully")

if __name__ == "__main__":
    main()
    