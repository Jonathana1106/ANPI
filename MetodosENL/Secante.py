# Metodo de la Secante
# Entradas:
            # func: es la funcion a analizar
            # x0: valor iniciar
            # MAXIT: es la cantidad de iteraciones máximas a realizar
            # TOL: es la tolerancia del algoritmo
# Salidas:
            # xAprox: es la solucion, valor aproximado de x
            # error: pocentaje de error del resultado obtenido

########################################################################################
import math
import matplotlib.pyplot as plt
from scipy.misc import derivative
import numpy as np
import sys
########################################################################################

def secante(func, x0, x1, MAXIT, TOL):
    itera = 0
    err = 1
    iterl = []
    errl = []
    xAprox = x0;

    while(err > TOL):

        xAprox = x1 - ((x1 - x0)/(func(x1) - func(x0)))  * func(x1)

        err = abs(xAprox - x1)/(xAprox)
        iterl.append(itera)
        errl.append(err)
        itera = itera + 1

        x0 = x1
        x1 = xAprox

    plt.plot(iterl, errl)
    plt.xlabel("Iteraciones")
    plt.ylabel("% Error")
    plt.title("Metodo de la Secante")
    plt.show()
    return xAprox, itera

if __name__ == '__main__':
    # Valor inicial
    x0 = 0
    x1 = 1
    # Tolerancia
    TOL = 0.0001
    # Maximo iteraciones
    MAXIT = 100
    # Funcion
    func = lambda x: (math.e)**(-(x**2)) - x
    # Llamado de la funcion
    xAprox, itera = secante(func, x0, x1, MAXIT, TOL)
    print('xAprox = {}\nIteraciones = {}'.format(xAprox, itera))