# create constants and variables to be used
MAX = 9
row = 0
column = 0
product = 0

# print the beginning of the first line of output
print ("    ", end="")   # first print four blanks as a spacer

# print the rest of the first line
for column in range(1, MAX + 1):
    print ("%4d" % column, end="")
print ()

# print the remaining 9 lines forming a table (outer loop)
for row in range(1, MAX + 1):

    # first item on each line is the row number
    print ("%4d" % row, end="")

    # next print the 9 products (inner loop)
    for column in range (1, MAX + 1):
        product = row * column
        print ("%4d" % product, end="")
    print ()

print ()
