#This program is going to allow the user 
#   to convert numbers from one base to 
#   another. User specifies the base of
#   the input and output

import math
from operator import concat

charList = {}
file = open("characterList.txt")
key = 0

for line in file:
    charList[key] = line.rstrip()
    key += 1

inputBase = 10
inputNumber = 0
outputBase = 2
outputNumber = ""

print('''This program is allows you to convert numbers from one base to another.
The base must be between 2 and 61.''')

# def inputs():
#     inputBase = input("What is the base of the input? ")    
#     inputNumber = input("What is the number to convert? ")
#     outputBase = input("What is the base of the output? ")
#     return inputBase, inputNumber, outputBase

def convert(inputBase, inputNumber, outputBase, outputNumber):
    quotient = inputNumber
    remainder = 0
    # print("Input Base", inputBase)
    # print("Output Base", outputBase)
    # print("Quotient", quotient)
    if (inputBase > outputBase):
        while quotient != 0:
            remainder = quotient % outputBase
            # print("Remainder ", remainder)
            quotient = quotient // outputBase
            # print("Quotient ", quotient)
            outputNumber = str(remainder) + outputNumber
        print(str(inputNumber) + " in base " + str(outputBase) + " is " + outputNumber)
    # else:
    #     print(outputNumber)


# inputs()
inputBase = int(input("What is the base of the input? "))
inputNumber = int(input("What is the number to convert? "))
outputBase = int(input("What is the base of the output? "))
print("inputNumber ", inputNumber)
if (int(inputBase) > 61 or int(inputBase) < 2):
    print("Please input a base between 2 and 50")
    #continue
else:
    convert(inputBase, inputNumber, outputBase, outputNumber)
