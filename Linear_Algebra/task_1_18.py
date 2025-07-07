'''
Create a 3x3 array and normalize its columns,
ie. scale the values such that sum of each column equals 1 (unit vectors).
'''

import numpy as np

matrix = np.array([
    [1, 3, 5],
    [2, 4, 6],
    [7, 8, 9]
])

column_sums = matrix.sum(axis=0)

normalized_matrix = matrix / column_sums

print("Original matrix:")
print(matrix)

print("\nNormalized matrix (columns sum to 1):")
print(normalized_matrix)

print("\nSum of each column:")
print(normalized_matrix.sum(axis=0))