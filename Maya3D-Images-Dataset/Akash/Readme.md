#Describing What my work in this project is:-

##Tasks:-

Learn Maya to take images of objects
Learn to rotate, render, scale, combine and translate objects
Write a script to take pictures of an object from different angles
Write a script to take pictures of objects with shadows using shader
Create a dataset of images extracted from images to feed it to a database
Finalise the attributes of the database

##Week1

In week 1, we learned to rotate objects in maya. I began with rotating the the objects in X,Y and Z plane. Here we had applied textures to the images.
 
<img src="https://github.com/nikunjlad/3D-Object-Classification-Using-Capsule-Networks/blob/akash/Maya3D-Images-Dataset/Akash/SwordZ280.jpg" width="960" height="540" /> 
<img src="https://github.com/nikunjlad/3D-Object-Classification-Using-Capsule-Networks/blob/akash/Maya3D-Images-Dataset/Akash/SwordX310.jpg" width="960" height="540" />

Script for rotating the objects
``` python
import maya.cmds as cmds 
import maya.mel
s = cmds.ls(selection = True)
axes = ['X','Y','Z']

for axis in axes:
    c=0
    while(c<=360):
        for a in s:
            x = a +"."+"rotate" +axis
            cmds.setAttr(x,c)
            
        mel.eval('renderWindowRender redoPreviousRender renderView')
        editor =  'renderView'
            #c= c+5
        cmds.renderWindowEditor( editor, e=True,refresh = True, writeImage=('/Users/tinyteddybear/Documents/Sword/Sword'+axis+str(c)))
        c=c+10
```
Week2 

In week 2, We started with added a camera and rotated the camera 360 around the object. Meanwhile, We started searching for objects in the categories that we wanted to collect images for.
My initial category was Weapons.
<img src="https://github.com/nikunjlad/3D-Object-Classification-Using-Capsule-Networks/blob/akash/Maya3D-Images-Dataset/Akash/Camera%20Rotation.png" width="960" height="540" /> 

Created image sequences for over 30 objects.
[Drive](https://drive.google.com/drive/u/2/folders/1sTMKZnjJm9GApuGnRVebdJTLefnl4hMh)
