'''
Create an array with the following elements: [23, 45, 112, 150, 43, 254, 95, 8]
and then filter out the ones greater than 100.
'''

import numpy as np

arr = np.array([23, 45, 112, 150, 43, 254, 95, 8])

print(arr[arr > 100])