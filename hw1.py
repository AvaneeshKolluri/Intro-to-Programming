#Avaneesh Kolluri
#9/9/18
#I pledge my honor that I have abided by the Stevens honor system.
from cs115 import *
import math

def mult(x,y):
    '''function that multiplies two numbers and returns the product of two numbers'''
    return x*y

def factorial(n):
    '''takes a factorial of a positive integer'''
    n = abs(n)
    list = range(1,n+1)
    return reduce(mult,list)

def add(x,y):
    '''this function takes the sum of two numbers'''
    return x+y

def mean(L):
    '''this function takes the mean of a list of numbers'''
    tot_num = len(L)
    sum_ = reduce(add,L)
    return sum_/tot_num

def div(k):
    '''this function is used to see if the remainder is zero or not'''
    return 42 % k == 0

def divides(n):
    '''returns the div function'''
    def div(k):
        '''Finds out if a number is divisable by another number without any remainders'''
        return n % k == 0
    return div

def prime(n):
    '''returns true, if number, n, is prime, else returns false'''
    list = range(2,n)
    new_num = map(divides(n),list)
    return sum(new_num) == 0
