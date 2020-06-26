#============================================================================================

# video 9 STRINGS ===========================================

'spam eggs'  # single quotes
#'spam eggs'

'doesn\'t'  # use \' to escape the single quote...
#"doesn't"

"doesn't"  # ...or use double quotes instead
#"doesn't"

'"Yes," he said.'
#'"Yes," he said.'

"\"Yes,\" he said."
#'"Yes," he said.'

'"Isn\'t," she said.'
#'"Isn\'t," she said.'

""" now we see triple quotes??  
    they can be comments put anywhere in your code
"""

# PATHS AND STRINGS VIDEO ==================================================================
path = 'C:\Users\geordie\Documents\maya\2015-x64\scripts'
# changes the 2011 to x815!
#forward slashes are escape characters and are shown in Sublime!!
path = 'C:\\Users\\geordie\\Documents\\maya\\2015-x64\\scripts' # escaped but this can be annoying

\205

# use the 'raw string literal' delclarative to auto escape all content
path = r'C:\Users\geordie\Documents\maya\2015-x64\scripts' # newline charactes won't work here

'''even if you use triple single quotes
       a comment if assigned to a variable 
            but you can put pretty much anything in between 
               and it won't cause problems'''
path = """C:\Users\geordie\Documents\maya\2011-x64\scripts"""
# not a comment if assigned to a variable but you STILL have to

# http://stackoverflow.com/questions/2081640/what-exactly-do-u-and-r-string-flags-do-in-python-and-what-are-raw-string-l

# JUST USE LINUX PATHS IN MAYA as we will see in the next section
path = 'J:/projects/slinkyAgent/scenes/sphere.ma' //

# NEW VIDEO ============================================================================
# == VARIABLES and WHAT'S HAPPENING UNDER THE HOOD ====================================
# Little bit more on strings what's happening in the computer

# I can reassign myName to some other value
myName = "Matt"
myName = "Daredevil"

hisName = "Daredevil"

id(myName)
id(hisName)

# what's happening in the computer
#http://foobarnbaz.com/2012/07/08/understanding-python-variables/

myName = "Matt"

myName = "Daredevil"

myName = "Matt"
id(myName)

hisName = "Matt"

id(hisName)

# Strings are sequences of characters indexed by integers.
# SHOW INT PHOTOSHOP
myName = "Daredevil"

# just D
myName[0]

# everything BUT the D
myName[0:]

# JUST Dare
myName[0:4]

# Just devil
myName[4: ]

# Just Dare again
myName[0:-5]

