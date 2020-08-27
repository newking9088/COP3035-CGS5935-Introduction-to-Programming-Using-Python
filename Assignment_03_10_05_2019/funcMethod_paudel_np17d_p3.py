################################################################################

################################################################################

    # Assignment : 3
    # Author : <Nawaraj Paudel>
    # Email : <np17d@my.fsu.edu>
    # Recitation_Section : <001>
    # TA : <Gradon Stone>
    # Date : <10/06/2019>

#################################################################################
                         # CONVERSION CALCULATOR #
#################################################################################

    ## SUMMARY ##
# This program allows to choose one of the conversion option: Inches to Centimeters,
# Feet to Meters, Miles to Kilometers, Pounds to Kilograms, Gallons to Liters, and 
# final option to Quit the program. It takes one of these choices as interactive
# user input and converts accordingly. It checks for the bad user input, if the 
# input is invalid it asks the user to enter the valid user input again and again  
# unless it is valid. It prints the unit converted as the output of the program.

    ## INPUT ##
# It allows the user to choose what they want to be converted among the given 
#  choices, the user eneters the input as prompted

    ## OUTPUT ##
# It prints the result of converted unit of user chosen unit and prints executed

    ## BAD DATA CHECKING ##
# this program makes sure that user provides a valid input, unless it is valid the 
# program asks to enter the valid again and again


# def main () function which is control structure of the program
       
def main ():
# its a good idea to write as many variables or whatever to write
# in main program than writing in sub-ordinate programs

# all the variables defined in main() method are local by definition and we cannot
# access out of the main function. Either we should define these variables outside
# the function or declare as global inside the main() method

    global INCHES_TO_CENTIMETERS, FEETS_TO_METERS, MILES_TO_KILOMETERS,\
           POUNDS_TO_KILOGRAMS, GALLONS_TO_LITERS 
          
# we should define these golbal variables before they are initiated or defined
           
           
# define the user conversion constant

    INCHES_TO_CENTIMETERS = 2.5400   # 1 inch = 2.5400 cm
    FEETS_TO_METERS = 0.3048         # 1 ft = 0.3048 m
    MILES_TO_KILOMETERS = 1.6094     # 1 mi = 1.6094 km
    POUNDS_TO_KILOGRAMS = 0.4536     # 1 lb = 0.4536 kg
    GALLONS_TO_LITERS = 3.7853       # 1 gal = 3.7853 lit

# define the user input variables

    inches = 0.0   
    feets = 0.0
    miles = 0.0       # user inputs are floats
    pounds = 0.0
    gallons = 0.0
    choice = 0        # its an integer

# call the introduction function wchich prints an Intro

    printIntro ()

# call the selection function which tells the choices

    printChoices ()

# call the conversion function

    convFunc ( )    

# print the progaram execution message

    print ( "  This program was executed successfully.\n" )

#############################################################
         # def the function called above in order  #
#############################################################

def printIntro ():    # this is the 1st func called

    print ("  ########################################################### \n\
           Scientific Conversion Calculator\n\
  ###########################################################\n")

def printChoices ():  # this is the 2nd func called
    print ("    1. Inches to Centimeters\n\n\
    2. Feets to Meters\n\n\
    3. Miles to Kilometers\n\n\
    4. Pounds to Kilograms\n\n\
    5. Gallons to Liters\n\n\
    6. Quit the program\n")


# Asks the user to choose number from 1 to 6
    
    print ( "  Please choose a number from 1 to 6 to perform\n\
  the operation you want to perform.\n" )
    global choice # if its not declared as global, we cannot use in convFunc()
    # choice is about to get a value..we should declare global just before that

    choice = int ( input ( "   Please enter your choice of operation: ") )
    print ()
      
    
# Make sure the choice is in between 1 to 6

    while ( choice < 1 or choice > 6 ): #when it is False this loop is skipped
        choice = int ( input ("Please enter your choice of operation: ") )
        print()                         # this loop repeats as long as while is True

def convFunc ():
    if ( choice == 1 ):
        inches = float ( input ( "   Enter the Inch to be converted into Centimeter : " ))
        print ()
        while ( inches < 0 ) :
            print ( "   This program does not convert inches in negative numbers.\n" )
            inches = float ( input ( " Please enter (positive number) inch  : " ))
            print ()   # exit the while loop when while is False
        centimeters = inches * INCHES_TO_CENTIMETERS
        print ( " {0: .4f} inches is equivalent to {cm: .4f} centimeters.\n " \
                .format (inches, cm = centimeters) )
    

    elif ( choice == 2 ):
        feets = float ( input ( " Enter the Feets to be converted into Meters : " ))
        print ()
        while ( feets < 0 ) :
            print ( " This program does not convert Feets in negative numbers.\n" )
            feets = float ( input ( " Please enter (positive number) Feets  : " ))
            print ()   # exit the while loop when while is False
        meters = feets * FEETS_TO_METERS
        print ( "   %.4f feets is equivalent to %.4f meters.\n " % (feets, meters) )

    elif ( choice == 3 ):
        miles = float ( input ( " Enter the Miles to be converted into Kilometers : " ))
        print ()
        while ( miles < 0 ) :
            print ( " This program does not convert Miles in negative numbers.\n" )
            miles = float ( input ( " Please enter (positive number) Miles  : " ))
            print ()   # exit the while loop when while is False
        kilometers = miles * MILES_TO_KILOMETERS
        print ( "   {0:.4f} miles is equivalent to {1:.4f} kilometers.\n " \
                .format(miles, kilometers) )

    elif ( choice == 4 ):
        pounds = float ( input ( " Enter the Pounds to be converted into Kilograms : " ))
        print ()
        while ( pounds < 0 ) :
            print ( " This program does not convert Pounds in negative numbers.\n" )
            pounds = float ( input ( " Please enter (positive number) Pounds  : " ))
            print ()   # exit the while loop when while is False
        kilograms = pounds * POUNDS_TO_KILOGRAMS
        print ( "  %.4f pounds is equivalent to %.4f kilograms.\n " % (pounds, kilograms) )

    elif ( choice == 5 ):
        gallons = float ( input ( " Enter the Gallons to be converted into Liters : " ))
        print ()
        while ( gallons < 0 ) :
            print ( " This program does not convert Gallons in negative numbers.\n" )
            pounds = float ( input ( " Please enter (positive number) Gallons  : " ))
            print ()   # exit the while loop when while is False
        liters = gallons * GALLONS_TO_LITERS 
        print ( "   {0:.4f} {1} gallons is equivalent to {2:.4f} {3}.\n "\
                .format(gallons, "gallons", liters, "liters" ) )

    else:
        print("  Thank you for using Scientific Conversion Calculator!\n\n\
  Please press any key to continue ......\n ")

############################################################################################
                         # call the main function #
############################################################################################
main ()

