def main():
    one = 0
    two = 0
    three = 0
    printStuff()
    one = 7
    two = 5
    three = 8

    halfOf(one)
    print(one, ' ', two, ' ', three, ' ')
    two,three = moveStuff(one,two,three)
    print(one,' ',two,' ',three, ' ')
    return
def printStuff():
    print("Python is fantastic")
    print("===================")
    return
def halfOf (num):
    print("Half of", num, "is",num/2.0)
    return
def moveStuff(first,second,third):
    third = second
    second = 4
    print(first, ' ', second, ' ',third)
    return (second, third)
main()
# Which line executes first? --> line 27 --> main()
# What is the output when line 11 executes? --> 7 5 8
#What is output when line 24 executes? --> 7 4 5
#Which statement executes last? --> line 14
