#Assignment:2
#Author:<Nawaraj Paudel>
#Email:<np17d@my.fsu.edu>
#Recitation_Section:<001>
#TA: <Gradon Stone>
#Date:<09/20/2019>

##################  This a program to calculate the sale as a "SALES SOFTWARE CALCULATOR"  ##############################

## SUMMARY ##

######### This program takes the unit of items sold from the user input makes sure the input is valid or it #############
######### does bad data checking then calculates total cost of purchase applies the discount depending on the ###########
######### number of units soldthen calculates the cost per unit after discount and the total price of the whole #########
######### sale finally, print the total cost of sale and effective cost per unit ########################################

## INPUT ##

#This program prompts the user to enter the correct input:ask the user to enter the number of units solds as a whole number

## OUTPUT ##

####### This program calculates the total cost of purchase for the user entered number of unitssold it then  ##############
######################## calculates the cost per unit after the discount and total price of the whole sale  ###############

## BAD DATA CHECKING ##

################# It checks the input provided by the user if the input is not a whole number it shows #####################
################# ErrorMessage and ask the user to enter whole number with specific instruction ############################

## ASSUMPTIONS ##

########### -unitsSold as a whole number is typed correctly : data is not mistaken #########################################

#################### print the software name at the head of output #########################################################

print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n Welcome to the Software \
Sales Calculator\n -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\n")

##############     Retails price per package..named_constant..always in capital letters   ##################################

RETAILS = 99.0        ## this price is in "$"..its a good idea to write as a float as program has to convert to float ######
CUT_OFF_1ST = 10      #other float numbers in math operation..ex: RETAILS*0.2..so RETAILS has to be converted to float first
CUT_OFF_2ND = 20      ###################################### CUT-OFFS are always an integer ################################
CUT_OFF_3RD = 50      ##### Discont rate varies with the unitsSold..CUT_OFFs indicate different class of discount ##########
CUT_OFF_4TH = 100
DISCOUNT_0TH = 0.0
DISCOUNT_1ST = 0.2    ################## DISCOUNT are converted from percentage to fraction ################################
DISCOUNT_2ND = 0.3
DISCOUNT_3RD = 0.4    #### NB:ALL THE NUMBERS GIVEN IN PROGRAM ARE NAMED_CONSTANTS..PEP8 SUGGESTS TO LIST ALL OF THEM ######
DISCOUNT_4TH = 0.5

################  declaring the variables used in the program   ############################################################

unitsSold = 0                    ############################### its always an integer #####################################
total_cost_of_purchase = 0.0     ############################### its a float ,or real number ###############################
effective_cost_per_unit = 0.0    ############################### its a float ,or real number ###############################

###############  set the flag for unitsSold data input      #################################################################

bad_input = True

############### Prompt the user to provide the number of units sold  #########################################################

############### Make sure program does not work untill the data is not a whole number ########################################
while True:
    try:

        unitsSold=int(input("How many items were sold --> "))
        print()                           ######### leaves a blank line after unitsSold ######################################

        bad_input=(unitsSold<=0)

        if bad_input:

            print("Please enter a valid input:\nUnits sold can only be positive integer or a whole number!\n")
            continue          ######## returns to the start of the while/for loop until it is a valid input ##################  
                              ## Enter 0 as input and remove continue...see what happens...that explains all #################
    except ValueError:        ## Pass , in contrast, takes it to next logical step and does calculation with 0 as input ######   

            print("Integer type input expected. Float or string is not a valid input.\n")

    else:

        print("Processing....Please wait for a while!\n")
        break                                ###########  break statement takes you out of the loop and moves to next step #######
                                             ########### without it the loops keep iterating and does not move to next step ######
if (unitsSold < CUT_OFF_1ST) :
    total_cost_of_purchase= (float(unitsSold) * RETAILS) * (1.0 - DISCOUNT_0TH)
    effective_cost_per_unit=RETAILS
    print("The effective cost per unit is: $%05.2f\n"%effective_cost_per_unit)    ## this is how we format the number to two decimals##
    print("The total cost of the purchase is: $%05.2f\n"%total_cost_of_purchase)  ### 05 means use at least 10 spaces;% means ######### 
                                                                                  ##  a placeholder..2f means 2 floors ################
elif (unitsSold < CUT_OFF_2ND) :
        total_cost_of_purchase = (float(unitsSold) * RETAILS) * (1.0 - DISCOUNT_1ST)        
        effective_cost_per_unit = total_cost_of_purchase / float(unitsSold)
        print("The effective cost per unit is: $%05.2f\n"%effective_cost_per_unit)    ### \n leaves a line after it is printed #########
        print("The total cost of the purchase is: $%05.2f\n"%total_cost_of_purchase)

elif (unitsSold < CUT_OFF_3RD) :
    total_cost_of_purchase = (float(unitsSold) * RETAILS) * (1.0 - DISCOUNT_2ND)
    effective_cost_per_unit = total_cost_of_purchase / float(unitsSold)
    print("The effective cost per unit is: $%05.2f\n"%effective_cost_per_unit)    
    print("The total cost of the purchase is: $%05.2f\n"%total_cost_of_purchase)

elif (unitsSold < CUT_OFF_4TH) :
    total_cost_of_purchase = (float(unitsSold) * RETAILS) * (1.0 - DISCOUNT_3RD)
    effective_cost_per_unit = total_cost_of_purchase / float(unitsSold)
    print("The effective cost per unit is: $%05.2f\n"%effective_cost_per_unit)    
    print("The total cost of the purchase is: $%05.2f\n"%total_cost_of_purchase)

else:
    total_cost_of_purchase = (float(unitsSold) * RETAILS) * (1.0 - DISCOUNT_4TH)
    effective_cost_per_unit = total_cost_of_purchase / float(unitsSold)
    print("The effective cost per unit is: $%05.2f\n"%effective_cost_per_unit)    
    print("The total cost of the purchase is: $%05.2f\n"%total_cost_of_purchase)       

   
###### This is a good idea as it makes sure that the program runs till the end and no syntax error occurred in between ################

print("Execution Terminated Normally.") 





    
               

