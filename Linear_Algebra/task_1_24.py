'''
Check whether the system solution exists:

x1−3x2+x3=4
−x1+2x2−5x3=3
5x1−13x2+13x3=8.

Correct answer: no, it does not.

Hint: matrix is not full-rank, i.e rank(A)=2≠3.
'''

import numpy as np

A = np.array([[1, -3, 3], [-1, 2, -5], [5, -13, 13]])
b = np.array([4, 3, 8])

print(f"rank(A) = {np.linalg.matrix_rank(A)}")
assert np.allclose(np.linalg.matrix_rank(A) , 2), "Not correct solution!"