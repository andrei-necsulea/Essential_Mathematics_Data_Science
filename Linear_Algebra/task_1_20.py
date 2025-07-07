'''
Solve the system of equations mentioned above.

1*X1 + 2*X2 = 5
4*X1 + 5*X2 = 17

Correct answer:
x=(x1,x2)=(3,1).

Hint: There are functioned defined within NumPy package for both of these tasks; matrix inverse & mathematical multiplication of two matrices.
'''

import numpy as np

A = np.array([[1, 2] , [4, 5]])
b = np.array([5, 17])

solution = np.linalg.solve(A , b)
print(f"System solution is : {solution}")