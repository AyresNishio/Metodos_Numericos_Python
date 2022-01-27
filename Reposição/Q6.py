
import numpy as np
import matplotlib.pyplot as plt
####Ajuste Não Polinomial

# //definição das funções que compõem o ajuste
def func1(x):
    y=np.e**x**2
    return y

def func2(x):
    y=x**3
    return y



if __name__ == '__main__':
    
    x = np.array([-1,0,1]);
    y = np.array([ 0,1,2]);

    #Número total de pontos da amostra
    n_pontos=x.shape[0]

    # Número de funções que compõem o ajuste
    n_funcoes=2;

    #Vetor de Funções
    funcs = [func1, func2]

    #Construção da Matriz A
    A=np.zeros([n_funcoes,n_funcoes],np.float64)

    #-Matriz contendo o resultado de cada função em cada ponto
    x_funcs = np.zeros([n_funcoes,n_pontos],np.float64)
    for f in range(n_funcoes):
        for i in range(n_pontos):
            x_funcs[f,i] = funcs[f](x[i])
    #-Constroi A com os resultados das funções
    for i in range(n_funcoes):
        for j in range(n_funcoes):
            soma = 0.0
            for k in range(n_pontos):
                soma = soma + x_funcs[i,k]*x_funcs[j,k]
            A[i,j] = soma
          

    #Construção do Vetor b
    b=np.zeros(n_funcoes,dtype = np.float64)
    for i in range(n_funcoes):
        for j in range(n_pontos):
            b[i] += y[j]*x_funcs[i,j]

    #Coeficientes da função de ajuste    
    alfa = np.linalg.inv(A)@np.transpose(b)

    ajuste = np.zeros(n_pontos,dtype=np.float64)
    for i in range(n_pontos):
        for j in range(n_funcoes):
            ajuste[i] = ajuste[i] +  alfa[j]*funcs[j](x[i])

     
    print("Matriz A")        
    print(A) 

    print("Matriz b")        
    print(b) 

    print("Parametros da Função de Ajuste")        
    print(alfa) 

    #Gráfico 
    #Pontos de entrada
    plt.scatter(x, y, marker = 'o',label = 'pontos da amostra', color = 'red')
    plt.plot(x, ajuste, label = 'Ajuste')

    
    # Nome dos Eixos
    plt.xlabel('Eixo - x')
    plt.ylabel('Eixo - y')
    # Título do Gráfico
    plt.title('Ajuste Não Polinomial')
    
    # Cria janela com Gráfico
    plt.legend()
    plt.show()
