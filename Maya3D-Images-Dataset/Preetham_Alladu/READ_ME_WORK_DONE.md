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
  ![Octocat](https://raw.githubusercontent.com/nikunjlad/3D-Object-Classification-Using-Capsule-Networks/master/Maya3D-Images-Dataset/Preetham_Alladu/2z705q.gif)
  
> In the above gif , the object is being rotated around its pivot and I was to rotate a camera around the object to make it look more natural.
  
After initial presentation to the project team, and as per the requirement I was asked to create an environment which supports shadows
  
Thus resulting a need to create a new environment with lights.

## Week 3 :-
 In week 3, my job was to create a environment with shadows and no gradients, I came up with an environment shown below
 ![Octocat](https://raw.githubusercontent.com/nikunjlad/3D-Object-Classification-Using-Capsule-Networks/master/Maya3D-Images-Dataset/Preetham_Alladu/BeFunky-collage.jpg)
 
 But the problem was that it had gradients which causes noise, thus resulting in a new environment
 
 #### Plain environmet and static shadows
 ![Branching](https://raw.githubusercontent.com/nikunjlad/3D-Object-Classification-Using-Capsule-Networks/master/Maya3D-Images-Dataset/Preetham_Alladu/2z72zl.gif)
 
 
 ## Week 4 :-
 In week 4, my Job was to create a website along with Abhi and link the database into the website. It has multiple filters which lets the users select which view to spectate, and what all categories along with what all objects are available.
 
 
 
 
 ## Finalized Script to rotate and take pictures and my contribution towards it.
 
``` python
import maya.cmds
cmds.setAttr('defaultRenderGlobals.ren', 'mayaHardware2', type = 'string')
cmds.setAttr('defaultRenderGlobals.imageFormat', 32) ## 32 indicates the image is being stored as .png file

cx = 0
i = 0
s = cmds.ls(selection = True)
camName = "camera1"
camPos = 0
obj = s[0]
deg = 45
cy = 0
cz = 0
def screenShot(i):
    mel.eval('renderWindowRender redoPreviousRender renderView')
    editor = 'renderView'
    cmds.renderWindowEditor(editor, e = True, refresh = True, writeImage = ('Path\\Telescope\\Telescope' + str(i)))


while(cx<= 360):
    for a in s:
        x = a +"."+"rotate" +"X"
        cmds.setAttr(x,cx)
    cy=0
    while(cy<=360):
        for a in s:
            x = a +"."+"rotate" +"Y"
            cmds.setAttr(x,cy)
        cz=0
        while(cz<=360):
            for a in s:
                x = a +"."+"rotate" +"Z"
                cmds.setAttr(x,cz)
            l = "_X_"+str(cx) + "_Y_"+str(cy) + "_Z_"+str(cz)
            camPos = cmds.xform(camName, q=True, ws=True, rp=True)
            if( camPos[1] > 1.0):
                screenShot(l)

            cz = cz + deg
        cy=cy+deg
    cx=cx+deg
```



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



* * * 
