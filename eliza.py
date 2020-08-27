# -------------------------------------------------------------------------------
# Eliza - the very famous and totally free psychotherapy program
# -------------------------------------------------------------------------------

# control some optional output with this flag
TESTING_ON = True

def main():

    # print some welcoming output and ask user's name
    name = input("Hello and welcome. What is your name? ")
    print ("Type quit any time you want to finish.")
    print ("There will be NO charge! Some say you get what you pay for...\n")
    line = input("Well " + name + ". What can we do for you today? ")

    # keep processing input and replying until user types quit
    while line != "quit":
        line = line.lower()
        reply = getReply(line, line.split())
        print()
        line = input(reply)

    # say goodbye and end the run
    print ("\nGoodbye " + name + ", see you again soon!")
    return
                     
# -------------------------------------------------------------------------------

def getReply (line, words):

    replyOut = ""    # the reply generated by this function

    if TESTING_ON:
        print (line)
        print (words)
    
    # find a reply based on words in the statement
    if len(words) == 0: 
        replyOut = "You have to talk to me. "
    elif line[-1] == '?':
        replyOut = "Why do you want to know? "
    elif "mother" in words:
        replyOut = "Tell me more about your mother. "
    elif "father" in words:
        replyOut = "Tell me more about your father. "
    elif "sister" in words:
        replyOut = "Tell me more about your sister. "
    elif "brother" in words:
        replyOut = "Tell me more about your brother. "
    elif "uncle" in words:
        replyOut = "Tell me more about your uncle. "
    elif "aunt" in words:
        replyOut = "Tell me more about your aunt. "
    elif words[0] == "i" and words[1] == "feel":
        replyOut = "Why do you feel that way? "
    elif words[0] == "i" and words[1] == "think":
        replyOut = "Do you really think so? "
    else:
        replyOut = "Tell me more. "

    # send back this amazing insightful comment !
    return(replyOut)

# -------------------------------------------------------------------------------

main ()

# -------------------------------------------------------------------------------