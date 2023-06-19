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
var = StringVar("Choisir un fichier svp") 

def get_filename() -> str:
    filename = filedialog.askopenfilename(
        initialdir= ".",
        title="Select File",
        filetypes=(("csv","*.csv"),)
        ) 
    var.set(filename)
    return filename


turn_on = Button(root, text="ON", command=get_filename)
turn_on.pack()
lbl = Label(root , textvariable=var)
lbl.pack()

root.mainloop()
