'''
Avaneesh Kolluri
9/27/18
I pledge my honor that I have abided by the Stevens Honor System.
'''

from cs115 import *

def knapsack(capacity, itemList):
    '''returns the amount of coins used, and which coins were used and how many times.'''
    if capacity == 0 or itemList == []:
        return [0,[]]
    elif capacity < itemList[0][0]:
        return knapsack(capacity,itemList [1:])
    else:
        use = knapsack(capacity - itemList[0][0], itemList[1:])
        lose = knapsack(capacity, itemList[1:])
        use2 = [itemList[0][1] + use[0], [itemList[0]] + use[1]]
        if use2[0] > lose[0]:
            return use2
        else:
            return lose
