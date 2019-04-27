# Describing What my work in this project is:-

## Tasks:-

Learn Maya to take images of objects<br>
Learn to rotate, render, scale, combine and translate objects<br>
Write a script to take pictures of an object from different angles<br>
Write a script to take pictures of objects with shadows using shader<br>
Create a dataset of images extracted from images to feed it to a database<br>
Finalise the attributes of the database<br>

## Week1

In week 1, we learned to rotate objects in maya. I began with rotating the the objects in X,Y and Z plane. Here we had applied textures to the images.
 
<img src="https://github.com/nikunjlad/3D-Object-Classification-Using-Capsule-Networks/blob/akash/Maya3D-Images-Dataset/Akash/SwordZ280.jpg" width="960" height="540" /> 
<img src="https://github.com/nikunjlad/3D-Object-Classification-Using-Capsule-Networks/blob/akash/Maya3D-Images-Dataset/Akash/SwordX310.jpg" width="960" height="540" />

#### Script for rotating the objects
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

# Week2 

In week 2, We started with added a camera and rotated the camera 360 around the object. Meanwhile, We started searching for objects in the categories that we wanted to collect images for.
My initial category was Weapons.

Here we decided that rendering the object is necessary as by using the saveimage function, there is a lot of noise that also gets captured. We used the renderer Maya Hardware 2.0 as it was the best suited for our objects in capturing shadow and creating images of our choosing.

<img src = "https://github.com/nikunjlad/3D-Object-Classification-Using-Capsule-Networks/blob/akash/Maya3D-Images-Dataset/Akash/Render%20settings.png"  width="300" height="700"  />
<img src="https://github.com/nikunjlad/3D-Object-Classification-Using-Capsule-Networks/blob/akash/Maya3D-Images-Dataset/Akash/Camera%20Rotation.png" width="960" height="540" /> 

Collected over 30 objects in the assigned category to work with in maya.

[Link for dataset used for testing](https://drive.google.com/drive/u/2/folders/1sTMKZnjJm9GApuGnRVebdJTLefnl4hMh)



# Week3

We tried several techniques to bring the images in a white backgorund, we went over 4 instances of background. We attempted to achieve the same with using the following methods:
1. Placing the object in front of a white plane<br>
2. Placing the object inside a white cuboid<br>
3. Placing the object inside a white shpere<br>
4. Placing an image view in the camera settings<br>


After we were done with the white background, our task was to create image sequences with shadows.

<img src="https://github.com/nikunjlad/3D-Object-Classification-Using-Capsule-Networks/blob/akash/Maya3D-Images-Dataset/Akash/White%20back.png" width="960" height="540" /> 


Finally, We came up with the finalized script and used that to create image sequences of the objects.

``` python
#this script has been contributed by preetham, akash and aditya
import maya.cmds as cmds 
import maya.mel

#for getting the list of selected objects
s = cmds.ls(selection = True)
#for selecting the camera
camName=cmds.listCameras()
cName=camName[0]

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
            cp=cmds.xform(cName,q=True,ws=True, rp=True)
            #will capture images only in positive y coordinate
            if(cp[1]>0):
                #for opening images in renderer
                mel.eval('renderWindowRender redoPreviousRender renderView')
                editor =  'renderView'
                #for writing  and storing in specific location
                cmds.renderWindowEditor( editor, e=True,refresh = True, writeImage=('.../Weapon_Scar-L_'+str(cx)+'_'+str(cy)+'_'+str(cz)))
            #incrementing the angles with specified step angle
            cz=cz+v
        cy=cy+v  
    cx=cx+v
```
<img src="https://github.com/nikunjlad/3D-Object-Classification-Using-Capsule-Networks/blob/akash/Maya3D-Images-Dataset/Akash/Image%20with%20shadow.png" width="960" height="540" /> 


# Week4 

In week 4, we were given a task to finalize the datset for the database. 

We have created objects with shadows and without shadows.
Objects have attributes like shader colour and background colour.

We have created different scenes in maya to collect image sequences for the objects.

Meanwhile, we were coming up with changes in the database as the dataset expanded.

<img src="https://github.com/nikunjlad/3D-Object-Classification-Using-Capsule-Networks/blob/akash/Maya3D-Images-Dataset/Akash/final%20db.PNG" width="1000" height="700" /> 


[Link for finalized dataset](https://drive.google.com/drive/u/2/folders/1c7wjh__WL8cVYCPE3ebdM8oSq1riKts6)

### My contribution towards the final script

Assembled the rendered to open and take images of the objects. This was an improvement on the savimage function that was being used before as it allows us to use different renderer and improve quality of the images while removing noise from it from the same time.

```
  mel.eval('renderWindowRender redoPreviousRender renderView')
  editor =  'renderView'
  cmds.renderWindowEditor( editor, e=True,refresh = True, writeImage=('/Users/tinyteddybear/Documents/Scar-H/Weapon_Scar-L_'+str(cx)+'_'+str(cy)+'_'+str(cz)))
```

Rotation function. Below code has been used to capture images with black background and white objects.

```python
import maya.cmds as cmds 
import maya.mel
s = cmds.ls(selection = True)
camName=cmds.listCameras()
cName=camName[0]

cx=0
cy=0
cz=0
v=45
im=0
while (cx <=360):
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
                
            mel.eval('renderWindowRender redoPreviousRender renderView')
            editor =  'renderView'
            cmds.renderWindowEditor( editor, e=True,refresh = True, writeImage=('/Users/tinyteddybear/Documents/NoShadow/Black/Weapons/Gun/ACR Bushmaster/Weapon_Gun_ACR Bushmaster'+'_X'+str(cx)+'_Y'+str(cy)+'_Z'+str(cz)+'_No'))
            im=im+1
            cz=cz+v
        cy=cy+v  
    cx=cx+v
```

### For Pipelining

Worked with the following functions to scale, change the pivot of the object to its center and then find the bounding box outputs to scale the object.

```python
import maya.cmds as cmds

bbox = cmds.exactWorldBoundingBox( 'd_model:Group_329')
print 'Bounding box ranges from: %f' % bbox[0], ', %f' % bbox[1], ', %f' % bbox[2],
print ' to %f' % bbox[3], ', %f' % bbox[4], ', %f' % bbox[5]
```
```python
import maya.cmds as cmds

cmds.xform( cp=True )
cmds.matchTransform('d_model:Group_329','nurbsCircle1', pos = True)
```
