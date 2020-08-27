############################### Chapter - 3, Exercise - 7 ########################################
# Author: <Nawaraj Paudel>
##################################################################################################
                                  ## GRADE CALCULATOR ##
##################################################################################################

## ** SUMMARY ** ##
#
# It takes the two tests score and main test score. It checks if the student has obtained 25 marks
#in main test and average of equal or more than 50 on all the tests. If average is less than 50 or
##score obtained on main test is less than 25, it prints Fail grade. Prints distinction if average
# is greater than 80; prints Credit if average is less than 80 but more than 60; prints pass grade
#if the average is less than 60 and more or equal to 50.

# ** INPUT **
# It takes the two tests and main tests scores as input. Makes sure the input are in the given range:
# two tests score should be between 0 and 25; main test score should be between 0 and 50.

# ** OUTPUT **
# It calculates the average and prints the grade depending on the average score obtained. It prints an
#error message if the scores are not in the given range

# ** ASSUMPTIONS **
# The user enters the test scores as an integer

#set the flag

test_score_badInput = False

# define the constants used in the program

OVERALL_AVERAGE_SCORE = 50
MAIN_TEST_CUT_OFF = 25
DISTINCTION = 80
CREDIT = 60
PASS = 50
TEST_CUT_OFF_0 = 0
TEST_CUT_OFF_1 = 25
TEST_CUT_OFF_2 = 50


# define the user calculated variables
testFirstScore = 0   
testSecondScore = 0   # all of these scores are integer
testMainScore = 0
totalScore = 0

# print the name of the software at the head of output

print ( "==========================================================\n\
               GRADE CALCULATOR SOFTWARE\n\
==========================================================\n" )
            

#ask the user for the test scores and make sure they are valid
testFirstScore = int(input("Enter the first test score -> " ))
print()

testSecondScore = int(input("Enter the second test score -> "))
print()

testMainScore = int(input("Enter the main test score -> "))
print()

# test for validity of the input test scores and set the data flag appropriately
test_score_badInput = ( testFirstScore > TEST_CUT_OFF_1 ) or ( testFirstScore < TEST_CUT_OFF_0 ) or \
                        ( testSecondScore > TEST_CUT_OFF_1 ) or ( testSecondScore < TEST_CUT_OFF_0 ) or \
                       (testMainScore > TEST_CUT_OFF_2) or ( testMainScore < TEST_CUT_OFF_1)

#use print(test_score_badInput) using different data to make sure this logic is working

# make the decisions and print the results
if test_score_badInput:
    print("At least one of the test score is not in the valid range.\nPlease try again with the valid test scores.\n")

else:
    totalScore = testFirstScore + testSecondScore + testMainScore  #calculate the sum of scores

    if ( testMainScore >= MAIN_TEST_CUT_OFF ) and ( totalScore >= PASS ):
        if ( totalScore >= DISTINCTION ):
            print ( "Congratulations! You got Distinction grade with total score of %d.\n " %totalScore )
        elif ( totalScore >= CREDIT ):
            print ( "Congratulations! You got Credit grade with total score of %d.\n " %totalScore )
        else:
            print ( "Congratulations! You passed the test with total score of %d.\n " %totalScore )
    
    else:   # the complement is if ( testMainScore < MAIN_TEST_CUT_OFF ) or ( totalScore < PASS )
        print ( " Sorry! You failed the test with total score of %d. " %totalScore )

print ( "This program was executed successfully!\n ")
