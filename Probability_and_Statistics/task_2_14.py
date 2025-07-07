'''
Standard deck of cards

There are 52 cards in a standard deck of cards.

What is the probability of drawing

    a Queen?
    a card that is a Heart?
    a Queen of Hearts?
    a Queen of Hearts?
    a face/court card (such as Jacks, Queens, or Kings)?
'''

import random
from collections import Counter

suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
deck = [(rank, suit) for suit in suits for rank in ranks]

trials = 100000
results = Counter()

for _ in range(trials):
    card = random.choice(deck)
    rank, suit = card

    if rank == 'Q':
        results['Queen'] += 1
    if suit == 'Hearts':
        results['Heart'] += 1
    if card == ('Q', 'Hearts'):
        results['Queen of Hearts'] += 1
    if rank in ['J', 'Q', 'K']:
        results['Face'] += 1

print(f"Estimated probability of Queen: {results['Queen'] / trials:.4f}")
print(f"Estimated probability of Heart: {results['Heart'] / trials:.4f}")
print(f"Estimated probability of Queen of Hearts: {results['Queen of Hearts'] / trials:.4f}")
print(f"Estimated probability of Face card: {results['Face'] / trials:.4f}")