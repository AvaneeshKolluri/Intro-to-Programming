# Avaneesh Kolluri
#I pledge my honor that I have abided by the stevens honor system.
# Lab 1

from cs115 import *
'''imports all functions from the cs 115 folder'''
import math
'''access to math commands'''

def inverse(n):
    '''Finds the inverse of a given number, n'''
    return 1/n

def add(x,y):
    '''adds two different numbers together'''
    return x+y

def e(n):
    '''Approximates a mathamatical value, e, using a Taylor expansion'''
    list1 = range(1,n+1)
    list2 = map(math.factorial, list1)
    list3 = map(inverse, list2)
    return 1 + reduce(add, list3)

def error(n):
    '''Function that returns the absolute value of e, and the approximation of the e(n) function'''
    diff = math.e - e(n)
    return abs(diff)
