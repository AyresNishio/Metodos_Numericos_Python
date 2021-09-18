import numpy as np

####Ajuste Polinomial
# //programa de ajuste polinomial pelo Método dos Mínimos Quadrados Ponderados
# //leitura dos dados de entrada
# Tabela=read('Cap7_Tabela1.txt',-1,2)
x = np.array([0.0,0.5,1.0,1.5,2.0,2.5,3.0,3.5,4.0,4.5,5.0, 5.5, 6.0,6.5,7.0,7.5,8.0]);
y = np.array([3.0,2.6,4.9,5.3,7.0,7.5,7.8,7.6,9.5,9.0,9.5,10.5,10.0,8.5,8.3,9.2,8.7]);
# y=Tabela(:,2);
n_pontos=x.shape[0];
print('Número total de pontos da amostra = %g \n', n_pontos)
# //definição do grau do polinômio a ser ajustado aos dados
n_grau= 2;
# //cálculo das somas dos valores de x e de suas potências
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
# A(1,k)=x_soma(k-1);
# end

# //Demais linhas de A
for i in range(1,n_grau+1):
    for j in range(n_grau+1):
        A[i,j]=x_soma[i+j-1]
# for i=2:(n_grau+1)
# for j=1:(n_grau+1)
# A(i,j)=x_soma(i+j-2);
# end
# //Formação do vetor b
for i in range(1,n_grau+1):
    for j in range(n_pontos):
        b[i] += y[j]*(x[j]**i) 

# b(i)=sum(x.^(i-1).*y);
# end
# printf('Matriz de coeficientes = \n'); A
# printf('Vetor independente = \n'); b
# //Determinação dos coeficientes do polinômio
# alfa=A\b
alfa = np.linalg.inv(A)@np.transpose(b)
# a_transposto=alfa'
# //formação do polinômio interpolante
# p=poly(a_transposto,"x","coeff")
# //obtenção do gráfico de y e p(x)
# for k=1:n_pontos
# f_ajuste(k)=horner(p,x(k));
# end
# plot2d(x,y,-5)
# plot2d(x,f_ajuste,5)

print('')





#if __name__ == '__main__':
