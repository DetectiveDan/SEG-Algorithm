# Created by Daniel C Smith
# DanielSmith.co
# Dependencies: No External Modules
# Python 3.6 with random library
# MIT License 2018
# Project Description: This is a simple checksum based on a algorithm I came up with based on Luhn's algorithm.
# CONT: This might be a duplicate of a current algorithm, but it was created as a learning project.
# For more info on this checksum algorithm please visit the readme file for instructions.

import random
import csv
import time

def generateAccount():
    account = str(random.randint(330648877494, 871023338043))
    #print(len(account))
    total = sum([int(x) for x in account])
    #print(total)

    firstSeg = account[0:4]
    secondSeg = account[4:8]
    thirdSeg = account[8:12]

    firstTotal = sum([int(x) for x in str(firstSeg)])
    secondTotal = sum([int(x) for x in str(secondSeg)])
    thirdTotal = sum([int(x) for x in str(thirdSeg)])
    grandTotal = sum([int(x) for x in str(account)])
    #print("grand {}".format(grandTotal))

    if len(str(firstTotal)) == 2:
        firstTotal = str(firstTotal)
        firstTotal = (firstTotal[1])
    if len(str(secondTotal)) == 2:
        secondTotal = str(secondTotal)
        secondTotal = (secondTotal[1])
    if len(str(thirdTotal)) == 2:
        thirdTotal = str(thirdTotal)
        thirdTotal = (thirdTotal[1])
    grandTotal = grandTotal / len(account)



    #print(firstSeg)
    #print(secondSeg)
    #print(thirdSeg)

    grandTotal = int(grandTotal)

    forthSeg = (str(firstTotal)) + (str(secondTotal) + (str(thirdTotal) + (str(grandTotal))))

    #print(forthSeg)


    account = "{}{}{}{}".format(firstSeg,secondSeg,thirdSeg,forthSeg)

    totalsum = sum([int(x) for x in str(account)])

    if len(str(totalsum)) > 2:
        totalsum = str(totalsum)
        totalsum = (totalsum[0:2])
    #print(totalsum)
    account = "{}{}{}{}{}".format(firstSeg, secondSeg, thirdSeg, forthSeg, totalsum)
    return(account)

def checkAccount(account):
    account = str(account)
    if len(account) != 18:
        print("INVALID ACCOUNT: LENGTH")
        return False
    else:
        print("Confirmed Length")
    if account.isdigit():
        print("Confirmed Digit")
    else:
        print("INVALID ACCOUNT: DIGIT LEN")
        return False
    firstSeg = account[0:4]
    secondSeg = account[4:8]
    thirdSeg = account[8:12]
    forthSeg = account[12:16]

    smallAccount = account[0:12]

    firstTotal = sum([int(x) for x in str(firstSeg)])
    secondTotal = sum([int(x) for x in str(secondSeg)])
    thirdTotal = sum([int(x) for x in str(thirdSeg)])
    grandTotal = sum([int(x) for x in str(smallAccount)])
    if len(str(firstTotal)) == 2:
        firstTotal = str(firstTotal)
        firstTotal = (firstTotal[1])
    if len(str(secondTotal)) == 2:
        secondTotal = str(secondTotal)
        secondTotal = (secondTotal[1])
    if len(str(thirdTotal)) == 2:
        thirdTotal = str(thirdTotal)
        thirdTotal = (thirdTotal[1])

    grandTotal = grandTotal / 12

    grandTotal = int(grandTotal)

    forthSeg = (str(firstTotal)) + (str(secondTotal) + (str(thirdTotal) + (str(grandTotal))))

    checkedNumber = "{}{}{}{}".format(firstSeg,secondSeg,thirdSeg,forthSeg)
    totalsum = sum([int(x) for x in str(checkedNumber)])

    if len(str(totalsum)) > 2:
        totalsum = str(totalsum)
        totalsum = (totalsum[0:2])
    checkedNumber = "{}{}{}{}{}".format(firstSeg, secondSeg, thirdSeg, forthSeg, totalsum)
    #print("{} VS {}".format(checkedNumber,account))
    #print(checkedNumber)
    if checkedNumber != account:
        print("INVALID ACCOUNT: CHECKSUM")
        return False
    else:
        print("Confirmed Checksum")
    print("VALID ACCOUNT")
    return True

while True:
    print("This program will generate a secure 18 digit number. If any digit is changed of the number, "
          "it will not be valid.")
    print("Options: Generate Number (g), Validate Number (v), Generate List (gl), Check List (cl), or Quit (q)")
    next = input("Enter a command: ")
    next = next.lower()
    if next == "g" or "v" or "q":
        if next == "g":
            number = generateAccount()
            print(number)
        if next == "v":
            checkAccount(input("Enter number: "))
        if next == "gl":
            run = 1
            listLength = int(input("How many numbers to generate?"))
            origLength = listLength
            startTime = time.time()
            with open('generatedList.csv', mode='w') as csv_file:
                fieldnames = ['number']
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames, delimiter=',', lineterminator='\n')
                writer.writeheader()
                while listLength >= 1:
                    number = generateAccount()
                    writer.writerow({'number': number})
                    #print(number)
                    listLength -= 1
                    run += 1
                endTime = time.time()
                print("Time taken (seconds): {}".format((endTime - startTime)))
        if next == "cl":
            run = 1
            startTime = time.time()
            with open('generatedList.csv') as csv_file:
                fieldnames = ['number']
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames, delimiter=',', lineterminator='\n')
                writer.writeheader()
                while listLength >= 1:
                    number = generateAccount()
                    writer.writerow({'run': run, 'number': number})
                    print(number)
                    listLength -= 1
                    run += 1
                endTime = time.time()
                print("Time taken (seconds): {}".format((endTime - startTime)))
        if next == "q":
            quit()
    else:
        print("Invalid command")
        continue
