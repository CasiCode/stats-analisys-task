# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 19:48:26 2024

@author: casi
"""

import numpy as np
from math import ceil as mceil
from constants import INTERVAL_NUMBER


class DescreteSeries:
    def __init__(self, data):
        self.data = np.array(data)
        self.calculate()

    def ceil(self, number):
        c = mceil(number)
        if (c == number):
            return int(number + 1)
        else:
            return c

    def calculate(self):
        x_min = np.min(self.data)
        x_max = np.max(self.data)
        data_range = x_max - x_min

        span = data_range / float(INTERVAL_NUMBER)
        temp = x_min + span / float(2)
        self.descretes = []
        for i in range(0, INTERVAL_NUMBER):
            self.descretes.append(temp)
            temp += span

        self.freq = [0] * INTERVAL_NUMBER
        for value in np.nditer(self.data):
            targetRangeIndex = self.ceil((value - x_min) / span)
            if (targetRangeIndex > INTERVAL_NUMBER):
                targetRangeIndex = INTERVAL_NUMBER
            self.freq[targetRangeIndex - 1] += 1

        self.relative_freq = [float(n)/len(self.data) for n in self.freq]

    def getDescretes(self):
        return self.descretes or []

    def getFreqs(self):
        return self.freq or []

    def getRelFreqs(self):
        return self.relative_freq or []
