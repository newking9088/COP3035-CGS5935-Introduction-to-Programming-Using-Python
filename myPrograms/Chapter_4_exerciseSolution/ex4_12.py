######################################################
              # 4.12 # Factorial
######################################################
nonnegativeInteger = int ( input ( " Enter the \
nonnegative integer to find the factorial -> " ) )

# set the accumulator
fact = 1

# set the count-controlled for loop

for i in range (1, nonnegativeInteger + 1 ):
    fact *= i

print (" The factorial of {0:1d} is : {1:4d}"\
       .format ( nonnegativeInteger, fact))
