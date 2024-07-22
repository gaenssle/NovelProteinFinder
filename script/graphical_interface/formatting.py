#!/usr/bin/python
# Written by ALGaenssle in 2024
# CLASSES
# For formatting the graphical interface

## ===========================================================================
## Set colors for window
class Colors():
	def __init__(self):
		self.col_main = "#80b3ff"
		self.col_sub = "#0066ff"
		self.col_accent = "#003380"
		self.button = "#bdccdb"
		self.heading = "#ffcc00"
		self.main = "#5377ac"
		self.accent = "#998566"
		self.note = "white"


## ============================================================================
## Set formatting for window
class Formatting():
	def __init__(self):
		self.lab_max_length = 250
		self.label_width = 25
		self.min_x_size = 300
		self.min_y_size = 550
		self.padx = 10
		self.pady = 10
		self.ipadx = 2
		self.ipady = 2
		self.display_height = 3
		self.font_heading = ("Verdana", 11, "bold")
		self.font_subheading = ("Verdana", 9, "bold")
		self.font_text = ("Verdana", 9)
		self.font_note = ("Verdana", 8)
		self.sticky = "ew"