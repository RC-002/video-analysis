# imports
import configparser
import os
import shutil

# Clarifai imports
from clarifai_grpc.channel.clarifai_channel import ClarifaiChannel
from clarifai_grpc.grpc.api import service_pb2_grpc
from clarifai_grpc.grpc.api import service_pb2, resources_pb2
from clarifai_grpc.grpc.api.status import status_code_pb2

def get_frame_attributes(video_id, frame_count):
    # Initialize the configuration parser
    config = configparser.ConfigParser()

    # Load and read the configuration file
    config_filename = "./config.ini"
    config.read(config_filename)

    # Extract parameters from the configuration
    key = config.get("Detector", "key", fallback="")
    model_id = config.get("Detector", "model_id", fallback="")
    remove_files = int(config.get("Detector", "remove_files", fallback="0"))
    frame_dir = config.get("Extract", "frame_path", fallback="frames")
    detection_path = config.get("Extract", "detection_path", fallback="extraction")
    frame_dir = config.get("Extract", "frame_path", fallback="frames")
    video_dir = config.get("Download", "download_path", fallback="videos")

    # Clarifai Authentication
    metadata = (('authorization', key),)
    stub = service_pb2_grpc.V2Stub(ClarifaiChannel.get_grpc_channel())

    if key == "" or model_id == "":
        return [False]
    
    frame_detection_path = os.path.join(frame_dir, video_id)
    
    if not os.path.exists(detection_path):
        os.makedirs(detection_path, exist_ok=True)
    
    frame_detection_text = os.path.join(detection_path, "{}.txt".format(video_id))
    for frame_number in range(1, frame_count+1):
        frame_path = os.path.join(frame_detection_path, "frame_{}.jpg".format(frame_number))
        frame_detection_path
        # check if frames exists already, else download it
        if not os.path.exists(frame_path):
            return [False]

        with open(frame_path, "rb") as f:
            file_bytes = f.read()

        request = service_pb2.PostModelOutputsRequest(
            # This is the model ID of a publicly available General model.
            model_id = model_id,
            inputs=[
                resources_pb2.Input(data=resources_pb2.Data(image=resources_pb2.Image(base64=file_bytes)))
            ])
        response = stub.PostModelOutputs(request, metadata=metadata)

        if response.status.code != status_code_pb2.SUCCESS:
            raise Exception("Request failed, status code: " + str(response.status.code))
        
        # Capture all the attributes

        with open(frame_detection_text, "a") as t:
            t.write("Frame {}:\n".format(frame_number))
            # attributes = list()
            for concept in response.outputs[0].data.concepts:
                if(concept.value > 0.8):
                    # attributes.append(concept.name)      
                    t.write("\t-{}\n".format(concept.name))
            t.write("\n")

    print(f"Detection Status: Successful!\n")

    if remove_files == 1:
        # Remove the video and the frames
        frames_path = os.path.join(frame_dir, video_id)  
        video_path = os.path.join(video_dir, "{}.mp4".format(video_id))

        shutil.rmtree(frames_path)
        os.remove(video_path)


if __name__ == "__main__":
    get_frame_attributes()