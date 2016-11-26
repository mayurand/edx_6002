#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 21 18:23:21 2016

@author: Mayur Andulkar
"""

import random
random.seed(0)

def all_same(items):
    return all(x == items[0] for x in items) 

def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3 
    balls of the same color were drawn.
    '''
    balls_all_same = 0
    
    for _ in range(numTrials):
        balls = ['R','G','R','G','R','G']
        for _ in range(0,3):
            balls.pop(random.randint(0,len(balls)-1))
        if (all_same(balls)):
            balls_all_same += 1
   
    return float(balls_all_same/numTrials)    
        
        
print(noReplacementSimulation(1000000))