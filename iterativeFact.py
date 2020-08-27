# Demo of an iteractive factorial calculation

def main():

    N = 0    # we need an integer variable
    print ("Compute N factorial")
    N = int(input("Enter an integer: "))
    print ("N is: ", N)
    print ("N factorial is: ", Nfact2(N))
    

def Nfact2 (N) :

    result = 1
    for countdown in range (N, 1, -1)  :
        result = result * countdown;
    return result
    

main()    # call to get things started

