import numpy as np





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

    return I_TR,

def func(x):
    y=x**2 - x -6
    return y


if __name__ == "__main__":
    #exemplo 8.3
    a=-2
    b=3
    m=5
    I_tr = metodo_trapezio(a,b,m)

    print(I_tr )