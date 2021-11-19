import numpy as np

def f(x):
    # f = x**6 - x -1
    # f = x**3 - 9*x + 3 
    #h = np.cos(x) - 3 + np.exp(x) 
    y=x**3 - 2*x -5
    #y = (1/x)*np.exp(1) - (x**2)*np.exp(-x)  -
    return y


#Método da Bisseção
#q5
# a=0.0
# b=5
# tol = 0.0005
#q2




x = (a+b)/2

iter=0

while abs(f(x)) > tol:

    print(f"Iteração {iter}\n")
    print(f"a = {a}\n")
    print(f"b = {b}\n")
    print(f"x = {x}\n")
    print(f"f(x) = {f(x)}\n")
    print(f'------------------')
    if f(a)*f(x)<0:
        a=a
        b=x
    elif f(x)*f(b)<0:
        a=x
        b=b
    
    x = (a+b)/2

    iter += 1

print(f"A raiz da função é : {x}")
print(f"Total de iterações = {iter}")