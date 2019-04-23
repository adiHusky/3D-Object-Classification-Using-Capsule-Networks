import maya.cmds
cmds.setAttr('defaultRenderGlobals.ren', 'mayaHardware2', type = 'string')
cmds.setAttr('defaultRenderGlobals.imageFormat', 8)# cmds.setAttr('defaultRenderGlobals.imageFormat ', 'jpg', type = 'string')# mel.eval('loadPreferredRenderGlobalsPreset("mayaHardware2")')# cmds.setAttr("defaultRenderGlobals.currentRenderer", "cameraShape1", type = "string")

cx = 0
i = 0
camName = "box_with_lights_and_camera:camera1"
camPos = 0
s = cmds.ls(selection = True)
obj = s[0]
deg = 45
cy = 0
cz = 0
def screenShot(i):
    mel.eval('renderWindowRender redoPreviousRender renderView')
    editor = 'renderView'
    cmds.renderWindowEditor(editor, e = True, refresh = True, writeImage = ('D:\\test\\images\\obj' + str(i)))


while(cx<= 180):
    x = obj +".rotateX"
    cx = cx * -1
    cmds.setAttr(x, cx)
    cx = cx * -1
    cx += deg
    screenShot(i)
    i = i + 1
    while(cy<=360):
        y = obj+".rotateY"
        cmds.setAttr(y, cy)
        cy +=deg
        screenShot(i)
        i += 1
        while(cz<=90):
            z = obj+".rotateZ"
            cmds.setAttr(z, cz)
            cz += deg
            screenShot(i)
            i += 1
            while (cz> -90):
            z = obj+".rotateZ"
            cz -= deg
            cmds.setAttr(z, cz)
            screenShot(i)
            i += 1
        cmds.setAttr(z,0)
    cmds.setAttr(y,0)
