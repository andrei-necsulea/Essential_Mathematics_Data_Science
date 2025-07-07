'''
Find eigenvalues and eigenvectors associated with them for the following matrices:

    A1 = [−5 2
          -7 4]

    A2 = [1 0
          0 −3]

    A3 = [5 -10 -5
          2  14  2
         -4  -8  6]

    A4 = [1 -1  2
          1  0  1
          1  1  2]

Solutions can be complex numbers, z∈C, as for A4.
'''

import numpy as np


A1 = np.array([ [-5, 2] , [-7, 4] ])
A2 = np.array([ [1, 0] , [0, -3] ])
A3 = np.array([ [5, 10, -5] , [2, 14, 2] , [-4, -8, 6] ])
A4 = np.array([ [1, -1, 2] , [1, 0, 1] , [1, 1, 2] ])

vector_of_matrix = [A1, A2, A3, A4]

def find_eigenvalues_eigenvectors(matrix):
    eigenvalues, eigenvectors = np.linalg.eig(matrix)
    #print(f"Eigen values are : {eigenvalues}" , f"\nEigen vectors are : \n{eigenvectors}\n\n")
    print("Eigenvalues:")
    for i, val in enumerate(eigenvalues):
        print(f"  λ{i + 1} = {val}")
    print("Eigenvectors (each column corresponds to an eigenvalue):")
    print(eigenvectors)
    print("\n" + "-" * 50 + "\n")

print("\n")

for i , matrix in enumerate(vector_of_matrix, start=1):
    print(f"Matrix A{i} :")
    find_eigenvalues_eigenvectors(matrix)