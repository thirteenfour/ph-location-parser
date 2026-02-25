# ======
# THIS PROGRAM COMPARES LOCATIONS IN A JSON FILE
# AGAINST LOCATIONS IN THE PSGC
# FOR LOCATION ASSIGNMENT.
# AUTHOR: Nikko Gammad https://github.com/thirteenfour
# ======

# ======
# Imports
# ======
# find the path
import os
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
# Globals
# ======
currentLocation = ""
uniqueLocationOutput = ""
# input files
filename_inputPSGC = ""
filename_inputLocations = ""
dataInputLocations = ""
dataPSGC = ""
# current working directory
current_directory = os.path.abspath(os.getcwd())
# location segments to assign
selectedRegion = "---"
selectedProvinceHUC = "---"
selectedCityMun = "---"
selectedBarangay = "---"

# ======
# Processing Functions
# ======
def browseLocations():
  global filename_inputLocations
  filename_inputLocations = filedialog.askopenfilename(initialdir = current_directory,
                                        title = "Select a File",
                                        filetypes = (("JSON Files", "*.json"),
                                                     ("All Files", "*.*")))
def browsePSGC():
  global filename_inputPSGC
  filename_inputPSGC = filedialog.askopenfilename(initialdir = current_directory,
                                        title = "Select a File",
                                        filetypes = (("JSON Files", "*.json"),
                                                     ("All Files", "*.*")))
def processFiles():
  global filename_inputLocations, filename_inputPSGC, dataInputLocations, dataPSGC, selectedRegion, selectedProvinceHUC, selectedCityMun
  # show the path
  # print(current_directory)
  # try showing the filenames
  # print(filename_inputLocations, filename_inputPSGC)
  # try opening the files
  try:
    dataInputLocations = json.load(open(filename_inputLocations, encoding="utf8"))
    print("Input Raw Locations Loaded.")
  except:
    print("Error in opening input raw locations file")
    raise
  try:
    dataPSGC = json.load(open(filename_inputPSGC, encoding="utf8"))
    print("PSGC Locations Loaded.")
  except:
    print("Error in opening PSGC locations file")

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
# input label for psgc json
label_json = Label(window,
                   text = "Input PSGC JSON File:",
                   width = 20,
                   height = 3)
# input psgc json file
button_explore_json = Button(window,
                             text = "Browse Files",
                             command = browsePSGC,
                             width = 15)
# label for current location
label_current_location = Label(window,
                   text = "Current Location:",
                   width = 20,
                   height = 3)
# input for location segments
dropdown_region = OptionMenu(window, selectedRegion, "---")
# input month
# dropdown_month = OptionMenu(window, 
#                             selectedMonth, 
#                             *MONTHS)
# input year
# text_year = Text(window, 
#                  height = 1,
#                  width = 10)
# status label/debug label
# label_status = Label(window,
#                      text = STATUSSTRINGS[0],
#                      width = 20,
#                      height = 1)
# process button
button_process = Button(window,
                        text="Process",
                        command = processFiles,
                        width = 10)
# exit button
button_exit = Button(window, 
                     text = "Exit",
                     command = exit,
                     width = 10) 

# component layout
label_json.grid(column = 1, row = 1)
button_explore_json.grid(column = 2, row = 1)
# dropdown_month.grid(column = 1, row = 2)
# text_year.grid(column = 2, row = 2)
inputlabel.grid(column = 1, row = 2)
button_explore.grid(column = 2, row = 2)
label_current_location.grid(column = 1, columnspan = 3, row = 3)
dropdown_region.grid(column = 1, row = 4)
# label_status.grid(column = 1, row = 4)
button_process.grid(column = 1, row = 5)
button_exit.grid(column = 2, row = 5)

# enter event loop
window.mainloop()