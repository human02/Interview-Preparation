"""

"""

# O(nd)


def numberOfWaysToMakeChange(n, denoms):
    # Initiating an array to get output
    ways = [0 for amt in range(n+1)]
    # only one way to make 0 amt i.e don't use any denom
    ways[0] = 1

    for denom in denoms:
        for amt in range(0, len(ways)):
            if denom <= amt:
                ways[amt] += ways[amt-denom]
    print(ways)
    return ways[n]
