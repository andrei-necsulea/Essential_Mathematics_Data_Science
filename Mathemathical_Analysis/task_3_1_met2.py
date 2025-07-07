import sympy as sp

x = sp.Symbol('x')
x1 = 0.75
delta_x = 0.01

# y(x) = sqrt(x)
y = sp.sqrt(x)

# Δy = y(x1 + Δx) - y(x1)
delta_y = y.subs(x, x1 + delta_x) - y.subs(x, x1)
print(f"Exact Δy (sympy): {delta_y}")
print(f"Approximate value: {float(delta_y):.5f}")
