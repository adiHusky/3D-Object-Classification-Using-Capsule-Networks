#This script has been contributed by Aditya
selection = cmds.ls(selection=True)
#function for storing images
def imageStorage(axis,step):
  ws = cmds.workspace(q = True, fullName = True)
  wsp = ws + "/" + "images"
  cmds.sysFile(wsp, makeDir=True)
  imageSnapshot = wsp + "/"+"image"+str(step)+"_"+str(axis)+"Snapshot.jpg"
  cmds.refresh(cv=True, fe = "jpg", fn = imageSnapshot)
#function for capturing images  by rotating camera	
def captureImages(axis,step,camDistance):
  #for scaling th distance of camera
  cmds.scale(camDistance,camDistance,camDistance)
  #for saving the screenshot of images
  cmds.saveImage(currentView=True) 
  for selected in selection:
   #for capturing images along y axis, x axis and yx axis
   if(axis=='Y'):
    angle=0
    while(angle<360):
      cmds.setAttr(selected + ".rotateY",angle)
      angle=angle+step
      imageStorage(axis='Y',step="0_"+str(angle))
   if(axis=='X'):
    angle=0
    while(angle<360):
     cmds.setAttr(selected + ".rotateX",angle)
     angle = angle+step
     imageStorage(axis='X',step=str(angle)+"_0")      
   if(axis=='YX'):
    angleY=0
    while(angleY<360):
     cmds.setAttr(selected + ".rotateY",angleY)
     angleY=angleY+step
     angleX=0
     while(angleX<360):
       cmds.setAttr(selected + ".rotateX",angleX)
       angleX=angleX+step
       imageStorage(axis='YX',step=str(angleX)+"_"+str(angleY))          
captureImages(axis='YX',step=10,camDistance=140)
#function where we need to pass axis, step angle and camera Distance from Object
#done for X, Y and YX axis
#Image stored in form of IMAGE_ANGLEX_ANGLEY_AXIS
#Problems: Need to add renderer logic, need to automate process of object pivot selection and adding the camera along the circle














