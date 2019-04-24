import maya.cmds as cmds
import random as rand
def getSpecificObjectsIntoArray(objectName):
	return cmds.ls(objectName)

def randomRotator(objectName):
	for objects in getSpecificObjectsIntoArray(objectName):
		
		rN = rand.uniform(40,80)
		print rN
		cmds.rotate(30,rN,50, objects, a = True)


randomRotator('trexGeoGrp')















import maya.cmds as cmds
import random as rand
def getSpecificObjectsIntoArray(objectName):
  return cmds.ls(objectName)

def randomRotator(objectName):
    startTime = cmds.playbackOptions(query = True, minTime = True)
    endTime = cmds.playbackOptions(query = True, maxTime = True)
    for objects in getSpecificObjectsIntoArray(objectName):
        rN = rand.uniform(40, 80)
        print rN
        cmds.rotate(30, rN, 50, objects, a = True)
        cmds.cutKey(objectName, time = (startTime, endTime), attribute = 'rotateY')
        cmds.setKeyframe(objectName, time = startTime, attribute = 'rotateY', value = 0)
        cmds.setKeyframe(objectName, time = endTime, attribute = 'rotateY', value = 360)

randomRotator('trexGeoGrp')









