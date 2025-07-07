'''
Play with different n values and see how the distribution changes with the greater ones.
Is the shape more symmetric?
'''

import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

def compare_binomial_distributions(n_values=[10, 20, 50, 100], p=0.5, trials=10000):
    plt.figure(figsize=(12, 8))

    for i, n in enumerate(n_values, 1):
        data = np.random.binomial(n=n, p=p, size=trials)
        counts = Counter(data)
        xs = sorted(counts.keys())
        ys = [counts[x] / trials for x in xs]

        plt.subplot(2, 2, i)
        plt.bar(xs, ys, width=0.8, color='cornflowerblue', edgecolor='black')
        plt.title(f'n={n}, p={p}')
        plt.xlabel('Number of Heads')
        plt.ylabel('Relative Frequency')
        plt.xticks(np.linspace(0, n, min(n + 1, 11), dtype=int))
        plt.grid(axis='y', linestyle='--', alpha=0.6)

    plt.tight_layout()
    plt.show()

compare_binomial_distributions()