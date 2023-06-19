#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 12:17:17 2023

@author: mfalce
"""

import pandas as pd 

fname = "TX_comb_3p63GHZ_deuxdents_shift2p3GHz_AWG_deuxfiltresIFDMS.CSV"
df = pd.read_csv(fname, sep=";", skiprows=31, columns=["freq", "db"])
