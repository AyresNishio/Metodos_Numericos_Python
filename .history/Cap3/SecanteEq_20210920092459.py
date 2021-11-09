#Programa do Método de Newton (Secantes)

#Algotirmo Apresentado no livro (página 92)

#Programa do Método de Newton

#Algotirmo Apresentado no livro (página 92)

import math as m


# Define Função
def fct(x):
    y =  m.cos(x) - 3 + m.exp(x)
    return y


x=[]
x.append( float(input("Digite o valor inicial do processo iterativo: ")))
x.append( float(input("Digite o SEGUNDO valor do processo iterativo: ")))
tol = float(input("Digite o valor inicial da tolerância: "))
precisao = len(str(tol)) + 1 # Ajusta as impressões na saida de acordo com o número de casas da tolerância
iter_max = int(input("Digite o número maximo de iterações: "))
iter = 1
desvio_absoluto = m.inf
while (desvio_absoluto > tol and iter <=iter_max):
    print(f"Iteração {iter}") 
    delta = fct(x[iter])*(x[iter]-x[iter-1])/(fct(x[iter])-fct(x[iter-1]))
    x.append(x[iter] - delta)
    print(f"x{iter}=",round(x[iter],precisao))
    desvio_absoluto = abs(x[iter]-x[iter-1])
    desvio_relativo = abs(desvio_absoluto/x[iter])
    print(f"Desvio Abs.= {round(desvio_absoluto,precisao)}")
    print(f"Desvio Rel.= {round(desvio_relativo,precisao)}")
    iter = iter + 1
    print("--------------------------------------")
iter -=1
if(iter > iter_max):
    print("limite máximo de iterações alcançado")
else:
    print(f"A solução obtida foi: {round(x[iter],precisao)}")
    print(f"o numero de iterações foi de {iter}")

