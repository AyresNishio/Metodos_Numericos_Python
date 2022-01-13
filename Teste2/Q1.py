import numpy as np


def vandermonde(x,y):
    num_points = x.shape[0]
    A=np.zeros((num_points,num_points),np.float64)
    
    for i in range(num_points):
        for j in range(num_points):
            A[i,j] = x[i]**j

    coef = np.linalg.inv(A)@np.transpose(y)
    
    return coef

if __name__ == '__main__':
    #Exemplo 6.1, 6.2, 6.3
    x = np.array([0, 88,  100]) 
    y = np.array([0,  4, 2.44])

    # Retorna Coeficientes do Polinômio
    coefs_vander = vandermonde(x,y)

    print('Polinômio obtido método de Vandermonde')
    print(round(coefs_vander[0],6)),
    for i in range(1,len(coefs_vander)):
        print(f'{round(coefs_vander[i],6)}x^{i}'),

    ang = np.arctan(coefs_vander[1])

    print(f'ang0 = {ang}')

    v0 = np.sqrt(-5/(np.cos(ang)**2 * coefs_vander[2]))

    print(f'v0 = {v0}')