#################################################################################################
                            # RESTAURANT TYPES BASED ON FOOD SERVING #
##################################################################################################

########################### DocString at the top of the program file   ###########################

""" THE RESTAURANT IN OUR CHAIN ARE LISTED BELOW.
    WE WELCOME TO OUR BUSINESS AND WE ARE HAPPY TO
    SERVE YOU TODAY AND FOREVER. HAVE A GOOD MEAL"""

#set the flag

inputOK = True

print("==========================================\n\
    WELCOME TO OUR RESTAURANT CHAIN\n\
==========================================\n")    
print("1. Joe's Gourmet Burgers\n")
print("2. Main Street Pizza Company\n")
print("3. Corner Cafe\n")
print("4. Mama's Fine Italian\n")
print("5. The Chef's Kitchen\n")

selectRestaurant = int (input ( "Enter one number from 1 to 5 to select your restaurant -> " ))
print()

inputOK= ( selectRestaurant >= 1 ) and ( selectRestaurant <= 5 )

while inputOK :
    if ( selectRestaurant == 1 ):
        print("Our restaurant choices are as follow:\n\
1. Vegeterian: NO\n\
2. Vegan : NO\n\
3. Glutten-Free: NO\n")
          
          
    elif  ( selectRestaurant == 2 ):
        print("Our restaurant choices are as follow:\n\
1. Vegeterian: YES\n\
2. Vegan : NO\n\
3. Glutten-Free: YES\n")

    elif ( selectRestaurant == 3 ):
        print("Our restaurant choices are as follow:\n\
1. Vegeterian: YES\n\
2. Vegan : YES\n\
3. Glutten-Free: YES\n")

    elif ( selectRestaurant == 4 ):
        print("Our restaurant choices are as follow:\n\
1. Vegeterian: YES\n\
2. Vegan : NO\n\
3. Glutten-Free: NO\n")

    elif ( selectRestaurant == 5 ):
        print("Our restaurant choices are as follow:\n\
1. Vegeterian: YES\n\
2. Vegan : YES\n\
3. Glutten-Free: YES\n")

    inputOK = ( selectRestaurant < 1 ) or ( selectRestaurant > 5 )   # this exits the while loop


else:
    print("Please make sure you chosose one of the five restaurants shown at the top in the list!\n")


print("This program was executed sucessfully.\n")

