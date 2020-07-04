from pymel.core import *

b = shadingNode('blinn', asShader=True)
sh, sg = createSurfaceShader('blinn')
sphere = PyNode('pSphere1')
sphere = PyNode('pSphere1.tx')
sh.color.set(1, 0, 0)

hyperShade(assign=sh)
sets(sh.shadingGroups()[0])
sets(sg, forceElement=sphere)

sphere.inputs()
sphere.outputs()
sphere.getShape().outputs()
sphere.getShape().outputs(type='shadingEngine')