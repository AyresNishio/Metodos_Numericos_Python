#Programa do para converter número binário fracionário para decimal

<<<<<<< HEAD
#Algoritmo Apresentado no livro (página 45)
=======
#Algotirmo Apresentado no livro (página 44): Ex 0.61 7 digitos -> 0.1001110

>>>>>>> 3d13694e9432631987acc61d51a69f68cdfc25ec
k=0
val_dec_frac=float(input("Digite o número fracionário a ser convertido [Obs: Utilize (.) para separar parte inteira da decimal]:"))
r=[val_dec_frac] # Lista para armazenar os valores de r (decimal fracionário) em cada iteração
k_lim=int(input("Digite o limite de dígitos binários desejados:"))
b=[]
while ((r[k] != 0) and (k<k_lim)):
    r_dobro = 2*r[k]
    if (r_dobro >= 1):
        b.append(1)
    else:
        b.append(0)

    r.append(r_dobro - float(b[k]))
    k=k+1
    
#Passo a Passo
for i in range(k_lim):
    print("k=",i+1,"| rk=",round(r[i],2),"| 2rk=",round(2*r[i],2),"| bk=",b[i])
    print("-------------------------------------------------")

print('Número Fracionário Decimal Convertido :')
print(str(b))