'''
If y = 2x^3−x^2, find the increment Δy at x=5 for Δx=0.01.
'''

import sympy as sp

x = sp.Symbol('x')

x1 = 5
delta_x = 0.01

y = 2*(x**3) - x**2

delta_y = y.subs(x , x1)

print(f"Exact Δy (sympy): {delta_y}")
print(f"Approximate value: {float(delta_y):.5f}")