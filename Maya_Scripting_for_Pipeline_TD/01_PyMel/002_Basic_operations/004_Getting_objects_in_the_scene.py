from pymel.core import *

ls(sl=1)
selected()

ls('pShere1')
ls('pSphere*')
ls('pSphere*,', type=nt.Transform)
ls('pSphere*,', type='transform')

ls(type='lambert')

[x for x in ls(type='lambert') if x.type() == 'lambert']

[x for x in ls(materials=1) if x.type() == 'lambert']
ls(transforms=1, sl=1)