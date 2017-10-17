# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 20:28:29 2017

@author: c3216945
"""
import glob
import numpy as np, pandas as pd
#import matplotlib.pyplot as plt
def readData(filename):
    rawdata = pd.read_csv(filename, delim_whitespace=True, comment='#',header=None,skiprows = 0)
    vdata = rawdata.values
    vp = vdata[:,1]
    return np.mean(vp)

filename = glob.glob('*.txt')
n = np.arange(len(filename))
v = np.zeros(len(filename))

for i in n:
    v[i] = readData(filename[i])
    with open('v.txt','a') as f:
        f.write("%s  %s \n"%(filename[i],str(v[i])))
