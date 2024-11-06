# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 19:57:48 2024

@author: casi
"""

import numpy as np
import math
from matplotlib import pyplot as plt
from constants import INTERVAL_NUMBER


class Histogram:
    def __init__(self, data, title, xlabel, ylabel):
        self.data = data
        self.title = title
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.build()

    def build(self):
        bins = np.linspace(math.ceil(np.min(self.data)),
                           math.floor(np.max(self.data)), INTERVAL_NUMBER)
        plt.xlim([np.min(self.data) - 5, np.max(self.data) + 5])

        w = np.ones_like(self.data[0]) / len(self.data[0])

        plt.hist(self.data, weights=w, bins=bins, alpha=0.5)
        plt.title(self.title)
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)

        plt.show()
