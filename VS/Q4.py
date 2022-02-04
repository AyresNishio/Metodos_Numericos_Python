import numpy as np

#Metodo de Gauss-Jacobi e Gauss Seidel

#Exemplo 4.5 e 4.6 com erros no livro

def calculo_erro(x,x2,tipo,n):
    erro = np.zeros(n,dtype=np.float64)
    if tipo == 'absoluto':
        for i in range(n):  
            erro[i] = x[i] - x2[i]
        
    if tipo == 'relativo':
        for i in range(n):
            erro[i] = (abs(x[i]-x2[i]))/abs(x[i])   

    return erro 

def GaussSeidel(A,x,b,tol):
    n = A.shape[0]
    erro= np.zeros(n,dtype=np.float64)
    erro[:]=1000
    iter=0
    while (max(abs(erro))>=tol):
        xk=x.copy()
        x=np.zeros(n,dtype=np.float64)
        for i in range(n):
            soma = 0
            for j in range(n):  
                if (i!=j):
                    if (j<i):
                        soma= soma + A[i,j]*x[j]
                    else:
                        soma= soma+ A[i,j]*xk[j]
            x[i] = (1/A[i,i])*(b[i] - soma)

        erro = calculo_erro(x,xk,'relativo',n)
        iter=iter+1  
        print(f'iteração{iter}:')
        print(x)  

        # print(f'Iteração {iter}: do método Gauss Seidel')   
        # for sol in x:
        #     print(round(sol,precisao))

    return x, iter        

#Main

if __name__ == '__main__':

    A = np.array(
        [[2,-1,0,0,0,0],
        [-1,2,-1,0,0,0],
        [0,-1,2,-1,0,0],
        [0,0,-1,2,-1,0,],
        [0,0,0,-1,2,-1],
        [0,0,0,0,-1,2],
        ])
    b = np.array([2,-1,7,5,4,3])
    x= np.array([0,0,0,0,0,0]) #initial solution
    tol = 10e-3
    # i = input('Digite 0 para Met. de Gauss e 1 para Gauss Seidel')
    # if i == '0' :
    
    # #Gauss Seidel 
    sol_GS,iter_GS =GaussSeidel(A,x,b,tol)    
      

    print("")
