from pymel.core import *

s = selected()[0]
c = createNode('animCurveTL', name='crv1')
times = range(100)
values = [util.sin(x*0.5)*5 for x in times]
c.addKeys(times, values)
c.getTime(5)
c.getValue(4)


s = selected()[0]
c = createNode('animCurveUU', name='crv1')
times = [0, 1]
values = [0]
setKeyframe(c, f=times[0], v=values[0])
setKeyframe(c, f=times[1], v=values[1])
