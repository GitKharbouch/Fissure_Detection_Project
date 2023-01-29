




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
