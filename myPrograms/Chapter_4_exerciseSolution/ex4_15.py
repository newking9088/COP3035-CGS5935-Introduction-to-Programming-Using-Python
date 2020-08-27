######################################################
           # 4.15 #
######################################################

for row in range (6):
    for column in range (2):
        print ('#', end = ' '*row)
    print()

# Note that  print () at the 4th line is necessary
# because it moves the screen to next line..end=' '
# prints a space after every iteration in column
# we have column range in 2 because we want it to
# iterate only two times and print two hash i.e.##
