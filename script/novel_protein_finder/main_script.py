#!/usr/bin/python
# Written by ALGaenssle in 2024

## ====================================================================
## SCRIPT - MAIN
## Main script for importing SEC data
## ====================================================================

from bs4 import BeautifulSoup
import os
import pandas as pd

# Import own modules
from . import functions


## ====================================================================
## Main export data funtion
def extract_html_data(files, default_values):
	if files.input_path == "":
		return {"m_type":"warning", "title":"Missing data", "message":"No input folder selected!"}

	# Extract data from html file
	try:
		with open(files.input_path) as file:
			soup = BeautifulSoup(file, features="html.parser")
		row_cols = functions.extract_data(soup)
	except:
		return {"m_type":"warning", 
				"title":"Incorrect data", 
				"message":"Could not parse html data!\nPlease check if you copied the source code \n(--> lots of <td></td>)"}

	# Extract data and convert to pandas dataframe
	try:
		data_frame = functions.clean_data(row_cols, default_values.col_names)
	except:
		return {"m_type":"warning", 
				"title":"Incorrect data", 
				"message":"Could not convert to table!\nPlease check if the column names are correct\n(--> see 'Configure')"}
			
	# Export data
	message = "Created files:\n\n"
	data_frame.to_csv(files.output_path, sep="\t", index=False)
	message += "- File with all PULs\n"

	return {"m_type": "info", "title": "Done exporting", "message": message}
