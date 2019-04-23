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