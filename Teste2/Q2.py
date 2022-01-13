import numpy as np
import matplotlib.pyplot as plt



if __name__ == '__main__':
    x = np.array([   1.9,    2.1,    2.4]);
    y = np.array([1.3961, 1.5432, 1.7349]);

    #Número Total de Pontos da Amostra
    n_pontos=x.shape[0];
    # Grau do polinômio a ser ajustado aos dados
    n_grau= 2;
    # Soma dos valores de x e de suas potências
    x_soma=np.zeros(2*n_grau, dtype = np.float64)
    for i in range(2*n_grau):
        x_soma[i]=sum(l**(i+1) for l in x)

    # //Formação da matriz A e do vetor b do sistema linear Ax=b, cuja solução
    # // corresponde aos coeficientes do polinômio a ser ajustado
    # //Primeira linha da matriz A e do vetor b
    A=np.zeros((n_grau+1,n_grau+1), dtype = np.float64)
    b=np.zeros(n_grau+1, dtype = np.float64)
    A[0,0]=n_pontos
    b[0]=sum(y)
    for k in range(1,n_grau+1):
        A[0,k] = x_soma[k-1]

    # //Demais linhas de A
    for i in range(1,n_grau+1):
        for j in range(n_grau+1):
            A[i,j]=x_soma[i+j-1]

    # //Formação do vetor b
    for i in range(1,n_grau+1):
        for j in range(n_pontos):
            b[i] += y[j]*(x[j]**i) 

    # //Determinação dos coeficientes do polinômio
    # alfa=A\b
    alfa = np.linalg.inv(A)@np.transpose(b)
    
    # POlinônio Interpolante
    y_ajuste = np.zeros(n_pontos,dtype=np.float64)
    for i in range(n_pontos):
        for j in range(n_grau+1):
            y_ajuste[i] = y_ajuste[i] + alfa[j]*x[i]**j

    print("Matriz A")        
    print(A) 

    print("Matriz b")        
    print(b) 

    print("Parametros da Função de Ajuste")        
    print(alfa) 

    pi = alfa[1] + 2*alfa[2]*2
    print(f'p\'(2) = {pi}')
    pii = 2*alfa[2]
    print(f'p\'\'(2) = {pii}')
