'''
Write a function get_sum_of_squared_naturals() that takes one argument as an input (call it max_value)
and returns the sum of all natural numbers such that k≤max_value.
Make sure that the input given by a user is a natural number. Set the default value to 5.
'''

import numpy as np

def get_sum_of_squared_naturals(max_value = 5):
    if not isinstance(max_value , int) or max_value < 1:
        raise ValueError("Input has to be a natural number!")
    return sum(np.arange(1, max_value + 1) ** 2)

input_value = int(input("Input a natural number : "))
print(get_sum_of_squared_naturals(input_value))