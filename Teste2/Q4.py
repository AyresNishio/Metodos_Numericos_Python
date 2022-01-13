import numpy as np


def func(x):
    y=x**2*np.log(x)
    return y

def d2func(x):
    y=2*np.log(x) + 3
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

def metodo_38Simpson(a,b,r):
    m=3*r
    h=(b-a)/m
    x = np.zeros(m+1)
    y = np.zeros(m+1)

    for i in range (m+1):
        x[i]=i*h+a
        y[i]=func(x[i])


    I_38SR= y[0]
    print(f'({y[0]}',end =" ")
    coef=3
    for i in range(1,m):
        if(i%3 == 0):coef = 2
        else: coef = 3
        I_38SR = I_38SR +  coef*y[i]
        print(f'+ {coef*y[i]}',end =" ")

    I_38SR = I_38SR + y[m]
    I_38SR = I_38SR*(h*3/8)
    print(f'+ {y[m]})*{h}*3/8')
    erro_38s = erro_38simpson(h,x,m)

    return I_38SR, erro_38s

def erro_38simpson(h,x,m):
    erro_38s = abs(-3*h**5*M4(x)/80*(m/3))
    return erro_38s


def M4(vec_x):
    vec_d4 = abs(d4func(vec_x))
    return max(vec_d4)

def d4func(x):
    y=-2/x**2
    return y


if __name__ == "__main__":
    #exemplo 8.3
    a=1
    b=1.5
    m=1
    ms=1
    I_tr , erro_tr   = metodo_trapezio(a,b,m)
    I_38s, erro_38s  = metodo_38Simpson(a,b,ms)

    print(I_tr , erro_tr)
    print(I_38s, erro_38s)