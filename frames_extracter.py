# imports
import cv2
import os
import configparser


# config file
config_filename="config.ini"

# download_video("Ln38av8gLng")
# download_video("tPEE9ZwTmy0")

def extract_frames(video_id):
    # Initialize the configuration parser
    config = configparser.ConfigParser()

    # Load and read the configuration file
    config.read(config_filename)

    # Extract parameters from the configuration
    video_dir = config.get("Download", "download_path", fallback="videos")
    frame_dir = config.get("Extract", "frame_path", fallback="frames")
    interval_size = int(config.get("Extract", "interval_size", fallback=60))

    os.makedirs(frame_dir, exist_ok=True)

    # Construct the file name
    video_filename = f"{video_id}.mp4"

    # Construct the output_path
    video_path = os.path.join(video_dir, video_filename)
    frames_path = os.path.join(frame_dir, video_id)

     # check if frames exists already, else download it
    if not os.path.exists(frames_path):
        os.makedirs(frames_path, exist_ok=True)

        # Open the video file
        cap = cv2.VideoCapture(video_path)

        if not cap.isOpened():
            print(f"Frames Extraction: Failure!")
            return [False, None]

        frame_rate = cap.get(cv2.CAP_PROP_FPS)
        frame_interval = int(frame_rate * interval_size)

        frame_count = 0
        frame_name = 1
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            if frame_count % frame_interval == 0:
                frame_filename = os.path.join(frames_path, f"frame_{frame_name}.jpg")
                cv2.imwrite(frame_filename, frame)
                frame_name += 1

            frame_count += 1
        cap.release()
        cv2.destroyAllWindows()
    
    frames_count = num_files = sum(1 for entry in os.scandir(frames_path) if entry.is_file())

    print(f"Frames Extraction: Successful!")
    return [True, frames_count]

if __name__ == "__main__":
    extract_frames()