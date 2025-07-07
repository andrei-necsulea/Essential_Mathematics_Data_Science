'''
Using SymPy library, find the partial derivative of a function f:

    f1(x,y)=x^2+y^2
    f2(x)=sin(x)
    f3(x)=−cos(x*y)+x^2
'''

import sympy as sp

x , y = sp.symbols("x y")

#derivative of function f1
f1 = x**2 + y**2
deriv_x_f1 = sp.diff(f1,x)
deriv_y_f1 = sp.diff(f1 , y)

#derivative of function f2
f2 = sp.sin(x)
deriv_x_f2 = sp.diff(f2, x)
deriv_y_f2 = sp.diff(f2, y)

#derivative of function f3
f3 = -sp.cos(x*y) + x**2
deriv_x_f3 = sp.diff(f3,  x)
deriv_y_f3 = sp.diff(f3, y)

f_deriv = {
    f1 : (deriv_x_f1, deriv_y_f1),
    f2 : (deriv_x_f2, deriv_y_f2),
    f3 : (deriv_x_f3, deriv_y_f3)
}

for i , (f , deriv) in enumerate(f_deriv.items() , start=1):
    print(f"\nFunction f{i} : {f}")
    print(f"Derivative with respect to x : {deriv[0]}")
    print(f"Derivative with respect to y : {deriv[1]}")