#Programa do Método da Bisseção

#Algotirmo Apresentado no livro (página 66)

import math as m
# Define Função
# Define Função
def fct(x):
    y =  m.cos(x) - 3 + m.exp(x)
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
    a=-m.inf
    b=m.inf

#ERRATA Livro invertido esquerda e direita
print(f'Valor a direita de {a}')
print(f'Valor a esquerda de {b}')