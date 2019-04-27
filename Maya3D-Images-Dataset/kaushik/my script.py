

import maya.cmds as cmds

def keyFullRotation (pObjectName, pStartTime,pEndTime,pTargetAttribute):

    cmds.cutKey(pObjectName, time=(pStartTime,pEndTime),attribute=pTargetAttribute)
    cmds.setKeyframe(pObjectName, time=pStartTime,attribute=pTargetAttribute, value=0)
    cmds.setKeyframe(pObjectName, time=pEndTime,attribute=pTargetAttribute, value=360)

    #from smooth to linear tangents
    cmds.selectKey(pObjectName, time=(pStartTime,pEndTime),attribute=pTargetAttribute)
    cmds.keyTangent(inTangentType='linear', outTangentType = 'linear')

selectionlist = cmds.ls(selection =True)

if len(selectionlist) >= 1:

    #ask current timeslider start and end
    startTime     = cmds.playbackOptions (query=1,minTime=1)
    endTime     = cmds.playbackOptions (query=1,maxTime=1)
#    print 'Selected items %s' %(selectionlist)

    for objectName in selectionlist:
        #objectTypeResult = cmds.objectType(objectName)
        #print '%s type %s' %(objectName ,objectTypeResult )
        keyFullRotation(objectName, startTime,endTime,'rotateY')

else :
    print 'you have no selection nitwit'