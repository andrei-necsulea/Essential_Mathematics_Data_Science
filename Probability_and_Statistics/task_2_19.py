'''
Split Iris data into two and
test whether both such samples origin from the same distribution.
'''

from sklearn.datasets import load_iris
import pandas as pd
from scipy.stats import ks_2samp

# Load Iris data
data = load_iris()
df = pd.DataFrame(data.data, columns=data.feature_names)

# Shuffle the data before splitting
df_shuffled = df.sample(frac=1, random_state=42).reset_index(drop=True)

# Split into two halves
half = len(df_shuffled) // 2
sample_1 = df_shuffled.iloc[:half]
sample_2 = df_shuffled.iloc[half:]

# Perform Kolmogorov–Smirnov test for each feature
print("Kolmogorov–Smirnov test results (for each feature):")
for col in df.columns:
    stat, p = ks_2samp(sample_1[col], sample_2[col])
    print(f"{col}: statistic = {stat:.4f}, p-value = {p:.4f}")

import matplotlib.pyplot as plt
import seaborn as sns

feature = "petal length (cm)"
plt.figure(figsize=(8, 5))
sns.kdeplot(sample_1[feature], label='Sample 1')
sns.kdeplot(sample_2[feature], label='Sample 2')
plt.title(f"Distribution of '{feature}' in both samples")
plt.legend()
plt.tight_layout()
plt.show()