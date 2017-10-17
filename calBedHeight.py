# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 17:55:21 2017

@author: c3216945
"""
import numpy as np
import pandas as pd
import glob

def calBedHeight(filename):
    rawdata = pd.read_csv(filename, delim_whitespace = True, comment='#',header=None,skiprows = 9)
    hdata = rawdata.values
    x = 2
    y = 3
    z = 4
    px =  hdata[:,x]
    py =  hdata[:,y]
    pz =  hdata[:,z]
    pz[::-1].sort()
    topparticle =  np.ones(139)
    nrp = 0
    for i in np.arange(len(px)-1):
        if nrp <30 and i < 139 and np.abs(px[i]-px[i+1]) > 0.008 and np.abs(py[i]-py[i+1]) > 0.008:
            topparticle [i] = 1
            nrp +=1
    toplayer = pz[np.nonzero(topparticle != 0)[0]]
    hmean = np.abs(np.average(toplayer[0:29-1]))
    return hmean

filename = glob.glob('*.liggghts_init')
itfile = iter(filename)
n = np.arange(len(filename))
h = np.zeros(len(filename))

for i in n:
    h[i] = calBedHeight(next(itfile))
    with open('hmean0.028','a') as f:
        f.write("%s  %s \n"%(str(i),str(h[i])))

with open('hmean0.028','a') as f:
        f.write("hmean0.028 =  %s \n"%(np.average(h)))



    
    
     
    

