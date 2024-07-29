# #!/usr/bin/python

import tkinter as tk
import tkinter.messagebox
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


# import sys
# sys.path.append('.')
# from script.graphical_interface.draw_window import draw_form
# from script.graphical_interface import formatting
# from . import default_values

from script.graphical_interface import formatting
from script.graphical_interface import draw_window
from script.novel_protein_finder.default_values import DefaultValues
from script.novel_protein_finder.data_classes import FilterSettings

data = 	[14, 11, 30, 26, 15, 14, 15, 41, 11, 21, 13, 8, 16, 11, 11, 18, 16, 10, 9, 18, 17, 15, 17, 52, 9, 40, 9, 15, 23, 39, 40, 15, 15, 40, 38, 10, 38, 10, 23, 23, 23, 24, 22] 
length_all = pd.Series(data)


## ===========================================================================
## Offer a way to temporarily change the default values with an entry mask
def get_length_range(length_all, window, len_plot_step, formatting, filter_settings):
	plot_bins = round((length_all.max() - length_all.min())/len_plot_step)


	## Check if the entered data in the column entry widgets are integers and within the correct range ----
	def get_integer(set_limit, variable, length_series, var_type):
		value_input = variable.get()
		try:
			value_input = int(value_input)
		except ValueError:
			tkinter.messagebox.showwarning("Incorrect data", f"Please enter full numbers for the {var_type} length")
			return False
		if value_input < length_series.min() or value_input > length_series.max():
			tkinter.messagebox.showwarning("Incorrect data", f"Please enter a {var_type} length within the allowed range ({length_series.min()}-{length_series.max()})")
			return False
		else:
			set_limit = value_input
			return True


	## Submit the changes to alter the default values ------------------------
	def submit_length_range():
		check_min = get_integer(filter_settings.length_min_range, min_length, length_all, "min")
		check_max = get_integer(filter_settings.length_max_range, max_length, length_all, "max")
		if all([check_min, check_max]):
			tkinter.messagebox.showinfo("Change range", f"The length range {filter_settings.length_min_range}-{filter_settings.length_max_range} has been saved.")



	# Draw plot
	def draw_length_plot(): 
		figure = plt.Figure(figsize=(6, 5), dpi=100)
		ax = figure.add_subplot(111)
		canvas = FigureCanvasTkAgg(figure, window_set_length_range)
		canvas.get_tk_widget(
			).grid(
					row=len(form_dict)+5, 
					columnspan=2, 
					padx=formatting.padx, 
					pady=formatting.pady
					)
		length_all.plot(kind="hist", bins=plot_bins, edgecolor='black', title="Distribution of PUL length", ax=ax)
		ax.set_ylabel("Occurences")
		ax.set_xlabel("Number of genes in the PUL")
		len_info_str = f"Min = {length_all.min()}\nMax = {length_all.max()}\nAverage = {length_all.mean():.2f}"
		ax.text(0.95, 0.95, len_info_str, horizontalalignment='right',
			verticalalignment='top', transform=ax.transAxes)









	len_range_info = "Please insert the minimum and maximum number of genes that a PUL should consist of in order to pass the filter."
	

	# Create window for changing the length range
	window_set_length_range = tk.Toplevel(window)
	window_set_length_range.title("Set PUL length")
	tk.Label(
			window_set_length_range, 
			text ="PUL length range", 
			font=formatting.font_heading
			).grid(
					row=0, 
					columnspan=2
					)
	show_info = tk.Text(
						window_set_length_range, 
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
	show_info.insert("end", len_range_info)
	show_info.config(state="disabled")

	# Create variables for the entry widgests
	min_length = tk.StringVar(value=filter_settings.length_min_range)
	max_length = tk.StringVar(value=filter_settings.length_max_range)

	# Show the current length range and show current in the entry widgets
	form_dict = {
		"Min length": min_length,
		"Max length:": max_length
	}

	draw_window.draw_form(form_dict, window_set_length_range, formatting, add=2)

	# Create button to submit the added changes
	set_range_button = tk.Button(
						window_set_length_range, 
						text="Set PUL length range", 
						command=submit_length_range, 
						font=formatting.font_text
						).grid(
							row=len(form_dict)+3, 
							columnspan=2, 
							padx=formatting.padx, 
							pady=formatting.pady
							)


	# button that displays the plot 
	plot_button = tk.Button(
						window_set_length_range,
						text = "Plot PUL length",
						command = draw_length_plot, 
						font=formatting.font_text	
						).grid(
							row=len(form_dict)+2, 
							columnspan=2, 
							padx=formatting.padx, 
							pady=formatting.pady
							) 


## ===========================================================================
## MAIN FUNCTIONS
## ===========================================================================
## ===========================================================================
# Create class objects
if __name__=="__main__":
	# files = FileSelection()
	default_values = DefaultValues()
	colors = formatting.Colors()
	formatting = formatting.Formatting()

def filter_length():
	filter_settings = FilterSettings(length_all)
	get_length_range(length_all, window, default_values.len_plot_step, formatting, filter_settings)



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
						text="Filter PULs length", 
						command=filter_length, 
						bg=colors.accent, 
						font=formatting.font_subheading)


## Draw widgets (as dict {widget: pady-multiplier})
widgets = {
			button_len_filter:2
			}
draw_window.draw_widget(widgets, formatting)

window.mainloop()