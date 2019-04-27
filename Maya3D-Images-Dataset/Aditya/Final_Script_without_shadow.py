
#this script has been contributed by preetham, akash and aditya
import maya.cmds as cmds
import maya.mel
import os

#for getting the list of selected objects
s = cmds.ls(selection = True)
camName=cmds.listCameras()
cName=camName[0]
#setting up initial angles of x, y and z axis to 0 ,0 ,0
cx=0
cy=0
cz=0
v=45
#for storing image in current work directory
zz=os.getcwd()

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
               #for opening images in renderer 
               mel.eval('renderWindowRender redoPreviousRender renderView')
               editor =  'renderView'
               #for writing  and storing in specific location
               cmds.renderWindowEditor( editor, e=True,refresh = True, writeImage=(ZZ+"\image"+str(cx)+'_X'+str(cy)+'_Y'+str(cz)+'_Z'))
               #incrementing the angles with specified step angle
           cz=cz+v
       cy=cy+v
   cx=cx+v