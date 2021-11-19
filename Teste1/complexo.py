import sympy as sym
import numpy as np 

print('Exemplo para múltiplas variaveis')
a,b = sym.symbols('a b')
print('df1/da:')
print(sym.diff(a**3 - 3*a*b**2 -2*a-5 ,a))
print('df1/db:')
print(sym.diff(a**3 - 3*a*b**2 -2*a-5, b ))

print('df2/da:')
print(sym.diff(3*a**2 - b**3 -2*b ,a))
print('df2/db:')
print(sym.diff(3*a**2 - b**3 -2*b, b ))


x = sym.symbols('x')
print('df/da:')
print(sym.diff(1/x - x**2*sym.exp(-x),x))