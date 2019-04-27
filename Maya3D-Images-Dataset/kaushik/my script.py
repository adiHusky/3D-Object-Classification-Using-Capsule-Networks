

import maya.cmds as cmds

##selects the objects in the scene 
selectionlist = cmds.ls(selection =True)
##defining object rotation. 
def keyFullRotation (pObjectName, pStartTime,pEndTime,pTargetAttribute):

    cmds.cutKey(pObjectName, time=(pStartTime,pEndTime),attribute=pTargetAttribute)
    cmds.setKeyframe(pObjectName, time=pStartTime,attribute=pTargetAttribute, value=0)
    cmds.setKeyframe(pObjectName, time=pEndTime,attribute=pTargetAttribute, value=360)

  
    cmds.selectKey(pObjectName, time=(pStartTime,pEndTime),attribute=pTargetAttribute)
    cmds.keyTangent(inTangentType='linear', outTangentType = 'linear')

##checking the number of objects in scene
selectionlist = cmds.ls(selection =True)

if len(selectionlist) >= 1:

    startTime     = cmds.playbackOptions (query=1,minTime=1)
    endTime     = cmds.playbackOptions (query=1,maxTime=1)
   
    for objectName in selectionlist:
        
        keyFullRotation(objectName, startTime,endTime,'rotateY')

        else :
    print 'you have no selection'

##taking screenshots of the image
def screenShot(i):
    mel.eval('renderWindowRender redoPreviousRender renderView')
    editor = 'renderView'
    cmds.renderWindowEditor(editor, e = True, refresh = True, writeImage = ('C:\\kaushik\\lol\\trex' + str(i)))