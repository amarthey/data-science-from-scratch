from __future__ import division
from collections import Counter
import math
from linear_algebra import sum_of_squares, dot

def mean(x):
    return sum(x) / len(x)


def median(x):
    x_sorted = sorted(x)
    quotient, remainder = divmod(len(x_sorted), 2)
    
    if remainder==0:        
        return (x_sorted[quotient-1] + x_sorted[quotient]) / 2
    else:
        return x_sorted[quotient]


def quantile(x, p):
    """returns the pth-percentile value in x"""
    x_sorted = sorted(x)
    n = len(x_sorted)
    p_idx = int(n * p)
    return x_sorted[p_idx]


def mode(x):
    """returns a list, might be more than one mode"""
    counter = Counter(x)
    max_cnt = max(counter.itervalues())
    return [num for num, cnt in counter.iteritems() if cnt==max_cnt]


def data_range(x):
    return max(x) - min(x)


def de_mean(x):
    """translate x by subtracting its mean (so the result has mean 0)"""
    x_mean = mean(x)
    return [val - x_mean for val in x]


def variance(x):
    """assumes x has at least two elements"""
    x_mean = mean(x)
    n = len(x)
    return sum([(val - x_mean)**2 for val in x]) / n


def standard_deviation(x):
    return math.sqrt(variance(x))


def interquartile_range(x):
    return quantile(x, 0.75) - quantile(x, 0.25)


def covariance(x, y):
    n = len(x)
    return dot(de_mean(x), de_mean(y)) / (n - 1)


def correlation(x, y):
    x_st = standard_deviation(x)
    y_st = standard_deviation(y)
    
    if x_st > 0 and y_st > 0:
        return covariance(x, y) / (x_st * y_st)
    else:
        # if no variation, correlation is zero
        return 0