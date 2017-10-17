# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 11:29:58 2017

@author: c3216945
"""

import pandas as pd
def readfile(filename):
    values =  pd.read_csv(filename,delim_whitespace = True, header =None)
    return values