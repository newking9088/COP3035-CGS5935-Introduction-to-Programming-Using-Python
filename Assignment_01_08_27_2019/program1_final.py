Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 23:09:28) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
# ==============================================================================
# PROGRAM: Movie Box Office Receipts
#
# AUTHOR: <Nawaraj Paudel>
# FSU MAIL NAME: <np17d@my.fsu.edu>
# RECITATION SECTION NUMBER: <001>
# RECITATION INSTRUCTOR NAME: <Gradon>
# COP 3035 - Fall 2019
# PROJECT NUMBER: 1 
# DUE DATE: Tuesday 9/10/2019
# PLATFORM: Windows OS / Python 3
# 
# SUMMARY
#
# This program takes as input the name of a movie and how many adult and
# child tickets have been sold.  It then calculates the theater's gross
# and net profit for the night.  The theater keeps a percentage of the
# revenue from ticket sales, and the remainder goes to the distributor.
#
#INPUT
#
# All input is interactive.  The user inputs the movie title as a string,
# which may contain blanks, and inputs the number of tickets sold as
# whole numbers.
#
# OUTPUT
#
# The program prints an output title, echoprints the user's input in
# a readable fashion, and then prints out the calculated results.
#
# ASSUMPTIONS
#
# We assume that all input data is valid and correctly entered by the user.
# The program is therefore not guaranteed to work correctly if bad data
# is entered.

# ==============================================================================

# Date the file when it was executed, for date just use date only, today=date.today()
from datetime import datetime
now=datetime.now()

#format datetime.now() using strftime() function
nowFormatted=now.strftime("%m/%d/%y %H:%M:%S")

# named constants
ADULT_PRICE = 8.50    # adult ticket price
CHILD_PRICE = 4.75    # child ticket price
KEPT_PERCENT = 0.2    # percentage kept by theater
   
# print introductory program output heading
print ("******************************")
print ("Box Office Receipts Calculator")
print ("******************************\n")
   
# read the name of the movie from the user
movieName = input("Enter the name of the movie: ")

# read the number of adult tickets sold
adultTicketsSold = int(input("Enter the number of adult tickets sold: "))

# read the number of child tickets sold
childTicketsSold = int(input("Enter the number of child tickets sold: "))
   
# calculate gross profit
grossProfit = (adultTicketsSold * ADULT_PRICE) + (childTicketsSold * CHILD_PRICE)

# calculate the net profit               
netProfit = KEPT_PERCENT * grossProfit
   
# calculate the distributor's portion
distributorAmt = grossProfit * netProfit

# display final results
print ("\nRevenue Report")
print ("==============\n")
print ("Movie Name: ", movieName)
print ("Adult Tickets Sold: ", adultTicketsSold)
print ("Child Tickets Sold: ", childTicketsSold)
print ("Gross Box Office Profit: $",format(grossProfit,'8,.2f'))
print ("Net Box Office Profit: $",format(netProfit,'8,.2f'))
print ("Amount Paid to Distributor: $",format(distributorAmt,'8,.2f'),'\n')

# print closing message
print ("******************************************************")
print ("Thanks for Using the Box Office Receipts Calculator!!!")
print ("******************************************************\n")

#print date and time
print("Purchased On:",nowFormatted)

# ==============================================================================
#                              END OF PROGRAM
# ==============================================================================

