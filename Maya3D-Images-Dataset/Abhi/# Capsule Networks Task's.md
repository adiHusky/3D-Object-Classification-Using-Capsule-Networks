# Capsule Networks

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

#Fuunction for rotating the obeject

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
                
#Function for taking screen shot

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
import maya.cmds as cmds 
import maya.mel
import os

#for getting the list of selected objects
s = cmds.ls(selection = True)
#for selecting the camera
camName=cmds.listCameras()
cName=camName[0]
imagePath = os.getcwd()

#setting up initial angles of x, y and z axis to 0 ,0 ,0
cx=0
cy=0
cz=0
v=45

#looping for getting various angles
while (cx <=360):
    for a in s:
        #setting the command to rotate the component in X axis
        x = a +"."+"rotate" +"X"
        #setting the attribute of component in X axis
        cmds.setAttr(x,cx)

    cy=0
    while(cy<=360):
        for a in s:
            #setting the command to rotate the component in Y axis
            x = a +"."+"rotate" +"Y"
            #setting the attribute of component in Y axis
            cmds.setAttr(x,cy)

        cz=0
        while(cz<=360):
            for a in s:
                #setting the command to rotate the component in Z axis
                x = a +"."+"rotate" +"Z"
                #setting the attribute of component in Z axis
                cmds.setAttr(x,cz)
            #for opening images in renderer
            mel.eval('renderWindowRender redoPreviousRender renderView')
            editor =  'renderView'
            #for writing  and storing in specific location
            cmds.renderWindowEditor( editor, e=True,refresh = True, writeImage=(imagePath+'Weapon_Gun_ACR Bushmaster'+'_X'+str(cx)+'_Y'+str(cy)+'_Z'+str(cz)+'_No'))
            #incrementing the angles with specified step angle
            cz=cz+v
        cy=cy+v  
    cx=cx+v

```

Here is an example of images Generated after the final scripts 

<img src="https://github.com/nikunjlad/3D-Object-Classification-Using-Capsule-Networks/blob/abhi/Maya3D-Images-Dataset/Abhi/image4.png" />

<img src="https://github.com/nikunjlad/3D-Object-Classification-Using-Capsule-Networks/blob/abhi/Maya3D-Images-Dataset/Abhi/image5.png" />

<img src="https://github.com/nikunjlad/3D-Object-Classification-Using-Capsule-Networks/blob/abhi/Maya3D-Images-Dataset/Abhi/image6.png" />

## Week 4

For the week 4 we created the database schema below is the Entity RelationShip Model 

<img src="https://github.com/nikunjlad/3D-Object-Classification-Using-Capsule-Networks/blob/abhi/Maya3D-Images-Dataset/Abhi/Final_DB_Schema.png" />

## My contribution in Website

1. Website design using html/css
2. Connection with database and database schema is created
3. Added pages for getting object images using search feature and filtering data by Category, Sub Category
4. Stored few categories & two objects data

## Website Source Code

https://github.com/nikunjlad/3D-Object-Classification-Using-Capsule-Networks/tree/abhi/Maya3D-Images-Dataset/Abhi/Website

## References 

1.https://knowledge.autodesk.com/support/maya/getting-started/caas/simplecontent/content/maya-document

2. https://knowledge.autodesk.com/support/maya/getting-started/caas/simplecontent/content/maya-documentation.html

3. http://help.autodesk.com/cloudhelp/2017/ENU/Maya-Tech-Docs/Commands/getAttr.html

4. http://help.autodesk.com/cloudhelp/2017/ENU/Maya-Tech-Docs/Commands/setAttr.html

5. http://help.autodesk.com/cloudhelp/2017/ENU/Maya-Tech-Docs/Commands/cat_General.html

6. https://help.autodesk.com/cloudhelp/2017/CHS/Maya-Tech-Docs/CommandsPython/saveImage.html

7. https://www.w3schools.com/

8. https://stackoverflow.com/

## MIT License

Copyright (c) 2019, Abhi Patodi All rights reserved.

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy,modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

