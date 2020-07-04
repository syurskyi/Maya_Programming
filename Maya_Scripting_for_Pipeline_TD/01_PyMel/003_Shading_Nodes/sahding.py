b = shadingNode('blinn', asShader=True)
sh, sg = createSurfaceShader('blinn')
sh.color.set(1,0,0)
sphere = PyNode('pSphere1')
hyperShade(assign=sh)
sets(sh.shadingGroups()[0], forceElement=sphere)


sphere.getShape().outputs(type='shadingEngine')
#listConnections(type='shadingEngine')

texNode = shadingNode("checker", asTexture = True)
placeNode = shadingNode("place2dTexture", asUtility=True)
placeNode.outUvFilterSize >> texNode.uvFilterSize
placeNode.outUV >> texNode.uv


r = PyNode(mel.eval('createRenderNodeCB -as2DTexture "" file "";'))

# mel to py
from pymel.tools.mel2py import mel2pyStr as m2p
mel.createRenderNodeCB('-as2DTexture', "", 'file', "")