
# ================================================================
# PROGRAM Lottery 

# AUTHOR: A. F. Tyson
# Example Program to be discussed in lecture

# *** SUMMARY *** 

# This program simulates one player playing a simple lottery  
# game. The rules are: 

#   the player bets $1 each play, then chooses a number between 1 
#       and 999
#   the computer draws a number in same range using a pseudo-random
#       number generator
#   if there is a match, the player wins $500
#   the player keeps playing the game until either he/she is broke
#       or wins once
    
# *** INPUT ***

# The player interactively enters each number he/she picks during play

# *** OUTPUT ***

# Consists of messages to the user indicating the status of his/her
# balance and whether he/she has won or not

# ================================================================

import random

# ================================================================

def main ():

    # create named constants                                                               int main ()
    START_BALANCE = 10   # player's starting balance
    WINNINGS = 500       # what player wins, if he/she does
    BET = 1              # the bet amount required
    MIN = 1              # minimum value to be picked or drawn
    MAX = 999            # maximum value to be picked or drawn

    # create variables
    numPicked = 0            # number player picks
    numDrawn = 0             # number computer draws
    balance = START_BALANCE  # start with this amount
    betNumber = 1            # number of current bet
    won = True               # flag; is true if the player wins

    # print an introductory title */
    print ("======================================================")
    print ("       Welcome to the Florida Mini-Lottery!!!")
    print ("======================================================")

    # keep playing until either the player runs out of money
    # or wins once
    while (balance != 0 and not won):
        # increment and print bet number
        betNumber += 1
        print ("\nThis is bet #", betNumber)
        
        # decrement balance and get number picked by player
        balance -= BET                     
        numPicked = int(input("Pick a number between %d and %d -> " % (MIN, MAX)))
        while numPicked <= MIN or numPicked >= MAX:
            numPicked = int(input("Invalid number! Please try again -> "))
        
        # get number drawn by computer and print it
        numDrawn = random.randint(1, MAX)
        print ("Number Drawn was: ", numDrawn )       

        # check for a match
        if numPicked == numDrawn:               # do match
            won = True
            print ("The numbers match! You win!")
        else:                                   # do NOT match
            print ("Sorry, no match.")
        # end of outer while loop
                              

    # print out an appropriate closing message
    print ("\nGame over !!!")
    if won:
        print ("You spent $%d" % (START_BALANCE - balance), end=" ")
        print ("to win $%d" % WINNINGS)
    else:
        print ("Oops! You''re BROKE! Better luck next time!" )

    # end of main function
    return


# ================================================================

main ()

# ================================================================

