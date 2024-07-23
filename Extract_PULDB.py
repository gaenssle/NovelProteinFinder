#!/usr/bin/python
# Written in Python 3.8 in 2024 by A.L.O. Gaenssle

from bs4 import BeautifulSoup
import os
import pandas as pd
import re
import urllib.request
import matplotlib.pyplot as plt

# Define file names
folder = "files"
input_file = "PULDB_GH154_short.txt"
input_path =  os.path.join(folder, "input_files", input_file)
output_path =  os.path.join(folder, "output_files", input_file.rsplit(".",1)[0] + "_extracted.txt")

# Names of dataframe columns
col_names = ["Species", "PUL ID", "Name", "Modularity", "Overlap IDs", "Overlap Names"]
marker_list =[ "GH154", "unk", "GH"]

## ================================================================================================
## FUNCTIONS
## ================================================================================================

# Extract all table elements
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
# Convert to pandas dataframe and combine overlap columns if they star with "#"
def clean_data(row_cols, col_names):
	data_frame = pd.DataFrame(row_cols)
	data_frame.replace("", float("NaN"), inplace=True)
	data_frame.replace(" ", float("NaN"), inplace=True)  
	data_frame.dropna(how='all', axis=1, inplace=True)

	# Check if there are multiple overlap columns and concat them, add new column names
	overlap_cols = data_frame.columns[len(col_names)-2:]
	if len(overlap_cols) > 2:
		try:
			data_frame[col_names[-2]] = data_frame[overlap_cols[::2]].apply(lambda x: x.str.cat(sep=', '), axis=1)
			data_frame[col_names[-1]] = data_frame[overlap_cols[1::2]].apply(lambda x: x.str.cat(sep=', '), axis=1)
			data_frame = data_frame.drop(columns=overlap_cols)
		except ValueError:
			add_names = len(data_frame.columns) - len(col_names)
			[col_names.append("Info_" + str(index+1)) for index in range(add_names)]

	data_frame.columns = col_names
	return(data_frame)

## ================================================================================================
def analyze_data(data_frame, marker_list):
	data_frame[col_names[3]] = data_frame[col_names[3]].str.strip() 
	data_frame["Length"] = data_frame[col_names[3]].str.count('\s+') + 1

	# Convert to list and extract position of each occurence of each marker
	mod_list = data_frame[col_names[3]].str.split(" ").to_list()
	for marker in marker_list:
		index_list = []
		count_list = []	
		for row in mod_list:
			pos_indices = [str(index) for index, string in enumerate(row) if marker in string]
			index_list.append(", ".join(pos_indices))
			count_list.append(len(pos_indices))
		data_frame[f"Postion_{marker}"] = index_list
		data_frame[f"Count_{marker}"] = count_list
	return(data_frame)

## ================================================================================================	
def plot_length(data_frame, col_names):
	length_all = data_frame[col_names[3]].str.count('\s+') + 1
	ax = length_all.plot(kind='hist', bins=20, edgecolor='black', title="Distribution of PUL length")
	ax.set_ylabel("Occurences")
	ax.set_xlabel("Number of genes in the PUL")
	len_info_str = f"Min = {length_all.min()}\nMax = {length_all.max()}\nAverage = {length_all.mean():.2f}"
	ax.text(0.95, 0.95, len_info_str, horizontalalignment='right',
		verticalalignment='top', transform=ax.transAxes)
	plt.axvline(x=length_all.mean(), color='r', linestyle='-')
	plt.show()

## ================================================================================================
## SCRIPT
## ================================================================================================

# Import file and parse to BeautifulSoup
with open(input_path) as file:
	soup = BeautifulSoup(file, features="html.parser")

row_cols = extract_data(soup)
data_frame = clean_data(row_cols, col_names)
data_frame = plot_length(data_frame, col_names)
# data_frame = analyze_data(data_frame, marker_list)

# data_frame.to_csv(output_path, sep="\t", index=False)
# print(f"\nData exported! Saved as:\n{output_path}")