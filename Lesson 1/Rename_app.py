                # This program will ask user for directory and target name. All
                # files in the directory will be renamed to the target name, followed by number.
                #This will also change files to type .txt

from tkinter import *
from tkinter import filedialog
#import tkinter as tk
import os

root = Tk()
root.title("Renaming files in a folder")
root.geometry("800x400")

# Creating the menubar
menubar = Menu(root)
root.config(menu=menubar)

# Create the submenu
submenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label="File", menu=submenu)
submenu.add_command(label="Open")
submenu.add_command(label="Exit", command=root.quit)


def start():
    # assigning name from user input to a variable
    tname = name.get()
    setting_directory(tname)


# Clicking function
def onclick(args):
    if args == 1:
        print("Button 1 is clicked")
    if args == 2:
        print("Button 2 is clicked")
#

# Function is to ask for directory

def setting_directory(targetname):

    path = filedialog.askdirectory()
    if path == "":
        sys.exit()
    i = 1

    for filename in os.listdir(path):
        # testing target name
        #target_name = targetname + str(i)
        if filename.lower().endswith(".txt"):
            target_name = targetname + str(i) + '.txt'
        elif filename.lower().endswith(".jpg"):
            target_name = targetname + str(i) + '.jpg'
        elif filename.lower().endswith(".pdf"):
            target_name = targetname + str(i) + '.pdf'
        else:
           target_name = filename

        old_name = os.path.join(path, filename)
        new_name = os.path.join(path, target_name)

        os.rename(old_name, new_name)
        i += 1


namelabel = Label(root, text="What would you like the name of your files to be: ")
namelabel.pack()

name = Entry(root)
name.pack()

caution = Label(root, text= "CAUTION: ONCE DIRECTORY IS SELECTED, ALL FILE NAMES WILL CHANGE",font=("Courier,14"))
caution.pack()

# This button initiates the program, first by asking directory of files to change
name_button = Button(root, text = "Choose directory", command = start)
name_button.pack()



root.mainloop()


