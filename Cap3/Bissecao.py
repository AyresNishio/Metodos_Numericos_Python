#Programa do Método da Bisseção

#Algotirmo Apresentado no livro (página 66)
# Ex 3.1 
# Ponto de origem: 0
# Valor do intervalo: 0.2
# Número máximo de iterações: 10
# Resposta [0.8, 1.0]
#ERRATA: Livro invertido esquerda e direita

# Biblioteca do python com funções matemáticas
import numpy as np 

# Define Função
def fct(x):
    y =  np.cos(x) - 3 + np.exp(x)
    return y

a = int(input("Digite o Ponto de origem: "))
delta = float(input("Digite o valor do intervalo: "))
b = delta + a
max_iter = int(input("Digite o número máximo de iterações: "))

iter = 0

while(fct(a)*fct(b)>0 and iter<max_iter):
    a=b
    b=a+delta
    iter += 1

if(fct(a)*fct(b)>0):
    print('Máximo de iterações atingido')
    a=-np.inf
    b=np.inf


print(f'Valor a direita de {a}')
print(f'Valor a esquerda de {b}')