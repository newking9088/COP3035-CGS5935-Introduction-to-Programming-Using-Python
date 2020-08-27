################################################################################
# Assignment No. --> <05>
# Name --> Nawaraj Paudel
# Date --> 11/21/2019
# Email --> np17d@my.fsu.edu
# Grader --> Gradon
# Recitation Section --> <01>
################################################################################

# INPUT
# This program takes the input as user provided text files that contaion DNA
# sequences.

# OUTPUT
# This program outputs complement of DNA, mutation of DNA, and find if a sub-
# string is in DNA or not.

# SUMMARY
# This program takes a DNA sequence text file as input and user has four choices
# which are find complement, mutate, find substring and quit the program.
# Whatever choice the user chooses, the program does that and prints the output.

################################################################################
#                  *** IMPORT REQUIRED MODULES ***                             #
################################################################################
import random
################################################################################

################################################################################
def main():
################################################################################
    complement = ' '
    textFile =readFiles()
    operationToDo = userChoice ()
    printChoice(operationToDo)
    if ( operationToDo == 1 ):
        complement = complementDNA(textFile)
    elif ( operationToDo == 2 ):
        mutateDNA (textFile)
    elif ( operationToDo == 3 ):
        searchDNAIndex (textFile)
    else:
        quitProgram()

################################################################################    
def readFiles():
################################################################################
    text = ' '     # initialize text..optional

    while True:    # ask for the file path unless it is valid

        try:
            file_path = input("\"Please provide the path for the file you want to open\" <-  ")
            file = open (file_path, "r")
            text = file.read().rstrip('\n')   # strip \n if it is at the end of each line
            #if len (file_path) < 1:
            #file = open("Correct file path","r")

            return text  # this exits the while loop

        except:
            print("File not Found! Please try again with valid file path.\n")

################################################################################            
def userChoice ():
################################################################################
    print("Please carefully read the operation you want to perform given\
in the menu and choose a number between 1 to 4.\n")
    print ( "\n1. Determine the complement of the original DNA sequence\
read in, and print both the original and the complement in a parallel output\
format, for ease of comparison.\n\
\n2. Create 5 random simulated simple mutations in the DNA sequence. That is,\
in 5 positions your program selects pseudo-randomly, insert an \"M\" into the\
position to replace the A, T, G or C that was previously there. Then print both\
the original and the mutated sequence in parallel output format, again, for\
ease of comparison.\n\
\n3. Allow the user to enter a substring that he or she wants to search for in\
the original DNA sequence. For example, the user might search for a sequence\
such as \"AGTCA\" and find out where this sequence is located. In this program,\
you only need to find the first instance of such a substring, and report at\
what index it was located at. If the substring is not found, you must\
report that.\n\
\n4. Quit the program.\n")

    while True:

        try:
            choice = int ( input ( "Please enter a number between 1 to 4 <-  " ) )
            print()
            if ( choice < 1 ) or ( choice > 4 ):
                continue      # returns to start of while loop

            else:
                return choice
                      
        except:
            print ( "\nPlease make sure it is an integer between 1 to 4.\n" )

################################################################################
def printChoice (choice):
################################################################################
    print ("======================================================\n\
        Your choice of Operation is : {0:d}\n\
======================================================\n".format(choice))  

################################################################################
def complementDNA (originalDNASequence):
################################################################################
    print ( " To find the complement of a DNA sequence As are replaced by Ts,\
Ts by As. Gs by Cs, and Cs by Gs. For example, the complement of\
AATTGCCGT is TTAACGGCA.")
    comp = []
    for ch in originalDNASequence:
        if ch == "A":
            comp.append("T")
        if ch == "T":
            comp.append("A")
        if ch == "G":
            comp.append("C")
        if ch == "C":
            comp.append("G")

        
    #return ''.join(comp)   # joins list with a character
    print("Original:  ",originalDNASequence,'\n'
"Complement:", ''.join(comp))

################################################################################
def searchDNAIndex ( DNASequence ):
################################################################################
    search = input ( "Enter the substring you want to search for <-  ")
    startIdx = DNASequence.find (search )
    print( "\nOriginal DNASequence:", DNASequence )
    print ( "\nSubstring:", search )
    if search in DNASequence:
        print("\nSubstring found! It is located at an index", startIdx ,'!')
    else:
        print("\nSubstring", search, "not found!")

################################################################################
def mutateDNA (mutatingSequence):
################################################################################
    mutation = mutatingSequence
    for i in range(0,5):
        rand_num = random.randint(0, len(mutatingSequence) - 1)
        mutation = mutation[:rand_num] + "M" + mutation[rand_num + 1:]
        #return mutation
    print ("Original: ", mutatingSequence,'\n'
"Mutated:  ", mutation)

################################################################################    
def quitProgram ():
################################################################################
    print( "The execution of program finished!")

################################################################################        
main()
################################################################################
