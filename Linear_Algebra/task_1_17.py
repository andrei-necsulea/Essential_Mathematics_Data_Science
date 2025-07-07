'''
Create the following 4x4 matrix 4x4, and then:

    print out an element from the second row and the third column (starting from 1),
    check which element is equal to 0,
    with array indexing:
        display element equal to 3,
        view vector [3, 11, 0],
    calculate its:
        determinant,
        trace (sum of diagonal entries),
        the maximum and mininum elements,
        the mean value of each column,
        the maximum value of each row,
    find its inverse and multiply both matrices mathematically, ie. get the product of A⋅AT,
    determine its eigenvalues and eigenvectors.
'''

import numpy as np

matrix_1 = np.array([
    [1, 15, 4, 13],
    [8, 21, 3, 12],
    [11, 13, 11, 5],
    [32, 13, 0, 2]
])

print(f"\nElement from second row, third column : {matrix_1[1,2]}")
print(f"Index of elements equal to 0 are : {np.where(matrix_1 == 0)}")
print(f"Elements equal to 3 are : {np.where(matrix_1 == 3)}")
print(f"Printing of [3, 11, 0] ,line 2, col 3 is : {matrix_1[1:,2]}")
print(f"det(matrix_1) = {np.linalg.det(matrix_1)}")
print(f"Trace(matrix_1) = {np.linalg.trace(matrix_1)}")
print(f"Max is : {matrix_1.max()}")
print(f"Min is : {matrix_1.min()}")
print(f"Mean is : {matrix_1.mean(axis=0)}")
print(f"Max is : {matrix_1.max(axis=1)}")
print(f"Inverse of matrix is : \n{np.linalg.inv(matrix_1)}")
print(f"Product of matrix_1 and inverse of it is (should be identity) : \n{np.linalg.matmul(matrix_1,np.linalg.inv(matrix_1))}")
print(f"Product of matrix_1 and its transpose is : \n{np.linalg.matmul(matrix_1,np.linalg.matrix_transpose(matrix_1))}")
eigenvalues, eigenvectors = np.linalg.eig(matrix_1)
print(f"Eigenvalues are : {eigenvalues}")
print(f"Eigenvectors are : \n{eigenvectors}")