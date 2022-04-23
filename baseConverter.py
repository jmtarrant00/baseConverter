#This program is going to allow the user 
#   to convert numbers from one base to 
#   another. User specifies the base of
#   the input and output

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
>>The base must be between 2 and 61.''')

def get_key(val):
    for key, value in charList.items():
        if val == value:
            return key

def inputs():
    global inputBase, inputNumber, outputBase
    inputBase = int(input("What is the base of the input? "))
    inputNumber = int(input("What is the number to convert? "))
    outputBase = int(input("What is the base of the output? "))


def convert(inputBase, inputNumber, outputBase, outputNumber):
    #Take input base and number and output base and number as variables
    #  convert input number to decimal then convert that to the output base
    remainder = 0
    quotient = inputNumber
    # inputLength = len(inputNumber)
    # if inputBase != 10:
    #     for x in inputLength:
    #         inputDec = (charList.index())
    # else:
    #     quotient = inputNumber

    while quotient != 0:
        print("While Loop")
        remainder = quotient % outputBase
        quotient = quotient // outputBase
        outputNumber = charList.get(remainder) + outputNumber
    # elif (inputBase < outputBase):
        
    print(str(inputNumber) + " in base " + str(outputBase) + " is " + outputNumber)


inputs()
print("inputNumber", inputNumber)
if (int(inputBase) > 61 or int(inputBase) < 2):
    print("Please input a base between 2 and 50")
    #continue
else:
    convert(inputBase, inputNumber, outputBase, outputNumber)
