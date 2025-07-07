'''
Create the following NumPy array: np.array([1, 23, 4, 31, 1, 1, 4, 23, 4, 1]);
and then list all unique (non-repeating) elements.
Perform similar task with the following NumPy array np.array([44, 1, 7, 12, 7, 44, 4, 7, 12, 1])
and then for each unique value, print out the value itself and the number of its occurences.
'''

import numpy as np
from collections import Counter

def print_unique_elements_and_count_other_occurences(arr):
    arr = np.sort(arr)
    counts = Counter(arr)

    if arr[0] != arr[1]:
        print(f"Element {arr[0]} is unique.")

    for i in range(1, len(arr) - 1):
        if arr[i] != arr[i - 1] and arr[i] != arr[i + 1]:
            print(f"Element {arr[i]} is unique.")

    if arr[-1] != arr[-2]:
        print(f"Element {arr[-1]} is unique.")

    for element,occurence in counts.items():
        if occurence > 1:
            print(f"Element {element} has {occurence} occurences.")


arr1 = np.array([1, 23, 4, 31, 1, 1, 4, 23, 4, 1])
print_unique_elements_and_count_other_occurences(arr1)

print("\n")

arr2 = np.array([44, 1, 7, 12, 7, 44, 4, 7, 12, 1])
print_unique_elements_and_count_other_occurences(arr2)