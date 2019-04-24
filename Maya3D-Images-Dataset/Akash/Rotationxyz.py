import maya.cmds as cmds 
import maya.mel
s = cmds.ls(selection = True)
axes = ['X','Y','Z']

for axis in axes:
    c=0
    while(c<=360):
        for a in s:
            x = a +"."+"rotate" +axis
            cmds.setAttr(x,c)
            
        mel.eval('renderWindowRender redoPreviousRender renderView')
        editor =  'renderView'
            #c= c+5
        cmds.renderWindowEditor( editor, e=True,refresh = True, writeImage=('/Users/tinyteddybear/Documents/Sword/Sword'+axis+str(c)))
        c=c+10
