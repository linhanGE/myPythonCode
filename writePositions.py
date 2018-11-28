# -*- coding: utf-8 -*-
"""
Created on Fri Dec 22 17:00:16 2017

@author: c3216945
"""

import pandas as pd
import numpy as np

filename = 'in.5liggghts_run'
rawdata = pd.read_csv(filename, delim_whitespace=True, skiprows = 9, header=None)

rawdata = rawdata.values
positions = np.asarray(rawdata[:,2:5])
x = positions[:,0]*0.01
y = positions[:,1]*0.01
z = positions[:,2]*0.01

for i in np.arange(positions.shape[0]):
    with open('particle_coordinates.txt','a') as f:
        f.write("({0:10.8f} {1:10.8f} {2:10.8f})\n".format(x[i], y[i], z[i]))

    
    
