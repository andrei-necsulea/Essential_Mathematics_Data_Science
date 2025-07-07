'''
Normalize each vector from Task 25.
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

#z-score normalization
def z_score_normalization(v):
    return (v - v.mean())/v.std()

#min-max normalization
def min_max_normalization(v):
    return ( v - v.min() )/( v.max() - v.min() )

#unit_length nomalization
def unit_length_normalization(v):
    if np.linalg.norm(v) != 0:
        return v / np.linalg.norm(v)
    else:
        return v

print("\n")
for i in range(len(vectors)):
        print(f"Z-score Normalized v{i+1} is : {z_score_normalization(vectors[i])}")
print("\n")


print("\n")
for i in range(len(vectors)):
        print(f"Min-Max Normalized v{i+1} is : {min_max_normalization(vectors[i])}")
print("\n")


print("\n")
for i in range(len(vectors)):
        print(f"Unit_length Normalized v{i+1} is : {unit_length_normalization(vectors[i])}")
print("\n")