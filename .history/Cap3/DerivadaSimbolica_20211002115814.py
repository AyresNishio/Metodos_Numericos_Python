# Este programa tem como finalidade apresentar o uso da biblioteca sympy para obter derivadas simbólicas  

import sympy as sym
import numpy as np


print('Exemplo base, uma única variável')
print('f(x)= x**5')
x = sym.symbols('x')
print('df/dx')
print(sym.diff(x**5))
print('-----------------------------------')
###############Var Múltiplas############
print('Exemplo para múltiplas variaveis')
print('f(x)= x**5 + 2*y**2')
x,y = sym.symbols('x y')
print('df/dx')
print(sym.diff(x**5 + 2*y**2,x))
print('df/dy')
print(sym.diff(x**5 + 2*y**2,y))
print('-----------------------------------')
#################Regra do produto#############
print('Exemplo da Regra do Produto')
print('f(x)= (x**2+1) * cos(x)')
x = sym.symbols('x')
print('df/dx')
print(sym.diff((x**2+1) * sym.cos(x)))
print('-----------------------------------') 
################Regra da Cadeia#############
print('Exemplo da Regra da Cadeia')
print('f(x)= (x**2-3*x +5)**3')
x = sym.symbols('x')
print('df/dx')
print(sym.diff((x**2-3*x +5)**3))

print('-----------------------------------') 
#################Exemplo5.1#############
print('Exemplo 5.1')
print('f(x)= 5*x -2*y**3 +113')
x = sym.symbols('x')
y = sym.symbols('y')
print('df/dx:')

print(sym.diff(5*x -2*(y**3) +113,x))
print('df/dy:')
print(sym.diff(5*x -2*(y**3) +113,y))
print('f(x)= 2*(x**3) + 4*(y**2) - 118')

print('df/dx:')
print(sym.diff(2*(x**3) + 4*(y**2) - 118,x))
print('df/dy:')
print(sym.diff(2*(x**3) + 4*(y**2) - 118,y))

print('-----------------------------------') 
#################Exemplo5.1#############
print('Exemplo 8.3')
print('f(x)= e**((-x**2))')
x = sym.symbols('x')
print('df/dx:')
print(sym.diff(sym.diff(sym.exp((-x**2)),x)))
print('df2/dx:')
print(sym.diff(sym.diff(sym.diff(sym.diff(sym.exp((-x**2)),x)))))
#e**((-x**2))