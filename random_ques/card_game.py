"""
Simulate a simple 2 player card game. Regular deck of cards with no jokers (suit doesn't matter, just value)
Players shuffle and divide the deck in 2. The players reveal 1 card at a time from the top of their decks.
The player with the lower card loses and has to take both cards to the bottom of their deck.
The first person to reach 0 cards wins.
"""

# values from 1- 13
# 4 suits. 4 cards of the same value.
# each player has half of the total cards i.e 26.

# comparing each top card with its value:
# deck 3with lower value will get the card removed from its deck
# deck having lower value will loose and append both its prev top and lower top top the end of its deck.
# if the values are equal then both card are appended to their respective lists.
import random
from collections import deque  # double ended queue


def soln():
    # build total deck of 4 suits × 13 cards = 52 cards
    total = []
    for i in range(4):
        for j in range(1, 14):
            total.append(j)

    random.shuffle(total)

    n = len(total)
    half_len = n // 2
    first_deck = deque(total[:half_len])
    second_deck = deque(total[half_len:])

    # game loop
    while len(first_deck) and len(second_deck):
        # players draw cards
        one = first_deck.popleft()
        two = second_deck.popleft()

        if one < two:
            # player 1 wins this round, gets both cards
            first_deck.append(one)
            first_deck.append(two)
        elif two < one:
            # player 2 wins this round
            second_deck.append(one)
            second_deck.append(two)
        else:
            # tie → each keeps their card
            first_deck.append(one)
            second_deck.append(two)

    # decide winner
    return 1 if not len(first_deck) > 0 else 2
