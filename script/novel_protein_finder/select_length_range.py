# #!/usr/bin/python

import tkinter as tk
import tkinter.messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import sys

## import own modules
sys.path.append('.')
from script.graphical_interface import draw_window



## ===========================================================================
## Set the range of length which the PUL are allowed to have to pass the filter
def get_length_range(length_series, window, len_plot_step, formatting, colors, filter_settings):
	plot_bins = round((length_series.max() - length_series.min())/len_plot_step)
	len_range_info = "Please insert the minimum and maximum number of genes that a PUL should consist of in order to pass the filter."


	## Check if inserted values are integers and within range
	def check_range(min_variable, max_variable, length_series):
		try:
			min_value = int(min_variable.get())
			max_value = int(max_variable.get())
		except ValueError:
			tkinter.messagebox.showwarning("Incorrect data", f"Please enter full numbers for the length range")
			return False
		if max_value < length_series.min() or min_value > length_series.max():
			tkinter.messagebox.showwarning("Incorrect data", f"Please enter values within the allowed range ({length_series.min()}-{length_series.max()})")
			return False
		else:
			return True


	## Submit the changes to change the range
	def submit_length_range():
		if check_range(min_length, max_length, length_series):
			filter_settings.length_min_range = int(min_length.get())
			filter_settings.length_max_range = int(max_length.get())
			tkinter.messagebox.showinfo("Change range", f"The length range {filter_settings.length_min_range}-{filter_settings.length_max_range} has been saved.")


	## Draw plot: Histogram of PUL length
	def draw_length_plot(): 
		figure = plt.Figure(figsize=(6, 5), dpi=100)
		ax = figure.add_subplot(111)
		canvas = FigureCanvasTkAgg(figure, window_set_length_range)
		canvas.draw()
		toolbar = NavigationToolbar2Tk(canvas, window_set_length_range, pack_toolbar=False)
		toolbar.update()
		canvas.get_tk_widget(
			).grid(
					row=len(form_dict)+5, 
					columnspan=2, 
					padx=formatting.padx, 
					pady=formatting.pady
					)
		toolbar.grid(
					row=len(form_dict)+6, 
					columnspan=2, 
					padx=formatting.padx, 
					pady=formatting.pady
					)
		length_series.plot(kind="hist", bins=plot_bins, edgecolor='black', title="Distribution of PUL length", ax=ax)
		ax.set_ylabel("Occurences")
		ax.set_xlabel("Number of genes in the PUL")
		len_info_str = f"Min = {length_series.min()}\nMax = {length_series.max()}\nAverage = {length_series.mean():.2f}"
		ax.text(0.95, 0.95, len_info_str, horizontalalignment='right',
			verticalalignment='top', transform=ax.transAxes)


	## ===========================================================================
	## Create window for changing the length range
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
						height=3, 
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
	draw_window.draw_form(form_dict, window_set_length_range, formatting, start_row=2)

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
						text = "Show plot",
						command = draw_length_plot, 
						font=formatting.font_text,
						bg=colors.accent	
						).grid(
							row=len(form_dict)+4, 
							columnspan=2, 
							padx=formatting.padx, 
							pady=formatting.pady
							) 