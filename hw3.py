'''
Created on 9/21/18
@author:   Avaneesh Kolluri
Pledge:    I pledge my honor that I have abided by the stevens honor system.

CS115 - Hw 3
'''
# Be sure to submit hw3.py.  Remove the '_template' from the file name.
from cs115 import *

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 0
' Implement the function giveChange() here:
' See the PDF in Canvas for more details.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# your code goes here


def giveChange(amount, coins):
    '''returns the amount of coins used, and which coins were used and how many times.'''
    if amount <= 0:
        return [0,[]]
    elif coins == [] or coins == [0]:
        return [float('inf'),[]]
    elif coins[0] > amount:
        return giveChange(amount, coins[1:])
    else:
        use = giveChange(amount - coins[0] , coins)
        lose = giveChange(amount, coins[1:])
        if 1 + use[0] <= lose[0]:
            List = use[1] + [coins[0]]
            return[1 + use[0], List]
        else:
            return lose
            

# Here's the list of letter values and a small dictionary to use.
# Leave the following lists in place.
scrabbleScores = \
   [ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
     ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
     ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
     ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]

Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo',
              'spam', 'spammy', 'zzyzva']

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 1
' Implement wordsWithScore() which is specified below.
' Hints: Use map. Feel free to use some of the functions you did for
' homework 2 (Scrabble Scoring). As always, include any helper
' functions in this file, so we can test it.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def wordsWithScore(dct, scores):
    '''List of words in dct, with their Scrabble score.

    Assume dct is a list of words and scores is a list of [letter,number]
    pairs. Return the dictionary annotated so each word is paired with its
    value. For example, wordsWithScore(Dictionary, scrabbleScores) should
    return [['a', 1], ['am', 4], ['at', 2] ...etc... ]
    '''
    if dct == []:
        return []
    if scores == []:
        return []
    else:
        return map(lambda y: [y,wordScore(y,scores)], dct)

def letterScore(letter,scorelist):
    '''Takes as input a single letter string called letter and a list. The list contains a string of lists as well: each list contains a number and a letter, and the user gets to input a letter and the function returns a numerical score for that letter'''
    if scorelist == []:
        return 0
    elif scorelist [0][0] == letter:
        return scorelist [0][1]
    else:
        return letterScore(letter, scorelist[1:])

def wordScore(S, scorelist):
    '''Takes an input of a string and a scorelist, and returns the output word scrabble score of the string'''
    if S == '':
        return 0
    else:
        return letterScore(S[0], scorelist) + wordScore(S[1:], scorelist)    



'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 2
' For the sake of an exercise, we will implement a function
' that does a kind of slice. You must use recursion for this
' one. Your code is allowed to refer to list index L[0] and
' also use slice notation L[1:] but no other slices.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def take(n, L):
    '''Returns the list L[0:n].'''
    if n == 0:
        return []
    if L == []:
        return []
    else:
        return [L[0]] + take(n-1,L[1:])


'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' PROBLEM 3
' Similar to problem 2, will implement another function
' that does a kind of slice. You must use recursion for this
' one. Your code is allowed to refer to list index L[0] and
' also use slice notation L[1:] but no other slices.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
def drop(n, L):
    '''Returns the list L[n:].'''
    if n == 0:
        return L
    if L == []:
        return []
    else:
        return drop(n-1,L[1:])

