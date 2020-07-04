from pymel.core import *
obj = selected()
for o in obj:
    new = duplicate(o)
    move(0, 2, 0, new, r=1)