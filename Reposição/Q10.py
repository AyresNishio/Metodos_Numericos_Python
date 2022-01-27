import numpy as np
import matplotlib.pyplot as plt




def func(x,y):
    dy_dx = y-x**2+1
    return dy_dx

def euler_modif(y0,x0,h,I):
    n =  (I[1] - I[0])/h
    x= []
    y= []
    x.append(x0)
    y.append(y0)
    print(f"y{0} = {y0}")
    for i in range(int(n)):
        yk_til = y0 + func(x0,y0)*h
        f_xy = func(x0,y0)
        x0 = x0 + h
        f_til_xy = func(x0,yk_til)
        k = (f_xy + f_til_xy)/2
        yk = y0+ k*h
        print(f"y{i+1} = {yk}")
        y0 = yk
        x.append(x0)
        y.append(y0)

     
    return


if __name__ == '__main__':
    #Pvi
    y0= 0.5
    x0= 0
    #intervalo
    I = [0,0.4]
    # Passo
    # num_sub_int = 4
    h = 0.2 
    # h = (I[1] - I[0])/num_sub_int
    euler_modif(y0,x0,h,I)
    
