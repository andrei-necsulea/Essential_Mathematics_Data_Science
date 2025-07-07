'''
Create an array with 10 random naturals from left-closed but right-open interval:
[10,30), ie. 10 ≤ x < 30.
'''

import numpy as np

arr = np.random.randint(10, 30, size = 10)

print(arr)