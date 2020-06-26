# video 7
#===== Print statement, commenting and variables ====================
#====================================================================

# A line of code is an instruction in text
# instructions with parentheses are called functions
# the stuff you put in between the parenthesies is called an argument

# strings are sequences of characters --  more on that in a few min.

print("today is tuesday") 

print('my name is Matt Murdock') # I am teaching python

# this is possible to not have the parentheses but it's not possible in new versions
# of python so it's best to use parentheses. 
print "this you can do" # only in python 2.7

# anything on this side of a hashtag or pound symbol is a comment
# you put comments in your code so you remember what you're doing 
# or so other people picking up your code can decipher what you were thinking

# you can put them after pretty much all of your code on any line more on that later


theHulk = 1  # and this is the second comment
          # ... and now a third!
text = "# This is not a comment because it's inside quotes."

pi = 3.14

# you just assigned a variable that is stored!! 
# this is called a string variable. 
# as I said earlier Strings are sequences of characters

text #hightlight and evaluate

# notice that text is BLUE in the maya script editor. This means it's a recognized command in MEL/maya.cmds. 
# as a python coder, I shouldn't use these as variable names. you don't want to accidentally reassign a command
# to some variable. but it's okay for now and you'll see why later. 

myName = "Matt" # when you see variables with a capital in the middle it's called camel case
my_name = 'Murdock' # underscores with all lower case is called PEP8. 
# notice you can use single quotes or double quotes. you can even use triple quotes.

someHtml = """ <strong>Matt Murdock </strong>"""

# triple quotes let you keep all the formatting inside. and they're used for other things. 
# I'll show you later when we talk about functions

print(myName)
print(my_name)
print(someHtml)

myName = '"Geordie"' #  you can use single quotes to preserve double quotes and vice versa
print(myName)



# let's talk a little bit about strings here
type(myName)
# Result: <type 'str'> # 

type(theHulk)
# Result: <type 'int'> # 

type(pi)
# Result: <type 'float'> # 

pi2 = "3.14"
type(pi2)
# Result: <type 'str'> # 

# python stores the type of var automatically. you don't have to think about it. 

# you can "cast" one type into another. you could convert a stringmy
# to a float 
useAsNumber = pi + float(pi2)
# Result: 6.28 # 

useAsWord = str(pi) + pi2
# Result: '3.143.14' # 
