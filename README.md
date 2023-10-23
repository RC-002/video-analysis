# Video Analysis of Youtube Videos
A frame by frame analysis of videos

## Steps to run the code

- Replace the ```key``` and ```model_id``` with your model and key (Clarifai)
- create a virtual environment using the command ```python -m venv myenv```
- Activate the virtual environment
- Download the packages from the ```requirements.txt``` file
- Run the ```main.py``` file and enter the ID of any youtube video.
<br>For the url of this video, *https://www.youtube.com/watch?v=tPEE9ZwTmy0*, **tPEE9ZwTmy0** is the ID.

## Design Considerations

 - Modular (high cohesion and low coupling)
 - Externalized configurations
 - The outputs from each stage is recorded to avoid recomputation.Based on cofigs, we perform space optimizations
