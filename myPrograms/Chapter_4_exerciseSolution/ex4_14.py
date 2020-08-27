######################################################
           # 4.14 #
######################################################
rows = 7          
for r in range (rows):
    for c in range (rows-r):
        print ('*', end = ' ')
    print()
#####################################################
# end = ' ' means do not print a new line as print
# function automatically prints a new line,adds space
# at the end and next print will be printed after
# this space on the same line..if no end = ' ' then
# the cursor moves to next line on the screen
#####################################################
# Note that  print () at the 4th line is necessary
# because it moves the screen to next line..end=' '
# prints a space after every iteration in column
# we have c in range (row-r) because we want to ite-
# rate this (inner loop) loop 7 times first and decr-
#crease gradually
