'''
Using scipy.stats calculate kurtosis and skewness
for numeric columns from the same file (see task 2.1).

skewness = assymetry of distribution
kurtosis = concentration of values in relation with mean value

'''

import pandas as pd
import scipy.stats as scst

df = pd.read_csv("brain_size.csv" , sep=";")
df.replace(".", pd.NA, inplace=True)
df = df.dropna()

numeric_columns = list(df.columns[2:8])

kurtosis_on_numeric_columns = [scst.kurtosis(df[col].astype(float)) for col in numeric_columns]
skewness_on_numeric_columns = [scst.skew(df[col].astype(float)) for col in numeric_columns]

print("\n")

for col, k, s in zip(numeric_columns, kurtosis_on_numeric_columns, skewness_on_numeric_columns):
    print(f"{col}: kurtosis = {k:.4f}, skewness = {s:.4f}")