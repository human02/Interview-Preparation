"""


"""

# O(nlog(n)) - time | O(1) - space


def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    totalPlayers = len(redShirtSpeeds)
    redShirtSpeeds.sort()
    blueShirtSpeeds.sort()
    sum = 0
    for i in range(totalPlayers):
        if fastest:
            sum += max(redShirtSpeeds[i], blueShirtSpeeds[totalPlayers-1-i])
        else:
            sum += max(redShirtSpeeds[i], blueShirtSpeeds[i])
    return sum


print(tandemBicycle([5, 5, 3, 9, 2], [3, 6, 7, 2, 1], True))
