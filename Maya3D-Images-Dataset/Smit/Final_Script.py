import maya.cmds as cmds #importing maya commands to python
import maya.mel #Maya Embbeded Language
s = cmds.ls(selection = True) #locking the selection of the user ( say object or camera or path,etc)
camName=cmds.listCameras()
cName=camName[0]

cx=0 #assigning angles to zero degrees on each axis
cy=0
cz=0
v=45 #increment angle
im=0
while (cx <=360): #while loop for X axis
  for a in s:
      x = a +"."+"rotate" +"X" #setting the input parameter to rotate camera on X axis
      cmds.setAttr(x,cx) #command to rotate on X axis

  cy=0
  while(cy<=360):
      for a in s:
          x = a +"."+"rotate" +"Y" #setting the input parameter to rotate camera on Y axis
          cmds.setAttr(x,cy)

      cz=0
      while(cz<=360):
          for a in s:
              x = a +"."+"rotate" +"Z" #setting the input parameter to rotate camera on Z axis
              cmds.setAttr(x,cz)
          cp=cmds.xform(cName,q=True,ws=True, rp=True) #cp = camera position
          if(cp[1]>0): #capturing everthing above X plane- remove this capture bottom views as well

              mel.eval('renderWindowRender redoPreviousRender renderView') #opening render view in Maya
              editor =  'renderView'
              cmds.renderWindowEditor( editor, e=True,refresh = True, writeImage=(r'Path_Name'+'_X'+str(cx)+'_Y'+str(cy)+'_Z'+str(cz))) #saving render image to specified path in local directory
          im=im+1 
          cz=cz+v
      cy=cy+v
  cx=cx+v
