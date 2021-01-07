#Avaneesh Kolluri
#I pledge my honor that I have abided by the stevens honor system

from cs115 import*
import math

def dot(L,K):
    '''outputs the dot product of the lists L and K'''
    if L == [] and K == []:
        return 0
    elif L == []:
        return 0
    elif K == []:
        return 0
    else:
        return L[0]*K[0] + dot(L[1:],K[1:])

def explode(S):
    '''takes a string S as input and returns a list of the characters'''
    if S == "":
        return []
    else:
        return [S[0]] + explode(S[1:])

def ind(e,L):
    '''takes in an element e and a sequence L where by "sequence" we mean either a list or a string'''
    if L == [] or L == "":
        return 0
    elif L[0] == e:
        return 0
    else:
        return 1 + ind(e,L[1:])

def removeAll(e,L):
    '''return another list that is identical to L except that all elements identical to e have been removed'''
    if L == []:
        return []
    elif L[0] == e:
        return removeAll(e,L[1:])
    else:
        return [L[0]] + removeAll(e,L[1:])
    
def even(X):
    if X % 2 == 0:
        return True
    else:
        return False

def myFilter(f,L):
    '''we get back a list of the function's true numbers in that list'''
    if L == []:
        return []
    elif f(L[0]) == False:
        return myFilter(f,L[1:])
    else:
        return [L[0]] + myFilter(f,L[1:])

def deepReverse(L):
    '''takes as input a list of elements where some of those elements may be lists themselves'''
    if L == []:
        return []
    elif isinstance (L[0], list):
        return deepReverse(L[1:]) + [deepReverse(L[0])]
    else:
        return deepReverse(L[1:]) + [L[0]]
    
    
