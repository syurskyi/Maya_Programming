from pymel.core import *

sh, sg = createSurfaceShader('blinn')
sphere = PyNode('pSphere1')

texNode = shadingNode('checker', asTexture = True)
placeNode = shadingNode('place2Texture', asUtility = True)
placeNode.outUvFilterSize >> texNode.outUvFilterSize
placeNode.outUV >> texNode.uv

# mel function

mel.eval('createRenderNodeCB -as2DTexture "" checker "";')
PyNode(mel.eval('createRenderNodeCB -as2DTexture "" checker "";'))


from pymel.tools.mel2py import mel2pyStr as m2p
m2p('createRenderNodesCB - as2DTexture "" checker "";')
from pymel.all import *
mel.createRenderNodesCB('-as2DTexture', "", 'checker', "")
PyNode(mel.createRenderNodesCB('-as2DTexture', "", 'checker', ""))
PyNode(mel.createRenderNodesCB('-as2DTexture', "", 'file', ""))