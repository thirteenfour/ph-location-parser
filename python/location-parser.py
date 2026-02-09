# Uses the PSA PSGC as the source of data 
# URL: https://psa.gov.ph/classification/psgc 

# ======
# THIS PROGRAM TAKES THE PSGC DATA
# AND PARSES IT INTO JSON FILE/S USABLE 
# FOR LOCATION TRACKING.
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
# Globals
# ======
filename_input_json = ""
current_year = "2025"
current_quarter = "Q4"
COLUMNNAMES = ["psgc_10dig",
               "name",
               "corr_code",
               "geo_level",
               "old_names",
               "city_class",
               "income_class",
               "urban_rural",
               "pop_2024",
               "unused",
               "status"]

#####
# Pre-processing
#####
# input the csv into dataframe
df = pd.read_csv("data/PSGC-4Q-2025-Publication-Datafile_raw.csv")
df.columns = COLUMNNAMES
df.drop(columns=["unused"], inplace=True)
# print(df.head(10))

#####
# Processing
#####
json_data = {}
# source
json_data["SOURCE"] = 'https://psa.gov.ph/classification/psgc'
# psgc version
json_data["PSGC_VERSION"] = current_year + '-' + current_quarter
# get date as string for the filename
time_now = datetime.now().strftime("%Y%m%d_%H%M%S")
json_data["DATE PARSED"] = time_now
# local variables
current_psgc_code = ""
current_geo_level = ""
current_rgn_name = ""
current_rgn_code = ""
current_provhuc_name = ""
current_provhuc_code = ""
current_citymun_name = ""
current_citymun_code = ""
current_bgy_name = ""
current_bgy_code = ""
total_entries = 0
# CODE (10-digit): [xx] region code [xxx] province/huc code [xx] city/mun code [xxx] barangay 
for i in range(len(df.index)):
  current_row = df.iloc[i]
  if (current_row["psgc_10dig"] < 1000000000):
    current_psgc_code = "0" + str(current_row["psgc_10dig"])
  else:
    current_psgc_code = str(current_row["psgc_10dig"])
  if (pd.isnull(current_row["geo_level"])):
    current_geo_level = "Other"
  else:
    current_geo_level = current_row["geo_level"]
  try:
    # add new region
    # if (current_row["geo_level"] == "Reg"):
    if (current_psgc_code[2:] == "00000000"):
      current_rgn_name = current_row["name"]
      current_rgn_code = current_psgc_code[0:2]
      json_data[current_rgn_name] = {"code": current_rgn_code, "geo_level": current_geo_level}
    # add new province/huc
    elif (current_psgc_code[5:] == "00000"):
      current_provhuc_name = current_row["name"]
      current_provhuc_code = current_psgc_code[2:5]
      json_data[current_rgn_name][current_provhuc_name] = {"code": current_provhuc_code, "geo_level": current_geo_level}
    # add new city/mun
    elif (current_psgc_code[7:] == "000"):
      current_citymun_name = current_row["name"]
      current_citymun_code = current_psgc_code[5:7]
      json_data[current_rgn_name][current_provhuc_name][current_citymun_name] = {"code": current_citymun_code, "geo_level": current_geo_level}
    else:
      current_bgy_name = current_row["name"]
      current_bgy_code = current_psgc_code[7:]
      # Check if part of HUC
      if (current_psgc_code[5:7] == "00"):
        json_data[current_rgn_name][current_provhuc_name][current_bgy_name] = {"code": current_bgy_code, "geo_level": current_geo_level}
      else:
        json_data[current_rgn_name][current_provhuc_name][current_citymun_name][current_bgy_name] = {"code": current_bgy_code, "geo_level": current_geo_level}
    total_entries = total_entries + 1
  except:
    print("problem at code: " + current_psgc_code)

# ======
# Output
# ======
print("total entries: " + str(total_entries))
# dump to json
filename_out_json = "out/philippines-location-data_" + current_year + current_quarter + "_" + time_now + ".json"
json.dump(json_data, open(filename_out_json, "w", encoding="utf8"), indent=2, ensure_ascii=False)