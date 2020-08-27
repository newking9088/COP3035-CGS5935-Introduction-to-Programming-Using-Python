inputPIN = 0   
validPIN = False
userPIN = 9999   # for example use only !

inputPIN = int(input("Please enter your PIN -> ")) 
validPIN = (inputPIN == userPIN)
while not validPIN:
    inputPIN = int(input("Please try again. Enter your PIN -> "))
    validPIN = (inputPIN == userPIN)

# know complement is true after loop exits
# therefore the PIN entered is valid here
