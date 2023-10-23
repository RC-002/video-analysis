# Video Analysis of YouTube Videos
A frame-by-frame analysis of videos

## Steps to run the code

- Replace the ```key``` and ```model_id``` with your model and key (Clarifai)
- create a virtual environment using the command ```python -m venv myenv```
- Activate the virtual environment
- Download the packages from the ```requirements.txt``` file
- Run the ```main.py``` file and enter the ID of any YouTube video.
<br>For example, in the given youtube link, *https://www.youtube.com/watch?v=tPEE9ZwTmy0*, **tPEE9ZwTmy0** is the ID.

## Design Considerations

 - Modular (high cohesion and low coupling)
 - Externalized configurations
 - The outputs from each stage are recorded to avoid recomputation. Based on configs, we perform space optimizations
