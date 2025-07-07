'''
What is the probability that sum of three dice will exceed 6?

Hint: Define a random variable using dict.
'''

from itertools import product

random_var = {}

for roll in product(range(1, 7), repeat=3):
    random_var[roll] = sum(roll)

favorable = [combo for combo, total in random_var.items() if total > 6]

probability = len(favorable) / len(random_var)

print(f"The probability that the sum is > 6 is: {probability:.4f}")