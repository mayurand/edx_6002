#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 14:20:33 2016

@author: Mayur Andulkar
"""

from pset2_random_walk_robots.ps2 import *

# === Problem 4
def runSimulation(num_robots, speed, width, height, min_coverage, num_trials,
                  robot_type):
    """
    Runs NUM_TRIALS trials of the simulation and returns the mean number of
    time-steps needed to clean the fraction MIN_COVERAGE of the room.

    The simulation is run with NUM_ROBOTS robots of type ROBOT_TYPE, each with
    speed SPEED, in a room of dimensions WIDTH x HEIGHT.

    num_robots: an int (num_robots > 0)
    speed: a float (speed > 0)
    width: an int (width > 0)
    height: an int (height > 0)
    min_coverage: a float (0 <= min_coverage <= 1.0)
    num_trials: an int (num_trials > 0)
    robot_type: class of robot to be instantiated (e.g. StandardRobot or
                RandomWalkRobot)
    """
    
    
    ticks = 0    
    #robot1 = robot_type(room, speed)
    #current_coverage = room.getNumCleanedTiles()/room.getNumTiles()

    for n in range(num_trials):
        robots_all = []
        room = RectangularRoom(width,height)

        for n in range(num_robots):
            robot = robot_type(room, speed)          
            robots_all.append(robot)
          
        current_coverage = room.getNumCleanedTiles()/room.getNumTiles()
        while (current_coverage<min_coverage):
            for n in range(num_robots):
                robots_all[n].updatePositionAndClean()
            ticks += 1
            #print("\n")
            current_coverage = room.getNumCleanedTiles()/room.getNumTiles()
                #print(ticks)
    return ticks/num_trials
    #raise NotImplementedError