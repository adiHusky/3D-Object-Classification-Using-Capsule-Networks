import maya.cmds as cmds
import maya.mel
#for selecting all objects 
cmds.select(all=True,visible=True)
#for deselecting circle
cmds.select('nurbsCircle1', d=True)
#for deselecting plane and deselecting other objects
cmds.select('nurbsPlane1', d=True)
#for center pivot 
cmds.xform(cp=True)
cmds.xform(a=True)
cmds.xform()
#for getting dimensions of objects
bbox = cmds.exactWorldBoundingBox( 'sphere1')
print 'Bounding box ranges from: %f' % bbox[0], ', %f' % bbox[1], ', %f' % bbox[2],
print ' to %f' % bbox[3], ', %f' % bbox[4], ', %f' % bbox[5]