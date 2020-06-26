# video 11  ATTRIBUTES ===================================================================================
# Welcome back let's recap using the Query flag
# if construction history was on then you could find it if not then you couldn't.
# WHY?
# some commands in maya have this odd behavior:
# 1. first if you're requesting an attribute value on a transform and it doesn't exist
# 2. then it checks the shape node for the value
# 3. if it's not on the shapeNode then it searches construction History inputs into the shape node for the value
# SIDE NOTE VIDEO on getting an attribute on transform + shapenode + input into shape node
# not very pythonic, but mayaish.

# this works but there is no attribute of that name on the rubiks transform
mc.polyCube('rubiks', w=True, q=True)

# NOW THE getAttr command
mc.getAttr("rubiks.width")
mc.getAttr("rubiksShape.width")
mc.getAttr("polyCube1.width")

# Error: No object matches name: rubiks.width
# Traceback (most recent call last):
#   File "<maya console>", line 1, in <module>
# ValueError: No object matches name: rubiks.width #
mc.getAttr("rubiks.width")
# Error: No object matches name: rubiks1.width
# Traceback (most recent call last):
#   File "<maya console>", line 1, in <module>
# ValueError: No object matches name: rubiks1.width #
mc.getAttr("rubiksShape.width")
# Error: No object matches name: rubiks1Shape.width
# Traceback (most recent call last):
#   File "<maya console>", line 1, in <module>
# ValueError: No object matches name: rubiks1Shape.width #
mc.getAttr("polyCube1.width")
# Result: 1.0 #

mc.polyCube(sx=10, sy=15, sz=5, h=1, ch=True)
# result is a 20 units height rectangular box
# with 10 subdivisions along X, 15 along Y and 20 along Z.


mc.polyCube(sx=1, sy=1, sz=1, ax=(0, 1, 0), cuv=4, ch=0, w=1, h=1, d=1, name="rubiks")

mc.polyCube(name="boxey", sx=1, sy=1, sz=1)
mc.move(2, 2, 2)
mc.rotate(60, 0, 0, 'boxey')
# result has 5 subdivisions along all directions, default size

# query the width of a cube
w = mc.polyCube(name='boxey', w=True, q=True)

# MEL
# sphere -p 0 0 0 -ax 0 1 0 -ssw 0 -esw 360 -r 1 -d 3 -ut 0 -tol 0.01 -s 8 -nsp 4 -ch 1;objectMoveCommand;
mc.sphere()

mc.polyCube()

w = mc.polyCube(name='head')
mc.rotate(273, 15, 23, w[0])

# CAPTURING THE OUTPUT
myList = ["cats", "dogs", "living together"]
myList[0] = "parakeets"

w = mc.polyCube(name='head')
mc.rotate(273, 15, 23, w[0])
mc.move(0, 10, 0, w[0])
mc.scale(2, 2, 2, w[0])

# WHY VARIABLES??? CAN'T YOU JUST CALL IT BY NAME???
#
mc.polyCube(name='head')
mc.polyCube(name='head')  # the second one doesn't keep the name 'head'
# so assign the result or return value to a variable

x = mc.polyCube(name='head')
y = mc.polyCube(name='head')

# even though it's not named "head" you can still refer to it by using 'y'

mc.rotate(273, 15, 23, x[0])
mc.move(0, 10, 0, x[0])
mc.scale(2, 2, 2, x[0])

mc.rotate(-273, 15, 23, y[0])
mc.move(0, 10, 0, y[0])
mc.scale(2, 2, 2, y[0])

# NEXT SESSION will show how names can not be unique in maya and it can cause problems


# MORE ON MODULES
import maya.cmds as mc

# JUST USE LINUX PATHS IN MAYA
path = 'J:/projects/slinkyAgent/scenes/sphere.ma'
mc.file(path, query=True, exists=True)
mc.file(path, open=True)

"""
ASSIGNMENT
1. create with python some sort of model using at least 10 primitives in Maya
2. with python move the primitives into their proper location 
3. use a variable to capture each piece's name
4. comment each step so I know what you're trying to do

copy and paste the script into a text file
name the text file: firstname_lastname_week1.py
and post it to the workshop homework section
"""

