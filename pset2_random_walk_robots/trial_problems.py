'''
Created on 26 Nov 2016

@author: osboxes
'''

import random

# Code Sample A
mylist = []

for i in range(random.randint(1, 10)):
    random.seed(0)
    a = random.randint(1, 10)
    if  a > 3:
        number = random.randint(1, 10)
        if number not in mylist:
            mylist.append(number)
print(mylist)