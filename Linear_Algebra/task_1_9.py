'''
Create a vector consisting of consecutive natural numbers: 6, 7, 8, ..., 35.
Change its shape in several ways.
'''

import numpy as np

arr = np.arange(6,35)

print(arr)
print("\n")
print(arr.reshape(-1)) #try to find automatically a possible reshape


#It appears that this array cannot be reshaped...Has size of 29.
#So, I am not able to do any reshaping...
#29 is a prime number, so it would not allow to do many things...
#Reshaping is related on how many divisors has the size of the array...
#So, the only possible solutions are:
#[ 6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29
# 30 31 32 33 34 35]

#However, if we have:
arr = np.arange(6,36)
#Size is not a prime number, so we can take all possible combinations of products
#Products of type line x column, 2 divisors per each multiplication
#So, all possible solutions are:

print("\n")
print(arr.reshape(5, 6))
print("\n")
print(arr.reshape(6, 5))
print("\n")
print(arr.reshape(2, 15))
print("\n")
print(arr.reshape(3, 10))