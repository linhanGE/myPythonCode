# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 16:37:14 2018

@author: c3216945
"""
import glob,re

def natural_sort(l): 
    convert = lambda text: int(text) if text.isdigit() else text.lower() 
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ] 
    return sorted(l, key = alphanum_key)

def getFilenames(fileFormat):
    filename = glob.glob('*.fileFormat')
    filename = natural_sort(filename)
    return filename