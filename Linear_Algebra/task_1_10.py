'''
Define two 3x3 real matrices, ie. whose elements consist entirely of real numbers.
For the first matrix, draw the numbers from standard normal (Gaussian)
distribution, ie. μ=0 and σ=1.

For the second one,
set the standard devation to 1 and mean value to 5.

Next, for each of them:

    multiply all elements by a scalar 10,
    extract the element in the middle,

    Possible formula :

    def extract_middle(matrix):
        rows, cols = matrix.shape
        return matrix[rows // 2, cols // 2]

    *** sau putem lua diagonala principala si gasim mijlocul ca find (len+1)/2

    transpose them
    get its trace & sum of all elements

and calculate their:

    sum
    difference
    element-wise multiplication result
    element-wise division result
    matrix product (matrix multiplication)

'''

import numpy as np

#This written lines are the same for the firs matrix creation:

'''
For the first matrix, draw the numbers from standard normal (Gaussian)
distribution, ie. μ=0 and σ=1.
'''

#matrix_1 = np.random.normal(loc = 0, scale = 1, size = (3,3))
#matrix_1 = np.random.randn(3, 3)
matrix_1 = np.random.standard_normal((3,3))

print(matrix_1)

'''
For the second one,
set the standard devation to 1 and mean value to 5.
'''

#loc = media
#scale = deviatia standard

matrix_2 = np.random.normal(loc = 5 , scale = 1, size = (3,3))

print("\n")
print(matrix_2)

print("\n\n\n")

print("Operations for matrix_1 : (order from requirement)")
print("__________________________________________________________")
print("\n")

print(matrix_1 * 10)
print("\n")
print(matrix_1[1,1])
print("\n")
print(matrix_1.transpose())
print("\n")
print(matrix_1.trace())
print("\n")
print(matrix_1.sum())



print("\n")
print("__________________________________________________________")

print("\n\n\n")

print("Operations for matrix_2 : (order from requirement)")
print("__________________________________________________________")
print("\n")

print(matrix_2 * 10)
print("\n")
print(matrix_2[1,1])
print("\n")
print(matrix_2.transpose())
print("\n")
print(matrix_2.trace())
print("\n")
print(matrix_2.sum())

print("\n")
print("__________________________________________________________")



print("\n\n\n")



print("Operations with matrix_1 and matrix_2 : (order from requirement)")
print("__________________________________________________________")
print("\n")

print(matrix_1 + matrix_2)
print("\n")
print(matrix_1 - matrix_2)
print("\n")
print(matrix_1 * matrix_2)
print("\n")
print(matrix_1 / matrix_2)
print("\n")
print(np.linalg.matmul(matrix_1 , matrix_2))

print("\n")
print("__________________________________________________________")
print("\n")