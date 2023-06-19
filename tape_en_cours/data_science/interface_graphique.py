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

root = Tk()  # create parent window

# fonction de callback / rappel
var = StringVar(root) 
fig = Figure(figsize=(5, 4), dpi=100)

def get_filename():
    filename = filedialog.askopenfilename(
        initialdir= ".",
        title="Select File",
        filetypes=(("csv","*.csv"),)
        ) 
    var.set(filename)
    return filename

def graph_from_filename(fname):
    fig = 
    df = pd.read_csv(
        fname, 
        sep=";", 
        skiprows=31, 
        names=["freq", "db"], 
        index_col=False
    )
    
    plt.plot(df.freq[100:200], df.db[100:200])

def graph_from_stringvar():
    fname = var.get()
    graph_from_filename(fname)


selct_file = Button(root, text="Fichier", command=get_filename)
selct_file.pack()
lbl = Label(root , textvariable=var)
lbl.pack()
graph = Button(root, text="Graph", command=graph_from_stringvar)
graph.pack()
canvas = FigureCanvasTkAgg(fig, master=root)  # A tk.DrawingArea.
canvas.draw()
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
root.mainloop()




from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
# Implement the default Matplotlib key bindings.
from matplotlib.backend_bases import key_press_handler

import numpy as np


root = tkinter.Tk()
root.wm_title("Embedding in Tk")

t = np.arange(0, 3, .01)
fig.add_subplot(111).plot(t, 2 * np.sin(2 * np.pi * t))


canvas.mpl_connect("key_press_event", on_key_press)


def _quit():
    root.quit()     # stops mainloop
    root.destroy()  # this is necessary on Windows to prevent
                    # Fatal Python Error: PyEval_RestoreThread: NULL tstate


button = tkinter.Button(master=root, text="Quit", command=_quit)
button.pack(side=tkinter.BOTTOM)

tkinter.mainloop()
# If you put root.destroy() here, it will cause an error if the window is
# closed with the window manager.