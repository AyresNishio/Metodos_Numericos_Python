import numpy as m


# Define Função
def fct(x):
   
    y = 7*(2-0.9**x)-10
    return y



x=[4, 4.1]
tol = 0.0001
precisao = len(str(tol)) + 1 # Ajusta as impressões na saida de acordo com o número de casas da tolerância
iter_max = 20
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
    print("liminte máximo de iterações alcançado")
else:
    print(f"A solução obtida foi: {x[iter]}")
    print(f"o numero de iterações foi de {iter}")
    print(f"tempo da lava = {x[iter]*60}")