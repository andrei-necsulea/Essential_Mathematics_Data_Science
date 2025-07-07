'''
Perform the exact same experiment as in
Task 2.5 with rolling a fair six-sided dice with the following sides {1,2,2,3,3,3}.
What are the number you get the most?
'''

import random
import matplotlib.pyplot as plt
from collections import Counter

def  dice_rolls(trials):
    dice = [1, 2, 2, 3, 3, 3]
    for n in trials:
        results = [random.choice(dice) for _ in range(n)]
        frequencies = Counter(results)

        print(f"\nFor {n} rolls : ")
        for value in sorted(frequencies.keys()):
            print(f"Value {value} appeared {frequencies[value]} times.")

        plt.figure(figsize=(6, 4))
        plt.bar(frequencies.keys(), frequencies.values())
        plt.axhline(y=0, color='black')
        plt.title(f"Distribution of dice rolls (n = {n})")
        plt.xlabel("Dice Value")
        plt.ylabel("Frequency")
        plt.xticks([1, 2, 3])
        plt.tight_layout()
        plt.show()

        most_common = frequencies.most_common(1)[0]
        print(f"Most common number: {most_common[0]} (appeared {most_common[1]} times)")

n_rolls = [10, 100, 1000, 1000000]
dice_rolls(n_rolls)