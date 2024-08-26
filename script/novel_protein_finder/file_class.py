#!/usr/bin/python
# Written by ALGaenssle in 2024
# CLASS
# Save all required file paths

import os
import tkinter as tk
import tkinter.filedialog


## ====================================================================
## Create class for storing file locations
class FileSelection():
	def __init__(self):
		self.save_path = ""
		self.input_path = ""
		self.path_data_all = ""
		self.path_data_filtered = ""
		self.remove_save_ending = "_raw"
		self.added_ending_all = "_extracted.csv"
		self.added_ending_filtered = "_filtered.csv"

	## FILES --------------------------------------------------------
	# Get save file path (how to save the downloaded html file)
	def get_save_path(self):
		self.save_path = tk.filedialog.asksaveasfilename(
										initialfile = "PULs_raw",
										defaultextension=".txt",
										title = "Select file name for raw data",
										filetypes = (("txt","*.txt"),("html","*.html"),("all files","*.*")))

	# auto-fill subsequent files after downloading the html data
	def forward_input_file(self):
		self.input_path = self.save_path
		if self.save_path.rsplit(".",1)[0].endswith(self.remove_save_ending):
			path = self.save_path.rsplit(self.remove_save_ending,1)[0]
		else:
			path = save_path.rsplit(".",1)[0]
		self.path_data_all = path + self.added_ending_all
		self.path_data_filtered = path + self.added_ending_filtered

	# Get input file path (file name of the html to import)
	def get_input_file(self, ask=True):
		if ask:
			self.input_path = tk.filedialog.askopenfilename(
											initialfile = "PULs_raw",
											title = "Select file to import",
											filetypes = (("txt","*.txt"),("html","*.html"),("all files","*.*")))

			self.path_data_all = self.input_path.rsplit(".", 1)[0] + self.added_ending_all
			self.path_data_filtered = self.input_path.rsplit(".", 1)[0] + self.added_ending_filtered
		else:
			self.input_path = ""
			self.path_data_all = ""
			self.path_data_filtered = ""

	# Set new path for exporting all data
	def get_path_data_all(self):
		self.path_data_all = tk.filedialog.asksaveasfilename(
											initialfile = "PULs_extracted",
											title = "Select file name for extracted data",
											filetypes = (("csv","*.csv"),("txt","*.txt"),("all files","*.*")))


	# Set new path for exporting all data
	def get_path_data_filtered(self):
		self.path_data_filtered = tk.filedialog.asksaveasfilename(
											initialfile = "PULs_filtered",
											title = "Select file name for filtered data",
											filetypes = (("csv","*.csv"),("txt","*.txt"),("all files","*.*")))
