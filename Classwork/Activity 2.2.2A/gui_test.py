from tkinter import *
from tkinter.ttk import *

# creates a Tk() object
main = Tk()

# sets the geometry of main 
main.geometry("500x500")

# 

# function to open a new window 
def openNewWindow():

    # Toplevel object which will 
    # be treated as a new window
    newWindow = Toplevel(main)

    # sets the title of the
    # Toplevel widget
    newWindow.title("New Window")

    # sets the geometry of toplevel
    newWindow.geometry("200x200")

    # A Label widget to show in toplevel
    Label(newWindow, text ="This is a new window").pack()

def printInput(): 
    inp = inputtxt.get(1.0, "end-1c") 
    lbl.config(text = "Provided Input: "+inp) 

# TextBox Creation 
encryption_input = Text(main, height = 5, width = 20) 

encryption_input.pack()

# Button Creation 
printButton = Button(main, text = "Print", command = printInput) 
printButton.pack() 

# Label Creation 
lbl = Label(main, text = "") 
lbl.pack() 

label = Label(main, text = "This is the main window")

label.pack(pady = 10)

# a button widget which will open a 
# new window on button click
btn = Button(main, text = "Click to open a new window", command = openNewWindow)
btn.pack(pady = 10)

# mainloop, runs infinitely
mainloop()