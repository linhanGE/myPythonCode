# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 16:44:37 2018

@author: c3216945
"""
import pandas as pd, numpy as np

def readDataFromFile(filename,skiprows):
    data = pd.read_csv(filename, delim_whitespace = True, comment='#',header=None,skiprows = skiprows)
    data = np.asarray(data)
    return data
    