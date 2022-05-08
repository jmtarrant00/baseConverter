#import Module
from tkinter import *

#Create root window
root = Tk()

#Set root title and dimension
root.title("Welcome to Base Conversion")
# Set geometry('WidthxHeight')
root.geometry('350x200')

# adding a label to root window
lbl = Label(root, text="Are you converting bases?")
lbl.grid()

# Adding a text entry field
txt = Entry(root, width=10)
txt.grid(column=1, row=0)

# Function to display text when button is clicked
def clicked():
    res = "You wrote " + txt.get()
    lbl.configure(text=res)

# Button widget with red text inside
btn = Button(root, text="Click me!", 
             fg = "red", command=clicked)
btn.grid(column=2, row=0)


# Execute Tkinter
root.mainloop()