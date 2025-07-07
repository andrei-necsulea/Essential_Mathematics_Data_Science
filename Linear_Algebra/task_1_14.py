'''
Create an array with the following elements:
[23, 45, 124, 112, 150, 43, 25, 17, 268, 254, 95, 97, 8]
and filter out the ones that are less than or equal to their mean value.
How many such numbers are there?
'''

import numpy as np

arr = np.array([23, 45, 124, 112, 150, 43, 25, 17, 268, 254, 95, 97, 8] )

print(arr[arr <= arr.mean()])