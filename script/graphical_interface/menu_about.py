#!/usr/bin/python
# Written by ALGaenssle in 2024
# MODULE - MENU BAR
# Show a window with info about the program


import tkinter as tk
import tkinter.scrolledtext 

## ===========================================================================
## Info text about the program
program_info = 	"""\
(Written in 2024 by a.l.o gaenssle, check github.com/gaenssle/NovelProteinFinder for updates)

This program imports html files from the PUL DB, extracts and filters the data
- It takes a file or link as input and extract the html data into a csv file
- It then allows you to filter the data bases on two types:
	* PUL length (accepts a range)
	* Specific proteins in puls (accepts selections from a list)


OVERALL REQUIREMENTS:
- The data has to be a link to a specific PULDB website or the source code from the given website
- There are default name endings but they can be changed

Problems with downloading from the website:
-Make sure that the link is correct.
-Check if you have internet.

If the error keeps persisting, open the link in a browser, right click on it and select 'view source code', copy all data and save as .txt file.
Then skip this part and go to the import section.
"""

## ===========================================================================
## Show info about the program
def about_program(window, font_heading, font_text):
	window_about = tk.Toplevel(window)
	window_about.title("About this program")
	window_about.geometry("600x500")

	tk.Label(
			window_about, 
			text ="NOVEL PROTEIN FINDER", 
			font=font_heading
			).pack()

	show_info = tkinter.scrolledtext.ScrolledText(
				window_about, 
				wrap=tk.WORD, 
				font=font_text)
	show_info.pack()
	show_info.insert("end", program_info)
	show_info.config(state="disabled")