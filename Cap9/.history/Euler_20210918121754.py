import numpy as np
import matplotlib.pyplot as plt

def func(x,y):
    dy_dx = (1/2)*np.exp(x/3) - (1/2)*y #Exemplo 9.2
    return dy_dx

def euler(y0,x0,h,I):
    n =  (I[1] - I[0])/h
    x= [x0]
    y= [y0]
    for i in range(int(n)):
        yk = y0+ h*func(x0,y0)
        print(f"y{i+1} = {yk}")
        y0 = yk
        x0 = x0 + h
        x.append(x0)
        y.append(y0)
    plt.scatter(x, y)
    plt.show()
    return


if __name__ == '__main__':
    #Pvi
    y0= 3
    x0= 0
    #intervalo
    I = [0,5]
    # Passo
    # num_sub_int = 4
    h = 1 
    # h = (I[1] - I[0])/num_sub_int
    euler(y0,x0,h,I)
    plt
