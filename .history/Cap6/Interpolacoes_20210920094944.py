import numpy as np

def vandermonde(x,y):
    num_points = x.shape[0]
    A=np.zeros((num_points,num_points),np.float64)
    
    for i in range(num_points):
        for j in range(num_points):
            A[i,j] = x[i]**j

    coef = np.linalg.inv(A)@np.transpose(y)
    
    return coef

def lagrange(x,y,x_interpol):
    #programa de interpolação pela Forma de Lagrange
    #dados de entrada
    #quantidade de pontos
    n=x.shape[0]
    L = np.zeros(n) 
    for i in range(n):
        L[i] = 1
        for j in range(n):
            if (j != i):
                L[i]=L[i]*(x_interpol-x[j])/(x[i]-x[j])
    
    soma=0
    for i in range(n):
        soma=soma+y[i]*L[i]
    
    #valor interpolado
    y_interpol=soma 

    return y_interpol


def newton_interpol(x,y,x_interpol):
    #Programa de interpolação pela Forma de Newton
    #construção da tabela de diferenças divididas
    n = x.shape[0]
    Dif_Div =  np.zeros((n,n))
    #cálculo das diferenças divididas de ordem 1
    for i in range(n-1):
        Dif_Div[i,0]=(y[i+1]-y[i])/(x[i+1]-x[i])
        
    #cálculo das diferenças divididas de ordem superior
    for j in range(1,n-1):
        cont = 0
        for i in range(1,n-j):
            Dif_Div[i,j] = (Dif_Div[i,j-1]-Dif_Div[i-1,j-1])/(x[j+i]-x[i-1])
            cont = cont + 1
        temp = Dif_Div[:,j].copy()
        temp = temp[temp != 0]
        Dif_Div[0:cont,j] = temp 
        Dif_Div[cont:n,j] = 0 

    #armazenamento das diferenças divididas
    d = np.zeros(n)
    d[0] = y[0]
    for k in range(1,n):
        d[k]=Dif_Div[0,k-1]
    
    #cálculo do valor de y_interpol no ponto x_interpol
    delta_x=1
    y_interpol=d[0]
    for i in range(1,n):
        compx =1
        for j in range(i):
            print(f'({x_interpol}-{x[j]})')
            compx = compx*(x_interpol-x[j])
        #     delta_x=delta_x*(x_interpol-x[i-1])
        y_interpol=y_interpol+d[i]*compx
    
    return y_interpol


if __name__ == '__main__':
    x = np.array([1.5, 3.5, 7. ,11.5, 14]) 
    y = np.array([3,6,2.5,9.5,7.4])
    x_interpol = 10
    coefs_vander = vandermonde(x,y)
    y_lagrange = lagrange(x,y,x_interpol)
    y_newton = newton_interpol(x,y,x_interpol) 
    print(coefs_vander)
    print(y_lagrange)
    print(y_newton)
    # print('')