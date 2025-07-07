'''
Visualize uniform distribution with the help
of a random number generator acting over an interval of numbers (5,12).
You can import uniform() function from scipy.stats package for that purpose.
Also, try using Seaborn package and distplot() function with kde=True.
Is the estimated denstity distribution similar to the theoretical one?
How does it change when the size=n varies? Check for n∈[10,100,1000,10000].
'''

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import uniform

def visualize_uniform_distribution(n_values=[10, 100, 1000, 10000], a=5, b=12):
    for n in n_values:
        data = uniform.rvs(loc=a, scale=b-a, size=n)
        x = np.linspace(a - 1, b + 1, 1000)
        y = uniform.pdf(x, loc=a, scale=b-a)

        plt.figure(figsize=(10, 5))
        sns.histplot(data, kde=True, stat='density', bins=30, color='skyblue', edgecolor='black', label="Sampled + KDE")

        plt.plot(x, y, 'r-', lw=2, label='Theoretical PDF')
        plt.title(f"Uniform Distribution U({a}, {b}) with n = {n}")
        plt.xlabel("Value")
        plt.ylabel("Density")
        plt.legend()
        plt.grid(alpha=0.3)
        plt.tight_layout()
        plt.show()

visualize_uniform_distribution()