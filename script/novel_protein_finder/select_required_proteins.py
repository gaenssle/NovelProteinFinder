# #!/usr/bin/python

import pandas as pd
import tkinter as tk
import tkinter.messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk


import os
import sys

## import own modules
sys.path.append('.')
from script.graphical_interface import formatting
from script.graphical_interface import draw_window
from script.graphical_interface.file_selection import FileSelection

from script.novel_protein_finder.default_values import DefaultValues
from script.novel_protein_finder.data_classes import FilterSettings

protein_selection_info = "Please select all the proteins that the PUL is required to contain to pass the filter."

## ========================================================================
## Create dataframe with all found proteins and their occurence
def get_protein_list(pul_list):
	temp1_list = [protein for pul in pul_list for protein in pul]
	temp2_list = [protein.split("|") for protein in temp1_list]
	protein_list = [domain for protein in temp2_list for domain in protein]
	protein_data = pd.Series(protein_list).value_counts()
	protein_count = pd.DataFrame(protein_data).reset_index()
	protein_count.columns = default_values.protein_col_names
	filter_settings.add_proteins(protein_count)


	
## ========================================================================
## Draw window for protein selection with all its contents
## ========================================================================
def draw_protein_window(window, protein_selection_info):

	## ========================================================================
	## Get all .txt files in folder and select all
	def set_protein_list(protein_list_string):
		filter_settings.get_protein_list(default_values.protein_col_names[0])
		protein_list_string.set(filter_settings.protein_list)
		# list_box_proteins.selection_set(0, "end")

	## ========================================================================
	## Toggle sort list by count of alphabetically
	def toggle_sort():
		if list(protein_list_string.get()) == filter_settings.protein_list:
			protein_list_string.set(sorted(filter_settings.protein_list))
		else:
			protein_list_string.set(filter_settings.protein_list)

	## ========================================================================
	## Toggle select/deselect all proteins in list
	def toggle_select_all():
		filter_settings.protein_selection = [list_box_proteins.get(index) 
							for index in list_box_proteins.curselection()]
		if len(filter_settings.protein_list) == len(filter_settings.protein_selection):
			list_box_proteins.select_clear(0, "end")
		else:
			list_box_proteins.selection_set(0, "end")
		filter_settings.protein_selection = [list_box_proteins.get(index) 
							for index in list_box_proteins.curselection()]

	## ========================================================================
	## Save selection of proteins
	def submit_selection():
		filter_settings.protein_selection = [list_box_proteins.get(index) 
							for index in list_box_proteins.curselection()]
		tkinter.messagebox.showinfo("Protein list updated", 
			f"There are now {len(filter_settings.protein_selection)} required proteins:\n{"\n".join(filter_settings.protein_selection)}")

	## ========================================================================
	## Draw the protein plot
	def draw_protein_plot(): 
		figure = plt.Figure(figsize=(6, 5), dpi=100)
		ax = figure.add_subplot(111)
		canvas = FigureCanvasTkAgg(figure, window_select_proteins)
		canvas.draw()
		toolbar = NavigationToolbar2Tk(canvas, window_select_proteins, pack_toolbar=False)
		toolbar.update()
		widgets_plot = {canvas.get_tk_widget():1, toolbar:1}
		draw_window.draw_widget(widgets_plot, formatting, start_row=4, start_col=1)		
		filter_settings.proteins.head(20).plot(kind="barh", 
									x=filter_settings.proteins.columns[0], 
									y=filter_settings.proteins.columns[1], 
									edgecolor='black', 
									title="Top 20 proteins found in the PULs", 
									legend=False, 
									ax=ax)
		ax.invert_yaxis()
		ax.set_xlabel("Occurences")


	window_select_proteins = tk.Toplevel(window)
	window_select_proteins.title("Select required proteins")

	heading = tk.Label(window_select_proteins, 
						text ="Select PUL protein markers", 
						font=formatting.font_heading)
	heading.grid(row=0,
				column=0, 
				columnspan=2)

	show_info = tk.Text(window_select_proteins, 
						wrap=tk.WORD, 
						height=4, 
						width=60, 
						font=formatting.font_text)
	show_info.grid(row=1,
					column=0, 
					columnspan=2, 
					padx=formatting.padx, 
					pady=formatting.pady)
	show_info.insert("end", protein_selection_info)
	show_info.config(state="disabled")


	## ========================================================================
	## Create list box displaying all proteins
	## ========================================================================
	## Define default values
	protein_list_string=tk.Variable(value=[""])

	## Create button to submit selection
	button_selection_submit = tk.Button(window_select_proteins, 
									text="Save selection", 
									bg=colors.accent, 
									command=submit_selection, 
									font=formatting.font_text)

	## Display/hide, correct, label and display input files
	button_toggle_sort = tk.Button(window_select_proteins,
									text="Toggle sort", 
									bg=colors.button, 
									command=toggle_sort, 
									font=formatting.font_text)
	labframe_proteins = tk.LabelFrame(window_select_proteins, 
										labelwidget=button_toggle_sort, 
										labelanchor="n") 

	## Create listbox with scrollbar
	list_box_proteins = tk.Listbox(labframe_proteins, 
									selectmode = "multiple", 
									listvariable=protein_list_string, 
									height=12)

	scrollbar_proteins = tk.Scrollbar(labframe_proteins, 
										orient="vertical", 
										command=list_box_proteins.yview)
	list_box_proteins["yscrollcommand"] = scrollbar_proteins.set

	button_toggle_select = tk.Button(window_select_proteins,
									text="Toggle select all", 
									bg=colors.button, 
									command=toggle_select_all, 
									font=formatting.font_text)


	## ========================================================================
	## Create button to display the top found proteins in a plot
	button_plot = tk.Button(window_select_proteins,
						text = "Show found proteins",
						command = draw_protein_plot,
						bg=colors.button_select, 
						font=formatting.font_text)

	## ========================================================================
	## Draw widgets (as dict {widget: pady-multiplier})
	widgets_list = {
				button_selection_submit:0,
				labframe_proteins:2, 
				list_box_proteins:1, 
				scrollbar_proteins:1,
				button_toggle_select:1
				}
	draw_window.draw_widget(widgets_list, formatting, start_row=3)

	widgets_plot_button = {button_plot:0}
	draw_window.draw_widget(widgets_plot_button, formatting, start_row=3, start_col=1)
	set_protein_list(protein_list_string)


## ===========================================================================
## MAIN FUNCTION
## ===========================================================================
def select_proteins():
	data_frame = pd.read_csv(files.path_data_all, sep=default_values.sep)
	data_frame["Length"] = data_frame[default_values.col_names[3]].str.count(r'\s+') + 1
	filter_settings.add_data(data_frame)
	if filter_settings.set_data:
		pul_list = filter_settings.data[default_values.col_names[3]].str.split(" ").to_list()
		get_protein_list(pul_list)


		draw_protein_window(window, protein_selection_info)
		# set_file_list()

	else:
		tkinter.messagebox.showwarning("Missing data","No file with all data!\nExport data first.")




## ===========================================================================
## SET CLASS INSTANCES
## ===========================================================================
# Create class objects
if __name__=="__main__":
	files = FileSelection()
	default_values = DefaultValues()
	colors = formatting.Colors()
	formatting = formatting.Formatting()
	filter_settings = FilterSettings()
	files.path_data_all = "/home/nepomuk/Desktop/Git/NovelProteinFinder/files/input_files/PULDB_GH154_short_filtered.csv"

## ===========================================================================
## MAIN WINDOW
## ===========================================================================
window = tk.Tk()
window.title("Find novel proteins")
window.resizable(False, False)


col_filter = tk.Frame(window, relief=tk.RAISED, bd=3, bg=colors.col_main)

# Draw frames
draw_window.draw_frame([col_filter])



## Conduct export
button_len_filter = tk.Button(col_filter, 
						text="Select required proteins", 
						command=select_proteins, 
						bg=colors.accent, 
						font=formatting.font_subheading)


## Draw widgets (as dict {widget: pady-multiplier})
widgets = {
			button_len_filter:2
			}
draw_window.draw_widget(widgets, formatting)

window.mainloop()