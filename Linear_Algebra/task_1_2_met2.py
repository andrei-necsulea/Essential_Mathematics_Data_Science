'''
Create the following NumPy array: np.array([1, 23, 4, 31, 1, 1, 4, 23, 4, 1]);
and then list all unique (non-repeating) elements.
Perform similar task with the following NumPy array np.array([44, 1, 7, 12, 7, 44, 4, 7, 12, 1])
and then for each unique value, print out the value itself and the number of its occurences.
'''

import numpy as np
from collections import Counter

def list_unique_non_repeating(arr):
    print("Unique elements :")
    counts = Counter(arr)
    for val, cnt in counts.items():
        if cnt == 1:
            print(val, end=" ")
    print("\n")

def print_elements_with_counts(arr):
    print("Number of occurences for every element : ")
    counts = Counter(arr)
    for val, cnt in counts.items():
        if cnt == 1:
            print(f"Element {val} is unique.")
        else:
            print(f"Element {val} has {cnt} occurences.")
    print("\n")


arr1 = np.array([1, 23, 4, 31, 1, 1, 4, 23, 4, 1])
list_unique_non_repeating(arr1)

arr2 = np.array([44, 1, 7, 12, 7, 44, 4, 7, 12, 1])
print_elements_with_counts(arr2)