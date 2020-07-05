from pymel.core import *

s = selected()[0]
c = createNode('animCurveUU', name='crv1')
times = [0, 1]
values = [0, 1]
setKeyframe(c, f=times[0], v=values[0])
setKeyframe(c, f=times[1], v=values[1])

c.setWeighted(1)
c.setWeightsLocked(0, 0)
c.setWeight(0, 12.5, 0)

# mel
keyTangent(c, edit=True, absolute=True, lock=0, index=(0,0), outAngle=0, outWeight=12.5)

keyTangent(c, edit=True, absolute=True, lock=0, index=(0,0), outAngle=90, outWeight=1)
keyTangent(c, edit=True, absolute=True, lock=0, index=(0,0), outAngle=-90, outWeight=1)

c.output  >> s.tx