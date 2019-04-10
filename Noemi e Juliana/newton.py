from math import log10
from math import fabs
#Importando a funcao de calcular modulo 
from sympy import *
#Importar as funcoes de calculos

erro_aceitavel = pow(10,-7)
x = Symbol('x') #usar icognita para calculo

def metodo(p):
    vezes = 0

    while erro_alto(p):
        vezes += 1
        p = p -(p*log10(p) -1.0)/derivada_no_ponto(x,p)
        p = float(p)

        print vezes
        print "ponto"
        print p
        print "funcao no ponto" 
        print 

    return p

def f(x):
    return x*log(x,10) -1.0

def erro_alto(p):
    y =  p*log10(p) -1.0

    if fabs(y) < erro_aceitavel:
        return False
    else:
        return True

def derivada_no_ponto(x,p):
    derivada = f(x).diff(x)
    return derivada.subs(x,p)

metodo(2.5)

