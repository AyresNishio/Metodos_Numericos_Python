import numpy as np
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
    dy_dx = 2*y/x +x**2*np.e**x 
    return dy_dx



if __name__ == '__main__':
    #Pvi
    y0= 0
    x0= 1
    #intervalo
    I = [1,1.1]

    # Passo
    # num_sub_int = 4
    h = 0.1 
    # h = (I[1] - I[0])/num_sub_int
    print('Euler 4')
    euler(y0,x0,h,I)

    print(1.1**2*(np.e**(1.1)-np.e))
