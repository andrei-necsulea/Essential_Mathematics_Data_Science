'''
For the following vectors a=[0, 3] and b=[2, 2],
determine their scalar product and the angle between these vectors.
Correct answer α=45∘.
'''

import numpy as np

a = np.array([0 , 3])
b = np.array([2 , 2])

print(f"\nScalar product of a and b is : {np.dot(a, b)}")

scalar_product = np.dot(a, b)

norm_a = np.linalg.norm(a)
norm_b = np.linalg.norm(b)

cos_angle = scalar_product / (norm_a * norm_b)

angle_in_radians = np.arccos(cos_angle)

angle_in_degrees = np.degrees(angle_in_radians)

print(f"The angle between these vectors is : {angle_in_degrees}")