#Programa do Método de Ponto Fixo

#Algotirmo Apresentado no livro (texto página 69)

import math as m

# Define Função
def fcth(x):
    y = m.cos(x) - 3 + m.exp(x)
    return y

def fctg(x):
    #y= m.log(m.cos(x) - 3 + m.exp(x))
    y = m.log(3-m.cos(x))
    return y

iter=0
x=[]
x.append(float(input('Digite o valor inicial: ')))
tol = float(input("Digite o valor inicial da tolerância: "))
precisao = len(str(tol)) + 1 # Ajusta as impressões na saida de acordo com o número de casas da tolerância
iter_max = int(input("Digite o número maximo de iterações: "))

desvio_absoluto = m.inf
while (abs(desvio_absoluto)> tol) and (iter<=iter_max):
    print(f"Iteração {iter+1}") 
    g = fctg(x[iter]) #g(x)
    h = fcth(x[iter]) #h(x)
    print(f"g(x{iter})=",round(x[iter],precisao))
    print(f"h(x{iter})=",round(x[iter],precisao))
    x.append(g)
    iter = iter + 1
    desvio_absoluto = x[iter] - x[iter-1]
    desvio_relativo = desvio_absoluto/abs(x[iter])
    print(f"Desvio Abs.= {round(desvio_absoluto,precisao)}")
    print(f"Desvio Rel.= {round(desvio_relativo,precisao)}")
    print("--------------------------------------")
if(iter > iter_max):
    print("limite máximo de iterações alcançado")
else:
    print(f"A solução obtida foi: {round(x[iter],precisao)}")
    print(f"o numero de iterações foi de {iter}")