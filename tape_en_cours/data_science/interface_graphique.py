#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 14:39:30 2023

@author: mfalce
"""

from tkinter import filedialog 
from tkinter import *

root = Tk()  # create parent window

# fonction de callback / rappel
var = StringVar(root) 

def get_filename() -> str:
    filename = filedialog.askopenfilename(
        initialdir= ".",
        title="Select File",
        filetypes=(("csv","*.csv"),)
        ) 
    var.set(filename)
    return filename

def graph_from_filename(fname):
    df = pd.read_csv(
        fname, 
        sep=";", 
        skiprows=31, 
        names=["freq", "db"], 
        index_col=False
    )
    
    plt.plot(df.freq[100:200], df.db[100:200])
    plt.show()


selct_file = Button(root, text="Fichier", command=get_filename)
selct_file.pack()
lbl = Label(root , textvariable=var)
lbl.pack()
graph = Button(root, text="Grpah", command=get_filename)
graph.pack()
root.mainloop()
