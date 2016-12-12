###########################
# 6.00.2x Problem Set 1: Space Cows 

from ps1_partition import *

import time

#================================
# Part A: Transporting Space Cows
#================================

def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """

    cow_dict = dict()

    f = open(filename, 'r')
    
    for line in f:
        line_data = line.split(',')
        cow_dict[line_data[0]] = int(line_data[1])
    return cow_dict


# Problem 1
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

      1. As long as the current trip can fit another cow, add the largest cow that    will fit to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # To get the cow name
    # list(cows.keys())[0]
    
    # To get the values listed with each cow
    # cows.get(list(cows.keys())[0])
    
    allTrips = []

    while len(cows)>0:    
      avail_limit = limit
      trip = []
      for cow in sorted(cows, key=cows.get, reverse = True):
        if cows.get(cow)>limit:
          cows.pop(cow)
        elif(cows.get(cow)<=avail_limit):
          trip.append(cow)
          avail_limit = avail_limit - cows.get(cow)
          cows.pop(cow)
      
      allTrips.append(trip) 
    
    return allTrips
    
    pass


def trip_limit(trip,cows):
  trip_limit = 0
  for cow in trip:
    trip_limit = trip_limit + cows.get(cow)
  return trip_limit
  
# Problem 2
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    for trip_list in (get_partitions(cows)):
      
      avail_trip = 0
      for trip in trip_list:
        trip_limit_val = trip_limit(trip, cows)
        if trip_limit_val > limit:
          break
        else:
          avail_trip += 1
    
      if avail_trip == len(trip_list):
        break

    return trip_list
    
    pass

        
# Problem 3
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    
    cows = load_cows("ps1_cow_data.txt")
    limit=10
    print(cows)
    
    start = time.time()
    print(greedy_cow_transport(cows, limit))
    end = time.time()
    print(end - start)
    
    cows = load_cows("ps1_cow_data.txt")
    limit=10
    print(cows)
    
    start = time.time()
    print(brute_force_cow_transport(cows, limit))
    end = time.time()
    print(end - start)
      
    pass


"""
Here is some test data for you to see the results of your algorithms with. 
Do not submit this along with any of your answers. Uncomment the last two
lines to print the result of your problem.
"""

#cows = load_cows("ps1_cow_data.txt")
#limit=10
#print(cows)

#print(greedy_cow_transport(cows, limit))
#print(brute_force_cow_transport(cows, limit))

compare_cow_transport_algorithms()
#print(brute_force_cow_transport(cows, limit))
