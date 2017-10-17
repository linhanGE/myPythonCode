# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 11:48:07 2017

@author: c3216945
"""
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

def plot_hist(data):
#    num_bins = 50
    fig, ax = plt.subplots()
    # the histogram of the data
    n, bins, patches = ax.hist(x, num_bins, normed=1)
    # add a 'best fit' line
    y = mlab.normpdf(bins, mu, sigma)
    ax.plot(bins, y, '--')
    ax.set_xlabel('Smarts')
    ax.set_ylabel('Probability density')
    ax.set_title(r'Histogram of IQ: $\mu=100$, $\sigma=15$')

    # Tweak spacing to prevent clipping of ylabel
    fig.tight_layout()
    plt.show()