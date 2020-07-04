import pymel
print(pymel.__version__)

b, s = polyCube()
s.height

polyCube(b, q=1, h=1) # query


polyCube(b, e=1, h=4) # edit

createNode('transform')