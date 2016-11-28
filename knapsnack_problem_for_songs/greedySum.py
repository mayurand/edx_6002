'''
    Created on 28 Nov 2016
    
    @author: Mayur Andulkar
'''

def greedySum(L, s):
    """ input: s, positive integer, what the sum should add up to
               L, list of unique positive integers sorted in descending order
        Use the greedy approach where you find the largest multiplier for 
        the largest value in L then for the second largest, and so on to 
        solve the equation s = L[0]*m_0 + L[1]*m_1 + ... + L[n-1]*m_(n-1)
        return: the sum of the multipliers or "no solution" if greedy approach does 
                not yield a set of multipliers such that the equation sums to 's'
    """
    m = []
    for i in range(len(L)):
        m.append(0)
    
    sum_val = 0
    
    for i in range(len(L)):
        m[i] = s//L[i]
        s = s - m[i]*L[i]
        sum_val = m[i]+sum_val  
    if s == 0:
        return sum_val
    else:
        return 'no solution'
    
    
    
L = [9,8,7,6]
s = 200001
print(greedySum(L, s))    
    