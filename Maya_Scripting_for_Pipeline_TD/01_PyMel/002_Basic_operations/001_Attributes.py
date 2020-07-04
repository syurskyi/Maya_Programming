# cmds

import maya.cmds as cmds
b1, s1 = cmds.polyCube()
cmds.setAttr(b1 + ".translateX", 0)
cmds.getAttr(b1 + ".translateX")
cmds.setAttr(s1 + ".height", 2)
cmds.setAttr(b1 + ".translateX", 0, 2, 3, type='double3')

# PyMel

import pymel.core as pm
b2, s2 = pm.polyCube()
pm.setAttr(b2 + ".tx", 1)
b2.setAttr('tx', 2)
b2.tx
print(b2.tx)
b2.tx.set(3)
b2.attr('tx').set(0)

s2.setHeight(3)
s2.height.set(20)
s2.getHeight()

b2.translate.set(1, 1, 1)
b2.translate.set([2, 2, 1])
b2.setTranslation([1, 2, 3])