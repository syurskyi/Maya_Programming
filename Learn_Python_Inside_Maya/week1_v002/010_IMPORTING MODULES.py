# video 10=== IMPORTING MODULES ============================

# Python programs are organized into modules and packages. More on Packages later.
# There are also hundreds of modules included in the python standard library.

# But what is a module?
#  -- any python source file can be used as a module with the 'import' statement
#
# What is the import statement?
# import is a command in python that brings in a bunch of commands.

# Here is a Dungeons and Dragons analogy
# in a game imagine you have a bunch of scrolls that have spells you need.
# but you can't cast the spell until you unfurl the scroll to get to the spell.
# that's import
#    it brings in the list of commands you need to run.
#
# here is an example
# say you need a pretty decently accurate value of pi for a conversion of some kind.
# 
# you could go to the web and look on google then bring it in and cut and paste it in
# 3.14. but that's not enough digits for accuracy. 
# one of the built ins has pi  -- math module


import math

# eval math
# Result: <module 'math' (built-in)> # 

# to look at a module you can use dir command
dir(math) # get a list of things in math

# try math.pi
math.pi
# Result: 3.141592653589793 # 

# here you see 

# why doesn't python just import all the modules? 
# has a bunch of modules you can use by default but they're not all 
# loaded at once to keep the memory down
# LIST of builtins
# https://docs.python.org/2/library/index.html

# CHECK TO SEE IF SOMETHING IS A KEYWORD
import keyword
keyword.iskeyword('text')
#True

# GET THE NUMBER OF VARIABLES POINTING TO A MEMORY ADDRESS
import sys
sys.getrefcount(myName)

# you can open a browser
import webbrowser
dir(webbrowser)
webbrowser.open

# use help on specific functions to see what they want
help(webbrowser.open)
#Help on function open in module webbrowser:

#open(url, new=0, autoraise=True)

#: summary modules hold commands and will load them when you import them.
# we will make our own module later in the workshop
# next video lets load some commands for maya
