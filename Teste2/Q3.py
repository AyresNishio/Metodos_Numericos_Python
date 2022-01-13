import numpy as np



def metodo_13Simpson(y,intervalos,h):
    
    intervalos = intervalos-1

    I_13SR= y[0]
    print(f'({y[0]}',end =" ")
    coef=4
    for i in range(1,intervalos):
        I_13SR = I_13SR +  coef*y[i]
        print(f'+ {coef*y[i]}',end =" ")
        if(coef==4): coef = 2
        else: coef = 4

    I_13SR = I_13SR + y[intervalos-1]
    I_13SR = I_13SR*(h/3)
    print(f'+ {y[intervalos-1]})*{h}/3')

    return I_13SR

if __name__ == "__main__":
    #exemplo 8.3
    
    y = [0, 4, 6, 5, 4, 3.5, 5, 8, 7, 6 , 0]

    intervalos = len(y) + 1
    espaçamento = 10

    area_da_curva= metodo_13Simpson(y,intervalos, espaçamento)

    volume_do_Corte = area_da_curva*25

    numero_de_caminhoes = volume_do_Corte/20
    print(f'Area da Curva = {area_da_curva}')
    print(f'Volume do Morrote = {volume_do_Corte}')
    print(f'Numero de caminhões necessários = {numero_de_caminhoes}')
