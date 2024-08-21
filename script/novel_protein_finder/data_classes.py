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
	def __init__(self, data_series):

		# Set range for filtering on length
		self.length_series = data_series
		self.length_min_range = data_series.min()
		self.length_max_range = data_series.max()

