'''
Determine the length of the following vectors using Euclidean norm:

    v1=[0,5]
    v2=[0,−3]
    v3=[7,0]
    v4=[−π,0]
    v5=[3,−4]
    v6=[1,7]
    v7=[5√3,−3,4]
    v8=[1,2,3,4]

Hint: using default parameters of numpy.linalg.norm() function will return Frobenius norm for matrices which is equivalent to Euclidean norm for vectors: https://numpy.org/doc/stable/reference/generated/numpy.linalg.norm.html
'''

import math
import numpy as np

v1=np.array([0,5])
v2=np.array([0,-3])
v3=np.array([7,0])
v4=np.array([-math.pi,0])
v5=np.array([3,-4])
v6=np.array([1,7])
v7=np.array([5*math.sqrt(3),-3,4])
v8=np.array([1,2,3,4])

vectors = [v1, v2, v3, v4, v5, v6, v7, v8]

print("\n")

for i in range(len(vectors)):
        print(f"Length (using Euclidean norm) of v{i+1} is : {np.linalg.norm(vectors[i])}")