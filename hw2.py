'''
Created on 9/18/18

Pledge:    I pledge my honor that I have abided by the Stevens honor system

CS115 - Hw 2
'''
import sys
from cs115 import map, reduce, filter
# Be sure to submit hw2.py.  Remove the '_template' from the file name.

# Allows up to 10000 recursive calls.
# The maximum permitted limit varies from system to system.
sys.setrecursionlimit(10000)

# Leave the following lists in place.
scrabbleScores = \
   [ ['a', 1], ['b', 3], ['c', 3], ['d', 2], ['e', 1], ['f', 4], ['g', 2],
     ['h', 4], ['i', 1], ['j', 8], ['k', 5], ['l', 1], ['m', 3], ['n', 1],
     ['o', 1], ['p', 3], ['q', 10], ['r', 1], ['s', 1], ['t', 1], ['u', 1],
     ['v', 4], ['w', 4], ['x', 8], ['y', 4], ['z', 10] ]

Dictionary = ['a', 'am', 'at', 'apple', 'bat', 'bar', 'babble', 'can', 'foo',
              'spam', 'spammy', 'zzyzva']

# Implement your functions here.

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

def removeFromRack(letter, Rack):
    '''function that tests if a letter of the rack is found in a word from the dictionary. If it is found, the letter is then removed from the rack, and the new rack is returned.'''
    if Rack == []:
        return Rack
    elif Rack[0] == letter:
        return Rack[1:]
    else:
        return [Rack[0]] + removeFromRack(letter, Rack[1:])

def testWord(word, Rack):
    '''Function that tests if a word can be built from the dictionary using the rack. It works by testing the first letter of each word from the dictionary, and checks if it is in the rack, and if it is, continues to test the rest of the word from the letters in the rack. If the word cannot be spelled, it moves on to test the next word in the dictionary.'''
    if word == '':
        return True
    elif word[0] in Rack:
        Rack = removeFromRack(word[0], Rack)
        return testWord(word[1:], Rack)
    else:
        return False

def wordsList(Dict, Rack):
    '''Filters the words in the dictionary and only returns the words that can actually be spelled given the rack.'''
    return filter(lambda word: testWord(word, Rack), Dict)

def scoreList(Rack):
    '''Given a bunch of of letters, this function returns all the possible words with their corresponding word score.'''
    return map(lambda word: [word, wordScore(word, scrabbleScores)], wordsList(Dictionary,Rack))

def bestWord(Rack):
    '''Function that returns the word with the highest score possible given a list of letters.'''
    allPossibleWords = scoreList(Rack)
    bestWord = ["word",0]
    def highestWord(allPossibleWords, bestWord):
        '''Sub-function that compares two words, and one by one, chooses the highest word possible using greater than. The comparing words are found by a returned list from the scoreList function.'''
        if allPossibleWords == []:
            return bestWord
        else:
            currentWordAndVal = allPossibleWords[0]
            if currentWordAndVal[1] > bestWord[1]: #if ( our current word's value > our best word's value)
                bestWord = currentWordAndVal          #our current word is our new best word
                return highestWord(allPossibleWords[1:], bestWord)
            else:
                return highestWord(allPossibleWords[1:], bestWord)
    return highestWord(allPossibleWords, bestWord)




        
