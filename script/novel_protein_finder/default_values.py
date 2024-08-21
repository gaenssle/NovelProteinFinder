#!/usr/bin/python
# Written by ALGaenssle in 2024

## ====================================================================
## CLASS
## Default values defining how the data is imported
## ====================================================================

## Class for default values
class DefaultValues():
	def __init__(self):

		# Set column names of the extracted pandas dataframe
		self.col_names = ["Species", "PUL ID", "Name", "Modularity", "Overlap IDs", "Overlap Names"]

		# Set default values for marker
		self.marker_list =[ "GH154", "unk", "GH"]

		# PUL length - Histrogram plot: Set step size (default=2.5)
		self.len_plot_step = 2.5

		# Separator of csv. files
		self.sep = "\t"

