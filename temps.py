# ##############################################################################
# PROGRAM Temperatures
# Example program for discussion "live" in class
# Platform: Python 3 IDLE
#
# SUMMARY
#
# This program takes as input three body temperatures for a patient, 
# calculates the average temperature, and prints a message indicating 
# whether the patient has a fever (has a temp >= 100.0), is normal but 
# borderline (99.0 < average < 100.0), or is normal (average <= 99.0). 
# The values 99.0 and 100.0 are called the normal cutoff and the fever 
# cutoff.  Both are declared as named constants so that the program can 
# be easily changed later if new cutoffs are chosen. 
#
# INPUT
#
# This program uses as input the standard input stream, the keyboard.
# The patient ID number and the three temperatures are prompted 
# for and read in interactively.  All data must be entered as 
# appropriate numeric values for the program to work correctly.  The ID 
# number is an integer.  Temperatures are positive real numbers. 
#
# BAD DATA CHECKING: The temperatures are each tested.  If any one is 
# not positive, the program does not perform any calculations and a 
# message indicating invalid data is printed. 
#
# OUTPUT
#
# - echoprinted patient ID number and the three temperatures
# - average of the three temperatures
# - a message giving the status of the patient (normal, normal 
#   but borderline, or feverish)
#
# ASSUMPTIONS
#
# - that the patient ID number is valid
# - that the temperature has been taken three times (none missing) 
# - that a temperature is valid as long as it is positive; i.e.
#   sub-normal temperatures and extremely high temperatures are not
#   being handled in any special way 
#
# ##############################################################################

# create named constants				
NUM_TEMPS = 3          # number of temps per patient
NORMAL_CUTOFF = 99.0   # maximum normal temp
FEVER_CUTOFF = 100.0   # minimum fever temp
		
# create input data variables..this is called variable initialization or declaration
patientID = 0          # patient's identification number which is always an integer
temp1 = 0.0            # patient's first temperature, a float
temp2 = 0.0            #          second temperature, a float
temp3 = 0.0            # third temperature, a float

# create calculated variables
average = 0.0          # average of the 3 temperatures
dataOK = True          # true if all data is valid and
                       # false otherwise...this is called setting the flag

# print overall output title */
print ("\n============================")
print ("PATIENT TEMPERATURE ANALYSIS")
print ("============================\n")

# read input data from the keyboard
patientID = int(input("Enter Patient ID Number -> "))
print ()   #while writing/debugging program..do echoprint..that is test print(patientID)
temp1 = float(input("Enter temperature 1 -> "))
print ()
temp2 = float(input("Enter temperature 2 -> "))
print ()
temp3 = float(input("Enter temperature 3 -> "))

# test for validity of the input temperatures and
# set the data flag appropriately
dataOK = (temp1 > 0.0) and (temp2 > 0.0) and (temp3 > 0.0)
#use print(dataOK) using different data to make sure this logic is working

# now compute the average temperature and output message on
# patient status only if all temps are valid
if dataOK:    # determine results for valid data set

    # calculate floating point temperature average and output result
    average = (temp1 + temp2 + temp3) / float(NUM_TEMPS) #explicit is better than implicit so float(NUM_TEMPS) instead of just NUM_TEMPS
    print ("\nAverage Temperature: %.3f\n" % average)

    # print message giving status of patient
    print ("This patient is", end=' ')
    if average < FEVER_CUTOFF:									
        print ("normal.", end="")    # patient is normal)
											
        if average > NORMAL_CUTOFF:    # patient is normal
				       # but close to fever 
            print ("However, the patient is borderline.")
        else:
            print ()    #does print nothing..nothing to say to print
    else:    # patient is feverish
        print ("feverish.")

else:    # dataOK is false; at least one temp is not positive
    print ("\nInvalid Data: At least one temp is not positive.")

# print a final program closing message
print ("\nProgram Terminates Normally.")
	
# ##############################################################################
