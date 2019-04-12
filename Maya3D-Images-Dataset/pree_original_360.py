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
    mel.eval('renderWindowRender redoPreviousRender renderView')
    editor =  'renderView'
    cmds.renderWindowEditor( editor, e=True,refresh = True,removeAllImages = True, writeImage=('D:\\test\\yo\\'+'awp'+str(l)), removeImage = True)


cmds.setAttr('defaultRenderGlobals.ren', 'mayaHardware2', type='string')

mel.eval('loadPreferredRenderGlobalsPreset("mayaHardware2")')


s = 'foldingchair_open'
name = 'foldingchair_open'
l = 'starting'
screenShot(name, l)
count = 0
rotateImage(name , 90)