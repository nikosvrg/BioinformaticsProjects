numChrom =1

#Liver = numA   //mhkos liver 39314
#Muscle = numB  // mhkos muscle 14327


numA=39314
numB=14327
numToDelete=0


input3=input("Would you like to play first? (y/n)")

print("There are 2 Chromosomes.Everytime you delete one the other is divided into two until there is none.")
# oso den exei mhdenistei kapoio xrwmoswma,ekteleite h while
while(numChrom>0):
    # an o xrhsths grapsei 'y' ksekinaei prwtos
    if(input3=="y"):
        # to programma rwtaei ton xrhsth poio apo ta 2 xrwmoswmata thelei na sbhsei
        numToDelete2 = input(("Which one would you like to delete? (", int(numA), " or ", int(numB), ")."))
        numToDelete = int(numToDelete2)

        # an epileksei to to numa tote to diarei me to tria,kai meta bazei sto numb to numb - numb/3
        if(numToDelete == int(numA)):
            numA = int(numB)/3
            numB = int(numB)-int(numB)/3
            print("Chromosome A turned to be ", int(numA), " and B ", int(numB), ".")


        elif(numToDelete==int(numB)):
            numB = int(numA) - int(numA) / 3
            numA = int(numA) / 3
            print("Chromosome A turned to be ", int(numA), " and B ", int(numB), ".")
        # an exoun mhdenistei kai ta 2 xrwmoswmata,tote kerdizei o paixths
        if(int(numA) == 0 and int(numB) == 0):
            print("You won")
            break



        # an numa>nub tote paizei o upologisths kai diagrafei to numa
        elif (int(numA) >= int(numB)):
            numToDelete = int(numA)
            numA = int(numB) / 3
            numB = int(numB) - int(numB) / 3
            print("Computer deleted chromosome A.")
            print("Chromosome A turned to be ", int(numA), " and B ", int(numB), ".")

        # an numb?numa tote paizei o upologisths kai diagrafei to numb
        elif (int(numA) <= int(numB)):
             numToDelete = int(numB)
             numB = int(numA) - int(numA) / 3
             numA = int(numA) / 3
             print("Computer deleted chromosome B.")
             print("Chromosome A turned to be ", int(numA), " and B ", int(numB), ".")

        # an einai kai ta 2 xrwmoswmata 0 tote o upologisths kerdizei
        if  (int(numA) == 0 and int(numB) == 0):
                print("you lost")
                break

    # an o xrhsths pathsei 'n' tote ksekinaei o upologisths
    if(input3 == "n"):
         print("Computer is playing!(", int(numA), " or ", int(numB), ").")
         if int(numA) <= int(numB):   #an numa<=numb tote o upologisths diagrafei to numb
             numToDelete = int(numB)
             numB = int(numA) - int(numA) / 3
             numA = int(numA) / 3
             print("Computer deleted chromosome B.")
             print("Chromosome A turned to be ", int(numA), " and B ", int(numB), ".")

         elif(int(numA) >= int(numB)):  #an numa>=numb tote o upologisths diagrafei to numa
             numToDelete = int(numA)
             numB = int(numB) - int(numB) / 3
             numA = int(numB) / 3
             print("Computer deleted chromosome A.")
             print("Chromosome A turned to be ", int(numA), " and B ", int(numB), ".")

         # an kai ta 2 xrwmoswmata einai 0 tote kerdizei o upologisths
         if (int(numA) == 0 and int(numB) == 0):
             print("You lost")
             break

         # rwtaei ton xrhsth poio apo ta 2 xrwmoswmata thelei na diagrapsei
         input1=input(("Which one would you like to delete? (", int(numA), " or ", int(numB), ")."))
         numToDelete=int(input1)
         # an epileksei to nua tote to numa diaireitai me to 3,kai sthn thesh tou numb mpainei to nua-numa/3
         if(numToDelete == int(numA)):
             numA = int(numB) / 3
             numB = int(numB) - int(numB) / 3
             print("Chromosome A turned to be ", int(numA), " and B ", int(numB), ".")

         # an epileksei to nub tote to numb diairetai me to 3 ,kai sthn thesh tou numb mpainei to nub-nub/3
         elif(numToDelete == int(numB)):
             numB = int(numA) - int(numA) / 3
             numA = int(numA) / 3
             print("Chromosome A turned to be ", int(numA), " and B ", int(numB), ".")

         if(int(numA) == 0 and int(numB) == 0):  # an kai ta 2 xrwmoswmata exoun mhdenistei tote kerdizei o xrhsths
             print("you won")
             break







