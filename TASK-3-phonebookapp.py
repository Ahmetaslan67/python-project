## Problem Statement

# - Write a program that creates a phonebook, adds requested contacts to the phonebook, finds them, and removes them.

# - There should be 4 options available to the user and from the options, users should be able to add, find, delete contacts, or terminate the program as shown below.

# - Phonebook has users and their corresponding phone numbers.

# - At the beginning of the program the phonebook will be empty and user can choose to add new contacts to the phonebook.

# - Program should ask user for the input, after giving information text shown as below.
# PB:"PhoneBook", ON: "OperationNumber", NM: "Name", NO: "Number"

print("Welcome to the phonebook application:")
print("1. Find phone number")
print("2. Insert a phone number")
print("3. Delete a person from the phonebook")
print("4. Terminate")


PB={}

while True:
    try:
        ON=int(input("Select an operation number (1 - 4): "))
        print(PB)
        print("Please enter a number between 1-4")
        if ON==1:
            if PB!={}:
                NM=input("Please enter person's name for the phone number: ").title()
                print(NM, PB[NM], sep= " : ")
            else:
                print("Empty list")
        elif ON==2:
            NM=input("Insert name of the person: ").title()
            NO=input("Insert phone number of the person: ")
            try:
                if type(int(NO)) == int:
                    PB[NM]=NO
                    print(f"Phone number of {NM} is inserted into the phonebook")
            except:
                print("Invalid input format, cancelling operation ...")
        elif ON==3:
            NM=input("Whom to delete from phonebook: ").title()
            if PB !={} and NM in PB:
                PB.pop(NM)
                print(f"{NM} is deleted from the phonebook")
            else:
                print(f"{NM} is not in the phonebook")
        elif ON==4:
            print("Exiting Phonebook")
            break
        else:
            print(f" operation number {ON} must be number and between 1-4")

    except:
        print("Not valid input")

