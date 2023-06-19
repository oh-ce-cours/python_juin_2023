#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 14:39:30 2023

@author: mfalce
"""

from tkinter import filedialog 
from tkinter import *
Tk().withdraw() 
filename = filedialog.askopenfilename(initialdir= "/",title="Select File",filetypes=(("png files","*.png"),("jpeg files","*.jpg"),("all files","*.*"))) 
print(filename)