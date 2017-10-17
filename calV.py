# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 18:00:59 2017

@author: c3216945
"""

import numpy as np, pandas as pd

def getv(filename):
    rawdata = pd.read_csv(filename, delim_whitespace=True, comment='#',header=None)
    vdata =  rawdata.values
    x,y,z = 1,2,3
    timestep = 0.001
    tstart = 0
    start_index = int(tstart/timestep)
    meanvx = np.mean(np.abs(vdata[start_index:,x]))
    meanvy = np.mean(np.abs(vdata[start_index:,y]))
    meanvz = np.mean(np.abs(vdata[start_index:,z]))
    return meanvx,meanvy,meanvz