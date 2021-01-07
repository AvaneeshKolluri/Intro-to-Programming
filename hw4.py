
'''
Avaneesh Kolluri
10/1/18
I pledge my honor that I have abided by the Stevens honor system
CS 115 HW 4
'''
from cs115 import *

def help_pascal(L):
    '''sums up the previous row numbers, to get a new row.'''
    if L[1:] == []:
        return []
    return [L[0] + L[1]] + help_pascal(L[1:])

def pascal_row(n):
    '''Gives the numbers for a specific row in the pascal triangle.'''
    if n==0:
        return [1]
    elif n==1:
        return [1,1]
    else:
        return [1] + help_pascal(pascal_row(n-1)) + [1]

def pascal_triangle(n):
    '''returns each row of a pascal triangle, until row 'n' is reached.'''
    if n == 0:
        return [[1]]
    return pascal_triangle(n-1) + [pascal_row(n)]

def test_pascal_row():
    '''Checks that pascal_row works properly.'''
    assert pascal_row(0) == [1]
    assert pascal_row(1) == [1,1]
    assert pascal_row(5) == [1, 5, 10, 10, 5, 1]
    assert pascal_row(10) == [1, 10, 45, 120, 210, 252, 210, 120, 45, 10, 1]

def test_pascal_triangle():
    '''Checks that pascal_triangle works properly.'''
    assert pascal_triangle(0) == [[1]]
    assert pascal_triangle(1) == [[1], [1, 1]]
    assert pascal_triangle(5) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]]
    assert pascal_triangle(10) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1], [1, 6, 15, 20, 15, 6, 1], [1, 7, 21, 35, 35, 21, 7, 1], [1, 8, 28, 56, 70, 56, 28, 8, 1], [1, 9, 36, 84, 126, 126, 84, 36, 9, 1], [1, 10, 45, 120, 210, 252, 210, 120, 45, 10, 1]]
