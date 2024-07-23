# #!/usr/bin/python

import tkinter as tk
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


data = 	[14, 11, 30, 26, 15, 14, 15, 41, 11, 21, 13, 8, 16, 11, 11, 18, 16, 10, 9, 18, 17, 15, 17, 52, 9, 40, 9, 15, 23, 39, 40, 15, 15, 40, 38, 10, 38, 10, 23, 23, 23, 24, 22] 
length_all = pd.Series(data)

# Draw plot
def plot(): 
	figure = plt.Figure(figsize=(6, 5), dpi=100)
	ax = figure.add_subplot(111)
	canvas = FigureCanvasTkAgg(figure, root)
	canvas.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH)
	length_all.plot(kind="hist", bins=20, edgecolor='black', title="Distribution of PUL length", ax=ax)
	ax.set_ylabel("Occurences")
	ax.set_xlabel("Number of genes in the PUL")
	len_info_str = f"Min = {length_all.min()}\nMax = {length_all.max()}\nAverage = {length_all.mean():.2f}"
	ax.text(0.95, 0.95, len_info_str, horizontalalignment='right',
		verticalalignment='top', transform=ax.transAxes)


# Setup main window
root = tk.Tk()
root.title('Plotting in Tkinter') 
root.geometry("500x500") 

# button that displays the plot 
plot_button = tk.Button(master = root, 
					command = plot, 
					height = 2, 
					width = 10, 
					text = "Plot") 
plot_button.pack() 



root.mainloop()