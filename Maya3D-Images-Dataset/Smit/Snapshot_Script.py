selection = cmds.ls(selection=True)

def screenShot(i):
    mel.eval('renderWindowRender redoPreviousRender renderView')
    editor = 'renderView'
    cmds.renderWindowEditor(editor, e = True, refresh = True, writeImage = ('D:\\test\\lol\\trex' + str(i)))
  
def captureImages(axis,step,camDistance):
  #cmds.scale(camDistance,camDistance,camDistance)
  #cmds.saveImage(currentView=True) 
  for selected in selection:
   if(axis=='Y'):
    angle=0
    while(angle<360):
      cmds.setAttr(selected + ".rotateY",angle)
      angle=angle+step
      screenShot(axis='Y',step="0_"+str(angle))
   if(axis=='X'):
    angle=0
    while(angle<360):
     cmds.setAttr(selected + ".rotateX",angle)
     angle = angle+step
     screenShot(axis='X',step=str(angle)+"_0")      
   if(axis=='YX'):
    angleY=0
    while(angleY<360):
     cmds.setAttr(selected + ".rotateY",angleY)
     angleY=angleY+step
     angleX=0
     while(angleX<360):
       cmds.setAttr(selected + ".rotateX",angleX)
       angleX=angleX+step
       screenshot(axis='YX',step=str(angleX)+"_"+str(angleY))          
captureImages(axis='YX',step=36,camDistance=1)
