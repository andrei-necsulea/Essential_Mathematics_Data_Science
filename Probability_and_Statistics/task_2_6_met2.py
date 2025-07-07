'''
Perform the exact same experiment as in
Task 2.5 with rolling a fair six-sided dice with the following sides {1,2,2,3,3,3}.
What are the number you get the most?
'''

import random
import matplotlib.pyplot as plt
from collections import Counter
import numpy as np

def roll_dice_grouped_plot(trials):
    dice = [1, 2, 2, 3, 3, 3]
    values = [1, 2, 3]
    all_counts = []

    for n in trials:
        results = [random.choice(dice) for _ in range(n)]
        freqs = Counter(results)
        counts = [freqs.get(val, 0) for val in values]
        all_counts.append(counts)

    bar_width = 0.18
    x = np.arange(len(values))

    plt.figure(figsize=(12, 6))

    for i, counts in enumerate(all_counts):
        offset = i * bar_width
        plt.bar(x + offset, counts, width=bar_width, label=f'n={trials[i]}')

    center_of_bars = x + bar_width * (len(trials) - 1) / 2
    plt.xticks(center_of_bars, values)
    plt.xlabel("Dice Value")
    plt.ylabel("Frequency")
    plt.title("Distribution of Dice Rolls for Different n")
    plt.yscale('log')
    plt.legend()
    plt.tight_layout()
    plt.show()

n_rolls = [10, 100, 1000, 1000000]
roll_dice_grouped_plot(n_rolls)