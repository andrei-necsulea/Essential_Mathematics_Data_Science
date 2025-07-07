'''
From the array of values: [23, 45, 112, 150, 43, 254, 95, 8]
filter for those that are greater than 100.
'''

import numpy as np

arr = np.array([23, 45, 112, 150, 43, 254, 95, 8])

print(arr[arr > 100])