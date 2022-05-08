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

#set default values for variables
inputBase = '10'
inputNumber = 0
outputBase = '2'
outputNumber = ""

print('''This program is allows you to convert numbers from one base to another.
>>The base must be between 2 and 61.''')

# get the key using the value entered
def get_key(val):
    for key, value in charList.items():
        if val == value:
            return key

# get the values from the user
def inputs():
    global inputBase, inputNumber, outputBase
    inputBase = int(input("What is the base of the input? ") or 10)
    inputNumber = str(input("What is the number to convert? ") or 0)
    outputBase = int(input("What is the base of the output? ") or 2)

# Convert from base 10 to any other base
def convertFrom10(quotient, outputBase):
    remainder = 0
    outputNumber = ""
    while quotient != 0:
        # print("While Loop")
        remainder = quotient % outputBase
        quotient = quotient // outputBase
        outputNumber = charList.get(remainder) + outputNumber
    return outputNumber
    

# Convert the number from input to outbut base
#   Take input base and number and output base and number as variables
#   convert input number to decimal then convert that to the output base
def convert(inputBase, inputNumber, outputBase, outputNumber = '0'):
    inputLength = len(inputNumber)
    inputDec = 0
    inputRev = inputNumber[::-1]
    if inputBase != 10:
        for x in range(inputLength-1, -1, -1):
            # print("x", x)
            inputDec = inputDec + (get_key(inputRev[x]) * (pow(inputBase, x)))
        print("InputDec:", inputDec)
        if outputBase == 10:
            outputNumber = str(inputDec)
        else:
            outputNumber = convertFrom10(inputDec, outputBase)
    else:
        outputNumber = convertFrom10(int(inputNumber), outputBase)
        
    print(str(inputNumber) + " in base " + str(outputBase) + " is " + outputNumber)


inputs()
print("inputNumber", inputNumber)
if (int(inputBase) > 61 or int(inputBase) < 2):
    print("Please input a base between 2 and 61")
    #continue
else:
    convert(inputBase, inputNumber, outputBase, outputNumber)
