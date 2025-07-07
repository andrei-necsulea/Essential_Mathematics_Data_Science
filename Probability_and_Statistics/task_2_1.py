'''
Load data from brain_size.csv file and determine the basic descriptive statistics using Pandas library.
Plot a histogram for selected columns (hint pandas has built-in methods .hist())
'''

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('brain_size.csv' , sep=';')
df.replace(".", pd.NA, inplace=True)
df = df.dropna()

numeric_columns = list(df.columns[2:8])

#figsize = (width_in_inch = 1500 pixels, height_in_inch = 800 pixels)
plt.figure(figsize=(15,8))

for i, column in enumerate(numeric_columns, start=1):
    #plt.subplot(number_of_rows, mumber_of_columns, index_of_subplot)
    plt.subplot(2, 3, i)
    plt.hist(df[column].astype(float))
    plt.title(column)

plt.tight_layout()
plt.show()