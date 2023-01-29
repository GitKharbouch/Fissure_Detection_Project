# Contents

    - The main file is Fiss_Detect.py running this file achieves the function of this project,it calls for two functions
    Notify.py and critic.py explained in the FUNCTIONS section.
    - yolov5-master is the yolo file to make our custom model work.
    - data contains the images of critic fissures that get saved while the program is running, an excel file containing 
    data about the fissures detected(coordinates,dimensions,time...),and a test video of our model.


# REQUIREMENTS

### yolov5 requirements:

The requirements file can be found inside the yolov5-master file, 
you can run it using the command : pip install -r requirements.txt

### Fissure detection script requirement:

The requirements file can be found inside the main file, 
you can run it using the command : pip install -r requirements.txt



# FUNCTIONS


## critic
Critic(x,y,w,h,j) is a function that takes five arguments (Coordinates, dimensions and frame number) and returns critique as True if the fissure is considered critic (Rules by a set of conditions) or False if it is not.

## notify
Notify() is a function that sends a windows notification and an email to notify that a critic fissure had been detected.


# Data

the data file contains a test video and the excel file containing coordinates and time of each fissure.
