
import sympy as sym
import numpy as np

#y = (5-x*m.exp(0.5*x))/1.2
#y  = 5/(m.exp(0.5*x + 1.2))
#y = (5 - 1.2*x)/(m.exp(0.5*x))

print('Derivada Ex 3')
x = sym.symbols('x')
print(sym.diff(x*sym.exp(0.5*x)  + 1.2*x -5))

print('1')
print(sym.diff((5-x*sym.exp(0.5*x))/1.2))

print('2')
print(sym.diff(5/(sym.exp(0.5*x)+1.2)))

print('3')
print(sym.diff((5-1.2*x)/(sym.exp(0.5*x))))

# print('ex 3')
# x = sym.symbols('x')
# print('   df/dx:')
# print(sym.diff(2*x**3 +sym.ln(x)-5))