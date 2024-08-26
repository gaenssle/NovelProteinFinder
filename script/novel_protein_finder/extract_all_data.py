#!/usr/bin/python
# Written by ALGaenssle in 2024
# MODULE - EXTRACT HTML
# Extract data from html file


from bs4 import BeautifulSoup
import os
import pandas as pd
import re



## ===========================================================================
## SUB-FUNCTIONS
## ===========================================================================
## Extract all table elements
def extract_data(soup):
	row_cols = []
	row_list = []
	tags = re.compile(r"<[^>!]+>")
	arrows = re.compile(r"\s?[▶◀]\s?[▶◀]?\s?")		
	soup_table = soup.find_all('table')
	for table in soup_table[2:]:	# Remove first two tables (=header elements)
		add_table = table.find_all('tr')
		row_list.extend(add_table[1:])			# Ignore header row

	# Convert & remove all tags to obtain columns
	for row in row_list[:]:
		row = str(row).replace("<td", "!< ")	# Convert td tags for subsequent string splitting
		row = row.replace("<a href=", "!")		# Convert href to save in separate column
		row = row.replace('index.php?pul=','#')
		row = tags.sub("", row)
		row = arrows.sub(" ", row)
		row = row.replace("\xa0", " ").replace("\n", "").replace("\"", "")
		row = row.replace(">", "!")
		cols = row.split("!")
		row_cols.append(cols)
	return(row_cols)


## ================================================================================================
## Convert to pandas dataframe and combine overlap columns if they start with "#"
def clean_data(row_cols, default_values):
	col_names = default_values.col_names
	data_frame = pd.DataFrame(row_cols)
	data_frame.replace("", float("NaN"), inplace=True)
	data_frame.replace(" ", float("NaN"), inplace=True)  
	data_frame.dropna(how='all', axis=1, inplace=True)

	# Check if there are multiple overlap columns and concat them, add new column names
	if len(data_frame.columns) < len(col_names):
		default_values.col_names = col_names[:len(data_frame.columns)]
	else:
		overlap_cols = data_frame.columns[len(col_names)-2:]
		if len(overlap_cols) > 2:
			try:
				data_frame[col_names[-2]] = data_frame[overlap_cols[::2]].apply(lambda x: x.str.cat(sep=', '), axis=1)
				data_frame[col_names[-1]] = data_frame[overlap_cols[1::2]].apply(lambda x: x.str.cat(sep=', '), axis=1)
				data_frame = data_frame.drop(columns=overlap_cols)
			except ValueError:
				add_names = len(data_frame.columns) - len(col_names)
				[col_names.append("Info_" + str(index+1)) for index in range(add_names)]

	data_frame.columns = default_values.col_names
	data_frame[col_names[3]] = data_frame[col_names[3]].str.strip() 
	data_frame["Link"] = "www.cazy.org/PULDB/index.php?pul=" +  data_frame[col_names[1]].str[1:]
	return(data_frame)


## ===========================================================================
## MAIN FUNCTION
## ===========================================================================
## Main funtion to export html data
def extract_html_data(files, default_values):
	if files.input_path == "":
		return {"m_type":"warning", "title":"Missing data", "message":"No input folder selected!"}

	# Extract data from html file
	try:
		with open(files.input_path) as file:
			soup = BeautifulSoup(file, features="html.parser")
		row_cols = extract_data(soup)
	except:
		return {"m_type":"warning", 
				"title":"Incorrect data", 
				"message":"Could not parse html data!\nPlease check if you copied the source code \n(--> lots of <td></td>)"}

	# Extract data and convert to pandas dataframe
	try:
		data_frame = clean_data(row_cols, default_values)
	except:
		return {"m_type":"warning", 
				"title":"Incorrect data", 
				"message":"Could not convert to table!\nPlease check if you have entered the correct link\n(e.g. http://www.cazy.org/PULDB/index.php?cazy_mod=GH43_31%2BGH115&sp_name2=&sp_ncbi2=)"}
			
	# Export data
	data_frame.to_csv(files.path_data_all, sep=default_values.sep, index=False)

	return {"m_type": "info", "title": "Done exporting", "message": "The raw data (all PUL) have been exported to a table."}
