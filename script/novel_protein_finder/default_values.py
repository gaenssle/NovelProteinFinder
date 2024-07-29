#!/usr/bin/python
# Written by ALGaenssle in 2024

## ====================================================================
## CLASS
## Default values defining how the data is imported
## ====================================================================

## Class for default values
class DefaultValues():
	def __init__(self):
		# Encoding of the raw data files
		self.file_encoding = "cp1252"

		# Extract sample name from the line starting with this string
		self.sample_line = "Sample :"

		# Set column names of the extracted pandas dataframe
		self.col_names = ["Species", "PUL ID", "Name", "Modularity", "Overlap IDs", "Overlap Names"]

		# Set default values for marker
		self.marker_list =[ "GH154", "unk", "GH"]

		# PUL length - Histrogram plot: Set step size (default=2.5)
		self.len_plot_step = 2.5

