# 3D Image dataset generation using Maya


1- I was assigned task to Study Maya and get used to its various functionalities, scripting and other parameters

2- I went through all the videos of Maya which covered the following points

a-Understanding MEL (Maya Embedded Language)
<br>
b-Implementing MEL Scripts for creating basic 3d objects like shperes and cubes
<br>
c-Understanding Python Scripts
<br>
d-Implementing Python scripts for creating basic 3d objects like polygons, planes and cubes
<br>
f- Going through documentation of Maya 
<br>
https://knowledge.autodesk.com/support/maya/getting-started/caas/simplecontent/content/maya-documentation.html
<br>
Understanding various methods like getAttr, setAttr, ls and other useful methods
<br>
![alt text](https://github.com/nikunjlad/3D-Object-Classification-Using-Capsule-Networks/blob/aditya/Maya3D-Images-Dataset/Aditya/Capture_getAttr.JPG)
The above image is one of the attributes named Translate of Cube Object. It is used for translating the object among specific axis
<br>
http://help.autodesk.com/cloudhelp/2017/ENU/Maya-Tech-Docs/Commands/getAttr.html
<br>


3- I started working on building a script for rotating the object and capture images in different angles by rotating a camera around it.  Below is the script which includes a function
<br>
![alt text](https://github.com/nikunjlad/3D-Object-Classification-Using-Capsule-Networks/blob/aditya/Maya3D-Images-Dataset/Aditya/Capture_image_script_1.JPG)
<br>
The above script has two user defined functions, one is for storing images and the second one is for capsturing images in different angles
These are images of Dog object captured around YX axis
<br>
![alt text]()
<br>
![alt text]()
<br>
![alt text]()
<br>
<br>
<br>
<br>
I have also used cmds.scale function, in which we can change the distance of the camera from the object in X, Y and Z axis respectively.
<br>
The saveImage function is used to take the snapshot of the images, but later on Akash found a better way of using a renderer which provides images in higher resolution
<br>

Finally after contributions from everyone, the script finalized for capturing the images is given below

<br>
![alt text]()



