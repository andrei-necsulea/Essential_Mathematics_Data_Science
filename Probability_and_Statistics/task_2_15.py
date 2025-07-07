'''
There are four Aces in a deck of cards,
how many combinations of pocket Aces are there?
(ie. pair of Aces when drawing two cards from the full deck)
'''

import random

suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
deck = [(rank, suit) for suit in suits for rank in ranks]

trials = 1_000_000
pocket_aces_count = 0

for _ in range(trials):
    hand = random.sample(deck, 2)  # Draw 2 cards without replacement
    if hand[0][0] == 'A' and hand[1][0] == 'A':
        pocket_aces_count += 1

estimated_probability = pocket_aces_count / trials
print(f"Estimated probability of pocket Aces: {estimated_probability:.5f}")