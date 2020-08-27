# a review of function action, side effect and return value

def main():

    # what does this print?
    callIt();

    print ("====================\n")

    # what does this print?
    print (callIt())
    print ()

def callIt ():

    # SIDE EFFECT: what the function does when it is called

    print ("hello there world!\n")

    # RETURN VALUE: what value it produces and puts in 
    # CPU register upon return

    return 5

main ()
