# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-
# """
# Created on Mon Jun 19 14:39:30 2023

# @author: mfalce
# """

# from tkinter import filedialog 
from tkinter import *
import tkinter
import pandas as pd 
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg)

root = Tk()  # create parent window

# fonction de callback / rappel
var = StringVar(root) 
fig = Figure(figsize=(5, 4), dpi=100)
canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.

def get_filename():
    filename = tkinter.filedialog.askopenfilename(
        initialdir= ".",
        title="Select File",
        filetypes=(("csv","*.csv"),)
        ) 
    var.set(filename)
    return filename

def graph_from_filename(fname):
    fig.clear()
    df = pd.read_csv(
        fname, 
        sep=";", 
        skiprows=31, 
        names=["freq", "db"], 
        index_col=False
    )
    fig.add_subplot(111).plot(df.freq[100:200], df.db[100:200])
    canvas.draw()

def graph_from_stringvar():
    fname = var.get()
    graph_from_filename(fname)


selct_file = Button(root, text="Fichier", command=get_filename)
selct_file.pack()
lbl = Label(root , textvariable=var)
lbl.pack()
graph = Button(root, text="Graph", command=graph_from_stringvar)
graph.pack()
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
root.mainloop()
