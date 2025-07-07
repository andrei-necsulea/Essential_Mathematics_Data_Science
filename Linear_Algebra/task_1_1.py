'''
Create a NumPy array with consecutive values from 1 to 9.
Display and then invert this array (first element becomes last, etc.).
Do the same for the numbers between 7 and 19 (including these numbers).
'''

import numpy as np

arr = np.arange(1,10)

print(f"Array no. 1 is : {arr}\n")
print(f"Inverted array no. 1 is : {arr[::-1]}\n")

arr1 = np.arange(1,20)
print(f"Array no. 2 is : {arr1}\n")
print(f"Inverted array no. 2 for interval [7,19] is : {arr1[20:5:-1]}")