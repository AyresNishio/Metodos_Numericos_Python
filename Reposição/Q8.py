import numpy as np


def func(x):
    y=1/(x+4)
    return y

def d2func(x):
    y=2*(x+4)**-3
    return y



def M2(vec_x):
    vec_d2 = d2func(vec_x)
    return max(vec_d2)




def metodo_trapezio(a,b,m):
    h=(b-a)/m
    x = np.zeros(m+1)
    y = np.zeros(m+1)
    for i in range (m+1):
        x[i]=i*h+a
        y[i]=func(x[i])

    #Trapezio
    I_TR= y[0]
    for i in range(1,m):
        I_TR = I_TR +  2*y[i]
    I_TR = I_TR + y[m]
    
    I_TR = I_TR*(h/2)

    erro_t = erro_trapezio(h,x,m)
    return I_TR, erro_t


def erro_trapezio(h,x,m):
    erro_t = abs(-m*h**3*M2(x)/12)
    return erro_t



if __name__ == '__main__':
    a = 0
    b = 2

    tol = 0.00001

    n_discret = 100
    x=a
    intervalo = np.linspace(a,b,num = n_discret)
    d_intervalo = d2func(intervalo)
    m2=max(d_intervalo)

    # //Número de subintervalos para que se atinja a tolerância especificada
    m=int(np.ceil(np.sqrt(((b-a)**3*m2)/(12*tol))))

    I_tr = metodo_trapezio(a,b,m)

    print(m, I_tr)