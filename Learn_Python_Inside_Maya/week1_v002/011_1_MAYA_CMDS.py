# video 11 = MAYA.CMDS =========================================== 

# Let's do some maya specific 
# press the cube button on the shelf
# look at the script editor

polyCube -w 1 -h 1 -d 1 -sx 1 -sy 1 -sz 1 -ax 0 1 0 -cuv 4 -ch 1;
// Result: pCube1 polyCube1 // 

# Every button and action is a "maya command" in maya
# these commands that are accessable by artists were called MEL commands
# until we run this next line of it's just generic python running in the script editor
import maya.cmds 
maya.cmds.polyCube()
#if you do this that's a lot of typing
# so alias the import to something short like 'mc'. this is called a namespace
import maya.cmds as mc

# I code a lot. I don't care what other coders do. I say type as little as you can. 
# save your wrists from carpal tunnel so you can have a long career.
# now we can command maya to make and do things.
# HOWEVER you may see this in someone else's code... 
from maya.cmds import *

# NEVER IMPORT * EVER EVER EVER EVER EVER
# they would do this if they didn't want to type mc. they could just type the command.
# I WILL KILL YOU IF YOU DO THIS. I WILL DISOWN YOU AND KICK YOU IN THE SHIN.
# this is lazy and stupid. lazy because mc. is not that much to type
# stupid because of collisions of commands. 
# if you do this the 'file' command that exists in python is now the 'file' command
# in maya commands. there are a bunch more. 

# LOOK AT THE MAYA Python DOcs
# find polyCube
# scroll to the bottom and look at examples
# polyCube  -sx 1  -sy 1  -sz 1  -ax 0 1 0  -cuv 4   -ch 0   -w 1    -h 1    -d 1 

# IN MEL the arguments with a dash at the beginning are called flags
# IN python they are called arguments
# in maya you can have a long name or a short name for the arguments.
# you can write your code with long names or short. 

#there are two types:
#    position and keyword args

# YOU CAN add arguments to these functions/methods that get used to create the objects
mc.polyCube(sx=1,sy=1,sz=1, ax=(0 1 0),  cuv=4,   ch=0,   w=1, h=1, d=1 )

# the ax argument requires three values in the middle the MEL command so put it in to the python as a tuple 

# A GENERAL RULE TO FOLLOW ABOUT MEL TO PYTHON
# 1. if there is a flag with 3 values in the middle somewhere, make it a tuple by putting it in parentheses



# =========== VIDEO commands in maya.cmds

# Move the cube and looks at the MEL
# example
# move -r 0.701215 2.684511 -2.714599 ;
# try and convert that to python and watch the error
mc.move(r=(2.5,2.5,2.5))

# Error: Flag 'r' must be passed a boolean argument
# Traceback (most recent call last):
#   File "<maya console>", line 1, in <module>
# TypeError: Flag 'r' must be passed a boolean argument # 

# LOOK AT THE MEL docs for the move command. 
# Notice that the floats are at the end.
# LOOK AT the PYTHON docs for the move tool.
# notice that the floats are at the beginning!, followed by keyword args, or args that have an equals sign in them.

mc.move(r=True,(2.5,2.5,2.5))
# Error: non-keyword arg after keyword arg
#   File "<maya console>", line 2
# SyntaxError: non-keyword arg after keyword arg # 

# What is a key word argument? More on this in a later session but what it basically means
# is that any argument with an equals sign has to go at the end. the ones in front are called positional
# this is a really big thing to know and applies to everything python. more on this in another session.
# KWargs ALWAYS come last in a method or function, because position is what is important to position args so they come first. 

mc.move((2.5,2.5,2.5),r=True)
# Error: Object (2.5, 2.5, 2.5) is invalid
# Traceback (most recent call last):
#   File "<maya console>", line 1, in <module>
# TypeError: Object (2.5, 2.5, 2.5) is invalid # 

# THE function wanted 3 floats but got one tuple. 
# what is a tuple? More on that in the next session. 
# remove the parentheses
mc.move(2.5,2.5,2.5,r=True)

# notice nothing happened but if you have the cube selected then it would move
# look at the docs under the first paragraph about default behavior

# select the cube and rerun
mc.move(2.5,2.5,2.5,r=True)


# CLEAR EVERYTING AND DO IT AGAIN ALL COMBINED
mc.polyCube(sx=1,sy=1,sz=1, ax=(0, 1, 0),  cuv=4,   ch=0,   w=1, h=1, d=1 )
mc.move(2.5,2.5,2.5,r=True,)
# notice it moved the cube because after the polyCube is created, maya selects it.
# so when the next line is run it is applied to the selected object.

# LET'S PUT IT ALL TOGETHER and add a rotate command
#    polyCube  -sx 1  -sy 1  -sz 1  -ax 0 1 0  -cuv 4   -ch 0   -w 1    -h 1    -d 1 
import maya.cmds as mc
mc.polyCube( sx=1, sy=1, sz=1, ax=(0, 1, 0),  cuv=4,   ch=0,   w=1, h=1, d=1 )
mc.move(3,4,5,r=True) 
mc.rotate(45,45,45)


# LETS LOOK AT SOME OF THE OTHER ARGUMENTS FOR polyCube.
# name=something
mc.polyCube( sx=1, sy=1, sz=1, ax=(0, 1, 0),  cuv=4,   ch=0,   w=1, h=1, d=1,name="rubiks" )

# BUT LOOK AT THE EXAMPLE in the docs, name is the first thing with no keyword. it is assigned to no variable. 
# w = cmds.polyCube( 'polyCube1', q=True, w=True )
# What is going on here? Let's try it with our cube
# query the width of a cube
w = cmds.polyCube( 'rubiks', q=True, w=True )

# Error: No object was specified to query
# Traceback (most recent call last):
#   File "<maya console>", line 1, in <module>
# RuntimeError: No object was specified to query # 
# WHY: construction history was off so no attr named 'width'
# so there is no "width" to query. recreate the cube with cn=True
mc.polyCube( sx=1, sy=1, sz=1, ax=(0, 1, 0),  cuv=4,   ch=1,   w=1, h=1, d=1,name="rubiks" )
mc.polyCube('rubiks', w=True,q=True)
# and now you get the width.
# maya has a weird attribute lookup in some commands that can be a bit confusing. I'll explain more 
# in the next video.
