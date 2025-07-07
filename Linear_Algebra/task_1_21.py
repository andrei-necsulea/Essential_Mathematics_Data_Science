'''
What is the solution to the system of equations below?
x1 − 2x2 + 3x3 = 9
−x1 + 3x2 − x3 = −6
2x1 − 5x2 + 5x3 = 17

Correct answer:
x=(x1,x2,x3)=(1,−1,2).
'''

import numpy as np

A = np.array([[1, -2, 3] , [-1, 3, -1], [2, -5, 5]])
b = np.array([9, -6, 17])

print(f"System solution is : {np.linalg.solve(A,b)}")