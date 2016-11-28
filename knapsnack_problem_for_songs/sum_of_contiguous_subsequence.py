'''
Created on 28 Nov 2016

@author: Mayur Andulkar
'''

def max_contig_sum(L):
    """ L, a list of integers, at least one positive
    Returns the maximum sum of a contiguous subsequence in L """
    #YOUR CODE HERE
    max_ending_val = max_till_now = 0
    for x in L:
        max_ending_val = max(0, max_ending_val + x)
        max_till_now = max(max_till_now, max_ending_val)
    return max_till_now    
    
    
    
L = [3, 4, -1, 5, -4]
print(max_contig_sum(L))