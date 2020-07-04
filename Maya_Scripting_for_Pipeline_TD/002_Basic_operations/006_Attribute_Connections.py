from pymel.core import *

c, sc = polyCube()
s, ss = polySphere()

connectAttr(c.tx, s.tx)
disconnectAttr(c.tx, s.tx)

s.connect('tx', c.tx)
s.ty.connect(c.ty)
s.ty.connect()
s.ty.disconnect(c.ty)
s.ty.disconnect()

s.tz >> c.tz

s.listConnections()
s.listConnections(plugs=1)

c.tz.inputs()
c.tz.inputs(plugs=1)

c.inputs(plugs=1)