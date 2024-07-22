#!/usr/bin/python
# Written by ALGaenssle in 2024
# MAIN
# main script to extract and find novel proteins

import os
import tkinter as tk
import tkinter.messagebox

# Own modules
from script.graphical_interface import formatting
from script.graphical_interface import draw_window
from script.graphical_interface.file_selection import FileSelection
from script.graphical_interface import menu_about
from script.graphical_interface import menu_change_markers

from script.novel_protein_finder.main_script import extract_html_data
from script.novel_protein_finder.default_values import DefaultValues



# Create class objects
if __name__=="__main__":
	files = FileSelection()
	default_values = DefaultValues()
	colors = formatting.Colors()
	formatting = formatting.Formatting()

## ===========================================================================
## FUNCTIONS
## ===========================================================================
# Get input name and set all variables according to it
def set_input_file(ask=True):
	files.get_input_file(ask=ask)
	set_truncated_path(files.input_path, input_path)
	set_truncated_path(files.output_path, output_path)

# Set costumized output folder
def set_output_file():
	files.get_output_file()
	set_truncated_path(files.output_path, output_path)

# Truncate paths that are too long
def set_truncated_path(path, tk_variable):
	max_length = formatting.lab_max_length//4
	if len(path) > max_length:
		tk_variable.set("..." + path[-max_length:])
	else:
		tk_variable.set(path)

# Save selection of input files
def submit_selection():
	if files.input_path == "":
		tkinter.messagebox.showwarning("Missing data","No input folder selected!")
		return

# Conduct importing, combining and exporting of files
def extract_initial_data():
	message = extract_html_data(files, default_values)
	if message["m_type"] == "info":
		tkinter.messagebox.showinfo(message["title"], message["message"])
	else:
		tkinter.messagebox.showwarning(message["title"], message["message"])


## ===========================================================================
## SETUP WINDOW
## ===========================================================================
## Create window
window = tk.Tk()
window.title("Find novel proteins")
window.resizable(False, False)


col_files = tk.Frame(window, relief=tk.RAISED, bd=3, bg=colors.col_main)
col_export = tk.Frame(window, relief=tk.RAISED, bd=3, bg=colors.col_main)

# Draw frames
draw_window.draw_frame([col_files, col_export])


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

# Draw menu bar
window.config(menu=menu_bar)


## ===========================================================================
## COLUMN: FOLDER
## ===========================================================================
## Define default values
input_path = tk.StringVar(value="#N/A")
output_path = tk.StringVar(value="#N/A")

## Header
lab_col_files = tk.Label(col_files, text="FILES", bg=colors.heading, 
				font=formatting.font_heading)

## Create section for input folder
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
								wraplength=formatting.lab_max_length/2, 
								height=formatting.display_height, 
								font=formatting.font_note)

## Create section for output folder
button_output_file = tk.Button(col_files, 
								text="Select output file", 
								bg=colors.button, 
								command=set_output_file, 
								font=formatting.font_text)
labframe_output_file = tk.LabelFrame(col_files, 
									bg=colors.col_main, 
									labelwidget=button_output_file, 
									labelanchor="n")
display_output_file = tk.Label(labframe_output_file, 
								textvariable=output_path, 
								bg=colors.col_main, 
								wraplength=formatting.lab_max_length/2, 
								height=formatting.display_height, 
								font=formatting.font_note)
## Conduct export
button_export = tk.Button(col_files, 
						text="EXPORT DATA!", 
						command=extract_initial_data, 
						bg=colors.accent, 
						font=formatting.font_subheading)


## Draw widgets (as dict {widget: pady-multiplier})
widgets = {
			lab_col_files:1, 
			labframe_input_file:2, 
			display_input_file:1, 
			labframe_output_file:2, 
			display_output_file:1,
			button_export:2
			}
draw_window.draw_widget(widgets, formatting)


# ## ===========================================================================
# ## COLUMN: EXPORT
# ## ===========================================================================
# ## Define default values
# file_name = tk.StringVar(value=files.file_name)
# export_info = tk.BooleanVar()
# export_raw = tk.BooleanVar()
# export_elute = tk.BooleanVar()

# ## Header
# lab_col_export = tk.Label(col_export, 
# 						text="EXPORT", 
# 						bg=colors.heading, 
# 						font=formatting.font_heading)

# ## Give option to change the export file name
# button_file_name = tk.Button(col_export, 
# 							text="Save output file name", 
# 							bg=colors.button, 
# 							command=set_file_name, 
# 							font=formatting.font_text)
# labframe_file_name = tk.LabelFrame(col_export, 
# 									bg=colors.col_main, 
# 									labelwidget=button_file_name, 
# 									labelanchor="n")
# entry_file_name = tk.Entry(labframe_file_name, 
# 							textvariable=file_name, 
# 							font=formatting.font_text)

# ## List types of output that can be exported
# lab_file_column = tk.Label(col_export, 
# 							text="SELECT OUTPUT", 
# 							bg=colors.heading, 
# 							font=formatting.font_heading)
# check_info = tk.Checkbutton(col_export, 
# 							text="Information data", 
# 							variable=export_info, 
# 							bg=colors.col_main, 
# 							font=formatting.font_text)
# check_raw = tk.Checkbutton(col_export, 
# 							text="Raw data",
# 							variable=export_raw, 
# 							bg=colors.col_main, 
# 							font=formatting.font_text)
# check_elute = tk.Checkbutton(col_export, 
# 							text="Elution data", 
# 							variable=export_elute, 
# 							bg=colors.col_main, 
# 							font=formatting.font_text)
# check_info.select()
# check_raw.select()
# check_elute.select()

# ## Conduct export
# button_export = tk.Button(col_export, 
# 						text="EXPORT DATA!", 
# 						command=extract_data, 
# 						bg=colors.accent, 
# 						font=formatting.font_subheading)


# ## Draw widgets (as dict {widget: pady-multiplier})
# widgets = {
# 			lab_col_export:1, 
# 			labframe_file_name:2, 
# 			entry_file_name:1, 
# 			lab_file_column:1, 
# 			check_info:0, 
# 			check_raw:0, 
# 			check_elute:0, 
# 			button_export:2
# 			}
# draw_window.draw_widget(widgets, formatting)


## ===========================================================================
## MAIN LOOP
## ===========================================================================
window.mainloop()