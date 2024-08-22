#!/usr/bin/python
# Written by ALGaenssle in 2024
# MAIN
# main script to extract and find novel proteins

import pandas as pd
import os
import tkinter as tk
import tkinter.messagebox

# Own modules
from script.graphical_interface import formatting
from script.graphical_interface import draw_window
from script.graphical_interface.file_selection import FileSelection
from script.graphical_interface import menu_about
from script.graphical_interface import menu_change_markers

from script.novel_protein_finder.extract_all_data import extract_html_data
from script.novel_protein_finder.default_values import DefaultValues
from script.novel_protein_finder.data_classes import FilterSettings
from script.novel_protein_finder.select_length_range import get_length_range
from script.novel_protein_finder.select_required_proteins import draw_protein_window

## ===========================================================================
## CREATE CLASS OBJECTS
## ===========================================================================
if __name__=="__main__":
	files = FileSelection()
	default_values = DefaultValues()
	colors = formatting.Colors()
	formatting = formatting.Formatting()
	filter_settings = FilterSettings()


## ===========================================================================
## FUNCTIONS
## ===========================================================================
## Get input name and set all variables according to it
def set_input_file(ask=True):
	files.get_input_file(ask=ask)
	set_truncated_path(files.input_path, input_path)
	set_truncated_path(files.path_data_all, path_data_all)
	set_truncated_path(files.path_data_filtered, path_data_filtered)

## Set costumized output file location and name
def set_path_data_all():
	files.get_path_data_all()
	set_truncated_path(files.path_data_all, path_data_all)

## Set costumized output file location and name
def set_path_data_filtered():
	files.get_path_data_filtered()
	set_truncated_path(files.path_data_filtered, path_data_filtered)

## Truncate paths that are too long
def set_truncated_path(path, tk_variable):
	max_length = formatting.lab_max_length//4
	if len(path) > max_length:
		tk_variable.set("..." + path[-max_length:])
	else:
		tk_variable.set(path)

## Save selection of input files
def submit_selection():
	if files.input_path == "":
		tkinter.messagebox.showwarning("Missing data","No input file selected!")
		return

## Conduct importing, combining and exporting of files
def extract_data_all():
	message = extract_html_data(files, default_values)
	if message["m_type"] == "info":
		tkinter.messagebox.showinfo(message["title"], message["message"])
	else:
		tkinter.messagebox.showwarning(message["title"], message["message"])

	# Set up fata for filtering	
	data_frame = pd.read_csv(files.path_data_all, sep=default_values.sep)
	data_frame["Length"] = data_frame[default_values.col_names[3]].str.count(r'\s+') + 1
	filter_settings.add_data(data_frame)


## Set filters for the PUL length
def set_filter_length():
	if filter_settings.set_data:
		length_series = filter_settings.data["Length"]
		get_length_range(length_series, window, default_values.len_plot_step, formatting, colors, filter_settings)
	else:
		tkinter.messagebox.showwarning("Missing data","No file with all data!\nExport data first.")

## Select proteins the PUL have to contain to pass the filter
def select_proteins():
	if filter_settings.set_data:
		pul_list = filter_settings.data[default_values.col_names[3]].str.split(" ").to_list()
		draw_protein_window(pul_list, window, formatting, colors, filter_settings, default_values)
	else:
		tkinter.messagebox.showwarning("Missing data","No file with all data!\nExport data first.")

## Filter the PULS based on length and/or required proteins
def filter_data():
	if filter_settings.set_data:
		data_filtered = filter_settings.data.copy()	# Make a copy to avoid errors

		# Filter data based on PUL length
		data_filtered = data_filtered[data_filtered["Length"] > filter_settings.length_min_range]
		data_filtered = data_filtered[data_filtered["Length"] < filter_settings.length_max_range]

		data_filtered.to_csv(files.path_data_filtered, sep=default_values.sep, index=False)
		tkinter.messagebox.showinfo("Data exported", "The filtered data has been exported.")
	else:
		tkinter.messagebox.showwarning("Missing data","No file with all data!\nExport data first.")


## ===========================================================================
## SETUP WINDOW
## ===========================================================================
## Create window
window = tk.Tk()
window.title("Find novel proteins")
window.resizable(False, False)


## Sert columns
col_files = tk.Frame(window, relief=tk.RAISED, bd=3, bg=colors.col_main)
col_filter = tk.Frame(window, relief=tk.RAISED, bd=3, bg=colors.col_main)

## Draw frames
draw_window.draw_frame([col_files, col_filter])


## ===========================================================================
## MENU BAR
## ===========================================================================
file_list_string=tk.StringVar(value=[""])

## Create main bar
menu_bar = tk.Menu(window)

## Create menu for files (reset, exit)
menu_file = tk.Menu(menu_bar, tearoff=0)
menu_file.add_command(label="Reset", 
						command=lambda: set_input_file(ask=False))
menu_file.add_command(label="Exit", command=exit)
menu_bar.add_cascade(label="Window", menu=menu_file)

## Create menu for help (about, set markers)
menu_help = tk.Menu(menu_bar, tearoff=0)
menu_help.add_command(label="About", 
						command=lambda: menu_about.about_program(window, 
						formatting.font_heading, formatting.font_text))
menu_help.add_command(label="Change markers", 
						command=lambda: menu_change_markers.change_markers(
							window, default_values, formatting))
menu_bar.add_cascade(label="Configure", menu=menu_help)

## Draw menu bar
window.config(menu=menu_bar)


## ===========================================================================
## COLUMN: FOLDER
## ===========================================================================
## Define default values
input_path = tk.StringVar(value="#N/A")
path_data_all = tk.StringVar(value="#N/A")

## Header
lab_col_files = tk.Label(col_files, text="FILES", bg=colors.heading, 
				font=formatting.font_heading)

## Create section for input file path
button_input_file = tk.Button(col_files, 
								text="Select input file", 
								bg=colors.button, 
								command=set_input_file, 
								font=formatting.font_text)
labframe_input_file = tk.LabelFrame(col_files, 
									bg=colors.col_main, 
									labelwidget=button_input_file, 
									labelanchor="n")
display_input_file = tk.Label(labframe_input_file, 
								textvariable=input_path, 
								bg=colors.col_main, 
								wraplength=formatting.lab_max_length/1.1, 
								height=formatting.display_height, 
								font=formatting.font_note)

## Create section for file path for all data
button_file_data_all = tk.Button(col_files, 
								text="Set file name for all data", 
								bg=colors.button, 
								command=set_path_data_all, 
								font=formatting.font_text)
labframe_file_data_all = tk.LabelFrame(col_files, 
									bg=colors.col_main, 
									labelwidget=button_file_data_all, 
									labelanchor="n")
display_file_data_all = tk.Label(labframe_file_data_all, 
								textvariable=path_data_all, 
								bg=colors.col_main, 
								wraplength=formatting.lab_max_length/1.1, 
								height=formatting.display_height, 
								font=formatting.font_note)
## Conduct export
button_export = tk.Button(col_files, 
						text="EXPORT DATA!", 
						command=extract_data_all, 
						bg=colors.accent, 
						font=formatting.font_subheading)


## Draw widgets (as dict {widget: pady-multiplier})
widgets = {
			lab_col_files:1, 
			labframe_input_file:2, 
			display_input_file:1, 
			labframe_file_data_all:2, 
			display_file_data_all:1,
			button_export:2
			}
draw_window.draw_widget(widgets, formatting)


## ===========================================================================
## COLUMN: FILTER
## ===========================================================================
## Define default values
path_data_filtered = tk.StringVar(value="#N/A")



## Header
lab_col_filter = tk.Label(col_filter, text="FILTER", bg=colors.heading, 
				font=formatting.font_heading)

## Set allowed range of PUL length
button_len_filter = tk.Button(col_filter, 
						text="Set PULs length", 
						command=set_filter_length, 
						bg=colors.button_select, 
						font=formatting.font_subheading)

## Set list of required CAZY
button_protein_filter = tk.Button(col_filter, 
						text="Select required proteins", 
						command=select_proteins, 
						bg=colors.button_select, 
						font=formatting.font_subheading)


## Create section for file path for filtered data
button_file_data_filtered = tk.Button(col_filter, 
								text="Define name for filtered data", 
								bg=colors.button, 
								command=set_path_data_filtered, 
								font=formatting.font_text)
labframe_file_data_filtered = tk.LabelFrame(col_filter, 
									bg=colors.col_main, 
									labelwidget=button_file_data_filtered, 
									labelanchor="n")
display_file_data_filtered = tk.Label(labframe_file_data_filtered, 
								textvariable=path_data_filtered, 
								bg=colors.col_main, 
								wraplength=formatting.lab_max_length/1.1, 
								height=formatting.display_height, 
								font=formatting.font_note)

## Conduct export
button_filter = tk.Button(col_filter, 
						text="FILTER DATA!", 
						command=filter_data, 
						bg=colors.accent, 
						font=formatting.font_subheading)


## Draw widgets (as dict {widget: pady-multiplier})
widgets = {
			lab_col_filter:1, 
			button_len_filter:2,
			button_protein_filter:2,
			labframe_file_data_filtered:2, 
			display_file_data_filtered:1,
			button_filter:2
			}
draw_window.draw_widget(widgets, formatting)



## ===========================================================================
## MAIN LOOP
## ===========================================================================
window.mainloop()