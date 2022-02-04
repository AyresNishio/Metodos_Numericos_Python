import numpy as np

def newton_interpol2(x,y,x_interpol):
    #Programa de interpolação pela Forma de Newton
    #construção da tabela de diferenças divididas
    n = x.shape[0]
    Dif_Div =  np.zeros((n,n))
    #Cálculo das diferenças divididas de ordem 1
    for i in range(n):
        Dif_Div[i,0]=y[i]

    for j in range(1,n):
        cont = 0
        for i in range(n-j):
            Dif_Div[i,j] = (Dif_Div[i+1,j-1]-Dif_Div[i,j-1])/(x[j+i]-x[i])
            cont = cont + 1
    print('Tabela de Diferenças divididas do método de Newton')
    print(Dif_Div)
    #armazenamento das diferenças divididas
    d = np.zeros(n)
    d[0] = y[0]
    for k in range(n):
        d[k]=Dif_Div[0,k]

    y_interpol=d[0]
    for i in range(1,n):
        #componentes (x-xi)
        compx =1
        for j in range(i):
            compx = compx*(x_interpol-x[j])
        y_interpol=y_interpol+d[i]*compx
    return y_interpol


if __name__ == '__main__':

    x = np.array([5,10,15, 20]) 
    y = np.array([9.85,14.32,17.63, 19.34])

    # x = np.array([5, 6,7]) 
    # y = np.array([0.38,0.51,0.67])
    x_interpol = 17.5

    
    
    y_newton = newton_interpol2(x,y,x_interpol) 

    print('Questão 6')
    print(f'Valor de f({x_interpol}), obtido pelo método de Newton')
    print(y_newton)