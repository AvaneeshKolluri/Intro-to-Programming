'''
Created on 10/11/18
@author:   Avaneesh Kolluri
Pledge:    I pledge my honor that I have abided by the Stevens Honor System

CS115 - Lab 6
'''
def isOdd(n):
    '''Returns whether or not the integer argument is odd.'''
    if n%2 == 0:
        return False
    else:
        return True

'''101010'''
'''Given an odd base 10 number, the least significant bit will be 1
because all the other bit places are even. Given an even base 10 number,
the least significant bit will be 0.'''
'''The original value is dividing by two, and rounding down if the result is a decimal.
This is called integer division.'''
'''If n is odd, then add a 1 in front of the least significant
bit, and if n is even, add a 0 in front of the least significant
bit.'''

def numToBinary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the binary representation of non-negative integer n.
    If n is 0, the empty string is returned.'''
    if n == 0:
        return ""
    elif n%2 == 0:
        return numToBinary(n/2) + "0"
    elif n%2 == 1:
        return numToBinary(n//2) + "1"

def binaryToNum(s):
    '''Precondition: s is a string of 0s and 1s.
    Returns the integer corresponding to the binary representation in s.
    Note: the empty string represents 0.'''
    if s == '':
        return 0
    else:
        return int(s[-1]) + 2*binaryToNum(s[:-1])

def increment(s):
    '''Precondition: s is a string of 8 bits.
    Returns the binary representation of binaryToNum(s) + 1.'''
    if s == '11111111':
        return '00000000'
    else:
        bi = numToBinary(binaryToNum(s) + 1)
        return (8-len(bi))*'0' + bi

def count(s, n):
    '''Precondition: s is an 8-bit string and n >= 0.
    Prints s and its n successors.'''
    if n<0:
        return
    else:
        print(s)
        count(increment(s),n-1)

def numToTernary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the ternary representation of non-negative integer
    n. If n is 0, the empty string is returned.'''
    if n == 0:
        return ""
    elif n%3 == 0:
        return numToTernary(n/3) + '0'
    elif n%3 == 1:
        return numToTernary(n//3) + '1'
    elif n%3 == 2:
        return numToTernary(n//3) +'2'
    
def ternaryToNum(s):
    '''Precondition: s is a string of 0s, 1s, and 2s.
    Returns the integer corresponding to the ternary representation in s.
    Note: the empty string represents 0.'''
    if s == '':
        return 0
    else:
        return int(s[-1]) + 3*ternaryToNum(s[:-1])
