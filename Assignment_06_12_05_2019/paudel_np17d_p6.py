# create a contact class 
class Contact():
# Contact() class has the following private attributes
# the __init__ method initializes the attributes
    def __init__( self, name = "unavailable", address = "unavailable", age = 0, phone = "unvailable", type = "NONE"):
        self.__name = name
        self.__address = address
        self.__age = age
        self.__phone = phone
        self.__type = type
# the following set methods set the corresponding attributes (setters)
    def setName ( self, name):
        self.__name = name
    def setAddress ( self, address):
        self.__address = address
    def setAge ( self, age):
        self.__age = age
    def setPhone ( self, phone):
        self.__phone = phone
    def setType ( self, type):
        self.__type = type
# the following get methods get (return) the corresponding attributes (getters)
    def getName ( self ):
        return self.__name
    def getAddress ( self ):
        return self.__address
    def getAge ( self ):
        return self.__age
    def getPhone ( self ):
        return self.__phone
    def getType ( self ):
        return self.__type
# the __str__ method returns the object's state as a string
# tells how to print that object
    def __str__ ( self ):
        return "Name: " + self.__name + \
               "\nAddress: " + self.__address + \
               "\nAge: " + self.__age + \
               "\nPhone: " + self.__phone + \
               "\nType: " + self.__type
# create an application using main (), class Contact() and other functions
# constant path for the file name
RAW_DIRECTORY = r"C:\Users\newki\Google Drive\Programming notes\Python\CGS_5935_Introduction_to_Programming_Using_Python\Assignment_06_12_05_2019\contacts.txt"
def main():
    # create a list of class objects which will store 5 contacts
    cont = make_contactList()
    # display the contacts in the list
    print ( " Here is the contact details you entered: " )
    display_contacts ( cont  )
    contactData = read_file(RAW_DIRECTORY)
def make_contactList():
    # create an empty list storing 5 contacts
    contact_list = []
    # add five Contact() objects to the list
    print( " Enter data for five contacts." )
    for contacts in range ( 1, 6 ):
        print ( " Contact number " + str (contacts) + ":" )
        name = input ( " Enter the person's name: " )
        address = input ( " Enter person's address: ")
        age = int ( input ( " Enter person's age: "))
        phone =  input ( " Enter person's phone number: ")
        type = input ( " Enter person's relation to you: ")
        print()

    #create a new Contact object in memory and assign
    # it to the phonr variable
        contact = Contact ( name, address, age, phone, type)

    # add the object to the list
        contact_list.append(contact)

    # return thr list
    return contact_list
            
def display_contacts ( contact_details ):
    for item in contact_details:
        print ( item.getName() )
        print ( item.getAddress() )
        print ( item.getAge() )
        print ( item.getPhone() )
        print ( item.getType() )
        print()
def open_file(filePath):
    try:
        inputFile = open ( filePath, 'r' )
        inputFile.close()
    except IOError:
        print(" Error occurred while opening the file. ")

    numContacts =  int ( inputFile.readline())
    print( numContacts )
                    
       
main()
                
            
               
    
