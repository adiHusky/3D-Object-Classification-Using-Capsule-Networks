import maya.cmds as cmds 
import maya.mel
s = cmds.ls(selection = True)
camName=cmds.listCameras()
cName=camName[0]

cx=0
cy=0
cz=0
v=45
im=0
while (cx <=360):
    for a in s:
        x = a +"."+"rotate" +"X"
        cmds.setAttr(x,cx)

    cy=0
    while(cy<=360):
        for a in s:
            x = a +"."+"rotate" +"Y"
            cmds.setAttr(x,cy)

        cz=0
        while(cz<=360):
            for a in s:
                x = a +"."+"rotate" +"Z"
                cmds.setAttr(x,cz)
                
            mel.eval('renderWindowRender redoPreviousRender renderView')
            editor =  'renderView'
            cmds.renderWindowEditor( editor, e=True,refresh = True, writeImage=('/Users/tinyteddybear/Documents/NoShadow/Black/Weapons/Gun/ACR Bushmaster/Weapon_Gun_ACR Bushmaster'+'_X'+str(cx)+'_Y'+str(cy)+'_Z'+str(cz)+'_No'))
            im=im+1
            cz=cz+v
        cy=cy+v  
    cx=cx+v