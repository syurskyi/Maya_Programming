from pymel.core import *

s = selected()[0]
setKeyframe(s.tx, v=2)
setKeyframe(s.tx, v=10, t=[3, 3])
s.tz.setKey(v=3)


s = selected()[0]
for i in range(50):
    s.tz.setKey(v=util.sin(i)*10, t=[i, i])
