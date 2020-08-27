def main():
    
    number = 0    # we need an int variable
    print ("TOWERS of Hanoi")
    print ("Enter a number of disks to play.")
    print ("    Then I'll give the necessary moves.")
    A = 'A'
    B = 'B'
    C = 'C'
    number = int(input("Enter a number: "))
    towers(number, A, B, C)

def towers(count, src, dest, spare):
    if (count == 1):
        print ("Move a disk from post " + \
              src + " to post " + \
              dest)
    else:
        towers(count - 1, src, spare, dest)
        towers(1, src, dest, spare)
        towers(count - 1, spare, dest, src)

main () 
