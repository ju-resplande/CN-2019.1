from math import *
#Importando a funcoes

erro_aceitavel = pow(10,-7)

def metodo(a,b):
    vezes = 0
    
    while erro_alto(a,b):
        vezes += 1        
        meio = (a+b)/2       

        print vezes
        print meio 
        print f(meio)
        print

        if (f(a)*f(meio) > 0):
            a = meio
        elif(f(a)*f(meio) < 0):
            b = meio

        if (f(a) == 0):
            print("chances bem baixas disso acontecer")
            return a
        if (f(b) == 0):
            print("chances bem baixas disso acontecer")
            return b
#    return meio

def f(x):
    return x*log10(x) - 1.0

def erro_alto(a,b):
    if fabs(b-a) < erro_aceitavel:
        return False
    else:
        return True

metodo(2.0,3.0)
