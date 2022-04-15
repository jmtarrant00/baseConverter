#This program is going to allow the user 
#   to convert numbers from one base to 
#   another. User specifies the base of
#   the input and output

import math

inputBase = 10
inputNumber = 0
outputBase = 2

print('''This This program is allows you to convert numbers from one base to another.
        the base must be between 2 and 50.''')

def inputs():
    inputBase = input("What is the base of the input? ")    
    inputNumber = input("What is the number to convert? ")
    outputBase = input("What is the base of the output? ")

if (inputBase > 50 or inputBase < 2):
    print("Please input a base between 2 and 50")