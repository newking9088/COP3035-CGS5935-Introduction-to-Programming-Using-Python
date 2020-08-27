# ##############################################################################
# PROGRAM Grading

# AUTHOR: A. Ford Tyson
# Example program for use in lecture

# Note: This program is meant to be an example of a longer program which 
# utilizes multiple functions.  With this program we will examine top-down
# design, program structure, style in a program using multiple functions,
# functions themselves and parameter passing.

# SUMMARY

# This program determines final letter grades for students, given their
# scores on 3 tests.  The average test score is calculated, and then the letter
# grade is determined based on the average using a "standard curve".  Using this
# curve, 90-100 gives an 'A', 80-89 a 'B', etc.  The program also reads and
# prints the student's ID number, determines if he/she is a state resident or
# not, and prints the residency status. 

# INPUT

# This program requires interactive input. For each student, the ID number
# and his/her test score are read.

# The ID number is a 6-digit integer which does not start with 
# a zero, and the test scores are numbers from 0 thru 100, inclusive.  If the
# sum of the digits in the ID number is even, then the student is a state
# resident.  If the sum is odd, the student is a non-resident. 

# OUTPUT >>>

# The program outputs values and results for each student including:
#    student's ID number
#    his/her residency status
#    his/her scores
#    his/her average score
#    his/her letter grade

# ASSUMPTIONS

# All input data is assumed to be present and valid. No bad data checking
# is done. Exercise for class: think about where and how you would add
# bad data checking in this program.

# DATA STRUCTURES

# No major data structures are used by this program.

# ##############################################################################
# GLOBAL NAMED CONSTANTS

# number of scores per student
NUM_SCORES = 3

# ##############################################################################
# MAIN FUNCTION

def main():

    # create variables
    average = 0        # average score for current student
    letgrade = ''      # current student's letter grade
    response = 'y'     # user's response, yes or no as a character
    
    # print output heading
    printHeading()

    # process one student at a time until user wants to stop
    while (response == 'y' or response == 'Y'):
        # read and print one student ID number, and his/her residency status
        processID()

        # obtain student's scores and average exam score
        average = getAverage()

        # find student's letter grade, then print average and letter grade
        letgrade = getLetGrade(average)
        print ("\nCalculated Results")
        print ("------------------")
        print ("Student Average: %.2f" % average)
        print ("Student Final Letter Grade: ", letgrade)

        # ask if user wants to enter another student or not
        response = input("\nDo you want to process another student?" +
                             " Enter y or n -> ")
        while (response != 'y' and response != 'n' and
               response != 'Y' and response != 'N'):
              response = input("Please re-enter -> ")

    # print a closing message
    print ("\nExecution Finished.")
    

# ##############################################################################


def printHeading():

    # This function simply prints the output heading and information
    # for the user.
    # Called By: main

    # print overall title for output
    print ("=============================")
    print ("STUDENT FINAL GRADING PROGRAM")
    print ("=============================\n")

    # print information for the user
    print ("This program will assist you in calculating final")
    print ("letter grades for your students. You will enter")
    print ("each student's ID number (a 6-digit integer that")
    print ("does not start with zero), and their %d scores." % NUM_SCORES)
    print ("This program will then display the student's")
    print ("average score and final letter grade.\n")
    print ("Please report any bugs to the COP 3035 class at FSU!!!\n")


# ##############################################################################


def processID():

    # This function reads the current student's ID number, and echoprints it.
    # Next it calls isSumDigEven to determine if the student is a state
    # resident or not, and prints a result giving the residency status.
    # Called By: main

    # create local variables
    IDnum = 0               # the student's ID number
    stateResident = True    # flag for residency status; true if a resident

    # get the ID number and echoprint it
    IDnum = int(input("Enter the ID number -> "))
    print ("The ID number is: ", IDnum)

    # call getResidency to determine if the student is a resident or not
    # then print the result
    stateResident = isSumDigEven(IDnum)
    print ("Residency Status of this student: ", end="")
    if (stateResident):
        print ("Resident\n")
    else:
        print ("Non-Resident\n")


# ##############################################################################


def isSumDigEven(num):    # receives integer number
			  # returns sum status
			  
    # This function illustrates a "generic" function

    # Takes an integer number as input, and determines if the sum of the
    # digits is even or not.  Returns a Boolean value giving the sum's status:
    # True if all digits in the number add up to an even number and False
    # if the digits add up to an odd value.
    # Called By: processID

    # create local variables
    isEven = False       # true if sum of digits is even
    digitSum = 0         # sum of the digits in the number
    remainder = 0        # used to store remainder from modulus divisions
    workingNum = 0       # used to store the number at first, then fewer and
                         # fewer digits of the number as digits are taken
                         # off the right end
						      
    workingNum = num     # copy the number passed in, to the working value

    while (workingNum >= 10):            # get the sum of the digits										// by breaking off each digit, going from
        remainder = workingNum % 10      # right to left in the number.
        workingNum = workingNum // 10    # keep a running total of the digits.
        digitSum = digitSum + remainder	

    digitSum = digitSum + workingNum     # add in the final, leftmost digit

    if (digitSum % 2 == 0):        # set the flag to return True if the
        isEven = True              # sum of the digits is even

    return isEven                  # then return the value of the flag


# ##############################################################################


def getAverage():

    # This function takes no input from the caller. It reads all the scores for
    # one student, keeps a running total of scores, and finally calculates the
    # student's score average using integer division. This average is returned
    # to the caller.
    # Called By: main

    # create local variables
    sum = 0        # running total of sum of scores
    score = 0      # current score read
    average = 0    # the average score calculated here
    count = 0      # loop control variable

    # accumulate total of all scores in sum
    for count in range(1, NUM_SCORES + 1):
        score = int(input("Enter a score -> "))
        print ("Score: ", score)
        sum = sum + score

    # determine this student's average
    average = sum / NUM_SCORES
    return average


# ##############################################################################


def getLetGrade(average):  # receives score average for one student 
			   # returns letter grade for that student

    # This function takes as input a student's score average, calculates the
    # corresponding letter grade based on a "standard curve", and then returns
    # this grade to the caller as its result.
    # Called By: main

    # create local variables
    letgrade = ''            # stores the calculated letter grade
    avgCase = average // 10  # break off 1st digit (or 1st 2 if 100)

    # determine the letter grade based on avgCase and return it
    if avgCase == 10 or avgCase == 9:
        letgrade = 'A'
    elif avgCase == 8:
        letgrade = 'B'
    elif avgCase == 7:
        letgrade = 'C'
    elif avgCase == 6:
        letgrade = 'D'
    else:
        letgrade = 'F'

    return letgrade


# ##############################################################################
# call  main to initiate program execution

main()

# ##############################################################################
#           E N D    O F    P R O G R A M    G R A D I N G                      
# ##############################################################################
