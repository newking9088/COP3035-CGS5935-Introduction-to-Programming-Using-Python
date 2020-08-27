# ==============================================================================
# PROGRAM Movie Box Office Receipts
#
# AUTHOR: <type your name here>
# FSU MAIL NAME: <type your FSU ID here>
# RECITATION SECTION NUMBER: <type your section number here>
# RECITATION INSTRUCTOR NAME: <type your TA's name here>
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

# named constants
ADULT_PRICE = 8.50    # adult ticket price
CHILD_PRICE = 4.75    # child ticket price
KEPT_PERCENT = 0.2    # percentage kept by theater
   
# print introductory program output heading
print ('******************************')
print ('Box Office Receipts Calculator')
print ('******************************\n')
   
# read the name of the movie from the user
movieName = input('Enter the name of the movie: ')

# read the number of adult tickets sold
adultTicketsSold = int(input('Enter the number of adult tickets sold: '))

# read the number of child tickets sold
childTicketsSold = int(input('Enter the number of child tickets sold: '))
   
# calculate gross profit
grossProfit = (adultTicketsSold * ADULT_PRICE) + (childTicketsSold * CHILD_PRICE)

# calculate the net profit               
netProfit = KEPT_PERCENT * grossProfit
   
# calculate the distributor's portion
distributorAmt = grossProfit * netProfit

# display final results
print ('\nRevenue Report')
print ('==============\n')
print ('Movie Name: ', movieName)
print ('Adult Tickets Sold: ', adultTicketsSold)
print ('Child Tickets Sold: ', childTicketsSold)
print ('Gross Box Office Profit: $%.2f' % grossProfit)
print ('Net Box Office Profit: $%.2f' % netProfit)
print ('Amount Paid to Distributor: $%.2f\n' % distributorAmt)

# print closing message
print ('******************************************************')
print ('Thanks for Using the Box Office Receipts Calculator!!!')
print ('******************************************************')

# ==============================================================================
#                              END OF PROGRAM
# ==============================================================================
