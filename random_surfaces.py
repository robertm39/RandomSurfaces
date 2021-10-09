# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 14:32:23 2021

@author: rober
"""

import numpy as np

class RandomWalk:
    def __init__(self, var_per_unit):
        self.var_per_unit = var_per_unit
        
        #All random walks start at zero
        self.points = {0: 0}
        
        self.min_x = 0
        self.max_x = 0
    
    def stdev_for_dist(self, dist):
        return np.sqrt(self.var_per_unit * dist)
    
    def sample_point_extreme_(self, x):
        start_x = self.min_x if x < self.min_x else self.max_x
        
        dist = abs(x -  start_x)
        # stdev = np.sqrt(self.var_per_unit * dist)
        stdev = self.stdev_for_dist(dist)
        mean = self.points[start_x]
        
        sample = np.random.normal(mean, stdev)
        
        self.min_x = min(x, self.min_x)
        self.max_x = max(x, self.max_x)
        
        return sample
    
    def sample_point_bracketed_(self, x):
        # Find the points directly before and after x
        # Make this more efficient later
        prev = None
        for check_x in sorted(self.points.keys()):
            if prev is None:
                prev = check_x
                continue
            if check_x > x:
                x_1 = prev
                x_2 = check_x
                break
            prev = check_x
        
        # s1 = self.stdev_per_unit * (x - x_1)
        # s2 = self.stdev_per_unit * (x_2 - x)
        s1 = self.stdev_for_dist(x - x_1)
        s2 = self.stdev_for_dist(x_2 - x)
        
        m1 = self.points[x_1]
        m2 = self.points[x_2]
        
        s1_inv_squ = s1 ** (-2)
        s2_inv_squ = s2 ** (-2)
        
        mean = (s1_inv_squ * m1 + s2_inv_squ * m2) / (s1_inv_squ + s2_inv_squ)
        stdev = np.sqrt(((s1 * s2)**2) / (s1**2 + s2**2) )
        
        sample = np.random.normal(mean, stdev)
        
        return sample
    
    def sample_point(self, x):
        #If we've already defined this, don't sample
        if x in self.points:
            return self.points[x]
        
        #If x is beyond the bounds, sample based on the bound
        if x > self.max_x or x < self.min_x:
            y = self.sample_point_extreme_(x)
        #Otherwise, sample based on the points directly before and after x
        else:
            y = self.sample_point_bracketed_(x)
        
        self.points[x] = y
        
        return y
    
    def items(self):
        return self.points.items()