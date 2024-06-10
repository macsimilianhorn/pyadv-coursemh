import numpy as np

def add_one(x):
    return np.array(x) + 1

def add_two(x):
    return np.array(x) + 2

def add_three(x):
    return np.array(x) + 3

def sum_thresholding_fun(x, threshold):
    """Threshold array and sum positive elements"""

    x = np.round(x)
    x_th = x > threshold
    out = np.sum(x_th)

    return out