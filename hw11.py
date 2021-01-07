'''
Avaneesh Kolluri
11/21/18
I pledge my honor that I have abided by the Stevens Honor System.
-Avaneesh Kolluri
'''

# nim template DNaumann (2018), for assignment nim_hw11.txt 

# Global variables used by several functions
piles = []         # list containing the current pile amounts
num_piles = 0      # number of piles, which should equal len(pile)


def play_nim():
    """ plays game of nim between user and computer; computer plays optimally """
    
    init_piles()
    display_piles()
    while True:
        user_plays()
        display_piles()
        if sum(piles) == 0:
            # TODO print a message telling the user they won
            print("You have won!")
            break
        computer_plays()
        display_piles()
        if sum(piles) == 0:
            # TODO print a message telling the user the computer won
            print("The computer has won!")
            break


def init_piles():
    """ Assign initial values to the global variables 'num_piles' and
        'piles'
        User chooses number of piles and initial size of each pile.
        Keep prompting until they enter valid values."""
    global piles
    global num_piles

    piles = []
    while True:
        try:
            num_piles = int(input("How many piles do you want to play with?"))
            while num_piles != abs(num_piles):
                print("Please enter a positive integer.")
                num_piles = int(input("How many piles do you want to play with?"))
            break
        except:
            print("Please enter a positive integer value for the piles.")
            
    num_piles = int(num_piles)
    for i in range(num_piles):
        while True:
            try:
                piles += [int(input("How many in pile "+str(i)+'?'))]
                while piles[i] != abs(piles[i]):
                    print("Enter a positive integer.")
                    piles[i] = int(input("How many in pile "+str(i)+'?'))
                break
            except:
                print("Please enter an integer value for the pile value.")

def display_piles():
    """ display current amount in each pile """
    global piles
    global num_piles

    for i in range(num_piles):
        pil = str(piles[i])
        print("pile " + str(i) + " = " + pil)

        

def user_plays():
    """ get user's choices and update chosen pile """
    global piles
    
    print("Your turn ...")
    p = get_pile()
    amt = get_number(p)
    piles[p] = piles[p] - amt


def get_pile():
    """ return user's choice of pile
        Keep prompting until the choice is valid, i.e.,
        in the range 0 to num_piles - 1. """
    global piles
    global num_piles

    global val
    while True:
            try:
                val = int(input("Which pile?"))
                while val != abs(val):
                    print("Enter a positive integer.")
                    val = int(input("Which pile?"))
                break
            except:
                print("Please enter an integer value for the pile value.")
                
    while (val not in range(0,num_piles) or piles[val] == 0):
        print("Please enter a valid pile.")
        val = int(input("Which pile?"))
    return val


def get_number(pnum):
    """ return user's choice of how many to remove from pile 'pnum'
        Keep prompting until the amount is valid, i.e., at least 1
        and at most the amount in the pile."""
    global piles

    global val
    t = piles[val]
    L = list(range(1,t+1))
    s = "".join(str(x) for x in L)
    pnum = (input("How many?"))
    while ((pnum) not in s or abs(int(pnum))!=int(pnum)):
        print("Sorry, you must input a positive integer value that the pile still has remaining")
        pnum = (input("How many?"))
    return int(pnum)

def game_nim_sum():
    """ return the nim-sum of the piles """
    global piles
    global num_piles 

    nimSum = 0
    initial = piles[0]
    nimSum = initial
    for i in range(1,len(piles)):
        nimSum = nimSum ^ piles[i]
    return nimSum


def opt_play():
    """ Return (p,n) where p is the pile number and n is the amt to
        remove, if there is an optimal play.  Otherwise, (p,1) where
        is the pile number of a non-zero pile.

        Implement this using game_nim_sum() and following instructions
        in the homework text."""
    global piles
    global num_piles 

    n = 0
    for i in range(len(piles)):
        if piles[i] > 0:
            n = piles[i] ^ game_nim_sum()
            if n < piles[i]:
                return (i,piles[i]-n)
    for i in range(len(piles)):
        if piles[i] > 0:
            return (i,1)

def computer_plays():
    """ compute optimal play, update chosen pile, and tell user what was played

        Implement this using opt_play(). """
    global piles
    global num_piles

    tup = opt_play()
    print("I remove " + str(tup[1]) + " from pile " + str(tup[0]))
    piles[tup[0]] -= tup[1]

#   start playing automatically
if __name__ == "__main__" : play_nim()
