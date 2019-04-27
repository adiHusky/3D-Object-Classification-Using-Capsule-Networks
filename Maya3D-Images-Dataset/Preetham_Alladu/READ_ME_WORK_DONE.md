# Describing What my work in this project is:-

## Tasks:-
  * Learning Maya environment and scripting
  * Learning to Translate , rotate, scale and other other things in Maya
  * Writing a script which rotates and takes pictures
  * Creating an environment which has no gradients
  * Creating an environment which provides shadows
  * Creating a website

## WEEK 1 :-
  In week 1 , we were given the task of learning and getting familar with Maya environment and how to script in python / mel
  #### Things I explored:
       • Script to reset environment
       • Script to translate and rotate an object
       • Animate a camera and smoothen its path using graphs
  
## Week 2 :-
  In week 2, I had to come up with a script which rotate an object and takes pictues and stores them in a folder
  
##### The initial images look like below
  ![Octocat](https://raw.githubusercontent.com/nikunjlad/3D-Object-Classification-Using-Capsule-Networks/preetham/Maya3D-Images-Dataset/Preetham_Alladu/pivot_chair_rotate.gif)
  
> In the above gif , the object is being rotated around its pivot and I was to rotate a camera around the object to make it look more natural.
  
After initial presentation to the project team, and as per the requirement I was asked to create an environment which supports shadows
  
Thus resulting a need to create a new environment with lights.

## Week 3 :-
 In week 3, my job was to create a environment with shadows and no gradients, I came up with an environment shown below
 ![Octocat](https://raw.githubusercontent.com/nikunjlad/3D-Object-Classification-Using-Capsule-Networks/preetham/Maya3D-Images-Dataset/Preetham_Alladu/box_environment_chair.jpg)
 
 But the problem was that it had gradients which causes noise, thus resulting in a new environment
 
 #### Plain environmet and static shadows
 ![Branching](https://raw.githubusercontent.com/nikunjlad/3D-Object-Classification-Using-Capsule-Networks/preetham/Maya3D-Images-Dataset/Preetham_Alladu/sphere_evnironment_chair.gif)
 
 
 ## Week 4 :-
 In week 4, my Job was to create a website along with Abhi and link the database into the website. It has multiple filters which lets the users select which view to spectate, and what all categories along with what all objects are available.
 
 
 
 
##### Finalized Script to rotate and take pictures and my contribution towards it.

[Finalized_Script](https://github.com/nikunjlad/3D-Object-Classification-Using-Capsule-Networks/blob/master/Maya3D-Images-Dataset/Preetham_Alladu/Final_Script.py)


### My contribution towards the final script

> This part of the script is very important as it prevents the renderer to take images when the camera is below the ground level.

``` python
camPos = cmds.xform(camName, q=True, ws=True, rp=True)
if( camPos[1] > 1.0):
                screenShot(l)
```
> To pipeline the process i found out a way to automate setting renderer as MayaHardware 2.0 and set image save format as .png file

``` python
import maya.cmds
cmds.setAttr('defaultRenderGlobals.ren', 'mayaHardware2', type = 'string')
cmds.setAttr('defaultRenderGlobals.imageFormat', 32) ## 32 indicates the image is being stored as .png file
```
> Came up with a Naming convention saved as Category_object_xdeg_ydeg_zdeg

``` python
Name = "_X"+str(cx) + "_Y"+str(cy) + "_Z"+str(cz)
```

> Initial Rotate Image Function

``` python
def rotateImage(objName, deg):
    for x in range(0, 360/deg):
        l = 'x'+str(x) + 'yna' + 'zna'
        cmds.xform(objName, relative=True, rotation=(deg, 0, 0) )
        screenShot(objName, l)
        for y in range(0, 360/deg):
            l = 'x'+str(x) + 'y'+str(y) + 'zna'
            cmds.xform(objName, relative=True, rotation=(0, deg, 0) )
            screenShot(objName, l)
            for z in range(0, 360/deg):
                l = 'x'+str(x) + 'y'+str(y) + 'z'+str(z)
                cmds.xform(objName, relative=True, rotation=(0, 0, deg) )
                screenShot(objName, l)
```
### Script to get image proerties and convert images to blob and export it into csv



## License

Copyright 2019 Preetham

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.



### Citations and References

* [https://knowledge.autodesk.com/support/maya/learn-explore/caas/CloudHelp/cloudhelp/2018/ENU/Maya-Scripting/files/GUID-C0F27A50-3DD6-454C-A4D1-9E3C44B3C990-htm.html](https://knowledge.autodesk.com/support/maya/learn-explore/caas/CloudHelp/cloudhelp/2018/ENU/Maya-Scripting/files/GUID-C0F27A50-3DD6-454C-A4D1-9E3C44B3C990-htm.html)

* [https://stackoverflow.com/](https://stackoverflow.com/)

* [https://pypi.org/project/opencv-python/](https://pypi.org/project/opencv-python/)

* [https://www.w3schools.com/python/](https://www.w3schools.com/python/)


* * * 
