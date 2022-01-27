#Programa do Método da Secante



import numpy as np


# Define Função
def fct(x):
    y =2*np.sin(x)/(3*x) -0.5
    return y

def dfct(x):
    y =2*(x*np.cos(x)-np.sin(x))/(3*x**2)
    return y

x=[]
x.append( float(input("Digite o valor inicial do processo iterativo: ")))
tol = float(input("Digite o valor inicial da tolerância: "))
# Ajusta as impressões na saida de acordo com o número de casas da tolerância
precisao = len(str(tol)) +1
iter_max = int(input("Digite o número maximo de iterações: "))

print(f'|df(x)/dx| = {abs(dfct(x[0]))}')
if(abs(dfct(x[0]))<=1): print('Convergência Garantida')
else: print('Convergencia NÃO Garantida')

iter = 0
desvio_absoluto = np.inf
while (desvio_absoluto > tol and iter <=iter_max):

    print(f"Iteração {iter+1}") 
    delta = fct(x[iter])/dfct(x[iter])
    x.append(x[iter] - delta)


    print(f"x{iter+1}=",round(x[iter+1],precisao))
    desvio_absoluto = abs(x[iter+1]-x[iter])
    desvio_relativo = abs(desvio_absoluto/x[iter+1])
    print(f"Desvio Abs.= {round(desvio_absoluto,precisao)}")
    print(f"Desvio Rel.= {round(desvio_relativo,precisao)}")
    iter = iter + 1
    print("--------------------------------------")
#iter -=1
if(iter > iter_max):
    print("liminte máximo de iterações alcançado")
else:
    print(f"A solução obtida foi: {round(x[iter],precisao)}")
    print(f"o numero de iterações foi de {iter}")

