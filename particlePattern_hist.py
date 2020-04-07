# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 16:35:35 2019

@author: c3216945
"""

import pyvista as pv
import numpy as np
import glob
import natsort
import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter,
                               AutoMinorLocator)
import seaborn as sns
from scipy.stats import norm
import matplotlib.mlab as mlab

f = glob.glob('*.vtk')
f = natsort.realsorted(f)

def getPos(filename):
    # read vtk as unstructured data
    data = pv.read(filename)
    pts = data.points
#    pts = pts[(pts[:,0]>=-0.002825) & (pts[:,0]<=0.002825)]
    pts = pts[:,1]
    return pts

w = 0.165
#tstep = 0.001
#tstart = 0.02
#startindex = int(tstart/tstep)
k = np.arange(len(f))
bin_nu = getPos(f[0])/w

for i in k:
    if i != 0:
        bin_nu = np.concatenate((bin_nu,getPos(f[i])/w))

bin_nu = bin_nu[np.where(np.abs(bin_nu))]

params = {
   'axes.labelsize': 11,
   'font.family': 'Arial',
   'legend.fontsize': 11,
   'xtick.labelsize': 11,
   'ytick.labelsize': 11,
   'figure.figsize': [2, 2.5]
   }
plt.rcParams.update(params)
fig,ax = plt.subplots()

#n, bins, patches = ax.hist(bin_nu, bins = 15, facecolor='#1b9e77',edgecolor= 'k')
kwargs = dict(hist_kws={'alpha':.6}, kde_kws={'color':'k','linewidth':2})
sns.distplot(bin_nu, bins=20,color="#1b9e77", **kwargs)
                           
#(mu, sigma) = norm.fit(bin_nu)
#y_fit = mlab.normpdf(bins, mu, sigma)
#ax.plot(bins,y_fit)
#ax.plot(y_pdf, x_pdf )
                           
ax.set_ylim(0,2.5)
ax.set_xlim(-0.5,0.5)
#
##majorLocatorY = MultipleLocator(5)
##majorLocatorX = MultipleLocator(0.2)
#minorLocatorY = MultipleLocator(0.001)
#minorLocatorX = MultipleLocator(5)
##ax.yaxis.set_major_formatter(ticker.FormatStrFormatter('%2.1f'))
#
##ax.xaxis.set_major_locator(majorLocatorX)
#ax.xaxis.set_minor_locator(minorLocatorX)
#ax.yaxis.set_minor_locator(minorLocatorY)
##ax.yaxis.set_major_locator(majorLocatorY)
#
ax.set_xlabel("y/w")
ax.set_ylabel('Probability density')
#
fig.text(0.15,0.8,'(a)',weight="bold",fontsize=15)
#
##ax.legend(loc=0,frameon=False)
#
#handles, labels = plt.gca().get_legend_handles_labels()
#order = [2,0,1]
#ax.legend([handles[idx] for idx in order],[labels[idx] for idx in order],frameon=False)
#
fig.savefig('A1gpDistribution.tiff', bbox_inches='tight',pad_inches=0,dpi = 300)
plt.show()
