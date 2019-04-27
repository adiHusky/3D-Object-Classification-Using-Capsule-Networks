import maya.cmds
import os
cmds.setAttr('defaultRenderGlobals.ren', 'mayaHardware2', type = 'string') # sets the renderer to mayaHardware2.0
cmds.setAttr('defaultRenderGlobals.imageFormat', 32)                       # sets the save image format as .png, 
                                                                           # 36 implies .png
                                                                           # 8 implies .jpeg

cx = 0
i = 0
s = cmds.ls(selection = True)
camName = "camera1"
camPos = 0
obj = s[0]
deg = 45

cx = 0      # initialize x degree
cy = 0      # initialize y degree
cz = 0      # initialize z degree

pathname = os.path.dirname(sys.argv[0])         # get path to current working directory

def screenShot(i):                              # a function used to take save rendered images with takes in a string input
    mel.eval('renderWindowRender redoPreviousRender renderView')
    editor = 'renderView'
    cmds.renderWindowEditor(editor, e = True, refresh = True, writeImage = (pathname + '\\ObjName\\ObjName' + str(i)))


while(cx<= 360):                                                # First while loop to rotate around the x axis
    for a in s:
        x = a +"."+"rotate" +"X"
        cmds.setAttr(x,cx)
    cy=0
    while(cy<=360):                                             # Second while loop to rotate around the x axis
        for a in s:
            x = a +"."+"rotate" +"Y"
            cmds.setAttr(x,cy)
        cz=0
        while(cz<=360):                                         # Second while loop to rotate around the x axis
            for a in s:
                x = a +"."+"rotate" +"Z"
                cmds.setAttr(x,cz)
            l = "_X_"+str(cx) + "_Y_"+str(cy) + "_Z_"+str(cz)   # Naming convention
            camPos = cmds.xform(camName, q=True, ws=True, rp=True)  # To get the current position of the camera returns a list of length 3
                                                                    # like so camPos = [X, Y, Z] 
            if( camPos[1] > 1.0):                                   # we need y co-ordinate to be always greater than 1 for the camera
                                                                    # to be above ground so we use camPos[1] which corresponds to Y 
                screenShot(l)

            cz = cz + deg                                           
        cy=cy+deg
    cx=cx+deg
