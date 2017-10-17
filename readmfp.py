# -*- coding: utf-8 -*-
"""
Created on Sat Jul 29 16:39:34 2017

@author: c3216945
"""
import glob

import numpy as np, pandas as pd

def readmfp(filename):
    rawdata = pd.read_csv(filename, delim_whitespace=True, comment='#',header=None)
    mfpdata = rawdata.values
    mfp,mfpx,mfpy,mfpz = 1,2,3,4
#    particleNr = np.asarray(mfpdata[:,n])
    mfpvalue = np.mean(np.asarray(mfpdata[:,mfp]))
    mfpvaluex = np.mean(np.asarray(mfpdata[:,mfpx]))
    mfpvaluey = np.mean(np.asarray(mfpdata[:,mfpy]))
    mfpvaluez = np.mean(np.asarray(mfpdata[:,mfpz]))
    return mfpvalue,mfpvaluex,mfpvaluey,mfpvaluez

filename = glob.glob('*.txt')
n = np.arange(len(filename))
mfp = np.zeros(len(filename))
mfp_x = np.zeros(len(filename))
mfp_y = np.zeros(len(filename))
mfp_z = np.zeros(len(filename))

for i in n:
    mfp[i],mfp_x[i],mfp_y[i],mfp_z[i] = readmfp(filename[i])
    with open('mfp','a') as f:
        f.write("%s  %s  %s  %s  %s\n"%(filename[i],str(mfp[i]),str(mfp_x[i]),str(mfp_y[i]),str(mfp_z[i])))