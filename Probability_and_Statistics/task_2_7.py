'''
Suppose we have n∈N1 independent random variables X1,X2,...,Xn,
and each of them has a Bernoulli distribution with parameter
p∈[0,1]. If X=X1+X2+...+Xn, then X has the binomial distribution
with parameters n and p, ie. X∼Bin(n,p).

An outcome of tossing a coin can be desribed
by a disrete random variable with a Bernoulli distribution with parameter
p=12 as we see in EX. 2.1.
Perform an experiment to know the number of trials with exactly x heads (H).

Write a function that allows for such simulations and accepts
n=10 and p=1/2 as an input and outputs a plot showing the results.
'''

import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

def simulate_binomial_experiment(n=10, p=0.5, trials=10000):
    experiments = np.random.binomial(n=n, p=p, size=trials)

    frequency = Counter(experiments)

    xs = sorted(frequency.keys())
    ys = [frequency[x] for x in xs]

    plt.figure(figsize=(10, 6))
    plt.bar(xs, ys, width=0.7, color='skyblue', edgecolor='black')
    plt.xlabel('Number of Heads (H) in 10 Tosses')
    plt.ylabel('Frequency')
    plt.title(f'Binomial Distribution Simulation: n={n}, p={p}, trials={trials}')
    plt.xticks(range(n+1))
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

simulate_binomial_experiment(n=10, p=0.5)