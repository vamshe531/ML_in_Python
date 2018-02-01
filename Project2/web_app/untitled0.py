#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 23:23:24 2018

@author: vamshi
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

ts = [3,10,12,13,12,10,12]
tsavg = ts


#Average
def avg(series):
    return float(sum(series))/len(series)
print(avg(ts))


#Moving window average
def movavg(series,n):
    return avg(series[-n:])
print movavg(ts,4)


#Weighted moving average- weights should add up to 1
def wgtavg(series,weights):
    return np.dot(series[-len(weights):],weights)
wgts = [0.1,0.2,0.3,0.4]
print(wgtavg(ts,wgts))

#Single exponential smoothing


