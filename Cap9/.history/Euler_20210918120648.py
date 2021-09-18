import numpy as np


def func(x,y):
    dy_dx = y - x
    return dy_dx

def euler(y0,x0,h,I):
    n =  (I[1] - I[0])/h
    for i in range(n):
        yk = y0+ h*func(x0,y0)
        print(f"y{i+1} = {yk}")
        y0 = yk
        x0 = x0 + h
    return


if __name__ == '__main__':
    #Pvi
    y0= 0 
    x0= 2
    #intervalo
    I = [0,1]
    # Passo
    num_sub_int = 4
    # h = 
    h = (I[1] - I[0])/num_sub_int
    euler(y0,x0,h,I)
