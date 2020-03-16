#Metodo del Punto Fijo
#Entradas:
    #g(x): se obtiene al despejar una x de f(x)
    #n: iteraciones
    #a: valor inicial
#Salidas:
    #respuesta: punto fijo encontrado


import numpy as np
import matplotlib.pyplot

def puntofijo(gx, a, tolera, n = 15):
    it=[]
    er=[]
    i = 1
    b = gx(a)
    tramo = abs(b-a)
    while(tramo>=tolera and i<=n):
        a = b
        b = gx(a)
        tramo = abs(b-a)
        i = i+1
        it.append(i)
        er.append(b)
    respuesta = b
    # Valida respuesta
    matplotlib.pyplot.plot(it, er)
    return(respuesta)


# Prueba
# fx: funcion ingresada
fx = lambda x: np.exp(-x) - x
# gx: funcio despejada
gx = lambda x: np.exp(-x)

a = 0 ; b = 1
tolera = 10e-8
tramos = 101

respuesta = puntofijo(gx,a,tolera)
print("Punto fijo: ", respuesta)
