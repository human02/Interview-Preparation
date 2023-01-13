"""

  Given an array of positive integers representing the values of coins in your
  possession, write a function that returns the minimum amount of change (the
  minimum sum of money) that you cannot create. The given coins can have
  any positive integer value and aren't necessarily unique (i.e., you can have
  multiple coins of the same value). coins [1,2,5] can't create minimum change of 4.

  Input:
    coins = [5,7,1,1,2,3,22]

  Output:
    20

"""
# idea - if current coin value > sum of coins before current coin +1, then we cant produce currChange + 1 value.

# O(nlog(n)) time | O(1)space


def nonConstructibleChange(coins):
    # When in doubt construee the input array to visualize better, sorting costs O(nlog(n)) time
    coins.sort()

    currChange = 0
    for coin in coins:
        if coin > currChange + 1:
            return currChange + 1
        currChange += coin

    return currChange + 1
