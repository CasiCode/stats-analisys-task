# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 17:43:20 2024

@author: casi
"""
import numpy as np


class RandomGenerator:
    def __init__(self):
        # self.size = size
        # self.scale = scale
        # self.loc = loc
        self.rng = np.random.default_rng()

    def generate(self,  loc: float, scale: float, size: int):
        return self.rng.normal(loc, scale, size)
