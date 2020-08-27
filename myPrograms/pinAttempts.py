#Author: <Nawaraj Paudel>

########## Created to understand multiterminal conditioned while loop #########


###############################################################################
                     #Password Security#
################################################################################

## *** SUMMARY *** ##
# This program asks the user to enter the password for the system and gives maximum 
#three attempts. If the passord is correct in given number of attempts it allows the 
#user to access the system otherwise it asks the user to try again after 15 minutes.

## *** INPUT *** ##
# It asks the user to enter four digits as password.#

## ** OUTPUT ** ##
#If the user input is correct it prints a message saying welcome otherwise asks the  
# user to wait for 15 minutes before they can try

# Define the constant used in the program

MAX_TRY=3

#Define the variable used in the program

inputPIN = 0        #one advantage of initialization is it is defined
validPIN = False    #initially it is always False
correctPIN = 5913

#print the title of the program
print("\t=========================================================\n\
             \tWelcome to CyberSecurity Program\n\
\t=========================================================\n")       


#ask the user for input so that we can set the flag to either True or False

inputPIN= int(input("Enter the pin-> "))
print()

validPIN= (inputPIN == correctPIN) #its False cos they are not equal initially

numTry=1                         # we can initialize to 0 as well

while (not validPIN) and (numTry != MAX_TRY):
    print("You have %d tries left\n"%(MAX_TRY-numTry))  #you should put it before inputPIN
    inputPIN = int(input("Try again! Enter the pin-> "))#cos you already have entered PIN once
    print()
    numTry += 1
    validPIN = (inputPIN == correctPIN)                      
#it exits the loop only when valid pin is true or set the compliment flag
#NB: but never write validPIN =True otherwise it exits the loop
# even when inputPIN!=correctPIN

#set the messages to print
    
if validPIN:
    print("Welcome to the program!\n")
else:
    print("Sorry! Please try again after 15 minutes.\n")

