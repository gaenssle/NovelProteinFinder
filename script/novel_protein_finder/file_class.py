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
		self.input_path = ""
		self.path_data_all = ""
		self.path_data_filtered = ""
		self.added_ending_all = "_extracted.csv"
		self.added_ending_filtered = "_filtered.csv"

	## FILES --------------------------------------------------------
	# Get input file path
	def get_input_file(self, ask=True):
		if ask:
			self.input_path = tk.filedialog.askopenfilename()
			self.path_data_all = self.input_path.rsplit(".", 1)[0] + self.added_ending_all
			self.path_data_filtered = self.input_path.rsplit(".", 1)[0] + self.added_ending_filtered
		else:
			self.input_path = ""
			self.path_data_all = ""
			self.path_data_filtered = ""

	# Set new path for exporting all data
	def get_path_data_all(self):
		self.path_data_all = tk.filedialog.asksaveasfilename()


	# Set new path for exporting all data
	def get_path_data_filtered(self):
		self.path_data_filtered = tk.filedialog.asksaveasfilename()
