'''
Select Iris versicolour, and virginica.
Test whether the mean sepal width are the same.
'''

from sklearn.datasets import load_iris
import pandas as pd
from scipy.stats import ttest_ind

# Load Iris dataset
data = load_iris()
df = pd.DataFrame(data.data, columns=data.feature_names)
df["species"] = pd.Categorical.from_codes(data.target, data.target_names)

# Select only versicolor and virginica
versicolor = df[df["species"] == "versicolor"]["sepal width (cm)"]
virginica = df[df["species"] == "virginica"]["sepal width (cm)"]

# Perform independent two-sample t-test
t_stat, p_value = ttest_ind(versicolor, virginica, equal_var=False)  # Welch's t-test

# Print results
print("Two-sample t-test (sepal width):")
print(f"t = {t_stat:.4f}, p = {p_value:.4f}")

# Optional: Show means
print(f"\nMean (versicolor): {versicolor.mean():.4f}")
print(f"Mean (virginica):  {virginica.mean():.4f}")