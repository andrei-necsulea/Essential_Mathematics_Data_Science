'''
Solve the system of equations in three variables:

2x1+x2−2x3=−1
3x1−3x2−x3=5
x1−2x2+3x3=6

Correct answer:
x=(x1,x2,x3)=(−1,1,1).
'''

import numpy as np

A = np.array([[2, 1, -2] , [3, -3, -1] , [1, -2, 3]])
b = np.array([-1, 5, 6])

print(f"System solution is : {np.linalg.solve(A, b)}")