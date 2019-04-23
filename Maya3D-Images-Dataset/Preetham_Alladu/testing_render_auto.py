import  maya.cmds as cmds



def rotateImage(objName, deg):
    for x in range(0, 360/deg):
        l = 'x'+str(x) + 'y0' + 'z0'
        cmds.xform(objName, relative=True, translation=(deg, 0, 0) )
        screenShot(objName, l) 

def screenShot(objName, l):
    ws = 'D:\\test'
    wsp = ws + "/" + "images"
    imageSnapshot = wsp + "/" + str(objName) + str(l) +".jpg"
    cmds.refresh(cv=True, fe = "jpg", fn = imageSnapshot)
  
  
cmds.setAttr('defaultRenderGlobals.ren', 'mayaHardware2', type='string')

mel.eval('loadPreferredRenderGlobalsPreset("mayaHardware2")') 
    
name = 'camera1'
l = 'starting'
screenShot(name, l)
rotateImage(name , 90)