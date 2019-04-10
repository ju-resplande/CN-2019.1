from math import *
#Importando a funcoes matematicas

erro_aceitavel = pow(10,-6)

def metodo(p):
    vezes = 0

    while erro_alto(p):
        vezes += 1
        p = phi(p)

        print vezes
        print p
        print f(p)

def phi(x):
    return (x+1.0)**(1.0/3)

def f(x):
    return x**3-x-1.0

def erro_alto(a):
    if fabs(f(a)) < erro_aceitavel:
        return False
    else:
        return True

metodo(1.0)
