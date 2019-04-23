import  maya.cmds as cmds



def rotateImage(objName, deg):
    for x in range(0, 360/deg):
        l = 'x'+str(x) + 'yna' + 'zna'
        cmds.xform(objName, relative=True, rotation=(deg, 0, 0) )
        screenShot(objName, l)
        for y in range(0, 360/deg):
            l = 'x'+str(x) + 'y'+str(y) + 'zna'
            cmds.xform(objName, relative=True, rotation=(0, deg, 0) )
            screenShot(objName, l)
            for z in range(0, 360/deg):
                l = 'x'+str(x) + 'y'+str(y) + 'z'+str(z)
                cmds.xform(objName, relative=True, rotation=(0, 0, deg) )
                screenShot(objName, l)
def screenShot(objName, l):
    mel.eval('renderWindowRender redoPreviousRender renderView')
    editor =  'renderView'
    cmds.renderWindowEditor( editor, e=True,refresh = True,removeAllImages = True,writeImage=('D:\\test\\jklol\\'+'chair_test_'+str(l)))

s = cmds.ls(selection = True)

objName = s[0]
l = 'starting'

screenShot(objName, l)
rotateImage(objName, 45)