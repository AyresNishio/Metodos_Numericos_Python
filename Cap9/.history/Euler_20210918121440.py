import numpy as np


def func(x,y):
    dy_dx = (1/2)*np.exp(x/3) - (1/2)*y #Exemplo 9.2
    return dy_dx

def euler(y0,x0,h,I):
    n =  (I[1] - I[0])/h
    for i in range(int(n)):
        yk = y0+ h*func(x0,y0)
        print(f"y{i+1} = {yk}")
        y0 = yk
        x0 = x0 + h
    return


if __name__ == '__main__':
    #Pvi
    y0= 3
    x0= 0
    #intervalo
    I = [0,1]
    # Passo
    num_sub_int = 4
    # h = 
    h = (I[1] - I[0])/num_sub_int
    euler(y0,x0,h,I)
