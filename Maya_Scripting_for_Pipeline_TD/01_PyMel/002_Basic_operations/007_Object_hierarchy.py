from pymel.core import *

c, sc = polyCube()
s, ss = polySphere()
t, st = polyTorus()

g = createNode('transform', name='parent')

g.addChild(c)
s.setParent(g)
s.setParent(None)

g.getChildren()
s.getParent()

t.getChildren()
t.getShape()

g.getShape()

g.listRelatives(s=1)
t.listRelatives(s=1)