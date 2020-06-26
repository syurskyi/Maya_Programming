#==========================================================================

# video 8 NUMBERS  ==================================================================
# lets see some math
2 + 2
#4

50 - 5*6
#20

 (50 - 5*6) / 4
#5

8 / 5  # division always returns a floating point number UNLESS YOU ARE IN python 2.x
"""
Until version 3, Python's division operator, /, behaved like C's division operator when 
presented with two integer arguments: it returns an integer result that's truncated 
down when there would be a fractional part. See: PEP 238
"""
#1   # python 2.7
#1.6 # python 3.x

17 / 3.0  # if one of the numbers is a float division returns a float
#
#5.666666666666667

17 // 3  # floor division discards the fractional part
#5
17 % 3  # the % (modulous) operator returns the remainder of the division
#2
5 * 3 + 2  # result * divisor + remainder
#17


5 ** 2  # 5 squared
#25
2 ** 7  # 2 to the power of 7
#128

# Order of operations
# PEMDAS but when in doubt... just use parentheses
10-3*5
# -5
(10-3)*5
# 35

# Assigning variables

width = 20
height = 5 * 9
width * height
#900

width = 20.0 # now it's a float
width * height
#900.0    -- the returned value is a float. any time a float is added to the mix. the answer will be a float

# not assigned
# blah

# this is called a traceback. this is an error.this is your friend.
# more on these later in the tracebacks section
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# NameError: name 'blah' is not defined