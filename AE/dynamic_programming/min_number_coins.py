"""
"""


# Breaking into small amoutn and solving, like getting min coins from 0 to n.

# O(nd) time where n is the number till n inp and d as the number of denoms
# O(n) space


def minNumberOfCoinsForChange(n, denoms):
    # Taking 1 extra space as we want to store for 0 as an amount
    numsOfCoins = [float("inf") for amount in range(n+1)]
    # need 0 coins to make 0 amount
    numsOfCoins[0] = 0

    # taking 1 denomination at a time
    for denom in denoms:
        for amount in range(len(numsOfCoins)):
            # denom can only be used to make amount if its <= amount
            if denom <= amount:
                numsOfCoins[amount] = min(
                    numsOfCoins[amount], 1+numsOfCoins[amount-denom])
    return numsOfCoins[n] if numsOfCoins[n] != float("inf") else -1
