'''
Play with different p values and see how the distribution changes.
Is the shape more skewed?
'''

import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

def compare_p_values(n=20, p_values=[0.1, 0.3, 0.5, 0.8], trials=10000):
    plt.figure(figsize=(12, 8))

    for i, p in enumerate(p_values, 1):
        data = np.random.binomial(n=n, p=p, size=trials)
        counts = Counter(data)
        xs = sorted(counts.keys())
        ys = [counts[x]/trials for x in xs]

        plt.subplot(2, 2, i)
        plt.bar(xs, ys, width=0.8, color='mediumseagreen', edgecolor='black')
        plt.title(f'p={p}, n={n}')
        plt.xlabel('Number of Heads')
        plt.ylabel('Relative Frequency')
        plt.grid(axis='y', linestyle='--', alpha=0.6)

    plt.tight_layout()
    plt.show()

compare_p_values()