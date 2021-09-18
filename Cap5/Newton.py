#Met. Newton
import numpy as np

#Entrar com as equacoes
def func(x):
    f1 = 5*x[0] - 2*(x[1]**3) + 113
    f2 = 2*(x[0]**3) + 4*(x[1]**2) - 118
    y = np.array([f1,f2])
    return y

def diff_func(x,num_eq):
    
    H = np.zeros((num_eq,num_eq))
    H[0,0] = 5  
    H[0,1] =  -6*(x[1]**2) 
    H[1,0] = 6*(x[0]**2)
    H[1,1] = 8*(x[1]) 

    return H

def newton(num_eq,x0,tol,delta_max,x,k,k_max,delta_x):

    while (delta_max>tol) and (k<k_max):
        #Matriz H
        print("----x----")
        print(x)
        H = diff_func(x,num_eq)
        print("----H(x)----")
        print(H)
        #Vetor h(x)
        print("----h(x)----")
        h=func(x)
        print(h)
        #Solve Lin. System
        delta_x= np.linalg.inv(H)@np.transpose(-h)
        print("----Delta_x----")
        print(delta_x)
        #Determina o desvio maxima
        delta_max=max(abs(delta_x))
        #Iteração Atual
        print(f"Iteracao atual = {k}")
        x= x + delta_x
        k=k+1
    return x

def newton_modif(num_eq,x0,tol,delta_max,x,k,k_max,delta_x):

    #Newton Modificado
    #Matriz H Fixa
    H = diff_func(x,num_eq) # constante
    H_inv = np.linalg.inv(H)
    while (delta_max>tol and k<k_max):
        print("----x----")
        print(x)
        # Vetor h(x)
        print("----h(x)----")
        h=func(x)
        print(h)
        #Solve Lin. System
        delta_x= H_inv@np.transpose(-h)
        print("----Delta_x----")
        print(delta_x)
        #Determina o desvio maxima
        delta_max=max(abs(delta_x))
        #Iteração Atual
        print(f"Iteracao atual = {k}")
        x= x + delta_x
        k=k+1
    return x
    


if __name__ == '__main__':
    #Inicializacao
    x0= np.array([2.5,5]) #para convergirem os dois métodos
    tol = 5e-3
    delta_max= np.Infinity
    x=x0
    k=0
    k_max=40
    num_eq = 2
    #select_method=input('Digite 1 para Método de Newton e 2 para Método de Newton Modificado')
    delta_x=0
    x_newton = newton(num_eq,x0,tol,delta_max,x,k,k_max,delta_x)
    x_newton_modif = newton_modif(num_eq,x0,tol,delta_max,x,k,k_max,delta_x)
    print("------Newton----\n")
    print(x_newton)
    print("------Newton Modificado----\n")
    print(x_newton_modif)