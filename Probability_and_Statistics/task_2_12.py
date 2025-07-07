'''
Perform the similiar analysis (see Task 2.11) with the standard normal distribution.
'''

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import norm

def visualize_standard_normal(n_values=[10, 100, 1000, 10000]):
    for n in n_values:
        data = norm.rvs(loc=0, scale=1, size=n)  # standard normal

        x = np.linspace(-4, 4, 1000)
        y = norm.pdf(x, loc=0, scale=1)

        plt.figure(figsize=(10, 5))
        sns.histplot(data, kde=True, stat='density', bins=30, color='skyblue', edgecolor='black', label="Sampled + KDE")

        plt.plot(x, y, 'r-', lw=2, label='Theoretical PDF')
        plt.title(f"Standard Normal Distribution N(0,1) with n = {n}")
        plt.xlabel("Value")
        plt.ylabel("Density")
        plt.legend()
        plt.grid(alpha=0.3)
        plt.tight_layout()
        plt.show()

visualize_standard_normal()