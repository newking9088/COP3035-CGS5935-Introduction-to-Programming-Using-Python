# how to sum digits in a given digit

digit = int (input ("Enter the number: "))
total = 0       # set accumulator to zero
count = digit   # priming read for while loop

while ( digit > 0 ):
    rem = digit % 10
    total += rem
    digit = int ( digit / 10 )
 
print ("The sum of {1} in a given {0} is: {2:3d}\n"\
.format ("number","digits",total)) # prints the sum
    
    
