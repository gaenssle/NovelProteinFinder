#!/usr/bin/python
# Written by ALGaenssle in 2024

## ====================================================================
## CLASS
## Default values defining how the data is imported
## ====================================================================

## Class for default values
class DataLength():
	def __init__(self, data_series):
		self.list = data_series

		# Get lowest and highest value
		self.min_value = self.list.min()
		self.max_value = self.list.max()

		# Set range for filtering
		self.min_range = self.min_value
		self.max_range = self.max_value



class FilterSettings():
	def __init__(self):
		self.data = []
		self.length_min_range = 0
		self.length_max_range = 100
		self.set_data = False

	def add_data(self, data_frame):
		self.data = data_frame

		# Set range for filtering on length
		self.length_min_range = self.data["Length"].min()
		self.length_max_range = self.data["Length"].max()
		self.set_data = True

