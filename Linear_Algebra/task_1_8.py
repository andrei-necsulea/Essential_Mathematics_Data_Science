'''
Print out all natural numbers less than 100 that are divisible by 11.
Try not to use any iteration over loop.
'''

import numpy as np

arr = np.arange(100)

print(arr[arr % 11 == 0])