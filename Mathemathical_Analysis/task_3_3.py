'''
Using SymPy library, find the derivative of a function f:

    f1(x)=−3x^2+x−3
    f2(x)=sin(x)
    f3(x)=−cos(x^3)
'''

import sympy as sp

x = sp.Symbol("x")

#derivative of function f1
f1 = -3*(x**2) + x - 3
deriv_f1 = sp.diff(f1,x)

#derivative of function f2
f2 = sp.sin(x)
deriv_f2 = sp.diff(f2, x)

#derivative of function f3
f3 = -sp.cos(x**3)
deriv_f3 = sp.diff(f3,  x)

f_deriv = {
    f1 : deriv_f1,
    f2 : deriv_f2,
    f3 : deriv_f3
}

for i , (f , deriv) in enumerate(f_deriv.items() , start=1):
    print(f"\nFunction f{i} : {f}")
    print(f"Derivative : {deriv}")