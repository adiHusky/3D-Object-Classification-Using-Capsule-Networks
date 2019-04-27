#this script has been contributed by preetham and akash
import maya.cmds as cmds 
import maya.mel

#for getting the list of selected objects
s = cmds.ls(selection = True)
#for selecting the camera
camName=cmds.listCameras()
cName=camName[0]

#setting up initial angles of x, y and z axis to 0 ,0 ,0
cx=0
cy=0
cz=0
v=45

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
            #for opening images in renderer
            mel.eval('renderWindowRender redoPreviousRender renderView')
            editor =  'renderView'
            #for writing  and storing in specific location
            cmds.renderWindowEditor( editor, e=True,refresh = True, writeImage=('/Users/tinyteddybear/Documents/NoShadow/Black/Weapons/Gun/ACR Bushmaster/Weapon_Gun_ACR Bushmaster'+'_X'+str(cx)+'_Y'+str(cy)+'_Z'+str(cz)+'_No'))
            #incrementing the angles with specified step angle
            cz=cz+v
        cy=cy+v  
    cx=cx+v
