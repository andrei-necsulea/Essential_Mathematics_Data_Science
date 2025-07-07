'''
If y = √x, find the increment Δy at x=0.75 for Δx=0.01.
'''

import math

x1 = 0.75
delta_x = 0.01

def y(x):
    return math.sqrt(x)

y1 = y(x1 + 0)
#y2 = y(x1 + delta_x)

delta_y1 = y(x1 + delta_x) - y(x1)
print(delta_y1)