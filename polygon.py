# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 20:18:16 2024

@author: casi
"""

import numpy as np
from matplotlib import pyplot as plt


class Polygon:
    def __init__(self, descretes, freqs, title, xlabel, ylabel):
        self.descretes = descretes
        self.freqs = freqs
        self.title = title
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.build()

    def build(self):
        plt.xlim([np.min(self.descretes) - 5, np.max(self.descretes) + 5])

        plt.plot(self.descretes, self.freqs)
        plt.title(self.title)  # "Statistical Data Analysys Histogram"
        plt.xlabel(self.xlabel)  # "Variable X (5 evenly spaced bins)"
        plt.ylabel(self.ylabel)  # "Count"

        plt.show()
