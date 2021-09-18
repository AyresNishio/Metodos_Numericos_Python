import numpy as np


def func(x,y):

    dy_dx = y - x
    
    return dy_dx

def euler(y0,x0,h,I):




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
