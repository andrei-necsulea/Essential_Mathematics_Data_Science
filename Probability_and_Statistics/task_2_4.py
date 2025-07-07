'''
What is the probability that half the product of three dice will exceed their sum?

Hint: Define a random variable using dict.
'''

import math
from itertools import product

random_var = {}

for roll in product(range(1,7) , repeat = 3):
    random_var[roll] = math.prod(roll)/2 , sum(roll)

favorable = [combo for combo , rolls in random_var.items() if rolls[0] > rolls[1]]

probability = len(favorable)/len(random_var)

print(f"The probability that half the product of three dice will exceed their sum is: {probability:.4f}")