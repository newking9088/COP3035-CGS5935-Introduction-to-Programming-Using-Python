# ####################################################################

# PROGRAM Functions 1
# AUTHOR: Mr. Wizard
# For discussion in lecture

# First example program with multiple functions.

# SUMMARY

# This program allows its user to enter three integers, and then 
# prints out the maximum of the three values. 

# INPUT 

# All input is interactive.  The user is prompted for the three 
# numbers.

# OUTPUT

# An introductory text is printed giving basic information to the 
# user about what the program does.  Next, he/she is prompted for the 
# three integers.  Finally the maximum is printed, and a brief 
# closing message.

# ASSUMPTIONS

# That all input data is valid, thus no bad data checking is done.       
# That nothing special has to be done in the case of equal values.

# ####################################################################

def main ():

    one = 0    # create three integer variables
    two = 0    # values to be entered by user later on
    three = 0  # these are called GLOBAL VARIABLE

    # print introductory material for the user
    printIntro ()            # this func is called

    # prompt for three integers, then read them
    one = int(input("Enter the first integer value -> "))
    two = int(input("Enter the second integer value -> "))
    three = int(input("Enter the third integer value -> "))

    # find the maximum of the three, and print it
    # findMax determines and then prints the max
    findMax (one, two, three)   # this func is called

    # print a closing message
    print ("Thanks for using our maximum determination program!")

# ####################################################################

def printIntro ():

    # This function simply prints out a welcoming message and some
    # initial information to the user about how the program works.

    print ("======================================================")
    print ("         Welcome to the the MAXIMUM program!")
    print ("======================================================\n") 
    print ("First you will be asked to enter three whole numbers.")
    print ("Then the program will give you the maximum value")
    print ("of the three.\n")

# ####################################################################

def findMax (first,    # the three values for which the
             second,   # max must be found
             third):		
														
    # This function takes as input three integer values.  It
    # determines the maximum of the three values, and then prints
    # out this number.

    print ("\nThe maximum is: ", end="")
    if first > second:		# this nested if finds the 
        if first > third:	# maximum value of first, 
            print (first)	# second, and third 
        else:
            print (third)
    else:
        if second > third:
            print (second)
        else:
            print (third)
    print

# ####################################################################

main ()

# ####################################################################




