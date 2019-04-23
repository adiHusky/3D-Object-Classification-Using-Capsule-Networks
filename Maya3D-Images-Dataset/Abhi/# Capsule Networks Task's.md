# Capsule Networks Task's

We were assigned the following task for according to weeks

## Week 1

Learning the Maya Software and how to set up an environment for different 3D models object and write Mel Scripts and Python scripts.

So during the first week, I create few python scripts


```python
import maya.cmds as cmds

cubelist= cmds.ls("myCube")

if len(cubelist)>0:
  cmds.delete(cubelist)

result = cmds.polycube(w=9.248, h=9.248, d=9.248, name='mycube',)

print 'result'+ str (result )

transformName = cmds.instance(transformName, name =transformName ) 


```
<img src="https://github.com/nikunjlad/3D-Object-Classification-Using-Capsule-Networks/blob/abhi/Maya3D-Images-Dataset/Abhi/image1.png" />

## Week 2

After learning we were given tasks to save the images of objects so for that i wrote the python scripting using which i was rotating the obects and then saving the images.

Below is the code for saveimage command

```python

import maya.cmds as cmds 

selection = cmds.ls(sl=True)
ws = cmds.workspace(q = True, fullName = True)
wsp = ws + "/" + "images"
cmds.sysFile(wsp, makeDir=True)


for i in range(0,50):
    cmds.xform('Lamborginhi_Aventador',  ws =True,  relative=True, rotation=(45, 45, 45) )
    cmds.saveImage( currentView=True )
    imageSnapshot = wsp + "/" + "image" + str(i) +".jpg"
    cmds.refresh(cv=True, fe = "jpg", fn = imageSnapshot)
```


After learning we were given tasks to save the images of objects so for that i wrote the python scripting using 
which i was rotating the obects and then saving the images.

Below is the code for saveimage command and rotate the 3D model object

```python


import  maya.cmds as cmds


def rotateImage(objName, deg):
    for x in range(0, 360/deg):
        l = 'x'+str(x) + 'y0' + 'z0'
        cmds.xform(objName, relative=True, rotation=(deg, 0, 0) )
        screenShot(objName, l) 
        for y in range(0, 360/deg):
            l = 'x'+str(x)+ 'Y' +str(y) + 'z0'
            cmds.xform(objName, relative=True, rotation=(0, deg, 0) ) 
            screenShot(objName, l) 
            for z in range (0, 360/deg):
                l = 'x'+str(x)+'y'+ str(y) +'Z' +str(z)
                cmds.xform(objName, relative=True, rotation=(0, 0, deg) )
                screenShot(objName, l)

def screenShot(objName, l):
    #imageSnapshot = wsp + "/" + str(objName) + str(l) +".jpg"
    mel.eval('renderWindowRender redoPreviousRender renderView')
    editor =  'renderView'
    cmds.renderWindowEditor( editor, e=True,refresh = True, writeImage=('D:\\test\\tr'+objName+str(l)))
    
    
    
name = 'nurbsCircle1'
l = 'starting'
screenShot(name, l)
rotateImage(name , 90)

```
<img src="https://github.com/nikunjlad/3D-Object-Classification-Using-Capsule-Networks/blob/abhi/Maya3D-Images-Dataset/Abhi/image2.png" />

<img src="https://github.com/nikunjlad/3D-Object-Classification-Using-Capsule-Networks/blob/abhi/Maya3D-Images-Dataset/Abhi/image3.png" />

## Week 3

Using final python script and enviroment I captured images for 26 objects 


Below is the code for final script command

```python

import maya.cmds
cmds.setAttr('defaultRenderGlobals.ren', 'mayaHardware2', type = 'string')
cmds.setAttr('defaultRenderGlobals.imageFormat', 32)# cmds.setAttr('defaultRenderGlobals.imageFormat ', 'jpg', type = 'string')# mel.eval('loadPreferredRenderGlobalsPreset("mayaHardware2")')# cmds.setAttr("defaultRenderGlobals.currentRenderer", "cameraShape1", type = "string")

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
    cmds.renderWindowEditor(editor, e = True, refresh = True, writeImage = ('D:\\test\\lol\\Telescope\\Telescope' + str(i)))


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

Here is an example of images Generated after the final scripts 

<img src="https://github.com/nikunjlad/3D-Object-Classification-Using-Capsule-Networks/blob/abhi/Maya3D-Images-Dataset/Abhi/image4.png" />

<img src="https://github.com/nikunjlad/3D-Object-Classification-Using-Capsule-Networks/blob/abhi/Maya3D-Images-Dataset/Abhi/image5.png" />

<img src="https://github.com/nikunjlad/3D-Object-Classification-Using-Capsule-Networks/blob/abhi/Maya3D-Images-Dataset/Abhi/image6.png" />



## Week 4

For the week 4 we created the database schema below is the Entity RelationShip Model 

<img src="https://github.com/nikunjlad/3D-Object-Classification-Using-Capsule-Networks/blob/akash/Maya3D-Images-Dataset/Akash/final%20db.PNG" />


## Under Working

I am working on website which is currently hosted on local server


