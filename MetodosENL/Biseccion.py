#Metodo de la Biseccion
#Entradas:
            #func: es la funcion a analizar
            #a: es "a" valor inferior en el intervalo de la funcion en el rango [a, b]
            #b: es "b" valor superior en el intervalo de la funcion en el rango [a, b]
            #MAXIT: es la cantidad de iteraciones máximas a realizar
            #TOL: es la tolerancia del algoritmo
#Salidas:
            #xAprox: es la solucion, valor aproximado de x
            #error: pocentaje de error del resultado obtenido

########################################################################################
import math
import matplotlib.pyplot as plt
import numpy as np
import sys
########################################################################################

def biseccion(func, a, b, MAXIT, TOL):

    if(func(a) * func(b) < 0):
        itera = 0
        err = 0
        iterl = []
        errl = []

        while(itera < MAXIT):
            xAprox = (a + b) / 2
            fx = func(xAprox)

            if(func(a) * fx  < 0):
                b = xAprox
            elif(func(b) * fx < 0):
                a = xAprox
            elif(abs(fx) < TOL):
                plt.plot(iterl, errl)
                plt.xlabel("Iteraciones")
                plt.ylabel("% Error")
                plt.title("Metodo de la Biseccion")
                plt.show()
                return xAprox, itera

            iterl.append(itera)
            errl.append(err)

            itera = itera + 1
            err = (b - a) / (2)
    else:
        print("Las condiciones  no garantizan el cero de la funcion")


if __name__ == '__main__':
    #Limites
    a = 0
    b = 2
    #Tolerancia
    TOL = 0.000001
    #Maximo iteraciones
    MAXIT = 100
    #Funcion
    func = lambda x: math.e**x - x - 2
    #Llamado de la funcion
    xAprox, iter = biseccion(func, a, b, MAXIT, TOL)
    #print(xAprox)
    print('xAprox = {}\nIteraciones = {}'.format(xAprox, iter))
