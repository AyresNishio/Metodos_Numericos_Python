import numpy as np


#Metodo de Gauss-Jacobi e Gauss Seidel


def GaussJacobi(A,x,b,tol):
    n = A.shape[0]
    erro = np.zeros(n,dtype=np.float64)
    erro[:]= 1000
    iter=0

    precisao = len(str(tol))+1
    while max(abs(erro))>=tol:
        xk = x.copy()
        x= np.zeros(n, dtype = np.float64)
        for i in range(n):
            soma= 0
            for j in range(n):  
                if (i != j):
                    soma= soma + A[i,j]*xk[j]
            x[i] = (1/A[i,i])*(b[i] - soma)
            
        erro = calculo_erro(x,xk,'absoluto',n)
        iter = iter+1 

        # print(f'Iteração {iter}: do método Gauss Jacobi')   
        # for sol in x:
        #     print(round(sol,precisao))
   
    return x,iter

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

def calculo_erro(x,x2,tipo,n):
    erro = np.zeros(n,dtype=np.float64)
    if tipo == 'absoluto':
        for i in range(n):  
            erro[i] = x[i] - x2[i]
        
    if tipo == 'relativo':
        for i in range(n):
            erro[i] = (abs(x[i]-x2[i]))/abs(x[i])   

    return erro 

#Função Principal do Código
if __name__ == '__main__':

    #Exemplo 4.5 e 4.6 OBS: livro apresenta Erros no número de iterações no metodo de Gauss Jacobi (Valor errado calculado dm x1)
    # A = np.array([[6,-1,2,0],[0,9,0,4],[2,-1,10,-1],[0,0,-1,8]])
    # b = np.array([2,22,-11,9])
    # x= np.array([0,0,0,0])
    # tol = 1e-3
    #Teste
    A = np.array([[24,4,0,0,6],[4,12,0,2,0],[0,0,3,0,3],[2,0,0,3,0],[4,0,2,0,6]])
    b = np.array([15,7,7,4,8])
    x= np.array([0,0,0,0,0])
    tol = 0.005

    #Precisão das Impressões
    precisao = len(str(tol))
    
    #Gauss Jacobi
    # sol_GJ,iter_GJ=GaussJacobi(A,x,b,tol) 
    # print(f"SOLUÇÃO FINAL obtida em {iter_GJ} iterações pelo metodo de Gauss Jacobi: ") 
    # for sol in sol_GJ:
    #     print(round(sol,precisao))
    # print('------------------------------------------------------------------------')
    # #Gauss Seidel 
    sol_GS,iter_GS =GaussSeidel(A,x,b,tol)   
    print(f"SOLUÇÃO FINAL  em {iter_GS} iterações pelo metodo de Gauss e Seidel: ") 
    for sol in sol_GS:
        print(round(sol,precisao)) 
   
