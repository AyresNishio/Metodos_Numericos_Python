import numpy as np
import matplotlib.pyplot as plt

def euler(y0,x0,h,I):
    n =  (I[1] - I[0])/h
    x= []
    y= []
    x.append(x0)
    y.append(y0)
    print(f"y{0} = {y0}")
    for i in range(int(n)):
        yk = y0+ h*func(x0,y0)
        print(f"y{i+1} = {yk}")
        y0 = yk
        x0 = x0 + h
        x.append(x0)
        y.append(y0)
      
    return

def func(x,y):
    dy_dx = 3 
    return dy_dx

def rk4(y0,x0,h,I):
    n = (I[1] - I[0])/h
    x= []
    y= []
    x.append(x0)
    y.append(y0)
    print(f"y{0} = {y0}")
    for i in range(int(n)):
        k1= func(x0,y0)
        k2= func(x0 + (1/2)*h, y0 + (1/2)*k1*h)
        k3= func(x0 + (1/2)*h, y0 + (1/2)*k2*h)
        k4= func(x0 + h, y0 + k3*h)
        kmedia = (k1 + 2*k2 + 2*k3 + k4)/6
        yk = y0 + kmedia*h
        print(f"y{i+1} = {yk}")
        y0 = yk
        x0 = x0 + h
        x.append(x0)
        y.append(y0)
    
    return

if __name__ == '__main__':
    #Pvi
    y0= 9
    x0= 1
    #intervalo
    I = [1,7]

    # Passo
    # num_sub_int = 4
    h = 2 
    # h = (I[1] - I[0])/num_sub_int
    print('Euler 4')
    euler(y0,x0,h,I)
    print('Runge kunta 4')
    rk4(y0,x0,h,I)