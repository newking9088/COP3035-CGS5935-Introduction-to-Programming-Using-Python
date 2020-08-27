# Demo of recursive N factorial calculation

def main():

    N = 0    # we need an integer variable
    print ("Compute N factorial")
    N = int(input("Enter an integer: "))
    print ("N is: ", N)
    print ("N factorial is: ", Nfact(N))
    

def Nfact(N) :

    if ( N  <=  1 ):		# base case
        return 1
    else:			# recursive case
        return ( N * Nfact(N - 1) )
    

main()    # call to get things started

