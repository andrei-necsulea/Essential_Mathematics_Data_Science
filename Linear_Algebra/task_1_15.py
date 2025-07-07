'''
Use the array defined above to evaluate mean value and standard deviation.
Check how many of these numbers is within a distance of at most one standard deviation from the mean,
ie. belongs to the closed interval [mean - std, mean + std].
'''

import numpy as np

arr = np.array([23, 45, 124, 112, 150, 43, 25, 17, 268, 254, 95, 97, 8])

arr_mean = arr.mean()
arr_std = arr.std()

left = arr_mean - arr_std
right = arr_mean + arr_std

filtering = (arr >= left) & (arr <= right)

print(arr[filtering])
print(arr[filtering].size)