#!/usr/bin/python
# Written by ALGaenssle in 2024
# CLASS
# Obtain all required information which data should be imported

import os
import tkinter as tk
import tkinter.filedialog


## ====================================================================
## Create class for storing file locations
class FileSelection():
	def __init__(self):
		self.input_path = ""
		self.output_path = ""
		self.added_ending = "_extracted.csv"

	## FILES --------------------------------------------------------
	# Get input file path
	def get_input_file(self, ask=True):
		if ask:
			self.input_path = tk.filedialog.askopenfilename()
			self.output_path = self.input_path.rsplit(".", 1)[0] + self.added_ending
		else:
			self.input_path = ""
			self.output_path = ""

	# Set new output file path
	def get_output_file(self):
		self.output_path = tk.filedialog.asksaveasfilename()
