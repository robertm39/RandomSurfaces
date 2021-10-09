# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 14:48:59 2021

@author: rober
"""

import random

import matplotlib.pyplot

import random_surfaces

def plot_walk(walk):
    xs = list()
    ys = list()
    
    for x, y in walk.items():
        xs.append(x)
        ys.append(y)
    
    matplotlib.pyplot.scatter(xs, ys, marker='.')

def random_walk_test_1():
    stdev_per_unit = 1.0
    
    divisions = 10000
    order = list([ x/divisions for x in range(1, divisions+1)])
    shuffle = False
    
    if shuffle:
        random.shuffle(order)
    
    walk = random_surfaces.RandomWalk(stdev_per_unit)
    for x in order:
        walk.sample_point(x)
    plot_walk(walk)

def main():
    random_walk_test_1()

if __name__ == '__main__':
    main()