# -*- coding: utf-8 -*-
"""
Created on Sun Jul 16 17:18:04 2017

@author: c3216945
"""
import numpy as np, pandas as pd

def calMeanFreePath(filename):
    # -----read data-----#
    rawdata = pd.read_csv(filename, sep=' ', comment='#',header=None)
    #tstart = 5.
    #tsbegin = int(round(tstart/0.00001))
    mfpdata = rawdata.values
    #mfpdata = rawdata.values[tsbegin:]
#    ts = 0
    cnr,x,y,z = 1,2,3,4      # contat number
    timestep = 0.00001
    tstart = 5
#    tend = -1
    start_index = int(tstart/timestep)
    # end_index = -1
    mfpcnr = mfpdata[start_index:,cnr]
    mfpx = mfpdata[start_index:,x]
    mfpy = mfpdata[start_index:,y]
    mfpz = mfpdata[start_index:,z]
    
    # -----extract contact sequence-----#
    def colCounter(contact):
        notzero = np.nonzero(mfpcnr)[0]
        notzeroplus1 =notzero+1
        notzeroplus1 = np.delete(notzeroplus1,-1)
        contactBegin = notzeroplus1[np.nonzero(mfpcnr[notzeroplus1]==0)[0]]
        notzerominus1 =notzero-1
        notzerominus1 = np.delete(notzerominus1,0)
        contactEnd = notzerominus1[np.nonzero(mfpcnr[notzerominus1]==0)[0]]
        return contactBegin,contactEnd
   
    # ------calculate the path between collisions----- #
    def calPath(begin,end,x,y,z):
        diffx = np.diff(x[begin:end])
        diffy = np.diff(y[begin:end])
        diffz = np.diff(z[begin:end])
        s = np.reshape(np.concatenate((diffx,diffy,diffz)),(3,-1)) # put every diffx,diffy,diffz into each column
        ssum = sum(np.sqrt(np.einsum('ij,ij->j',s,s)))   # np.einsum is used to sum squre of each element in a column
        return ssum
    
    contactBegin,contactEnd = colCounter(mfpcnr)
    itconBegin = iter(contactBegin) # iterator 
    itconEnd = iter(contactEnd)     # iterator
    lencon = len(contactBegin)
    mfp = np.zeros(lencon)
    
    for i in np.arange(lencon):
        begin = next(itconBegin)
        end = next(itconEnd)
        mfp[i] = calPath(begin,end,mfpx,mfpy,mfpz)
            
    meanmfp = np.average(mfp)
    return meanmfp

