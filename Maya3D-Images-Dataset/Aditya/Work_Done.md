# 3D Image dataset generation using Maya

## Exploring Maya and Creating Python Script
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
<br> Please refer capture image function
The above script has two user defined functions, one is for storing images and the second one is for capsturing images in different angles
<br>
I have also used cmds.scale function, in which we can change the distance of the camera from the object in X, Y and Z axis respectively.
<br>
The saveImage function is used to take the snapshot of the images, but later on Akash found a better way of using a renderer which provides images in higher resolution
<br>
These are images of Dog object captured around YX axis
<br>
![alt text](https://github.com/nikunjlad/3D-Object-Classification-Using-Capsule-Networks/blob/aditya/Maya3D-Images-Dataset/Aditya/dog_gif.gif)
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

<br>

Finally after contributions from everyone, the script finalized for capturing the images is given below

<br>

![alt text](https://github.com/nikunjlad/3D-Object-Classification-Using-Capsule-Networks/blob/aditya/Maya3D-Images-Dataset/Aditya/final_script_image.JPG)

<br>

Please refer the .py script for actual script in my folder

## Setting Up the Right Environment

<br>
1-I figured out and explored the implementations of shaders and textures on various objects. There are different kind of shaders in Maya which can be assigned to objects by using Assign New Material or existing Material. There are some inbuilt materials included in Maya like Lambert, Blinn, Layered Shader and so on
<br>
All these materials have some of the common attributes which give either a glossy or plain, either a colorfull or grayscale look to the objects.
<br>
Some of the attributes I tried are
<br>
Color, Incandescence, Transparency and Transluscence Depth
<br>
2- Some of the objects have had their predefined textures which I had to import directly and assigned to respective objects.
<br>
3-Background of objects also played a important role in defining attributes. I tried to set up environment by inserting curved planes in the background of objects so as to avoid any noise in the form of lines.
<br>

![alt text](https://github.com/nikunjlad/3D-Object-Classification-Using-Capsule-Networks/blob/aditya/Maya3D-Images-Dataset/Aditya/folding_plane_capture.JPG)

<br>

In the above image, you can see that the plane has been folded from one side so that light falls on the object properly and there is sharp change in the background of image in terms of gradient and colors
<br>

4-Creating such a background was a complicated task. So we finalized a better way of creating a plane background in the form of a white image and turning out the color of plane same as that of background. This method was implemented by Akash and finalized as environment.
<br>

5-I also contributed in setting up various other parameters of the environment like
<br>

a-Setting color level of Lambert material
<br>

b-Finalizing Lambert as material
<br>

c-Setting up intensity of directional Light
<br>

d-Trying out various lights like point light, ambient light etc
<br>

e-Setting up the shadow resolution, Shadow Color, Width Focus and Fog Shadow Intensity
<br>

f-Changing the settings of Renderer (GPU Instancing, Sampling Count etc)
<br>

g-Use of different tools like Scale Tool, Tumble Tool, Track Tool, Move Tool etc
<br>

I tried out various versions of environment using different parameters and then finalized the best one
<br>

These are some of the Images obtained using the finalized environment

<br>

![alt image](https://github.com/nikunjlad/3D-Object-Classification-Using-Capsule-Networks/blob/aditya/Maya3D-Images-Dataset/Aditya/Electronics_Accessories_Headphone_X0_Y0_Z135_Yes_Black_White.png)

<br>
<br>

![alt image](https://github.com/nikunjlad/3D-Object-Classification-Using-Capsule-Networks/blob/aditya/Maya3D-Images-Dataset/Aditya/Electronics_Storage_Pendrive_X0_Y135_Z225_Yes_Black_White.png)

<br>

## Image Sequence Generation

<br>
1- I was assigned a task for generating image sequences of various objects using the finalized environment and code. Initially I developed images for 40 objects and also assisted Nikunj Doshi, Kaushik and Smit in solving environment issues pertaining to image sequence generation


## Maya Automation, Effort for Pipelining.


<br>

In  order to pipeline the process of creating environment and selection of objects, I worked with Akash collabaratively in order to make a script 

<br>

![alt img](https://github.com/nikunjlad/3D-Object-Classification-Using-Capsule-Networks/blob/aditya/Maya3D-Images-Dataset/Aditya/automate.JPG)

<br>

In this script I have tried some functions, which selects the object through script, then selects its pivot point and recenter it at the center of the axis. It also makes the coordinate of pivot to 0,0,0. exactWorldBoundingBox() method gives the dimensions of the bounding box of object. By using this dimension, the radius of the circle in which Camera is present can be scaled accordingly. The script is not ready and needs to be revised for its implementation.
Please refer the .py scripts in my folder
<br>

## Database Schema 

<br>
In addition to normal decided dataset, I have also added some additional parameters like, objects with shadow, objects without shadow, objects with different backgrounds and shaders. The database shcema has been modified according to the new parameters.
<br>
The below image is the finalised Database
<br>

![alt image](https://github.com/nikunjlad/3D-Object-Classification-Using-Capsule-Networks/blob/aditya/Maya3D-Images-Dataset/Aditya/DB_Schema.png)

<br>

<br>

## Images without Shadows

These are some of the images without Shadows and White Background

<br>

![alt image](https://github.com/nikunjlad/3D-Object-Classification-Using-Capsule-Networks/blob/aditya/Maya3D-Images-Dataset/Aditya/Animal_Mammal_Gorilla_X0_Y0_Z0_No_Black_White.png)

<br>

![alt image](https://github.com/nikunjlad/3D-Object-Classification-Using-Capsule-Networks/blob/aditya/Maya3D-Images-Dataset/Aditya/gorilla_gif.gif)

<br>

<br>

## Images with Different Backgrounds


<br>

![alt image](https://github.com/nikunjlad/3D-Object-Classification-Using-Capsule-Networks/blob/aditya/Maya3D-Images-Dataset/Aditya/Electronics_Appliance_Rotary-Telephone_X0_Y225_Z315_No_White_Black.png)

<br>

![alt image](https://github.com/nikunjlad/3D-Object-Classification-Using-Capsule-Networks/blob/aditya/Maya3D-Images-Dataset/Aditya/rotary_telephone_gif.gif)


<br>


## Image Dataset Finalization

<br> Images, naming convention was decided along with, categories, sub categories
<br> Went through everyone objects, corrected the image sequence generation for improper objects
<br> Generated 540 images per objects and worked on 40 objects of Electronics and Food Category
<br> Generated images for objects without shadow and different backgrounds







<br>


## Contributions


<br> Maya Scripting : - Akash, Preetham and Aditya
<br> Maya Environment : Akash, Preetham Aditya
<br> Object Dataset Finalization : Akash, Aditya, Kaushik and Smit
<br> Database : Sindhura, Harini
<br> Cloud : Anindita, Nikunj
<br> Website : Abhi





## References




<br> 1 - https://knowledge.autodesk.com/support/maya/getting-started/caas/simplecontent/content/maya-document

<br> 2- https://knowledge.autodesk.com/support/maya/getting-started/caas/simplecontent/content/maya-documentation.html

<br> 3- http://help.autodesk.com/cloudhelp/2017/ENU/Maya-Tech-Docs/Commands/getAttr.html

<br> 4- http://help.autodesk.com/cloudhelp/2017/ENU/Maya-Tech-Docs/Commands/setAttr.html

<br> 5- http://help.autodesk.com/cloudhelp/2017/ENU/Maya-Tech-Docs/Commands/cat_General.html

<br> 6- https://knowledge.autodesk.com/support/maya/learn-explore/caas/CloudHelp/cloudhelp/2019/ENU/Maya-GettingStarted/files/GUID-305BF77B-150D-44CE-8190-695DB821BAFD-htm.html





















