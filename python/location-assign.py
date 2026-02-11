# ======
# THIS PROGRAM COMPARES LOCATIONS IN A JSON FILE
# AGAINST LOCATIONS IN THE PSGC
# FOR LOCATION ASSIGNMENT.
# AUTHOR: Nikko Gammad https://github.com/thirteenfour
# ======

# TKinter components
from tkinter import *
from tkinter import filedialog
# dealing with csv
import pandas as pd
# JSON functions
import json
# for date and time
from datetime import datetime

# ======
# TKinter
# ======
# create blank window
window = Tk()
# Set window title
window.title('Location Assigner')
# Set window size
window.geometry("300x300")

#####
# Components
#####
# input label for locations with unknown assignment
inputlabel = Label(window,
                   text = "Input Locations JSON File:",
                   width = 20,
                   height = 3)
# input user locations json file
button_explore = Button(window, 
                        text = "Browse Files",
                        command = browseLocations,
                        width = 15)
# input label for input json
label_json = Label(window,
                   text = "Input PSGC JSON File:",
                   width = 20,
                   height = 3)
# input json file
button_explore_json = Button(window,
                             text = "Browse Files",
                             command = browseJSON,
                             width = 15)
# input month
dropdown_month = OptionMenu(window, 
                            selectedMonth, 
                            *MONTHS)
# input year
text_year = Text(window, 
                 height = 1,
                 width = 10)
# status label/debug label
label_status = Label(window,
                     text = STATUSSTRINGS[0],
                     width = 20,
                     height = 1)
# process button
button_process = Button(window,
                        text="Process",
                        command = processFile,
                        width = 10)
# exit button
button_exit = Button(window, 
                     text = "Exit",
                     command = exit,
                     width = 10) 

# component layout
label_json.grid(column = 1, row = 1)
button_explore_json.grid(column = 2, row = 1)
dropdown_month.grid(column = 1, row = 2)
text_year.grid(column = 2, row = 2)
inputlabel.grid(column = 1, row = 3)
button_explore.grid(column = 2, row = 3)
label_status.grid(column = 1, row = 4)
button_process.grid(column = 2, row = 4)
button_exit.grid(column = 1, row = 5)

# enter event loop
window.mainloop()