#!/usr/bin/python
# Written by ALGaenssle in 2024
# MODULE - DRAW WINDOW
# Draw all tkinter windows, frames, widgets and forms

import tkinter as tk

## ===========================================================================
## Create counter class to assure correct row sequence
class Counter():
	def __init__(self):
		self.counter = 0

	def add(self, step=1):
		self.counter += step
		return self.counter

	def __str__(self):
		return str(self.counter)

## ===========================================================================
## Draw frames for window (generalize formatting)
def draw_frame(frames):
	counter = Counter()	
	for frame in frames:
		frame.grid(
					row=0, 
					column=counter.add(), 
					sticky="nsew"
					)
		frame.columnconfigure(0, weight=1)
		# frame.grid_propagate(0)

## ===========================================================================
## Draw widgets for window (generalize formatting)
def draw_widget(widgets, formatting, start_row=0, start_col=0):
	counter = Counter()
	counter.add(start_row)
	for widget in widgets:
		sticky = formatting.sticky
		row = counter.add()
		column = start_col
		padx = formatting.padx
		if isinstance(widget, tk.Checkbutton):
			sticky = "nw"
		elif isinstance(widget, tk.Scrollbar):
			sticky = "ns"
			column += 1
			row -= 1
			padx = (0, padx)
			counter.add(-2)
		elif isinstance(widget, tk.Listbox):
			padx = (padx, 0)
		widget.grid(
					row=row, 
					column=column, 
					sticky=sticky, 
					padx=padx, 
					pady=formatting.pady*widgets[widget],
					ipadx=formatting.ipadx, 
					ipady=formatting.ipady
					)
		if isinstance(widget, tk.LabelFrame):
			widget.grid_columnconfigure(0, weight=1)

def draw_form(form_dict, window, formatting, start_row=0, start_col=0):
	counter = Counter()
	counter.add(start_row)	
	for label in form_dict:
		row = counter.add()
		tk.Label(
				window, 
				text=label, 
				font=formatting.font_text
				).grid(
					row=row, 
					column=start_col, 
					sticky = "w", 
					padx=formatting.padx
					)
		tk.Entry(
				window, 
				textvariable=form_dict[label], 
				font=formatting.font_text
				).grid(
					row=row, 
					column=start_col + 1, 
					padx=formatting.padx
					)
