#
# life.py - Game of Life lab
#
# Name: Avaneesh Kolluri
# Pledge: I pledge my honor that I have abided by the Stevens honor system.
#

import random
import sys
import random

def createOneRow(width):
    """Returns one row of zeros of width "width"...  
       You should use this in your
       createBoard(width, height) function."""
    row = []
    for col in range(width):
        row += [0]
    return row

def createBoard(width,height):
    """ returns a 2d array with "height" rows and "width" cols """
    A = []
    for row in range(height):
        A += [createOneRow(width)]
    return A

def printBoard( A ):
    """ this function prints the 2d list-of-lists/
        A without spaces (using sys.stdout.write)"""
    for row in A:
        for col in row:
            sys.stdout.write(str(col))
        sys.stdout.write('\n')

def diagonalize(width,height):
    """ creates an empty board and then modifies it/
        so that it has a diagonal strip of "on" cells."""
    A = createBoard( width, height )
    for row in range(height):
        for col in range(width):
            if row == col:
                A[row][col] = 1
            else:
                A[row][col] = 0
    return A

def innerCells(w,h):
    """returns a 2d array of all live cells - with the/
        value of 1 - except for a one-cell-wide border of empty cells"""
    A = createBoard(w,h)
    for row in range(h-1):
        for col in range(w-1):
            if row == 0 or col == 0:
                A[row][col] = 0
            else:
                A[row][col] = 1
    return A

def randomCells(w,h):
    """returns an array of randomly-assigned 1's and 0's except that the/
        outer edge of the array is still completely empty"""
    A = createBoard(w,h)
    for row in range(h-1):
        for col in range(w-1):
            if row == 0 or col == 0:
                A[row][col] = 0
            else:
                A[row][col] = random.choice([0,1])
    return A

def copy(A):
    B = createBoard(len(A[0]),len(A))
    for row in range(len(A)):
        for col in range(len(A[0])):
            B[row][col]=A[row][col]
    return B

def innerReverse(A):
    B = copy(A)
    for row in range(1,len(A)-1):
        for col in range(1,len(A[0])-1):
            if B[row][col] == 0:
                B[row][col] = 1
            else:
                B[row][col] = 0
    return B

def next_life_generation( A ):
    """ makes a copy of A and then advanced one/
        generation of Conway's game of life within/
        the *inner cells* of that copy.The outer edge always stays 0."""
    def count_Neighbors(row,col,A):
        total = 0
        for y in range(col-1,col+2):
            for x in range(row-1,row+2):
                if A[x][y] == 0:
                    total += 0
                if A[x][y] == 1:
                    total += 1
        return total - A[row][col]

    newA = copy(A)
    for row in range(1,len(A)-1):
        for col in range(1,len(A[0])-1):
            if A[row][col] == 1 and count_Neighbors(row,col,A) < 2:
                newA[row][col] = 0
            elif A[row][col] == 1 and count_Neighbors(row,col,A) > 3:
                newA[row][col] = 0
            elif A[row][col] == 0 and count_Neighbors(row,col,A) == 3:
                newA[row][col] = 1
    return newA
                







