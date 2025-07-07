'''
Consider petal length of Iris setosa.
Plot a histogram and test whether samples origin from a normal distribution.
'''

from sklearn.datasets import load_iris
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Load dataset
data = load_iris()
df = pd.DataFrame(data.data, columns=data.feature_names)
df['target'] = data.target
df['species'] = df['target'].map(dict(zip(range(3), data.target_names)))

# Filter setosa samples
setosa = df[df['species'] == 'setosa']
petal_length = setosa['petal length (cm)']

plt.figure(figsize=(8, 5))
sns.histplot(petal_length, bins=10, kde=True, color='skyblue', edgecolor='black')
plt.title('Histogram of Petal Lengths – Iris Setosa')
plt.xlabel('Petal Length (cm)')
plt.ylabel('Frequency')
plt.grid(True)
plt.tight_layout()
plt.show()

# Shapiro–Wilk test
shapiro_stat, shapiro_p = stats.shapiro(petal_length)
print(f"Shapiro-Wilk test: statistic = {shapiro_stat:.4f}, p-value = {shapiro_p:.4f}")

# D'Agostino and Pearson test
normaltest_stat, normaltest_p = stats.normaltest(petal_length)
print(f"Normaltest (D'Agostino): statistic = {normaltest_stat:.4f}, p-value = {normaltest_p:.4f}")

import scipy.stats as stats

plt.figure(figsize=(6, 6))
stats.probplot(petal_length, dist="norm", plot=plt)
plt.title("Q-Q Plot – Petal Length (Iris Setosa)")
plt.grid(True)
plt.tight_layout()
plt.show()