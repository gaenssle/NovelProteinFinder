#!/usr/bin/python
# Written by ALGaenssle in 2024


import tkinter as tk


len_min = 8
len_max = 52


def update_lower_value(new_value):
    label1.config(text=f"Value: {new_value}")
    slider_variable1.set(new_value)

def update_upper_value(new_value):
    label2.config(text=f"Value: {new_value}")
    slider_variable2.set(new_value)

root = tk.Tk()
root.title("Slider Customization")


slider_variable1 = tk.DoubleVar()
slider_variable2 = tk.DoubleVar()
slider_variable1.set(len_min)
slider_variable2.set(len_max)

slider1 = tk.Scale(root, 
					from_=len_min, 
					to=len_max, 
					digits=2, 
					length=300, 
					width=20, 
					label="Lower limit",
					orient="horizontal", 
					command=update_lower_value)
slider1.pack()

slider2 = tk.Scale(root, 
					from_=len_min, 
					to=len_max, 
					digits=2, 
					length=300, 
					width=20, 
					label="Upper limit",
					orient="horizontal", 
					command=update_upper_value)
slider2.pack()


label1 = tk.Label(root, text="Value: 0")
label1.pack()

label2 = tk.Label(root, text="Value: 0")
label2.pack()

root.mainloop()