
def change(amount, coins):
'''This function returns the minimum amount of coins you can fullfill the required amount with'''
    if amount == 0:
        return 0
    elif coins == []:
        return float('inf')
    elif coins[0] > amount:
        return change(amount, coins[1:])
    else:
        use = change(amount - coins[0] , coins)
        lose = change(amount, coins[1:])
        return min(1 + use, lose)
