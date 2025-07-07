'''
Select Iris setosa and test whether the mean petal width can origin
from the population with mean petal width:

    0.1,
    0.2,
    0.25,
    1.2.

'''

from sklearn.datasets import load_iris
import pandas as pd
from scipy.stats import ttest_1samp

# Load Iris dataset
data = load_iris()
df = pd.DataFrame(data.data, columns=data.feature_names)
df["species"] = pd.Categorical.from_codes(data.target, data.target_names)

# Filter only Iris setosa
setosa = df[df["species"] == "setosa"]
petal_width = setosa["petal width (cm)"]

# Hypothesized means
hypothesized_means = [0.1, 0.2, 0.25, 1.2]

# Perform one-sample t-tests
print("Testing mean of Setosa's petal width against hypothesized values:\n")
for mu in hypothesized_means:
    t_stat, p_value = ttest_1samp(petal_width, mu)
    print(f"H0: mean = {mu:.2f} → t = {t_stat:.4f}, p = {p_value:.4f}")