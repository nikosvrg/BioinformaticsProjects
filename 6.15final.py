numLetters = 30
numToTake = 0
numToTakePC = 1
input3 = input(print("Would you like to play first?(y/n)"))


while numLetters > 0:
    if (input3 == "y"):  # an o xrhsths pathsei y tote tha paiksei prwtos
        print("\nThere are ", numLetters, " letters.")
        numToTake = input(print("How many letters to take? (1 or 2)"))
        numToTake = int(numToTake)

        if (numToTake >= 2):  # an o xrhsths pathsei to 2 tote sto numtotake tha apothkeutei to 2
            numToTake = 2

        elif numToTake <= 1:  # antistoixa an pathsei 1
            numToTake = 1

        numLetters = numLetters - numToTake  # analoga me to ti exei dwsei ws input o xrhsths,tha afairethei apo to numbletters

        if numLetters <= 0:  # an den uparxoun alla numletters tote o xrhsths kerdizei
            print("You won!")

        elif ((numLetters - numToTakePC) <= 0 or numLetters <= 0):  # an o upologisths kerdizei afairwntas 2 tote afairei 2
            numToTakePC = 2
            print("Computer takes ", numToTakePC, " letters.")
            print("You lost")

        else:  # alliws afairei 1
            numToTakePC = 1
            print("Computer takes ", numToTakePC, " letters.")
            if (numLetters <=0):
                print("You lost")

        numLetters = numLetters - numToTakePC




    elif(input3 == "n"):  # an paizei deuteros o xrhsths

        print("There are ", numLetters, " letters.")

        numLetters = numLetters - numToTakePC
        print("\nComputer takes ", numToTakePC, " letters.")

        print("There are ", numLetters, " letters.")
        numToTake = input(print("\nHow many letters to take? (1 or 2)"))
        numToTake = int(numToTake)

        if (numToTake == 2):  # an o xrhsths pathsei to 2 tote sto numtotake tha apothkeutei to 2
            numToTake = 2
            numToTakePC = 1

            numLetters = numLetters - numToTake

        elif(numToTake == 1):  # antistoixa an pathsei 1
            numToTake = 1
            numToTakePC = 2

            numLetters = numLetters - numToTake  # analoga me to ti exei dwsei ws input o xrhsths,tha afairethei apo to numbletters



        if numLetters == 0:  # an den uparxoun alla numletters tote o xrhsths kerdizei
            print("You won!")

        elif ((numLetters - numToTakePC) == 0 or numLetters < 0):  # an o upologisths kerdizei afairwntas 2 tote afairei 2

            print("You lost")

    else:
        print("Parakalw eisagete mono y/n")






















