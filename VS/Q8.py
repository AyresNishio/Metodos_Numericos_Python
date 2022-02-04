import numpy as np


def func(x):
    y=1/x
    return y


def metodo_13Simpson(a,b,r):
    m=2*r
    h=(b-a)/(m)
    n_pontos =m+1
    x = np.zeros(n_pontos)
    y = np.zeros(n_pontos)

    for i in range (n_pontos):
        x[i]=i*h+a
        y[i]=func(x[i])

    I_13SR= y[0]
    coef=4
    print(y)
    for i in range(1,m):
        I_13SR = I_13SR +  coef*y[i]
        print(coef,y[i])
        if(coef==4): coef = 2
        else: coef = 4

    I_13SR = I_13SR + y[m]
    I_13SR = I_13SR*(h/3)

    return I_13SR

if __name__ == "__main__":
    #exemplo 8.3
    
    

    area_da_curva= metodo_13Simpson(1,9, 2)

    area_da_curva = area_da_curva + np.log(1)

    print(area_da_curva)

    
