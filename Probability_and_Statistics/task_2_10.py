'''
Let n=10 and p=0.5 for Binomial distribution. Use the .pmf() to get random sample.

Next, use the .rvs() method to get a random sample of size n from a
Bernoulli distribution and then calculate its sum.
Repeat this sampling procedure s∈{10,100,1000,10000} times to have a sample of size s from the Binomial distribution:

sample = [bernoulli.rvs(p=p, size=n).sum() for i in range(s)]

Compare both distributions by plotting them.
Do they differ a lot? Does the difference change with consecutive p values increase?
'''

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom, bernoulli

def compare_binomial_sampling(n=10, p=0.5, sample_sizes=[10, 100, 1000, 10000]):
    for s in sample_sizes:
        #normal binomial distribution - theoretical
        x = np.arange(0, n+1)
        binomial_pmf = binom.pmf(x, n=n, p=p)

        #bernoulli distribution simulated by use of variables
        simulated_sample = [bernoulli.rvs(p=p, size=n).sum() for _ in range(s)]

        plt.figure(figsize=(10, 5))
        plt.hist(simulated_sample, bins=np.arange(-0.5, n+1.5, 1), density=True,
                 alpha=0.6, label=f'Simulated Binomial via Bernoulli (s={s})', color='skyblue', edgecolor='black')

        plt.plot(x, binomial_pmf, 'ro-', label='Theoretical Binomial PMF')
        plt.title(f'Binomial Distribution Comparison (n={n}, p={p}, s={s})')
        plt.xlabel('Number of Successes')
        plt.ylabel('Probability')
        plt.xticks(np.arange(0, n+1))
        plt.grid(axis='y', linestyle='--', alpha=0.5)
        plt.legend()
        plt.tight_layout()
        plt.show()

compare_binomial_sampling()