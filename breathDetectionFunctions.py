import numpy as np
from scipy import stats

def slp(y):
    x = np.arange(len(y))/20
    slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
    return slope

def expSmoothen(y,t):
    w = np.exp(-((len(y) - np.arange(len(y)) - 1)/t))
    return (w*y/w.sum()).sum()

def gauSmoothen(y,t):
    w = np.exp(-(((len(y) - np.arange(len(y)) - 1)/t))**2)
    return (w*y/w.sum()).sum()

def phase(yslp):
    if yslp > 0:
        return 1
    elif yslp < 0:
        return -1

def breathFilter(x,mint, maxt):
    y = [i for i in x if i >= mint and i <= maxt]
    return y
