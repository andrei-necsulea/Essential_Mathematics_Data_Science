'''
Determine whether the triple x=(x1,x2,x3)=(3,−2,1) is a solution to the system:

x1+x2+x3=2
6x1−4x2+5x3=31
5x1+2x2+2x3=13.

Correct answer: yes, it is.
'''

import numpy as np

A = np.array([[1, 1, 1], [6, -4, 5], [5, 2, 2]])
b = np.array([2, 31, 13])

assert np.allclose( np.linalg.solve(A, b), (3., -2., 1.)), "This is not the solution of the system."
print("Correct solution!")