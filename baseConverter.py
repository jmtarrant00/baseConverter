#This program is going to allow the user 
#   to convert numbers from one base to 
#   another. User specifies the base of
#   the input and output

from asyncio.windows_events import NULL
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
outputNumber = None

print('''This This program is allows you to convert numbers from one base to another.
        the base must be between 2 and 61.''')

def inputs():
    inputBase = input("What is the base of the input? ")    
    inputNumber = input("What is the number to convert? ")
    outputBase = input("What is the base of the output? ")

def convert(inputBase, inputNumber, outputBase):
    quotient = inputNumber
    remainder = 0
    if inputBase < outputBase:
        while quotient != 0:
            quotient = inputNumber // outputBase
            remainder = inputNumber % outputBase
            outputNumber = remainder + outputNumber


while True:
    inputs()
    if (inputBase > 61 or inputBase < 2):
        print("Please input a base between 2 and 50")
        continue
    else:
        convert(inputBase, inputNumber, outputBase)