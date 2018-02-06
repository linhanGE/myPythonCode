# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 11:14:20 2017

@author: c3216945
"""
import numpy as np, pandas as pd

def readVelocity(filename):
    rawdata = pd.read_csv(filename, delim_whitespace=True, comment='#',header=None,skiprows = 2)
    vdata = rawdata.values
    x,y,z = 1,2,3
    vx = np.asarray(vdata[:,x])
    vy = np.asarray(vdata[:,y])
    vz = np.asarray(vdata[:,z])
    return vx,vy,vz



