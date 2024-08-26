#!/usr/bin/python
# Written by ALGaenssle in 2024
# CLASS
# Default values for how the data is imported and exported


## Class for default values
class DefaultValues():
	def __init__(self):

		# Set column names of the extracted pandas dataframe
		self.col_names = ["Species", "PUL ID", "Name", "Modularity", "Overlap IDs", "Overlap Names"]

		# Set column names for protein count pandas dataframe
		self.protein_col_names = ["Protein", "Occurences"]

		# PUL length - Histrogram plot: Set step size (default=2.5)
		self.len_plot_step = 2.5

		# Separator of csv. files
		self.sep = ";"

