#!/usr/bin/python
# Written by ALGaenssle in 2024
# MODULE - MENU BAR
# Show a window with info about the program


import tkinter as tk
import tkinter.messagebox
# import tkinter.filedialog

import urllib.request
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

from script.graphical_interface import formatting
from script.graphical_interface import draw_window
from script.novel_protein_finder import file_class


# link = "http://www.cazy.org/PULDB/index.php?cazy_mod=GH154&sp_name2=&sp_ncbi2="

if __name__=="__main__":
	colors = formatting.Colors()
	formatting = formatting.Formatting()
	files = file_class.FileSelection()


def get_data_from_link():
	url = text_download_html.get("1.0", "end-1c")
	if url == "":
		tkinter.messagebox.showwarning("Missing link","Please enter a link.")
	elif files.save_path == "":
		tkinter.messagebox.showwarning("Missing file name","Please provide a save file first")
	else:
		try:
			website =  urllib.request.urlopen(url)
			raw_data = website.read()
			with open(files.save_path, "wb") as save_html:
				save_html.write(raw_data)
			tkinter.messagebox.showinfo("Data downloaded", "The raw data has been downloaded. You can proceed to the next section.")
		except:
			tkinter.messagebox.showwarning("Error while downloading","-Make sure that the link is correct.\n-Check if you have internet.\n\nIf the error keeps persisting, open the link in a browser, right click on it and select 'view source code', copy all data and save as .txt file.\nThen skip this part and go to the import section.")


def set_save_path():
	files.get_save_path()
	set_truncated_path(files.save_path, save_path)

## Truncate paths that are too long
def set_truncated_path(path, tk_variable):
	max_length = formatting.lab_max_length//4
	if len(path) > max_length:
		tk_variable.set("..." + path[-max_length:])
	else:
		tk_variable.set(path)


## ===========================================================================
## Show info about the program
window = tk.Tk()
window.title("Find novel proteins")

col_download = tk.Frame(window, relief=tk.RAISED, bd=3, bg=colors.col_main)

## Draw frames
draw_window.draw_frame([col_download])

## ===========================================================================
# download_link = tk.StringVar()
save_path = tk.StringVar(value="#N/A")

lab_col_download = tk.Label(col_download, text="DOWNLOAD", bg=colors.heading, 
				font=formatting.font_heading)

label_download_html = tk.Label(col_download, 
							text ="Download data from link", 
							font=formatting.font_heading)

text_download_html = tk.Text(col_download,
							# textvariable=download_link, 
							font=formatting.font_text,
							height=3,
							width=40)

## Create section for input file path
button_save_data = tk.Button(col_download, 
								text="Save as...", 
								bg=colors.button, 
								command=set_save_path, 
								font=formatting.font_text)
labframe_save_data = tk.LabelFrame(col_download, 
									bg=colors.col_main, 
									labelwidget=button_save_data, 
									labelanchor="n")
display_save_data = tk.Label(labframe_save_data, 
								textvariable=save_path, 
								bg=colors.col_main, 
								wraplength=formatting.lab_max_length/1.1, 
								height=formatting.display_height, 
								font=formatting.font_note)

button_download_data = tk.Button(col_download, 
								text="download", 
								bg=colors.button, 
								command=get_data_from_link, 
								font=formatting.font_text)


widgets = {
			lab_col_download:1, 
			label_download_html:2, 
			text_download_html:1, 
			labframe_save_data:2, 
			display_save_data:1,
			button_download_data:2
			}
draw_window.draw_widget(widgets, formatting)


window.mainloop()