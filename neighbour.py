# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 19:02:22 2017

@author: c3216945
"""

def neighbour(iterable):
    iterable = iter(iterable)
    prv = None
    cur = next(iterable)
    try:
        while True:
            nxt = next(iterable)
            yield(prv,cur,nxt)
            prv = cur
            cur = nxt
    except StopIteration:
        yield(prv,cur,None)