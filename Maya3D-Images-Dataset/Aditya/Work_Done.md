# 3D Image dataset generation using Maya

####Exploring Maya and Creating Python Script
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
<br>
The above image is one of the attributes named Translate of Cube Object. It is used for translating the object among specific axis
<br>
http://help.autodesk.com/cloudhelp/2017/ENU/Maya-Tech-Docs/Commands/getAttr.html
<br>


3- I started working on building a script for rotating the object and capture images in different angles by rotating a camera around it.  Below is the script which includes a function
<br>
![alt text](https://github.com/nikunjlad/3D-Object-Classification-Using-Capsule-Networks/blob/aditya/Maya3D-Images-Dataset/Aditya/Capture_image_script_1.JPG)
<br>
The above script has two user defined functions, one is for storing images and the second one is for capsturing images in different angles
<br>
I have also used cmds.scale function, in which we can change the distance of the camera from the object in X, Y and Z axis respectively.
<br>
The saveImage function is used to take the snapshot of the images, but later on Akash found a better way of using a renderer which provides images in higher resolution
<br>
These are images of Dog object captured around YX axis
<br>
![alt text](https://github.com/nikunjlad/3D-Object-Classification-Using-Capsule-Networks/blob/aditya/Maya3D-Images-Dataset/Aditya/image10_10_YXSnapshot.jpg)
<br>
<br>
![alt text](https://github.com/nikunjlad/3D-Object-Classification-Using-Capsule-Networks/blob/aditya/Maya3D-Images-Dataset/Aditya/image10_20_YXSnapshot.jpg)
<br>
![alt text](https://github.com/nikunjlad/3D-Object-Classification-Using-Capsule-Networks/blob/aditya/Maya3D-Images-Dataset/Aditya/image10_30_YXSnapshot.jpg)
<br>
<br>
The below images shows, how the camera is rotating around dog for capturing the images in different angles
<br>
![alt text](https://github.com/nikunjlad/3D-Object-Classification-Using-Capsule-Networks/blob/aditya/Maya3D-Images-Dataset/Aditya/end10_Y_100Snapshot.jpg)
<br>
<br>
![alt text](https://github.com/nikunjlad/3D-Object-Classification-Using-Capsule-Networks/blob/aditya/Maya3D-Images-Dataset/Aditya/end20_Y_100Snapshot.jpg)
<br>
<br>
![alt text](https://github.com/nikunjlad/3D-Object-Classification-Using-Capsule-Networks/blob/aditya/Maya3D-Images-Dataset/Aditya/end30_Y_100Snapshot.jpg)


Finally after contributions from everyone, the script finalized for capturing the images is given below

<br>
![alt text](https://github.com/nikunjlad/3D-Object-Classification-Using-Capsule-Networks/blob/aditya/Maya3D-Images-Dataset/Aditya/final_script_image.JPG)
<br>
##Setting Up the Right Environment
<br>
1-I figured out and explored the implementations of shaders and textures on various objects. There are different kind of shaders in Maya which can be assigned to objects by using Assign New Material or existing Material. There are some inbuilt materials included in Maya like Lambert, Blinn, Layered Shader and so on
<br>
All these materials have some of the common attributes which give either a glossy or plain, either a colorfull or grayscale look to the objects.
<br>
Some of the attributes I tried are
<br>
####Color, Incandescence, Transparency and Transluscence Depth
<br>
2- Some of the objects have had their predefined textures which I had to import directly and assigned to respective objects.
<br>
3-Background of objects also played a important role in defining attributes. I tried to set up environment by inserting curved planes in the background of objects so as to avoid any noise in the form of lines.
<br>
![alt text](https://github.com/nikunjlad/3D-Object-Classification-Using-Capsule-Networks/blob/aditya/Maya3D-Images-Dataset/Aditya/folding_plane_capture.JPG)
<br>
In the above image, you can see that the plane has been folded from one side so that light falls on the object properly and there is sharp change in the background of image in terms of gradient and colors
<br>










