'''
Plot the distribution of sepal length of Iris setosa and virginica,
grouping them by colors.
Test whether the samples were pulled from the same population.
'''

from sklearn.datasets import load_iris
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Load dataset
data = load_iris()
df = pd.DataFrame(data.data, columns=data.feature_names)
df["species"] = pd.Categorical.from_codes(data.target, data.target_names)

# Filter species
setosa = df[df["species"] == "setosa"]
virginica = df[df["species"] == "virginica"]

plt.figure(figsize=(8, 5))
sns.histplot(setosa["sepal length (cm)"], color="blue", label="Setosa", kde=True, stat="density")
sns.histplot(virginica["sepal length (cm)"], color="green", label="Virginica", kde=True, stat="density")
plt.title("Distribution of Sepal Length – Setosa vs Virginica")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Density")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

t_stat, t_p = stats.ttest_ind(setosa["sepal length (cm)"],
                               virginica["sepal length (cm)"],
                               equal_var=False)
print(f"T-test: statistic = {t_stat:.4f}, p-value = {t_p:.4e}")

u_stat, u_p = stats.mannwhitneyu(setosa["sepal length (cm)"],
                                 virginica["sepal length (cm)"],
                                 alternative='two-sided')
print(f"Mann–Whitney U test: statistic = {u_stat:.4f}, p-value = {u_p:.4e}")