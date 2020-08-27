
# This purpose of this program is to demonstrate a
# few functions in the math module

import math

def main ():

    x = math.sqrt (3.5)
    y = math.sin (math.pi/2)   # should be in radians
    z = math.degrees (math.pi) # converts radians into degrees
    a = math.radians ( 30 )    # converts degrees into radians
    i = math.ceil (x)
    j = math.floor (y)

    print(x)
    print(y)
    print (a)
    print()

    print(i)
    print(j)

main ()   #calling the main () function
