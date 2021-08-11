# Este programa tem como finalidade apreentar o uso da biblioteca sympy para obter derivadas simbólicas  

import sympy as sym

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
#################Regra da Cadeia#############
print('Exemplo da Regra da Cadeia')
print('f(x)= (x**2-3*x +5)**3')
x = sym.symbols('x')
print('df/dx')
print(sym.diff((x**2-3*x +5)**3))