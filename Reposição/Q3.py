import numpy as np

#Fatoração LDU
def fat_LDU(L,A,b):
    n = L.shape[0]
    D=np.identity(n)
    U=A
    for i in  range(n):
        D[i,i]=U[i,i]
        U[i,:]=U[i,:]/U[i,i] 
    
    
    # Fatora b
    for j in range(n-1):
        for i in range(j+1,n):
            b[i] = b[i] - L[i,j]*b[j]
     
    y=b
    for i in range(n):
        y[i]=y[i]/D[i,i]
        
    z=y

    #x=U\z ou x = U^-1 x z
    x = np.linalg.inv(U)@z
    return L,D,U,x      
    
# Eliminação de Gauss
def elimGauss(A):
    n=A.shape[0]
    L=np.identity(n)
    for i in range(n-1):
        #Elemento pivô
        piv =  A[i,i]
        for j in range(i+1,n):
            #Multiplicador 
            m = (A[j,i]/piv)
            L[j,i] = m
            A[j,:] = A[j,:] - m*A[i,:]
 
    return L,A

# Função Principal do programa   
if __name__ == '__main__':
  
    A=[ [2, -1, 0, 0, 0, 0], 
        [-1, 2, -1, 0, 0, 0], 
        [0, -1, 2, -1, 0, 0], 
        [0,  0, -1, 2, -1, 0], 
        [0,  0, 0, -1, 2, -1], 
        [0,  0, 0, 0, -1, 2] ]

    b = [2, -1, 7, 5, 4, 3]


    
    A=np.array(A,dtype=np.float64)
    print(f'Determinante de A: {np.linalg.det(A)}')
    
    # Eliminação
    L,A = elimGauss(A)
    # Solução do Sistema
    L,D,U,x = fat_LDU(L,A,b)

    print('Matriz A:')
    print(A)
    print('Matriz L:')
    print(L)
    print('Matriz D:')
    print(D)
    print('Matriz U:')
    print(U)
    print('Solução x:')
    print(x)