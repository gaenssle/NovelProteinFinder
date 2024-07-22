#!/usr/bin/python
# Written by ALGaenssle in 2024
# MODULE - MENU BAR
# Change default values (temporarily)

import tkinter as tk
import tkinter.messagebox

from .draw_window import draw_form

## ===========================================================================
## Offer a way to temporarily change the default values with an entry mask
def change_markers(window, default_values, formatting):
	
	## Check if the markers have been edited and update them -----------------
	def update_markers(default, variable):
		if "\n" not in variable.get():
			default = variable.get() + "\n"

	## Submit the changes to alter the default values ------------------------
	def submit_marker_change():
		update_markers(default_values.file_encoding, file_encoding)
		update_markers(default_values.sample_line, sample_line)
		tkinter.messagebox.showinfo("Changed markers", "Markers were changed sucessfully and remain set until program is closed")



	marker_info = """\
The program imports the data from the files by using markers, lines in the text directly before and after the lines which should be imported.
These lines might differ for other systems and can be changed temporarily here.

If you want to change them permanently, copy-paste the program files, and edit the markers in the file 'novel_protein_finder' > 'default_values.py'.\
"""
	

	# Create window for changing the markers
	window_change_markers = tk.Toplevel(window)
	window_change_markers.title("Change markers")
	tk.Label(
			window_change_markers, 
			text ="MARKERS", 
			font=formatting.font_heading
			).grid(
					row=0, 
					columnspan=2
					)
	show_info = tk.Text(
						window_change_markers, 
						wrap=tk.WORD, 
						height=8, 
						width=60, 
						font=formatting.font_text
						)
	show_info.grid(
				row=1, 
				columnspan=2, 
				padx=formatting.padx, 
				pady=formatting.pady)
	show_info.insert("end", marker_info)
	show_info.config(state="disabled")

	# Create variables for the entry widgests
	file_encoding = tk.StringVar(value=default_values.file_encoding)
	sample_line = tk.StringVar(value=default_values.sample_line)

	# List all markers and show current in the entry widgets
	form_dict = {
		"Encoding of input files": file_encoding,
		"Start of line to import sample name:": sample_line,
	}

	draw_form(form_dict, window_change_markers, formatting, add=2)

	# Create button to submit the added changes
	tk.Button(
			window_change_markers, 
			text="Submit changes", 
			command=submit_marker_change, 
			font=formatting.font_text
			).grid(
					row=len(form_dict)+3, 
					columnspan=2, 
					padx=formatting.padx, 
					pady=formatting.pady
					)