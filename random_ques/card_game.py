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
