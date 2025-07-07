'''
Create the 4x4 matrix below, then:
    display the item from the second row and the third column,
    calculate its determinant,
    calculate its trace (the sum of elements on the main diagonal),
    find the largest and smallest item.
'''

import numpy as np
from numpy import random

A = random.randint(100 , size=(4,4))
print(f"Random matrix is : \n {A} \n")

print(f"Item from the second row and the third column is {A[1,2]}.")
print(f"Det(A) = {np.linalg.det(A)}.")
print(f"Trace(A) = {np.linalg.trace(A)}.")
print(f"MIN(A) = {np.min(A)}.")
print(f"MAX(A) = {np.max(A)}.")