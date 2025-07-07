'''
Use the following code to define 2D array, ie. matrix,
and then determine its dimension and number of elements.

A = np.array([[1, 2, 3, 4], [5, 6, -7, 1]])
'''

import numpy as np

A = np.array([[1, 2, 3, 4], [5, 6, -7, 1]])

print(f"Dimension of  A is {A.shape}.")
print(f"Matrix A has {A.shape[0]} lines and {A.shape[1]} columns.")
print(f"Matrix A has {A.shape[0]*A.shape[1]} elements (computed by formula lines x columns).")
print(f"Matrix A has {A.size} elements (computed with size keyword).")