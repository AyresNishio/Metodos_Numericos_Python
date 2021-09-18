import numpy as np

#####Trapézios
# //Programa para se obter o valor da integral de uma função no intervalo [a,b],
# // através da Regra dos Trapézios Repetida, com certo grau de precisão,
# //estabelecido pelo parâmetro tol (tolerância)
# //=====================================================
# //definição da função a ser integrada
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
