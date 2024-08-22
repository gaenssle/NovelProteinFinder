#!/usr/bin/python
# Written by ALGaenssle in 2024

## ====================================================================
## CLASS
## Default values defining how the data is imported
## ====================================================================


class FilterSettings():
	def __init__(self):
		self.data = []
		self.length_min_range = 0
		self.length_max_range = 100
		self.set_data = False
		self.proteins = []
		self.protein_list = []
		self.protein_selection = []

	def add_data(self, data_frame):
		self.data = data_frame

		# Set range for filtering on length
		self.length_min_range = self.data["Length"].min()
		self.length_max_range = self.data["Length"].max()
		self.set_data = True

	def add_proteins(self, data_proteins):
		self.proteins = data_proteins

	def get_protein_list(self, col):
		self.protein_list = self.proteins[col].to_list()