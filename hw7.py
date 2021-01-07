"""
Avaneesh Kolluri
10/20/18
I pledge my honor that I have abided by the Stevens honor system.
"""

from cs115 import *

def numToBaseB(N,B):
    '''takes as input a non-negative (0 or larger)
    integer N and a base B (between 2 and 10 inclusive)
    and returns a string representing the number N inbase B.'''
    if N < 0:
        return
    elif N == 0:
        return str(0)
    def help_numToBaseB(N,B):
        '''helper function for the numToBaseB
        function so it can return an empty string when
        N==0'''
        if N == 0:
            return ""
        return help_numToBaseB(N//B,B) + str(N%B)
    return help_numToBaseB(N,B)

def baseBToNum(S,B):
    '''converts a base number to an integer
    number'''
    if S == "":
        return 0
    else:
        return int(S[-1]) + B*baseBToNum(S[:-1],B)

def baseToBase(B1,B2,SinB1):
    '''converts a string in one base to another base string'''
    num = baseBToNum(SinB1,B1)
    return numToBaseB(num,B2)

def add(S,T):
    '''adds the integer value of two binary strings and returns the
    binary representation of the string.'''
    N1 = baseBToNum(S,2)
    N2 = baseBToNum(T,2)
    mysum = N1 + N2
    return numToBaseB(N1 + N2,2)

# Each row has (x,y,carry-in) : (sum,carry-out)
FullAdder ={ ('0','0','0') : ('0','0'),\
              ('0','0','1') : ('1','0'),\
              ('0','1','0') : ('1','0'),\
              ('0','1','1') : ('0','1'),\
              ('1','0','0') : ('1','0'),\
              ('1','0','1') : ('0','1'),\
              ('1','1','0') : ('0','1'),\
              ('1','1','1') : ('1','1') }

def addB(S1,S2):
    '''adds two strings together working in
    binary strings only.'''
    def help_addB(S1,S2,cry):
        '''helper function for the addB function'''
        if S1 == "" and S2 == "":
            return cry
        if S1 == "":
            tup = FullAdder["0",S2[-1],cry]
            return help_addB("",S2[:-1],tup[1]) + tup[0]
        if S2 == "":
            tup = FullAdder[S1[-1],"0",cry]
            return help_addB(S1[:-1],"",tup[1]) + tup[0]
        else:
            tup = FullAdder[S1[-1],S2[-1],cry]
            return help_addB(S1[:-1],S2[:-1],tup[1]) + tup[0]
    var = help_addB(S1,S2,"0")
    if var[0] == "0":
        return var[1:]
    else:
        return var






        
