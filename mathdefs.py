# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 20:24:30 2024

@author: casi
"""

import descreteSeries
from constants import INTERVAL_NUMBER
from math import sqrt


def sampleMean(data):
    series = descreteSeries.DescreteSeries(data)
    n = len(data)
    xs = series.getDescretes()
    ns = series.getFreqs()

    summ = 0
    for i in range(0, INTERVAL_NUMBER):
        summ += xs[i] * ns[i]
    return summ / float(n)


def sampleDispersion(data):
    series = descreteSeries.DescreteSeries(data)
    n = len(data)
    xs = series.getDescretes()
    ns = series.getFreqs()
    mean = sampleMean(data)

    summ = 0
    for i in range(0, INTERVAL_NUMBER):
        summ += xs[i]**2 * ns[i] - mean*mean

    return summ / float(n)


def sampleStandardDeviation(data):
    disp = sampleDispersion(data)

    return sqrt(disp)
