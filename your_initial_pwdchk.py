####################################
# File name:                       #
# Author:                          #
# Submission:                      #
# Instructor:                      #
####################################

import re
import random
import string
import msvcrt
import os
import time


print("-------------------------------------------------------------------")
print("                    Password Checker Program                      ")
print("-------------------------------------------------------------------")


def passwordTester(n):

    containUpper = False
    containLower = False
    containNumber = False
    containSymbol = False

   # Check if the char is Upper or lower character
    if(n.isupper() == True):
        containUpper = True
    elif(n.islower() == True):
        containLower = True
    else:
        for a in n:
            # checking if the string has lower or upper
            if(a.isupper()) == True:
                containUpper = True
            elif(a.islower()) == True:
                containLower = True

    # Check if the Char is digit
    if(n.isdigit() == True):
        containNumber = True
    else:
        for a in n:
            # checking if the string has any number
            if(a.isdigit()) == True:
                containNumber = True

    # Check if it has any special character
    specialChar = re.compile('[!+=?#%*@&^$_-]')
    if(specialChar.search(n) != None):
        containSymbol = True
    if(containSymbol and containNumber and containLower and containUpper):
        if(len(n) > 10):
            rank = "strong"
        elif(len(n) <= 10 and len(n) >= 8):
            rank = "moderate"
        else:
            rank = "week"
    elif (containNumber and containLower and containUpper or
          containNumber and containSymbol and containUpper or
          containNumber and containSymbol and containLower or
          containSymbol and containLower and containUpper
          ):
        if(len(n) >= 8):
            rank = "moderate"
        else:
            rank = "weak"
    else:
        rank = "week"
    return rank


def generateRandomPwd():
    generatedPassword = ""
    ppp = ""
    x = 0
    symbols = "[!+=?#%*@&^$_-]"  # symbols given
    # Make at least 12 characters, 3 of each 4 prototype to make the password strong mentioned in the project
    while(x < 3):
        ppp += ''.join(random.sample(symbols, 1))
        ppp += random.choice(string.ascii_uppercase)
        ppp += random.choice(string.ascii_lowercase)
        ppp += str(random.randint(0, 9))  # random number from 0-9
        x += 1

    shuffledList = list(ppp)
    random.shuffle(shuffledList)
    return (''.join(shuffledList))


while True:
    print("Please choose from the options below")
    print("1) Input Text File")
    print("2) System Generated Password")
    print("3) Quit the Program")
    try:
        print("\nPlease select option [1 or 2 or 3] :", end=' ')
        selectedOption = str(msvcrt.getch().decode("utf8"))
        print(selectedOption)
        assert selectedOption in ["1", "2", "3"]

        if selectedOption == "1":
            while True:
                try:
                    pathToBeRead = input(
                        "Enter the path of your file : ")
                    assert os.path.exists(
                        pathToBeRead)
                    streamOpenFile = open(pathToBeRead, "rt")
                    line = streamOpenFile.readline()
                    count = 0
                    print(' {:<12}     {:>12}'.format(
                        "PASSWORD", "STRENGTH"))
                    print(" -----------------------------")
                    while line != "":
                        # split by ,
                        pwd = line.split(",")
                        pwd[1] = pwd[1].rstrip("\n")  # take 2nd value
                        print(' {:<12}  =  {:>12}'.format(
                            pwd[1], passwordTester(pwd[1])))
                        line = streamOpenFile.readline()
                        count = count+1
                    streamOpenFile.close()
                    print("\n####################################")
                    break
                except:
                    print(
                        "ERR :- File doesnt exist [ " +
                        str(pathToBeRead) + " ]. "
                    )
                    print(
                        "Hint:- Please Generate a txt file before entering here\n")
        elif selectedOption == "2":
            while True:
                try:
                    userName = input(
                        "\nPlease Type your user name [20] : "
                    )
                    if(len(userName) > 20):
                        print("ERR:- User Name should not be more than 20 characters")
                    else:
                        while True:
                            try:
                                print(
                                    "\nWould like to save this UserName/Password (y or n) :", end=' ')
                                wantToSave = str(msvcrt.getch().decode("utf8"))
                                print(wantToSave)
                                assert wantToSave in ["y", "n", "Y", "N"]
                                break
                            except:
                                print("ERR :- Please Select y or n or Y or N")
                        if(wantToSave.lower() == "y"):
                            # push to a file
                            userNamePwd = [userName, generateRandomPwd(
                            ), passwordTester(generateRandomPwd())]

                            while True:
                                try:
                                    pathToBeSaved = input(
                                        "Enter the path of your file: ")
                                    assert os.path.exists(
                                        pathToBeSaved)
                                    stream = open(pathToBeSaved, "wt")
                                    stream.write(','.join(userNamePwd))
                                    print("Saving.......")
                                    time.sleep(2)  # sleep for 2
                                    stream.close()
                                    break
                                except:
                                    print("ERR :- File doesnt exist [ " +
                                          str(pathToBeSaved) + " ]. ")
                                    print(
                                        "Hint:- Please Generate a txt file before entering here\n")

                            print("\n####################################")
                            break
                        else:
                            while True:
                                try:
                                    print(
                                        "\nWould like to generate new pwd (y or n) :", end=' ')
                                    wantNewPwd = str(
                                        msvcrt.getch().decode("utf8"))
                                    print(wantNewPwd)
                                    assert wantNewPwd in ["y", "n", "Y", "N"]
                                    break
                                except:
                                    print("ERR :- Please Select y or n or Y or N")

                            if(wantNewPwd == "n"):
                                print("\n####################################")
                                break
                except IOError as ERR:
                    print(
                        "ERR :- I/O error occured:", ERR.strerror
                    )
                except:
                    print(
                        "ERR :- Please type your username"
                    )
        elif selectedOption == "3":
            print("Quitting...")
            time.sleep(2)
            print("This program is courtesy of: YourName")
            break

    except:
        print(
            "ERR :- Please select option 1 or 2 or 3 only!!\n"
        )
