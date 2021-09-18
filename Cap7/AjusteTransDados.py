import numpy as np
####Ajuste Não Polinomial
# //programa de ajuste não polinomial
# clear
# printf('Dados de entrada (valores de x e y) \n')
# Tabela=read('Cap7_Tabela2.txt',-1,2)
# x = np.array([-1.,-.7,-.4,-.1,0.2,0.5,0.8,1.0]);
# y = np.array([ 36, 17,8.5,4.0,1.6,0.7,0.4,0.1]);
x = np.array([0.25,0.65,0.95,1.25,1.75,2.00,2.25,2.55,2.75,3.05]);
y = np.array([0.20,-.25,-1.1,-.45,0.25,0.10,-.30,0.25,0.55,1.05]);
n_pontos=x.shape[0]
# printf('Número total de pontos da amostra = %g \n', n_pontos)
# //definição do número de funções que compõem o ajuste
n_funcoes=3;
# printf('Número de funções que participam do ajuste = %g \n', n_funcoes)
# funcprot(0);
# //definição das funções que compõem o ajuste
def func1(x):
    y=np.log(x)
    return y

def func2(x):
    y=np.cos(x)
    return y

def func3(x):
    y=np.e**x
    return y

funcs = [func1, func2, func3]

A=np.zeros([n_funcoes,n_funcoes],np.float64)

x_funcs = np.zeros([n_funcoes,n_pontos],np.float64)
for f in range(n_funcoes):
    for i in range(n_pontos):
        x_funcs[f,i] = funcs[f](x[i])

for i in range(n_funcoes):
    for j in range(n_funcoes):
        soma = 0.0
        for k in range(n_pontos):
            soma = soma + x_funcs[i,k]*x_funcs[j,k]
        A[i,j] = soma

b=np.zeros(n_funcoes,dtype = np.float64)
for i in range(n_funcoes):
    for j in range(n_pontos):
        b[i] += y[j]*x_funcs[i,j]

alfa = np.linalg.inv(A)@np.transpose(b)
# //valores de funcao1
# for i=1:n_pontos
# Aux(i,1)=funcao1(x(i));
# end
# function g2=funcao2(x)
# g2=cos(x)
# endfunction
# //valores da funcao2
# for i=1:n_pontos
# Aux(i,2)=funcao2(x(i));
# end
# function g3=funcao3(x)
# g3=exp(x)
# endfunction
# //valores da funcao3
# for i=1:n_pontos
# Aux(i,3)=funcao3(x(i));
# end
# //Formação da matriz A e do vetor b do sistema linear Ax=b, cuja solução
# // corresponde aos coeficientes da função global a ser ajustada

# for i=1:n_funcoes
# for j=1:n_funcoes
# soma=0;
# for k=1:n_pontos
# soma=soma+Aux(k,i)*Aux(k,j);
# end
# A(i,j)=soma;
# end
# end
# //matriz A
# printf('Matriz de coeficientes = \n'); A
# //Formação do vetor b
# for i=1:n_funcoes
# soma=0;
# for k=1:n_pontos
# soma=soma+y(k)*Aux(k,i);
# end
# b(i)=soma;
# end
# //vetor b
# printf('Vetor independente = \n'); b
# //Obtenção dos parâmetros da função de ajuste
# alfa=A\b
# //obtenção do gráfico de y e da função de ajuste
# for k=1:n_pontos
# f_ajuste(k)=alfa(1)*funcao1(x(k))+alfa(2)*funcao2(x(k))+alfa(3)*funcao3(x(k));
# end
# plot2d(x,y,-5)
# plot2d(x,f_ajuste,5)
print('')