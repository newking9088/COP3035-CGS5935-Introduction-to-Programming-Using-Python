# ##############################################################################
# zipZap.py
# if you can trace through this program by hand and predict
# the output correctly yourself, you have a 
# decent understanding of the basics of parameter passing,
# block structure and scope
#
# the correct output values are
#       0     100     200
#       0       7     203
#      -5       5     203
#
# ##############################################################################

SPACER  =  "     "		# a global constant string of 5 blanks
z = 10                          # a global variable

# ##############################################################################
def main():
    global z
    x = -5
    y = 5		
    z = 15
    zip (x, y)
    print (x, SPACER, y, SPACER, z)

# ##############################################################################
def zip (y, x):
    global z
    x = x + y
    y = 7	
    z = zap(y, x)
    print (x, SPACER, y, SPACER, z)

# ##############################################################################
def zap (x, y):
    z = 0    # this z is local !!!
    x = y
    y = 100
    z = 200
    print (x, SPACER, y, SPACER, z)
    return (z + 3)

# ##############################################################################
main()
# ##############################################################################
