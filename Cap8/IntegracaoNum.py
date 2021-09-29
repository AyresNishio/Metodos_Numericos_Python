import numpy as np

#####Trapézios
# //Programa para se obter o valor da integral de uma função no intervalo [a,b],
# // através da Regra dos Trapézios Repetida, com certo grau de precisão,
# //estabelecido pelo parâmetro tol (tolerância)
# //=====================================================
# //definição da função a ser integrada
def func(x):
    y =np.e**((-x**2))
    #y = np.sqrt(6*x-5)
    return y
# //definição da derivada a segunda a ser integrada
def d2func(x):
    y =4*x**2*np.e**(-x**2) - 2*np.e**(-x**2)
    return y
# //definição da derivada a segunda a ser integrada
def d4func(x):
    y=16*x**4*np.e**(-x**2) - 48*x**2*np.e**(-x**2) + 12*np.e**(-x**2)
    return y

def M2(vec_x):
    vec_d2 = d2func(vec_x)
    return max(vec_d2)

def M4(vec_x):
    vec_d4 = d2func(vec_x)
    return max(vec_d4)


def metodo_trapezio(a,b,m):
    h=(b-a)/m
    x = np.zeros(m+1)
    y = np.zeros(m+1)
    for i in range (m+1):
        x[i]=i*h+a
        y[i]=func(x[i])

    #Trapezio
    I_TR= y[0]
    for i in range(1,m):
        I_TR = I_TR +  2*y[i]
    I_TR = I_TR + y[m]
    
    I_TR = I_TR*(h/2)

    erro_t = erro_trapezio(h,x,m)
    return I_TR, erro_t

def metodo_13Simpson(a,b,r):
    m=2*r
    h=(b-a)/(m)
    n_pontos =m+1
    x = np.zeros(n_pontos)
    y = np.zeros(n_pontos)

    for i in range (n_pontos):
        x[i]=i*h+a
        y[i]=func(x[i])

    I_13SR= y[0]
    coef=4
    for i in range(1,m):
        I_13SR = I_13SR +  coef*y[i]
        if(coef==4): coef = 2
        else: coef = 4

    I_13SR = I_13SR + y[m]
    I_13SR = I_13SR*(h/3)

    erro_13s = erro_13simpson(h,x,m)

    return I_13SR, erro_13s

def metodo_38Simpson(a,b,r):
    m=3*r
    h=(b-a)/m
    x = np.zeros(m+1)
    y = np.zeros(m+1)

    for i in range (m+1):
        x[i]=i*h+a
        y[i]=func(x[i])


    I_38SR= y[0]
    coef=3
    for i in range(1,m):
        if(i%3 == 0):coef = 2
        else: coef = 3
        I_38SR = I_38SR +  coef*y[i]

    I_38SR = I_38SR + y[m]
    I_38SR = I_38SR*(h*3/8)

    erro_38s = erro_38simpson(h,x,m)

    return I_38SR, erro_38s

def erro_trapezio(h,x,m):
    erro_t = -m*h**3*M2(x)/12
    return erro_t

def erro_13simpson(h,x,m):
    erro_13s = -h**5*M4(x)/90*(m/2)
    return erro_13s

def erro_38simpson(h,x,m):
    erro_38s = -3*h**5*M4(x)/80*(m/3)
    return erro_38s
if __name__ == "__main__":
    #exemplo 8.3
    a=0
    b=2
    m=4;
    ms=2
    I_tr , erro_tr    = metodo_trapezio(a,b,m)
    I_13s, erro_13s  = metodo_13Simpson(a,b,ms)
    I_38s, erro_38s  = metodo_38Simpson(a,b,ms)


    print('')


# function y=funcao(x)
# y=2*(x^3)+x^2+1
# endfunction
# //=====================================================
# //definição do intervalo de integração
# a=input('entre com o extremo inferior do intervalo de integração ');
# b=input('entre com o extremo superior do intervalo de integração ');
# tol=input('entre com o valor da tolerância (precisão) para integração ');
# //====================================================
# //número de pontos para se discretizar a 2a. derivada do integrando
# // no intervalo de integração [a,b]
# n_discret=100;
# d=(b-a)/n_discret;
# x=a;
# for i=1:n_discret+1
# [deriv1,deriv2]=numderivative(funcao,x,[],2);
# aux(i)=deriv2;
# if x<=b
# x=x+d;
# else
# end
# end
# //obtenção do valor máximo aproximado da 2a. derivada do integrando
# M2=max(aux);
# //Número de subintervalos para que se atinja a tolerância especificada
# m=sqrt(((b-a)^3*M2)/(12*tol));
# m_subinterv=ceil(m)
# //tamanho de cada subintervalo
# h=(b-a)/m_subinterv;
# x=a:h:b;
# for i=1:m_subinterv+1
# aux(i)=funcao(x(i));
# end
# I_trapezios=(h/2)*(aux(1)+2*sum(aux(2:m_subinterv))+aux(m_subinterv+1))

######1/3 Simpson
# //Programa para integração numérica no intervalo [a,b],
# //subdividido em n_subint partes (no. par), adotando-se a Regra 1/3 de Simpson
# //===============================================
# clear(); //limpa a memória
# global I //declara I (valor da integral) como variável global
# //===============================================
# //definição da função a ser integrada
# deff('integrando=funcao(x)','integrando=x*exp(-x)')
# //===============================================
# funcprot(0);
# //cálculos da Regra de Simpson
# function I=regra_simpson_1(a, b, n_subint, funcao)
# global I
# h=(b-a)/n_subint
# x=a:h:b
# for i=1:n_subint+1
# y(i)=funcao(x(i))
# end
# I=(h/3)*(y(1)+4*sum(y(2:2:n_subint))+2*sum(y(3:2:n_subint-1))+y(n_subint+1))
# endfunction
# //===================================================
# //determinação do valor da integral
# regra_simpson_1(0,1,20,funcao);
# printf('Valor da Integral pela Regra 1/3 de Simpson = %g', I)


######3/8
# //Programa para integração numérica no intervalo [a,b],
# //subdividido em n_subint partes (múltiplo de 3), adotando-se a Regra 3/8 de Simpson
# //==================================================
# clear(); //limpa a memória
# global I //declara I (valor da integral) como variável global
# //==================================================
# //definição da função a ser integrada
# deff('integrando=funcao(x)','integrando=(log(x)^2)/x')
# //==================================================
# funcprot(0);
# //cálculos da Regra de Simpson
# function I=regra_simpson_2(a, b, n_subint, funcao)
# global I
# h=(b-a)/n_subint
# x=a:h:b
# for i=1:n_subint+1
# y(i)=funcao(x(i))
# end
# I=(3*h/8)*(y(1)+3*sum(y(2:3:n_subint-1))+3*sum(y(3:3:n_subint))+...
# 2*sum(y(4:3:n_subint-2))+y(n_subint+1))
# endfunction
# //===================================================
# //determinação do valor da integral
# regra_simpson_2(1,%e^2,75,funcao);
# printf('Valor da Integral pela Regra 3/8 de Simpson = %g', I)

if __name__ == '__main__':
