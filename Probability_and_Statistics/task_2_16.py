'''
Use the following code to download the Iris dataset (classification):

from sklearn.datasets import load_iris

data = load_iris()

X = data.data[:, :2]
y = data.target

This data set consists of 3 different types of irises’ (Setosa, Versicolour, and Virginica), stored in a 150x4 np.ndarray().

The rows being the samples and the columns being: Sepal Length, Sepal Width, Petal Length and Petal Width.

See more Iris flower data set.

    Plot a histogram of the petal lengths of Iris versicolor.
    For each column, compute basic descriptive statistics. Include 10th and 90th percentile.
    Plot a boxplot of the sepal width of Iris grouped by their type.
'''

from sklearn.datasets import load_iris
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Load dataset
data = load_iris()
df = pd.DataFrame(data.data, columns=data.feature_names)
df['target'] = data.target
df['species'] = df['target'].map(dict(zip(range(3), data.target_names)))

# Filter versicolor
versicolor = df[df['species'] == 'versicolor']

# Histogram of petal length
plt.figure(figsize=(8, 5))
plt.hist(versicolor['petal length (cm)'], bins=15, color='purple', edgecolor='black')
plt.title('Histogram of Petal Lengths - Iris Versicolor')
plt.xlabel('Petal Length (cm)')
plt.ylabel('Frequency')
plt.grid(True)
plt.tight_layout()
plt.show()

desc_stats = df.drop(columns=['target', 'species']).describe().T

# Add 10th and 90th percentiles
#first 10% of values
desc_stats['10%'] = df.drop(columns=['target', 'species']).quantile(0.10)
#last 10% of values
desc_stats['90%'] = df.drop(columns=['target', 'species']).quantile(0.90)

print(desc_stats)

plt.figure(figsize=(8, 5))
sns.boxplot(x='species', y='sepal width (cm)', data=df, palette='Set2')
plt.title('Boxplot of Sepal Width by Iris Species')
plt.xlabel('Species')
plt.ylabel('Sepal Width (cm)')
plt.grid(True)
plt.tight_layout()
plt.show()