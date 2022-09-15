#This program is going to allow the user 
#   to convert numbers from one base to 
#   another. User specifies the base of
#   the input and output

#import tkinter
import tkinter as tk
from tkinter import CENTER, ttk

#set default values for variables
inputBase = '10'
inputNumber = 0
outputBase = '2'
outputNumber = '0'
outputText = ""

# create character dictionary
charList = {}
file = open("characterList.txt")
key = 0
# every line in the txt file is assigned a key in ascending order starting at 0 
for line in file:
    charList[key] = line.rstrip()
    key += 1

# create root window 
root = tk.Tk()

# set window title and geometry
root.title("Base Converter")
root.geometry("250x180")
root.resizable(0,0)
root.configure(bg='#0047AB')

#configure the grid
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=3)

# get the key using the value entered
def get_key(val):
    for key, value in charList.items():
        if val == value:
            return key

# Get the values from the entry boxes on the UI, or set them to a default value
#   if there isn't anything in the box
#   Also checks the input and output bases to see if the user has entered 
#   a valid value
def inputs():
    global inputBase, inputNumber, outputBase, outputNumber
    inputBase = int(inputBaseEntry.get() or 10)
    inputNumber = str(inputNumberEntry.get() or 0)
    outputBase = int(outputBaseEntry.get() or 2)

    # Check if user input bases are within valid range
    if (int(inputBase) < 2 or int(inputBase) > 61):
        outputText = "Please input an input base between 2 and 61"
    elif (int(outputBase) < 2 or int(outputBase) > 61):
        outputText = "Please input an output base between 2 and 61"
    else: # if user input bases within range, convert inputNumber
        outputNumber = convert(inputBase, inputNumber, outputBase)
        outputText = str(inputNumber) + " in base " + str(outputBase) + " is " + outputNumber

    # set the output number lable to the output text string
    outputNumberLabel.configure(text=outputText)

# Convert from base 10 to any other base
def convertFrom10(quotient, outputBase):
    remainder = 0
    outputNumber = ""
    while quotient != 0:
        remainder = quotient % outputBase
        quotient = quotient // outputBase
        outputNumber = charList.get(remainder) + outputNumber
    return outputNumber

# Convert the number from input to outbut base
#   Take input base and number and output base and number as variables
#   convert input number to decimal then convert that to the output base
def convert(inputBase, inputNumber, outputBase):
    global outputNumber
    inputLength = len(inputNumber)
    inputDec = 0
    inputRev = inputNumber[::-1]
    # If the inputNumber isn't already in base 10, convert it to 
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

    # print(str(inputNumber) + " base " + str(outputBase) + " is " + outputNumber)
    return outputNumber    

# info text
info = ttk.Label(root, text="Convert Bases! Range: 2 to 61")
info.grid(column=0, row=0, sticky=tk.W, columnspan=2)

# inputBase Field
inputBaseLabel = ttk.Label(root, text="Input Base:")
inputBaseEntry = ttk.Entry(root)
inputBaseLabel.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)
inputBaseEntry.grid(column=1, row=1, sticky=tk.W, padx=5, pady=5)

# inputNumber Field
inputNumberLabel = ttk.Label(root, text="Input Number:")
inputNumberEntry = ttk.Entry(root)
inputNumberLabel.grid(column=0, row=2, sticky=tk.W, padx=5, pady=5)
inputNumberEntry.grid(column=1, row=2, sticky=tk.W, padx=5, pady=5)

# outputBase Field
outputBaseLabel = ttk.Label(root, text="Output Base")
outputBaseEntry = ttk.Entry(root)
outputBaseLabel.grid(column=0, row=3, sticky=tk.W, padx=5, pady=5)
outputBaseEntry.grid(column=1, row=3, sticky=tk.W, padx=5, pady=5)

# Convert button
convertBtn = ttk.Button(root, text="Convert", command=inputs)
convertBtn.grid(column=0, row=4, columnspan=2)

# outputNumber Field
outputNumberLabel = ttk.Label(root, text="0 in base 2 is 0", justify=CENTER, wraplength=200)
outputNumberLabel.grid(column=0, row=5, columnspan=2)

# Styling the window

style = ttk.Style(root)
style.configure('TLabel', font=('SegoeUI', 11), background="#0047AB", foreground="#F0f0f0")
style.configure('TButton', font=('SegoeUI', 11), background="#0047AB")


# call mainloop of ttkinter
root.mainloop()